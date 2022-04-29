from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from db.database import Base


class Driver(Base):
    __tableName__ = "drivers"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    driver_ref = Column(String, unique=True, index=True)
    number = Column(Integer, index=True)
    code = Column(String, index=True)
    forename = Column(String, nullable=False, index=True)
    surname = Column(String, nullable=False, index=True)
    date_of_birth = Column(Date, nullable=False, index=True)
    nationality = Column(String, nullable=False, index=True)
    url = Column(String, nullable=False, index=True)

    lap_times = relationship("LapTime", back_populates="driver")
