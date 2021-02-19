#!/usr/bin/env python
#
# Stop all servers.
#

import time

from multiprocessing.shared_memory import SharedMemory

from num_gen.servers import Server01
from num_gen.servers import Server02


def shutdown(*, names=[]):
    for name in names:
        shm = SharedMemory(name=name, create=False)
        shm.buf[4] = 0 # Stop the while loops.
        shm.close()
        time.sleep(5)
        shm.unlink()


if __name__ == '__main__':
    import sys

    names = [Server01.get_sm_name(), Server02.get_sm_name()]
    shutdown(names=names)
    sys.exit(0)
