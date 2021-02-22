#
# num_gen/servers/server_02.py
#

from .server import BaseServer


class Server(BaseServer):
    """
    This server generates a random number.
    """
    _DFLT_SM_NAME = 'Server02'

    def get_sm_name(self):
        """
        This method must define a valid SharedMemory name.
        """
        return self._DFLT_SM_NAME
