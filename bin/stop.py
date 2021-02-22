#!/usr/bin/env python
#
# Stop all servers.
#

import os
import sys

#from subprocess import Popen
from multiprocessing.shared_memory import SharedMemory

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(BASE_DIR)

from num_gen.servers import Server01
from num_gen.servers import Server02


def shutdown(*, names=()):
    for name in names:
        try:
            shm = SharedMemory(name=name, create=False)
            shm.buf[0] = 0 # Interrupt the while loops.
            shm.close()
        except FileNotFoundError:
            #Popen(['/usr/bin/killall', 'start_servers.py'])
            pass


if __name__ == '__main__':
    import sys

    names = (Server01._DFLT_SM_NAME, Server02._DFLT_SM_NAME)
    shutdown(names=names)
    sys.exit(0)
