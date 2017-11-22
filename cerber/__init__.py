#!/usr/bin/python
import distutils.spawn
import json
import sys
import textwrap
from subprocess import Popen
from tempfile import NamedTemporaryFile


OUTFILE = 'seccomp_profile.json'
STRACEFILE = 'strace_statistics'


def strace_cmd_available():
    if not distutils.spawn.find_executable('strace'):
        print(textwrap.dedent('''
            System error! strace need to be installed\n
            Please install strace\n
            Execution aborted\n
        '''))
        sys.exit(1)


def trace(command):
    tmpfile = NamedTemporaryFile()
    cmd = ['strace', '-c', '-o']
    cmd.append(tmpfile.name)
    cmd.append('--')
    cmd.extend(command)
    Popen(cmd).wait()
    tmpfile.seek(0)
    strace = tmpfile.read().decode()
    tmpfile.close()
    return strace


def extract(syscalls):
    syscalls = syscalls.split("\n")
    calls = []
    record = False
    for line in syscalls:
        if line.startswith("---") and not record:
            record = True
            continue
        elif line.startswith("---") and record:
            break
        if record:
            infos = line.split()
            if len(infos) > 5:
                name = infos[5]
            else:
                name = infos[4]
            calls.append(name)
    return calls


def generate_seccomp(syscalls):
    seccomp = {
        'defaultAction': 'SCMP_ACT_ERRNO',
        'architecture': [
            'SCMP_ARCH_X86_64',
            'SCMP_ARCH_X86',
            'SCMP_ARCH_X32',
        ],
        'syscalls': []
    }
    for call in syscalls:
        call = {
            'name': call,
            'action': 'SCMP_ACT_ALLOW',
            'args': []
        }
        seccomp['syscalls'].append(call)
    return seccomp


def jsonify(seccomp):
    output = json.dumps(seccomp, indent=4)
    return output


def main():
    strace_cmd_available()
    raw_syscalls = trace(sys.argv[1:])
    syscalls = extract(raw_syscalls)
    seccomp = generate_seccomp(syscalls)

    with open(OUTFILE, 'w+') as f:
        f.write(jsonify(seccomp))

    with open(STRACEFILE, 'w+') as f:
        f.write(raw_syscalls)


if __name__ == "__main__":
    sys.exit(main())
