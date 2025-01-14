#!/usr/bin/env python3
# TODO: add support for multiple pbs_server
import re
import os
import sys
import json
import copy
import shutil
import xml.etree.ElementTree as ET
from time import sleep
from pathlib import Path
from datetime import datetime
from itertools import product
from subprocess import getstatusoutput
from collections import namedtuple, defaultdict
__version__ = '0.4.0'
PATTERN = re.compile(r'\{\S*?\}')
HIGHLIGHT = "\033[1;32m"
NORMAL = "\033[0m"

# Check python version
if not sys.version.startswith('3'):
    sys.stderr.write(f"Error traceback:\n  python version {sys.version}\n")
    sys.stderr.write(f"\nFailed reason:\n  only {HIGHLIGHT}python3.6+{NORMAL} is supported!\n")
    sys.exit(1)

# Import tomli libarary
try:
    import tomli
except ModuleNotFoundError as e:
    sys.stderr.write(f"Error traceback:\n  import tomli\n")
    sys.stderr.write(f"\nFailed reason:\n  the {HIGHLIGHT}tomli'{NORMAL} library is not installed, run {HIGHLIGHT} 'pip install tomli'{NORMAL} to install it.\n")
    sys.exit(1)


def ensure_file_exist(file_name):
    """Make sure file exists

    Args:
        file_name (str): path to file to check

    Returns:
        Path: pathlib Path of given file
    """
    file_path = Path(file_name)
    if not file_path.exists():
        warn(f"File not exists: {file_name}")
        exit()

    return file_path


def timestamp():
    """Get current timestamp

    Returns:
        str: formatted time stamp
    """
    now = datetime.now()
    t = now.strftime("%a %Y-%m-%d %H:%M:%S")
    return t


def strptime(s):
    t = datetime.strptime(s, "%a %Y-%m-%d %H:%M:%S")
    return t.strftime("%Y%m%d%H%M%S")


