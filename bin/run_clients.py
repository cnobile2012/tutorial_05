#!/usr/bin/env python
#
# run_clients.py: Get data from all servers.
#

import os
import sys
import time

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(BASE_DIR)

from num_gen.clients import Client01, Client02


def start():
    sleep = 1
    clnt1 = Client01()
    clnt2 = Client02()

    for i  in range(20):
        time.sleep(1)
        print(f"Client01: {clnt1.get_data()} Client02: {clnt2.get_data()}")

    #clnt1.close_shm()
    #clnt2.close_shm()


if __name__ == '__main__':
    try:
        start()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
