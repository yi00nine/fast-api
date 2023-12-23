from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, event
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property

class CustomBase:
  def to_dict(self):
    dict_copy = self.__dict__.copy()
    dict_copy.pop("_sa_instance_state", None)
    return dict_copy
  
Base = declarative_base(cls=CustomBase)

class TimestampMixin:
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    created_at._creation_order = 9000
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at._creation_order = 9000

    @staticmethod
    def _updated_at(mapper, connection, target):
        target.updated_at = datetime.utcnow()

    @classmethod
    def __declare_last__(cls):
        event.listen(cls, "before_update", cls._updated_at)

class SoftDeleteMixin:
    deleted_at = Column(DateTime, nullable=True)
    deleted_at._creation_order = 9000

    @hybrid_property
    def alive(self):
        return self.deleted_at == None

    @alive.expression
    def is_alive(cls):
        return cls.deleted_at == None