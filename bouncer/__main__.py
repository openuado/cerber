#!/usr/bin/python
import json
import sys
from subprocess import Popen, PIPE


def trace(command):
    cmd = ['strace', '-c']
    cmd.extend(command)
    process = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = process.communicate()
    return err.decode()


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
    raw_syscalls = trace(sys.argv[1:])
    syscalls = extract(raw_syscalls)
    seccomp = generate_seccomp(syscalls)
    print(jsonify(seccomp))


if __name__ == "__main__":
    main()
