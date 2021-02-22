#
# num_gen/clients/client_02.py
#

from .client import BaseClient
from num_gen.servers import Server02


class Client(BaseClient):

    def __init__(self):
        super().__init__(Server02._DFLT_SM_NAME)
