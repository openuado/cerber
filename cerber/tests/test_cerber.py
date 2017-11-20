import textwrap
import unittest

import cerber


class TestExtract(unittest.TestCase):

    def setUp(self):
        # simulate strace for docker run hello-world
        self.strace_output = textwrap.dedent('''
            % time     seconds  usecs/call     calls    errors syscall
            ------ ----------- ----------- --------- --------- ----------------
            100.00    0.001100          29        38         2 futex
            0.00    0.000000           0        11         4 read
            0.00    0.000000           0         5           open
            0.00    0.000000           0         9           close
            0.00    0.000000           0        24        24 stat
            0.00    0.000000           0         5           fstat
            0.00    0.000000           0        38           mmap
            0.00    0.000000           0        14           mprotect
            0.00    0.000000           0         2           munmap
            0.00    0.000000           0         3           brk
            0.00    0.000000           0       120           rt_sigaction
            0.00    0.000000           0        11           rt_sigprocmask
            0.00    0.000000           0         3           ioctl
            0.00    0.000000           0         6         6 access
            0.00    0.000000           0         1           sched_yield
            0.00    0.000000           0         4           socket
            0.00    0.000000           0         1           connect
            0.00    0.000000           0         1           shutdown
            0.00    0.000000           0         2           bind
            0.00    0.000000           0         1           getsockname
            0.00    0.000000           0         1           getpeername
            0.00    0.000000           0         3           setsockopt
            0.00    0.000000           0         4           clone
            0.00    0.000000           0         1           execve
            0.00    0.000000           0         1           getrlimit
            0.00    0.000000           0         2           sigaltstack
            0.00    0.000000           0         1           arch_prctl
            0.00    0.000000           0         1           gettid
            0.00    0.000000           0         1           sched_getaffinity
            0.00    0.000000           0         1           set_tid_address
            0.00    0.000000           0         7           epoll_wait
            0.00    0.000000           0         1           epoll_ctl
            0.00    0.000000           0         1           openat
            0.00    0.000000           0         1           readlinkat
            0.00    0.000000           0         4           pselect6
            0.00    0.000000           0         1           set_robust_list
            0.00    0.000000           0         1           epoll_create1
            0.00    0.000000           0         2           getrandom
            ------ ----------- ----------- --------- --------- ----------------
            100.00    0.001100                   333        36 total
        ''')

    def test_extract_strace(self):
        # 38 syscalls must be available
        extract = cerber.extract(self.strace_output)
        self.assertEqual(38, len(extract))
        self.assertIn('sched_yield', extract)
