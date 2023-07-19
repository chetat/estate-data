import abc

from app.models import db


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, item: db.Model):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> db.Model:
        raise NotImplementedError
