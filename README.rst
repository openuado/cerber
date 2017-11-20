======
Cerber
======
A straightforward command line tool for generate seccomp json file

Install
=======
.. code:: shell

    $ git clone https://github.com/gr0und-s3ct0r/cerber
    $ cd cerber
    $ pip install pbr
    $ python setup.py install # cerber is now installed in your environment

Usage
=====
.. code:: shell

    $ cerber docker run hello-world # a seccomp_profil.json was created in the current directory
    $ ls
    seccomp_profil.json
    $ cat seccomp_profil.json
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

and now you can assign this security profil to your container at run:

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

Authors
=======
- `Sébastien Boyron (dj4ngo) <https://github.com/dj4ngo>`_
- `Hervé Beraud (4383) <https://github.com/4383>`_