class Pipeline(object):

    def __init__(self, file_name, is_continue):
        """Load TOML configuration into Pipeline object

        Args:
            file_name (str): path to TOML file
        """
        self.is_continue = is_continue

        # Load TOML configuration
        toml_file = ensure_file_exist(file_name)
        with open(toml_file, "rb") as f:
            self.dict = tomli.load(f)
            self.map_()

        # Naive check of configuration file
        for key in ['pipeline', 'version', 'work_dir', 'job']:
            if key not in self.dict:
                sys.stderr.write(f"\nError traceback:\n{key} not found in {file_name}\n")
                sys.stderr.write(f"\nFailed reason:\nrequired field {HIGHLIGHT}{key}{NORMAL} not found in the header of toml file.\n")
                sys.exit(1)

        # Create work_dir
        self.work_dir = Path(self.dict['work_dir'])
        if not self.work_dir.exists():
            self.work_dir.mkdir()

        # Directory to store scripts
        self.script_dir = self.work_dir / "sc"
        if not self.script_dir.exists():
            self.script_dir.mkdir()

        # Make a copy of configuration file
        self.json = self.work_dir / "info"
        self.lock = self.work_dir / "jobs"
        self.checkpint = self.work_dir / "checkpoint"
        self.jobs = None
        self.toml = self.work_dir / "pipeline"
        if not self.toml.exists():
            shutil.copy(file_name, str(self.toml))

        # Directory to store log files
        self.log_dir = self.work_dir / "logs"
        if not self.log_dir.exists():
            self.log_dir.mkdir()


    def __getitem__(self, key):
        """Expose self.dict as iterator values"""
        keys = key.split('.')
        p = self.dict
        for i in keys:
            if i not in p:
                raise KeyError(f"Value {key} not found.")
            p = p[i]
        return p

    def __iter__(self):
        """Expose self.dict as iterator"""
        return iter(self.dict)

    def init(self):
        """Init pipeline object"""
        t = self.load_json()
        self.jobs = self.load_checkpoint()

        # Move old files
        if t is not None:
            if self.json.exists():
                self.json.rename(self.log_dir / f"info.{t}")
            if self.checkpint.exists():
                self.checkpint.rename(self.log_dir / f"checkpoint.{t}")
            if self.lock.exists():
                self.lock.rename(self.log_dir / f"jobs.{t}")

        # Record some information
        header = {
            "Python version": sys.version.split(' ')[0],
            "Qbatch version": __version__,
            "Command line": ' '.join(sys.argv),
            "Pipeline name": self['pipeline'],
            "Pipeline version": self['version'],
            "Submit time": timestamp(),
        }
        with open(self.json, 'w') as js:
            json.dump(header, js)

        print("===========================================")
        k_len = max([len(i) for i in header]) + 1
        for k, v in header.items():
            print(f"{k+':'+(k_len-len(k))*' '}{v}")
        print("===========================================")

    def map_(self):
        for k, v in self.dict.items():
            if k == "jobs":
                continue
            if not isinstance(v, str):
                continue
            params = self.get_param(v)
            if params is None:
                continue

            formatter = {}
            for param in params:
                try:
                    p_value = self.dict[param]
                    formatter[param] = p_value
                except Exception:
                    sys.stderr.write(f"\nError traceback:\n{v.strip()}\n")
                    sys.stderr.write(f"\nFailed reason:\nfield {HIGHLIGHT}{param}{NORMAL} not found.\n")
                    sys.stderr.write(f"\nPipeline attributes:\n{self.dict}\n")
                    sys.exit(0)

            new_v = v
            for i, j in formatter.items():
                if not isinstance(i, str) or not (isinstance(j, int) or isinstance(j, str)):
                    sys.stderr.write(f"\nFailed to parse parameter:\nkey: {i}, value: {j}\n")
                    sys.stderr.write(f"\nFailed reason:\nkey and value should be strings.\n")
                    sys.exit(0)
                new_v = new_v.replace("{"+str(i)+"}", str(j))
            self.dict[k] = new_v


    def load_sample_sheet(self, ss_file):
        """Load sample sheet

        Returns:
            list: list of sample as namedtuple
        """
        samples = []
        with open(ss_file, 'r') as f:
            field_names = f.readline().rstrip().split(',')
            Sample = namedtuple("Sample", field_names)
            for line in f:
                content = line.rstrip().split(',')
                if len(content) > 1 or content[0] != "":
                    samples.append(Sample(*content))

        return samples

    def load_group_sheet(self, gs_file):
        """Load group sheet

        Returns:
            list: list of groups as named tuple
        """
        groups = []
        with open(gs_file, 'r') as f:
            field_names = f.readline().rstrip().split(',')
            Group = namedtuple("Group", field_names)
            for line in f:
                content = line.rstrip().split(',')
                if len(content) > 1 or content[0] != "":
                    groups.append(Group(*content))
        return groups

    def load_checkpoint(self):
        """Get unfinished jobs in the last run

        Returns:
            list: list of unfinished jobs
        """
        if not self.checkpint.exists() and not self.lock.exists():
            return None

        checkpoint = []
        if self.checkpint.exists():
            with open(self.checkpint, 'r') as f:
                for line in f:
                    checkpoint.append(line.rstrip())

        jobs = []
        if self.lock.exists():
            with open(self.lock, 'r') as f:
                for line in f:
                    job_name, job_id, job_cmd = line.rstrip().split('\t')
                    if job_id in checkpoint:
                        continue
                    jobs.append(job_name)

        return jobs

    def load_json(self):
        """Load last submit time stamp from json file

        Returns:
            str: formatted timestamp
        """
        if self.json.exists():
            with open(self.json, 'r') as f:
                js = json.load(f)
                t = strptime(js['Submit time'])
                return t
        else:
            return None

    @staticmethod
    def get_param(cmd):
        """Get parameters inside brace

        Args:
            cmd (str): command lines to parse

        Returns:
            list: list of extracted parameters
        """
        params = re.findall(PATTERN, cmd)
        if len(params) > 0:
            return list(set([i.strip('{}') for i in params]))
        else:
            return None

    def run(self, is_dry):
        if is_dry:
            print("Validating jobs because `--dry` is specified.")
        lock = open(self.lock, 'w')
        job_ids = {}

        # For each job
        for job_name, job_dict in self['job'].items():
            template = Template(job_name, job_dict)
            template.map_(self.dict)

            if 'sample_sheet' in job_dict:
                samples = self.load_sample_sheet(template['sample_sheet'])
            else:
                samples = {}

            if 'group_sheet' in job_dict:
                groups = self.load_group_sheet(template['group_sheet'])
            else:
                groups = {}

            # Iter through samples & groups
            if len(samples) > 0 and len(groups) > 0:
                for sample, group in product(samples, groups):
                    # Init job object & parse job
                    job = Job(job_name+'.'+sample.name+'.'+group.name, template.dict)
                    job.map_(sample, group, self.dict)

                    # Create PBS job script
                    pbs_file = self.script_dir / (job.name + ".sh")
                    pbs_job = PBSJob(job, self.dict, pbs_file)
                    pbs_job.write()

                    # If checkpoint defined
                    if self.is_continue and self.jobs is not None:
                        # If job has been finished
                        if job.name not in self.jobs:
                            job_ids[job.name] = None
                            continue

                    # Get dependencies
                    depend_ids = []
                    if 'depend' in job:
                        job_depends = job['depend'] if isinstance(job['depend'], list) else [job['depend']]
                        for i in job_depends:
                            # For group jobs
                            d_prefix = i+'.'+sample.name+'.'+group.name
                            if d_prefix in job_ids:
                                d_id = job_ids[d_prefix]
                                depend_ids.append(d_id)
                                continue

                            # For sample jobs
                            d_prefix = i+'.'+sample.name
                            if d_prefix in job_ids:
                                d_id = job_ids[d_prefix]
                                depend_ids.append(d_id)
                                continue

                            # For integrative jobs
                            d_prefix = i
                            if d_prefix in job_ids:
                                d_id = job_ids[d_prefix]
                                depend_ids.append(d_id)
                                continue

                            sys.stderr.write(f"\nError traceback:\n{job['depend']}\n")
                            sys.stderr.write(f"\nFailed reason:\nfailed to find job dependencies\n")
                            sys.exit(0)

                    # Remove finished dependencies
                    depend_ids = [i for i in depend_ids if i is not None]

                    # Submit PBS job
                    pbs_cmd, pbs_id = pbs_job.submit(depend_ids, is_dry)
                    job_ids[job.name] = pbs_id

                    # Record submission
                    if pbs_cmd is not None:
                        lock.write(f"{job.name}\t{pbs_id}\t{pbs_cmd}\n")

            # Iter through samples only
            elif len(samples) > 0:
                for sample in samples:
                    # Init job object & parse job
                    job = Job(job_name+'.'+sample.name, template.dict)
                    job.map_(sample, {}, self.dict)

                    # Create PBS job script
                    pbs_file = self.script_dir / (job.name + ".sh")
                    pbs_job = PBSJob(job, self.dict, pbs_file)
                    pbs_job.write()

                    # If checkpoint defined
                    if self.is_continue and self.jobs is not None:
                        # If job has been finished
                        if job.name not in self.jobs:
                            job_ids[job.name] = None
                            continue

                    # Get dependencies
                    depend_ids = []
                    if 'depend' in job:
                        job_depends = job['depend'] if isinstance(job['depend'], list) else [job['depend']]
                        for i in job_depends:
                            # For sample / group jobs
                            d_prefix = i+'.'+sample.name
                            for d_name, d_id in job_ids.items():
                                if d_name.startswith(d_prefix):
                                    depend_ids.append(d_id)
                            if len(depend_ids) > 0:
                                continue

                            # For integretive jobs
                            d_prefix = i
                            if d_prefix in job_ids:
                                d_id = job_ids[d_prefix]
                                depend_ids.append(d_id)
                                continue

                            sys.stderr.write(f"\nError traceback:\n{job['depend']}\n")
                            sys.stderr.write(f"\nFailed reason:\nfailed to find job dependencies\n")
                            sys.exit(0)

                    # Remove finished dependencies
                    depend_ids = [i for i in depend_ids if i is not None]

                    # Submit PBS job
                    pbs_cmd, pbs_id = pbs_job.submit(depend_ids, is_dry)
                    job_ids[job.name] = pbs_id

                    # Record submission
                    if pbs_cmd is not None:
                        lock.write(f"{job.name}\t{pbs_id}\t{pbs_cmd}\n")

            # Itergrative job
            else:
                # Init job object & parse job
                job = Job(job_name, template.dict)
                job.map_({}, {}, self.dict)

                # Create PBS job script
                pbs_file = self.script_dir / (job.name + ".sh")
                pbs_job = PBSJob(job, self.dict, pbs_file)
                pbs_job.write()

                # If checkpoint defined
                if self.is_continue and self.jobs is not None:
                    # If job has been finished
                    if job.name not in self.jobs:
                        job_ids[job.name] = None
                        continue

                # Get dependencies
                depend_ids = []
                if 'depend' in job:
                    job_depends = job['depend'] if isinstance(job['depend'], list) else [job['depend']]
                    for i in job_depends:
                        # For all jobs
                        d_prefix = i
                        for d_name, d_id in job_ids.items():
                            if d_name.startswith(d_prefix):
                                depend_ids.append(d_id)
                        if len(depend_ids) > 0:
                            continue

                        sys.stderr.write(f"\nError traceback:\n{job['depend']}\n")
                        sys.stderr.write(f"\nFailed reason:\nfailed to find job dependencies\n")
                        sys.exit(0)

                # Remove finished dependencies
                depend_ids = [i for i in depend_ids if i is not None]

                # Submit PBS job
                pbs_cmd, pbs_id = pbs_job.submit(depend_ids, is_dry)
                job_ids[job.name] = pbs_id

                # Record submission
                if pbs_cmd is not None:
                    lock.write(f"{job.name}\t{pbs_id}\t{pbs_cmd}\n")

        lock.close()

        n_skip = sum([1 for i in job_ids.values() if i is None])
        n_total = len(job_ids)
        print(f"Submitted {n_total-n_skip} jobs, skipped {n_skip} jobs.")
        if is_dry:
            print(f"All jobs seems fine.")


