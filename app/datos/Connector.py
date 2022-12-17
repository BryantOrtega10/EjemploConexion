from abc import ABCMeta
from abc import abstractmethod


class Connector(metaclass=ABCMeta):
   
    @abstractmethod
    def select(self, fields=['*'], tables=[], where='', values=[] , order_by=[], group_by=[], from_s=0, limit=None):
        pass

    @abstractmethod
    def update(self, table, update=[], where='', values={}):
        pass

    @abstractmethod
    def insert(self, table, insert={}):
        pass

    @abstractmethod
    def delete(self, table, where='', values={}):
        pass

    @abstractmethod
    def raw_update(self, sql):
        pass

    @abstractmethod
    def raw_select(self, sql):
        pass
    

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass

    @abstractmethod
    def set_autocommit(self, value):
        pass