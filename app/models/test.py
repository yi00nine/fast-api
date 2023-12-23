from app.models.base import Base, SoftDeleteMixin, TimestampMixin
from sqlalchemy import INT, TIMESTAMP, BigInteger, Column, String
from sqlalchemy.orm import Session, Query
from typing import Optional
from typing_extensions import Self
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Test(TimestampMixin, SoftDeleteMixin, Base):
    __tablename__ = "test"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        comment="datasetID",
    )

    name = Column(String(50), index=True, nullable=False, comment="名称")
    major = Column(String(50), index=True, nullable=False, comment="专业")

    @classmethod
    def get_tests(
        cls,
        name: str,
        limit: int,
        offset: int,
        session: Session,
    ) -> Query:
        return session.query(cls).first()