class Template(object):

    def __init__(self, job_name, job_dict):
        """Init job from job dict

        Args:
            job_name (str): name of job
            job_dict (dict): job dict
        """
        self.name = job_name
        template_dict = job_dict.copy()
        self.nested_dict(template_dict)
        self.dict = template_dict
        for x in ['shell']:
            if x not in self.dict:
                sys.stderr.write(f"\nError traceback:\n{HIGHLIGHT}{x}{NORMAL} not found in {HIGHLIGHT}{self.name}{NORMAL}\n")
                sys.stderr.write(f"\nFailed reason:\nthe [shell] fields should be specified for each job.\n")
                sys.exit(1)

    def __getitem__(self, key):
        """Expose self.dict as iterator values"""
        keys = key.split('.')
        p = copy.deepcopy(self.dict)
        for i in keys:
            if i not in p:
                raise KeyError(f"Value {key} not found.")
            p = p[i]
        return p

    def __iter__(self):
        """Expose self.dict as iterator"""
        return iter(self.dict)

    def nested_dict(self, d):
        """Convert raw job dict to nested dict
        Due to the limitation of TOML format, nested dict is not elegant and easy to use.
        So use list of single-dict instead. This function is intend to convert list of
        single-dict to nested dicts. For example:

        Raw TOML:
            output = [
                {fq = "{work_dir}/out_guppy/{sample.name}.fastq.gz"},
                {pass_fq = "{work_dir}/out_guppy/{sample.name}.pass.fastq.gz"},
            ]

        Nested dict:
            output = {
                fq: "{work_dir}/out_guppy/{sample.name}.fastq.gz",
                pass_fq: "{work_dir}/out_guppy/{sample.name}.pass.fastq.gz",
            }

        Args:
            d (tree): nested job dict
        """
        for k, v in d.items():
            if isinstance(v, dict):
                self.nested_dict(d[k])
            elif isinstance(v, list):
                if k in ['input', 'output']:
                    new_v = {}
                    for i in v:
                        if not isinstance(i, dict):
                            sys.stderr.write(f"\nError traceback:\ncan not parse {HIGHLIGHT}{i}{NORMAL} in {HIGHLIGHT}{k}{NORMAL}\n")
                            sys.stderr.write(f"\nFailed reason:\nEvery element of a list must be dict.\n")
                            sys.exit(0)
                        new_v.update(i)
                    d[k] = new_v
                    self.nested_dict(d[k])
            else:
                pass

    def map_(self, env):
        """Map template dict using sample and pipeline arguments

        Args:
            sample (Sample): namedtuple of sample
            env (dict): dict of Pipeline object
        """
        self.resolve(self.dict, env)

    def resolve(self, d, env):
        """Iterative through each leaf node to parse parameters using pipeline environment
        and sample attributes

        Args:
            d (dict): dict to parse
            sample (Sample): namedtuple of sample
            env (dict): dict of Pipeline object
        """
        for k, v in d.items():
            if isinstance(v, dict):
                self.resolve(d[k], env)
            elif isinstance(v, str):
                params = self.get_param(v)
                if params is None:
                    pass
                else:
                    formatter = {}
                    for param in params:
                        p_value = None

                        # Skip sample and group attributes
                        if param.split('.')[0] in ["sample", "group"]:
                            continue

                        # From local variables
                        if k != param:
                            try:
                                p_value = self[param]
                                formatter[param] = p_value
                                continue
                            except Exception:
                                pass

                        # From global variables
                        try:
                            p_value = env[param]
                            formatter[param] = p_value
                            continue
                        except Exception:
                            pass

                        # Not found
                        sys.stderr.write(f"\nError traceback:\n{v.strip()}\n")
                        sys.stderr.write(f"\nFailed reason:\nfield {HIGHLIGHT}{param}{NORMAL} not found.\n")
                        sys.stderr.write(f"\nPipeline attributes:\n{env}\n")
                        sys.stderr.write(f"\nJob attributes:\n{self.dict}\n")
                        sys.exit(0)

                    new_v = v
                    for i, j in formatter.items():
                        if not isinstance(i, str) or not (isinstance(j, int) or isinstance(j, str)):
                            sys.stderr.write(f"\nFailed to parse parameter:\nkey: {i}, value: {j}\n")
                            sys.stderr.write(f"\nFailed reason:\nkey and value should be strings.\n")
                            sys.exit(0)
                        new_v = new_v.replace("{"+str(i)+"}", str(j))
                    d[k] = new_v
            else:
                pass

    @staticmethod
    def get_param(cmd):
        """Get parameters inside brace

        Args:
            cmd (str): command lines to parse

        Returns:
            list: list of extracted parameters
        """
        params = re.findall(PATTERN, cmd)
        if len(params) > 0:
            return list(set([i.strip('{}') for i in params]))
        else:
            return None


