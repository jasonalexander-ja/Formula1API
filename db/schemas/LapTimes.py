from sqlalchemy import Column, ForeignKey, Integer, Time
from sqlalchemy.orm import relationship

from db.database import Base


class LapTime(Base):
    __tablename__ = "lap_times"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    lap = Column(Integer, nullable=False, index=True)
    position = Column(Integer, nullable=False, index=True)
    time = Column(Time, nullable=False, index=True)
    time_milli = Column(Integer, nullable=False, index=True)

    race_id = Column(Integer, ForeignKey("races.id"))
    driver_id = Column(Integer, ForeignKey("drivers.id"))

    race = relationship("Race", back_populates="lap_times")
    driver = relationship("Driver", back_populates="lap_times")
