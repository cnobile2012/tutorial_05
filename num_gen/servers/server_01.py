#
# num_gen/servers/server_01.py
#

from .server import BaseServer


class Server(BaseServer):
    """
    This server generates a random number.
    """
    _DFLT_SM_NAME = 'Server01'

    @classmethod
    def get_sm_name(cls):
        """
        The subclass version of this method must define a valid SM name.
        """
        return self._DFLT_SM_NAME


if __name__ == '__main__':
    import sys

    start = 1000
    sleep = 5 # 5 seconds between generated integers

    try:
        svr = Server(start=start)
        svr.start(sleep)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    else:
        sys.exit(0)
