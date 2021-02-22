#
# num_gen/clients/client_01.py
#

from .client import BaseClient
from num_gen.servers import Server01


class Client(BaseClient):

    def __init__(self):
        super().__init__(Server01._DFLT_SM_NAME)
