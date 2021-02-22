#!/usr/bin/env python
#
# Start all the servers.
#

import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(BASE_DIR)

from num_gen.servers import Server01, Server02


def start():
    sleep = 5
    # Server 1
    start = 1000
    srv = Server01(start=start)
    srv.start(sleep)
    # Server 2
    start = 10000
    srv = Server02(start=start)
    srv.start(sleep)


if __name__ == '__main__':
    try:
        start()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
