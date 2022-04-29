from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from db.database import Base


class Circuit(Base):
    __tableName__ = "circuits"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    circuit_ref = Column(String, unique=True, index=True)
    name = Column(String, nullable=False, index=True)
    location = Column(String, nullable=False, index=True)
    country = Column(String, nullable=False, index=True)
    latitude = Column(Float, nullable=False, index=True)
    longitude = Column(Float, nullable=False, index=True)
    alt = Column(Integer, index=True)
    url = Column(String, nullable=False, index=True)

    races = relationship("Race", back_populates="circuit")
