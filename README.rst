======
Cerber
======

.. image:: https://travis-ci.org/gr0und-s3ct0r/cerber.svg?branch=devel
       :target: https://travis-ci.org/gr0und-s3ct0r/cerber
.. image:: https://badge.fury.io/py/cerber.svg
       :target: https://badge.fury.io/py/cerber

A straightforward command line tool for generate seccomp json profile

Overview
========
Seccomp (short for secure computing mode) is a computer security 
facility in the Linux kernel.
Seccomp allows a process to make a one-way transition into a "secure"
state where it cannot make any system calls except exit(),
sigreturn(), read() and write() to already-open file descriptors.
Should it attempt any other system calls, the kernel will terminate
the process with SIGKILL or SIGSYS.
In this sense, it does not virtualize the system's resources but isolates 
the process from them entirely.

Seccomp profile is used with by a lot of applications like:

- docker
- firefox
- systemd
- openssh
- chrome
- and more...

Cerber help you to generate seccomp profile that you can
use with docker per example.

Prerequisites
=============

- Linux
- Python3.5+
- Strace

Install
=======
.. code:: shell

    $ pip install cerber

Usage
=====

Generate a seccomp_profile.json in your current directory:

.. code:: shell

    $ cerber docker run hello-world
    $ ls
    seccomp_profile.json
    $ cat seccomp_profile.json
    {
        "defaultAction": "SCMP_ACT_ERRNO", 
        "architecture": [
            "SCMP_ARCH_X86_64", 
            "SCMP_ARCH_X86", 
            "SCMP_ARCH_X32"
        ], 
        "syscalls": [
            {
                "action": "SCMP_ACT_ALLOW", 
                "args": [], 
                "name": "read"
            }, 
            ...
            {
                "action": "SCMP_ACT_ALLOW", 
                "args": [], 
                "name": "execve"
            }, 
            {
                "action": "SCMP_ACT_ALLOW", 
                "args": [], 
                "name": "arch_prctl"
            }
        ]
    }

Now you can assign this seccomp profile to your container at run:

.. code:: shell

    $ docker run \
    --rm \
    --security-opt="no-new-privileges" \
    --security-opt seccomp=seccomp_profile.json \
    hello-world # you can get the following output for docker hello world

    Hello from Docker!
    This message shows that your installation appears to be working correctly.

    To generate this message, Docker took the following steps:
    1. The Docker client contacted the Docker daemon.
    ...
    For more examples and ideas, visit:
     https://docs.docker.com/engine/userguide/

Becareful to generate seccomp profile with cerber on the same cpu architecture
that your production environment (where you want run your container).

Features
========

- detect syscalls
- generate seccomp profile from detected syscalls

Contribute
==========

.. code:: shell

    $ git clone https://github.com/gr0und-s3ct0r/cerber
    $ cd cerber
    $ pipenv install pbr
    $ pipenv shell # generate a virtual environment
    $ python setup.py develop # install cerber in development mode
    $ pip install -e .[test] # install testing dependencies
    $ # make your changes
    $ tox

Further readings
================
- `docker security seccomp documentation <https://docs.docker.com/engine/security/seccomp/#pass-a-profile-for-a-container>`_
- `docker seccomp json format <https://antitree.com/2017/09/docker-seccomp-json-format/>`_
- `docker no new privileges security flag <https://www.projectatomic.io/blog/2016/03/no-new-privs-docker/>`_

Original Authors
================
- `Sébastien Boyron (dj4ngo) <https://github.com/dj4ngo>`_
- `Hervé Beraud (4383) <https://github.com/4383>`_
