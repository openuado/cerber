# Bouncer
A straightforward tool for generate seccomp json

## Usage
```sh
$ python bouncer docker run hello-world # display output on stdout
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
```

Or save output to json file
```sh
$ python bouncer docker run hello-world > seccomp.json # save output inside seccomp.json file
```

## Further reading
- [docker seccomp json format](https://antitree.com/2017/09/docker-seccomp-json-format/)


## Contributors
- [Hervé Beraud (4383)](https://github.com/4383)
- [Sébastien Boyron (dj4ngo)](https://github.com/dj4ngo)
