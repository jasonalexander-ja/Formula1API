from typing import Optional
from datetime import date, time

from pydantic import BaseModel

import response_model as rm


class StatusBase(BaseModel):
    status_name: str


class Status(StatusBase):
    id: int = 0
    given_id: int

    class Config:
        orm_mode = True


class ResultsBase(BaseModel):
    number: Optional[int]
    grid: int
    position: Optional[int]
    position_text: str
    position_order: int
    points: float
    laps: int
    time_str: Optional[str]
    time_milli: Optional[int]
    rank: Optional[int]
    fastest_lap: Optional[int]
    fastest_time: Optional[str]
    fastest_speed: Optional[float]

    race_id: int
    status_id: int
    driver_id: int
    constructor_id: int


class Results(ResultsBase):
    id: int = 0
    given_id: int

    class Config:
        orm_mode = True


class RaceBase(BaseModel):
    year: int
    round: int
    name: str
    date: date
    time: Optional[time]
    url: str

    circuit_id: int


class Race(RaceBase):
    id: int = 0
    given_id: int

    class Config:
        orm_mode = True


class LapTimeBase(BaseModel):
    lap: int
    position: int
    time_str: str
    time_milli: int

    race_id: int
    driver_id: int


class LapTime(LapTimeBase):
    id: int = 0

    class Config:
        orm_mode = True


class DriverBase(BaseModel):
    driver_ref: str
    number: Optional[int]
    code: Optional[str]
    forename: str
    surname: str
    date_of_birth: date
    nationality: str
    url: str


class Driver(DriverBase):
    id: int = 0
    given_id: int

    class Config:
        orm_mode = True


class ConstructorBase(BaseModel):
    reference: str
    name: str
    nationality: str
    url: str


class Constructor(ConstructorBase):
    id: int = 0
    given_id: int

    class Config:
        orm_mode = True


class CircuitBase(BaseModel):
    circuit_ref: str
    name: str
    location: str
    country: str
    latitude: float
    longitude: float
    alt: Optional[int]
    url: str


class Circuit(CircuitBase):
    id: int = 0
    given_id: int

    class Config:
        orm_mode = True
