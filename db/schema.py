from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Time
from sqlalchemy.orm import relationship

from .database import Base


class Circuit(Base):
    __tablename__ = "circuits"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    given_id = Column(Integer, unique=True, index=True)
    circuit_ref = Column(String, unique=True, index=True)
    name = Column(String, nullable=False, index=True)
    location = Column(String, nullable=False, index=True)
    country = Column(String, nullable=False, index=True)
    latitude = Column(Float, nullable=False, index=True)
    longitude = Column(Float, nullable=False, index=True)
    alt = Column(Integer, index=True)
    url = Column(String, nullable=False, index=True)

    races = relationship("Race", back_populates="circuit")


class Constructor(Base):
    __tablename__ = "constructors"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    given_id = Column(Integer, unique=True, index=True)
    reference = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False, index=True)
    nationality = Column(String, nullable=False, index=True)
    url = Column(String, nullable=False, index=True)


class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    given_id = Column(Integer, unique=True, index=True)
    driver_ref = Column(String, unique=True, index=True)
    number = Column(Integer, index=True)
    code = Column(String, index=True)
    forename = Column(String, nullable=False, index=True)
    surname = Column(String, nullable=False, index=True)
    date_of_birth = Column(Date, nullable=False, index=True)
    nationality = Column(String, nullable=False, index=True)
    url = Column(String, nullable=False, index=True)

    lap_times = relationship("LapTime", back_populates="driver")
    results = relationship("Results", back_populates="driver")


class LapTime(Base):
    __tablename__ = "lap_times"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    lap = Column(Integer, nullable=False, index=True)
    position = Column(Integer, nullable=False, index=True)
    time_str = Column(String, nullable=False, index=True)
    time_milli = Column(Integer, nullable=False, index=True)

    race_id = Column(Integer, ForeignKey("races.id"))
    driver_id = Column(Integer, ForeignKey("drivers.id"))

    race = relationship("Race", back_populates="lap_times")
    driver = relationship("Driver", back_populates="lap_times")


class Race(Base):
    __tablename__ = "races"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    given_id = Column(Integer, unique=True, index=True)
    year = Column(Integer, nullable=False, index=True)
    round = Column(Integer, nullable=False, index=True)
    name = Column(String, nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)
    time = Column(Time, index=True)
    url = Column(String, nullable=False, index=True)

    circuit_id = Column(Integer, ForeignKey("circuits.id"))

    circuit = relationship("Circuit", back_populates="races")
    lap_times = relationship("LapTime", back_populates="race")
    result = relationship("Results", back_populates="race")


class Status(Base):
    __tablename__ = "statuses"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    given_id = Column(Integer, unique=True, index=True)
    status_name = Column(String, unique=True, nullable=False, index=True)


class Results(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    given_id = Column(Integer, unique=True, index=True)
    number = Column(Integer, index=True)
    grid = Column(Integer, nullable=False, index=True)
    position = Column(Integer, index=True)
    position_text = Column(String, nullable=False, index=True)
    position_order = Column(Integer, nullable=False, index=True)
    points = Column(Float, nullable=False, index=True)
    laps = Column(Integer, nullable=False, index=True)
    time_str = Column(String, index=True)
    time_milli = Column(Integer, index=True)
    rank = Column(Integer, index=True)
    fastest_lap = Column(Integer, index=True)
    fastest_time = Column(String, index=True)
    fastest_speed = Column(Float, index=True)

    race_id = Column(Integer, ForeignKey("races.id"))
    status_id = Column(Integer, ForeignKey("statuses.id"))
    driver_id = Column(Integer, ForeignKey("drivers.id"))
    constructor_id = Column(Integer, ForeignKey("constructors.id"))

    race = relationship("Race", back_populates="result")
    driver = relationship("Driver", back_populates="results")