class Job(Template):

    def __init__(self, job_name, job_dict):
        """Init sub job from template name and dict

        Args:
            job_name (str): name of job
            job_dict (dict): nested dict of Template
        """
        self.name = job_name
        self.dict = copy.deepcopy(job_dict)

    def map_(self, sample, group, env):
        """Map template dict using sample and pipeline arguments

        Args:
            sample (Sample): namedtuple of sample
            env (dict): dict of Pipeline object
        """
        self.resolve(self.dict, sample, group, env)

    def resolve(self, d, sample, group, env):
        """Iterative through each leaf node to parse parameters using pipeline environment
        and sample attributes

        Args:
            d (dict): dict to parse
            sample (Sample): namedtuple of sample
            env (dict): dict of Pipeline object
        """
        for k, v in d.items():
            if isinstance(v, dict):
                self.resolve(d[k], sample, group, env)
            elif isinstance(v, str):
                params = self.get_param(v)
                if params is None:
                    pass
                else:
                    formatter = {}
                    for param in params:
                        p_value = None

                        # From sample attributes
                        if param.split('.')[0] == "sample":
                            if len(sample) == 0:
                                sys.stderr.write(f"\nError traceback:\nfield {param} specified but no sample_sheet was provided.\n")
                                sys.exit(0)
                            s_k = param.split('.')[1]
                            if s_k not in sample._fields:
                                sys.stderr.write(f"\nError traceback:\nfield {s_k} not found for sample {sample}\n")
                                sys.stderr.write(f"\nFailed reason:\nthe {HIGHLIGHT}{param}{NORMAL} requires each sample has {HIGHLIGHT}{s_k}{NORMAL} field.\n")
                                sys.exit(0)
                            p_value = getattr(sample, s_k)
                            formatter[param] = p_value
                            continue

                        # From group attributes
                        if param.split('.')[0] == "group":
                            if len(group) == 0:
                                sys.stderr.write(f"\nError traceback:\nfield {param} specified but no group_sheet was provided.\n")
                                sys.exit(0)
                            s_k = param.split(".")[1]
                            if s_k not in group._fields:
                                sys.stderr.write(f"\nError traceback:\nfield {s_k} not found for group {group}\n")
                                sys.stderr.write(f"\nFailed reason:\nthe {HIGHLIGHT}{param}{NORMAL} requires each sample has {HIGHLIGHT}{s_k}{NORMAL} field.\n")
                                sys.exit(0)
                            p_value = getattr(group, s_k)
                            formatter[param] = p_value
                            continue

                        # From local variables
                        if param != k:
                            try:
                                p_value = self[param]
                                formatter[param] = p_value
                                continue
                            except Exception:
                                pass

                        # From global variables
                        try:
                            p_value = env[param]
                            formatter[param] = p_value
                            continue
                        except Exception:
                            pass

                        # Not found
                        sys.stderr.write(f"\nError traceback:\n{v.strip()}\n")
                        sys.stderr.write(f"\nFailed reason:\nfield {HIGHLIGHT}{param}{NORMAL} not found.\n")
                        sys.stderr.write(f"\nPipeline attributes:\n{env}\n")
                        sys.stderr.write(f"\nJob attributes:\n{self.dict}\n")
                        sys.exit(0)

                    new_v = v
                    for i, j in formatter.items():
                        if not isinstance(i, str) or not (isinstance(j, int) or isinstance(j, str)):
                            sys.stderr.write(f"\nFailed to parse parameter:\nkey: {i}, value: {j}\n")
                            sys.stderr.write(f"\nFailed reason:\nkey and value should be strings.\n")
                            sys.exit(0)
                        new_v = new_v.replace("{"+str(i)+"}", str(j))
                    d[k] = new_v
            else:
                pass

    def is_finished(self):
        # No defined output file
        if 'output' not in self.dict:
            return False

        # Determine if output has been generated
        flag = True
        # For multiple output files
        if isinstance(self['output'], dict):
            for k, v in self['output'].items():
                p = Path(v)
                if not p.exists():
                    flag = False
        else:
            # For single output file
            p = Path(self['output'])
            if not p.exists():
                flag = False
        return flag


