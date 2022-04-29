from sqlalchemy import Column, Integer, String

from db.database import Base


class Constructor(Base):
    __tableName__ = "constructors"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    reference = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False, index=True)
    nationality = Column(String, nullable=False, index=True)
    url = Column(String, nullable=False, index=True)
