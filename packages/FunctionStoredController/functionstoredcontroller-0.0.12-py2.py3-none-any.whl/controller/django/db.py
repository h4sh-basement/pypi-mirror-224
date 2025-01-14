from django.db import connections

from controller.core.db import AbstractDataBase


class DjangoDataBase(AbstractDataBase):

    def __init__(self, db_name: str = 'default', *args):
        super(DjangoDataBase, self).__init__(*args)
        self.db_name = db_name

    def __enter__(self):
        self.conn = connections[self.db_name]
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
