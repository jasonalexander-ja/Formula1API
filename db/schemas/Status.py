from sqlalchemy import Column, Integer, String

from db.database import Base


class Status(Base):
    __tableName__ = "statuses"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    status_name = Column(String, unique=True, nullable=False, index=True)
