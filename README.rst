======
Cerber
======
A straightforward command line tool for generate seccomp json file

Install
=======
.. code:: shell

    $ git clone https://github.com/gr0und-s3ct0r/cerber
    $ cd cerber
    $ python setup.py install # cerber is now installed in your environment

Usage
=====
.. code:: shell

    $ cerber docker run hello-world # display output on stdout
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

Or save output to json file

.. code:: shell

    $ cerber docker run hello-world > seccomp.json # save output inside seccomp.json file

Contribute
==========

.. code:: shell

    $ git clone https://github.com/gr0und-s3ct0r/cerber
    $ cd cerber
    $ pipenv shell # generate a virtual environment
    $ python setup.py develop # cerber is now installed in your virtual environment on develop mode

Further reading
===============
- `docker seccomp json format <https://antitree.com/2017/09/docker-seccomp-json-format/>`_


Authors
=======
- `Sébastien Boyron (dj4ngo) <https://github.com/dj4ngo>`_
- `Hervé Beraud (4383) <https://github.com/4383>`_
