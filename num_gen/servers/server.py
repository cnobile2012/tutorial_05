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
        self._running = True
        self._shm = None
        signal.signal(self.__DFLT_SIGNUM, self.shutdown)

    def start(self, sleep):
        """
        This method starts the process.
        """
        print(f"Starting ...")
        self._shm = SharedMemory(name=self.get_sm_name(), create=True, size=5)
        print(f"shm name: {self._shm.name}")
        process = Process(target=self.random_num, args=(self._start, sleep))
        process.daemon = False
        process.start()
        #process.join()

    def random_num(self, seed, sleep):
        """
        Generate an integer between the seed value and the next order
        of magnitude.
        """
        buf = self._shm.buf
        int_to_four_bytes = struct.Struct('<I').pack
        buf[4] = 1 # Set the default True

        while self._running:
            try:
                num = random.randrange(seed, seed*10-1)
                buf[:4] = int_to_four_bytes(num & 0xFFFFFFFF)
                #num = struct.unpack('<I', buf[:4]) # And back again
                self._running = (False
                                 if isinstance(buf[4], int) and buf[4] < 1
                                 else True)
                #print(f"_running: {self._running}, {buf[4]}")

                if self._running:
                    time.sleep(sleep)
                else:
                    self.shutdown()
            except Exception as e:
                print(f"Found error: {e}")
                self.shutdown()

    def get_int(self):
        """
        Get the random integer.
        """
        return self._rand_int

    def shutdown(self, signum=__DFLT_SIGNUM, frame=None):
        """
        Signal shutdown method.
        """
        self._running = False
        self._shm.close()
        #self._shm.unlink()

        if frame:
            print(f"Stopping with signum: {signum} ...")
        else:
            print(f"Stopping with SharedMemory ...")

    @classmethod
    def get_sm_name(self):
        """
        The subclass version of this method must define a valid SM name.
        """
        raise NotImplementedError("The 'get_sm_name' class method must be "
                                  "defined in subclasses.")