class PBSJob(object):

    def __init__(self, job, env, pbs_file):
        self.job_name = job.name
        self.skip = job.is_finished()

        # Job scheduler
        self.scheduler = env['pbs_scheduler']
        if self.scheduler not in ['slurm', 'torque']:
            sys.stderr.write(f"\nError traceback:\n{self.scheduler}\n")
            sys.stderr.write(f"\nFailed reason:\nunsupported scheduler, only slurm and torque is supported.\n")
            sys.exit(0)

        # Queue name
        if 'queue' in job:
            self.queue = job['queue']
        elif 'pbs_queue' in env:
            self.queue = env['pbs_queue']
        else:
            sys.stderr.write(f"\nFailed reason: no queue specified, please use 'pbs_queue' in the header section or 'queue' in each job.\n")
            sys.exit(0)

        # Walltime
        if 'walltime' in job:
            self.walltime = job['walltime']
        elif 'pbs_walltime' in env:
            self.walltime = env['pbs_walltime']
        else:
            sys.stderr.write("\nFailed reason: no walltime specified, please use 'pbs_walltime' in the header section or 'walltime' in each job.\n")
            sys.exit(0)

        # Work directory
        if 'dir' in job:
            self.work_dir = job['dir']
        elif 'work_dir' in env:
            self.work_dir = env['work_dir']
        else:
            sys.stderr.write("\nFailed reason: no work dir specified, please use 'work_dir' in the header section.\n")
            sys.exit(0)

        # Other parameters
        if 'log' in job:
            self.log = job['log']
        else:
            self.log = f"{env['work_dir']}/logs/{self.job_name}.logs"

        if 'threads' in job:
            self.threads = job['threads']
        else:
            self.threads = env['threads']

        if 'gpus' in job:
            self.gpus = job['gpus']
        else:
            self.gpus = 0

        self.shell = job['shell']
        self.pbs_file = str(pbs_file)

    def write(self):
        if self.scheduler == 'slurm':
            self.write_slurm()
        else:
            self.write_torque()

    def write_slurm(self):
        with open(self.pbs_file, 'w') as out:
            out.write(f"#!/bin/bash\n")
            out.write(f"#SBATCH -J {self.job_name}\n")
            out.write(f"#SBATCH -p {self.queue}\n")
            out.write(f"#SBATCH -n {self.threads}\n")
            out.write(f"#SBATCH -o {self.log}\n")
            out.write(f"#SBATCH -e {self.log}\n")
            out.write(f"#SBATCH --mail-type=ALL\n")
            out.write(f"#SBATCH -t {self.walltime}:00:00\n")
            out.write(f"#SBATCH -D {self.work_dir}\n")
            out.write(f"set -e\n")
            out.write(f"cd {self.work_dir}\n")
            out.write(f"echo \"[$(date)] {self.job_name} started\"\n")
            out.write(self.shell)
            out.write(f"echo \"[$(date)] {self.job_name} finished\"\n")
            out.write(f"echo $SLURM_JOB_ID >> {self.work_dir}/checkpoint\n")

    def write_torque(self):
        with open(self.pbs_file, 'w') as out:
            out.write(f"#!/bin/bash\n")
            out.write(f"#PBS -N {self.job_name}\n")
            out.write(f"#PBS -q {self.queue}\n")
            out.write(f"#PBS -o {self.log}\n")
            out.write(f"#PBS -e {self.log}\n")
            if self.gpus != 0:
                out.write(f"#PBS -l nodes=1:ppn={self.threads}:gpus={self.gpus}\n")
            else:
                out.write(f"#PBS -l nodes=1:ppn={self.threads}\n")
            out.write(f"#PBS -l walltime={self.walltime}:00:00\n")
            out.write(f"#PBS -d {self.work_dir}\n")
            out.write(f"set -e\n")
            out.write(f"cd {self.work_dir}\n")
            out.write(f"echo \"[$(date)] {self.job_name} started\"\n")
            out.write(self.shell)
            out.write(f"echo \"[$(date)] {self.job_name} finished\"\n")
            out.write(f"echo $PBS_JOBID >> {self.work_dir}/checkpoint\n")

    def submit(self, depend_ids=[], is_dry=False):
        if self.skip:
            sys.stderr.write(f"Skip {self.job_name} because it has been finished.\n")
            return None, None

        sys.stderr.write(f"Submitting {self.job_name}\n")
        if self.scheduler == 'slurm':
            return self.submit_slurm(depend_ids, is_dry)
        else:
            return self.submit_torque(depend_ids, is_dry)

    def submit_slurm(self, depend_ids=[], is_dry=False):
        # Get dependencies
        if len(depend_ids) > 0:
            cmd = f"sbatch --dependency=afterok:{':'.join(depend_ids)} {self.pbs_file}"
        else:
            cmd = f"sbatch {self.pbs_file}"

        # Dry run
        if is_dry:
            return cmd, self.job_name

        status, ret = getstatusoutput(cmd)
        if status != 0:
            sys.stderr.write(f"\nError traceback:\n{cmd}\n{ret}")
            sys.stderr.write(f"\nFailed reason:\nfailed to submit job {self.pbs_file}\n")
            sys.exit(0)
        else:
            sleep(0.1)
            qid = ret.split(' ')[-1]
            return cmd, qid

    def submit_torque(self, depend_ids=[], is_dry=False):
        if len(depend_ids) > 0:
            cmd = f"qsub -W depend=afterok:{':'.join(depend_ids)} {self.pbs_file}"
        else:
            cmd = f"qsub {self.pbs_file}"

        # Dry run
        if is_dry:
            return cmd, self.job_name

        # Submit
        status, ret = getstatusoutput(cmd)
        while status == 208:
            # Failed to solve dependencies
            # Get dependencies
            running_depends = [i for i in depend_ids if validate_torque_job(i)]
            if len(running_depends) == len(depend_ids):
                sys.stderr.write(f"\nError traceback:\n{cmd}\n{ret}\n")
                sys.stderr.write(f"\nFailed reason:\nfailed to submit job {self.pbs_file}\n")
                sys.exit(0)

            if len(running_depends) > 0:
                cmd = f"qsub -W depend=afterok:{':'.join(running_depends)} {self.pbs_file}"
            else:
                cmd = f"qsub {self.pbs_file}"
            status, ret = getstatusoutput(cmd)

        if status != 0:
            sys.stderr.write(f"\nError traceback (status {status}):\n{cmd}\n{ret}\n")
            sys.stderr.write(f"\nFailed reason:\nfailed to submit job {self.pbs_file}\n")
            sys.exit(0)
        else:
            sleep(0.1)
            return cmd, ret


