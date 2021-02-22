#
# num_gen/servers/server.py
#

import time
import array
import random
import signal
import struct

from multiprocessing import Process
from multiprocessing.shared_memory import SharedMemory


class BaseServer:
    """
    This server generates a random number.
    """
    __DFLT_SIGNUM = signal.SIGTERM
    __DFLT_START = 1000

    def __init__(self, start=__DFLT_START):
        self._start = start
        signal.signal(self.__DFLT_SIGNUM, self.shutdown)

    def start(self, sleep):
        """
        This method starts the process.
        """
        print("Starting ...")
        process = Process(target=self.random_num, args=(self._start, sleep))
        process.daemon = True
        process.start()
        #process.join()

    def random_num(self, start, sleep):
        """
        Generate an integer between the start value and the next order
        of magnitude.
        """
        shm = SharedMemory(name=self.get_sm_name(), create=True, size=5)
        print(f"SHM name: {shm.name}")
        buf = shm.buf
        int_to_four_bytes = struct.Struct('<I').pack
        buf[0] = 1 # Set the default run state to True.
        self._running = True

        while self._running:
            try:
                num = random.randrange(start, start*10-1)
                buf[1:] = int_to_four_bytes(num & 0xFFFFFFFF)
                self._running = (False
                                 if isinstance(buf[0], int) and buf[0] < 1
                                 else True)
                #print(f"_running: {self._running}, {buf[0]}")

                if self._running:
                    time.sleep(sleep)
                else:
                    print(f"_running: {self._running}, {buf[0]}")
                    self.shutdown()
            except Exception as e:
                print(f"Found error: {e}")
                self.shutdown()

        try:
            shm.close()
            shm.unlink()
        except FileNotFoundError:
            pass

    def shutdown(self, signum=__DFLT_SIGNUM, frame=None):
        """
        Signal shutdown method.
        """
        self._running = False

        if frame:
            print(f"Stopping with signum: {signum} ...")
        else:
            print(f"Stopping with SharedMemory ...")

    def get_sm_name(self):
        """
        The subclass version of this method must define a valid SM name.
        """
        raise NotImplementedError("The 'get_sm_name' class method must be "
                                  "defined in subclasses.")
