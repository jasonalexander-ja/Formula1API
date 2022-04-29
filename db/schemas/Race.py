from sqlalchemy import Column, Integer, String, Date, ForeignKey, Time
from sqlalchemy.orm import relationship

from db.database import Base


class Race(Base):
    __tablename__ = "races"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    year = Column(Integer, nullable=False, index=True)
    round = Column(Integer, nullable=False, index=True)
    name = Column(String, nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)
    time = Column(Time, index=True)
    url = Column(String, nullable=False, index=True)

    circuit_id = Column(Integer, ForeignKey("circuits.id"))

    circuit = relationship("Circuit", back_populates="races")
    lap_times = relationship("LapTime", back_populates="race")