def etree_to_dict(t):
    """From https://stackoverflow.com/questions/2148119/how-to-convert-an-xml-string-to-a-dictionary

    Args:
        t (ElementTree): ET

    Returns:
        dict: dict of XML data
    """
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k:v[0] if len(v) == 1 else v for k, v in dd.items()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
              d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d


def validate_torque_job(job_id):
    """Whether job has been finished

    Args:
        job_id (str): job identifier

    Returns:
        bool: True for valid jobs, False for finished / not existed jobs
    """
    status, ret = getstatusoutput(f"qstat -x {job_id}")
    if status == 0:
        root = ET.fromstring(ret)
        d = etree_to_dict(root)
        job_state = d['Data']['Job']['job_state']
        if job_state == "C" or job_state == "E":
            return False
        else:
            return True
    else:
        # status == 153
        return False

def init(args):
    """Init pipeline toml file"""
    cwd = Path().resolve()
    file_name = Path(args.toml).name
    time_stamp = timestamp()
    toml_content = [
        '#Parameters',
        'pipeline = "{}"'.format(file_name),
        'version = "{}"'.format(time_stamp),
        'cwd = "{}"'.format(cwd),
        'work_dir = "{{cwd}}/qsub.{}"'.format(file_name),
        'sample_sheet = "{cwd}/samples.csv"',
        'pbs_scheduler = "torque"',
        'pbs_server = "mu02"',
        'pbs_queue = "batch"',
        'pbs_walltime = 1200',
        'threads = 32',
        '',
        '#Jobs',
        '[job.name]',
        'sample_sheet = "{sample_sheet}"',
        'input = "{sample.name}"',
        'output = "{cwd}/out/{sample.name}"',
        'log = "{work_dir}/logs/{sample.name}.tool.logs"',
        'shell = """',
        'mkdir -p {cwd}/out/{sample.name}',
        '"""',
    ]
    with open(args.toml, 'w') as out:
        for line in toml_content:
            out.write(line + '\n')


