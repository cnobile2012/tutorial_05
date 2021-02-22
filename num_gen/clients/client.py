#
# num_gen/clients/client.py
#

import struct

from multiprocessing.shared_memory import SharedMemory


class BaseClient:
    """
    Base client class.
    """

    def __init__(self, name):
        self._shm = SharedMemory(name=name, create=False, size=5)
        print(f"SHM name: {self._shm.name}")

    def get_data(self):
        buf = self._shm.buf
        return struct.unpack('<I', buf[1:]) # And back again

    def close_shm(self):
        self._shm.close()