def run(args):
    """
    Run pipeline
    """
    toml_file = args.toml
    pl = Pipeline(toml_file, args.c)
    pl.init()
    pl.run(is_dry=False)


def check(args):
    """
    Perform a dry run
    """
    toml_file = args.toml
    pl = Pipeline(toml_file, args.c)
    pl.init()
    pl.run(is_dry=True)


def cancel(args):
    """Cancel a pipeline"""
    with open(args.csv, 'r') as f:
        for line in f:
            content = line.rstrip().split('\t')
            sample = content[0]
            qid = content[1]
            status, ret = getstatusoutput(f"qdel {qid}")
            if status != 0:
                sys.stderr.write(f"Failed to delete job {sample}, {ret}:\n")
    sys.stderr.write("All jobs canceled!\n")


def main():
    import argparse
    parser = argparse.ArgumentParser(
        prog='qbatch', description='a python-based job scheduler',
        epilog='use native torque/slurm job dependencies for build analysis pipeline'
    )
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s v{version}'.format(version=__version__))
    subparsers = parser.add_subparsers(help='commands')

    # Create new pipeline
    init_parser = subparsers.add_parser('init', help='init new pipeline')
    init_parser.add_argument('toml', metavar='toml',
                             help='path to output toml file')
    init_parser.set_defaults(func=init)

    # Run new pipeline
    run_parser = subparsers.add_parser('run', help="Run qbatch pipeline")
    run_parser.add_argument('toml', metavar='toml',
                            help='path to input toml file')
    run_parser.add_argument('-c', '--continue', dest='c', default=False, action='store_true',
                            help='continue jobs from checkpoint, (default: %(default)s)')
    run_parser.set_defaults(func=run)

    # Check pipeline files
    check_parser = subparsers.add_parser('check', help="Check qbatch pipeline without running it")
    check_parser.add_argument('toml', metavar='toml',
                              help='path to input toml file')
    check_parser.add_argument('-c', '--continue', dest='c', default=False, action='store_true',
                              help='continue jobs from checkpoint, (default: %(default)s)')
    check_parser.set_defaults(func=check)

    # Cancel a running pipeline
    cancel_parser = subparsers.add_parser('cancel', help="Cancel all unfinished jobs in a pipeline")
    cancel_parser.add_argument('csv', metavar='job file',
                               help='path to workdir/jobs')
    cancel_parser.set_defaults(func=cancel)

    # Parse parsers
    args = parser.parse_args()

    # Run function
    try:
        func = args.func
    except AttributeError:
        parser.error("qbatch only supports [init/run/check] arguments!")
    func(args)
