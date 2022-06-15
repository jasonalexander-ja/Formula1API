from typing import Optional, List
from datetime import date, time

from pydantic_collections import BaseCollectionModel
from pydantic import BaseModel

from db import database as sch


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


class PingResponseBase(BaseModel):
    name: str
    status: str
    version: str


class PingResponse(PingResponseBase):
    pass


class ResultResponseBase(BaseModel):
    constructor_id: int = 0
    driver_id: int = 0
    position: Optional[int]
    status: str = ""


class ResultResponse(ResultResponseBase):
    @classmethod
    def from_db_class(cls, db_obj: sch.Results, status: str) -> "ResultResponse":
        res = cls()
        res.constructor_id = db_obj.constructor_id
        res.driver_id = db_obj.driver_id
        res.position = db_obj.position
        res.status = status
        return res

    class Config:
        schema_extra = {
            "constructor_id": 166,
            "driver_id": 816,
            "position": 14,
            "status": "Finished"
        }


class ResultResList(BaseCollectionModel[ResultResponse]):
    pass


class DriverResponseBase(BaseModel):
    code: str = ""
    dob: str = ""
    driver_id: int = 0
    forename: str = ""
    nationality: str = ""
    number: int = 0
    surname: str = ""
    url: str = ""


class DriverResponse(DriverResponseBase):
    @classmethod
    def from_db_class(cls, driver: sch.Driver) -> "DriverResponse":
        dob: date = driver.date_of_birth
        res = cls()
        res.code = driver.code
        res.dob = f"{dob.day}/{dob.month}/{dob.year}"
        res.driver_id = driver.id
        res.forename = driver.forename
        res.nationality = driver.nationality
        res.number = driver.number
        res.surname = driver.surname
        res.url = driver.url
        return res

    class Config:
        schema_extra = {
            "code": "HAM",
            "dob": "7/1/1985",
            "driver_id": 1,
            "forename": "Lewis",
            "nationality": "British",
            "number": 44,
            "surname": "Hamilton",
            "url": "http://en.wikipedia.org/wiki/Lewis_Hamilton"
        }


class LapTimeResponseBase(BaseModel):
    lap_number: int = 0
    seconds: float = 0


class LapTimeResponse(LapTimeResponseBase):
    @classmethod
    def from_db_class(cls, lap_time: sch.LapTime) -> "LapTimeResponse":
        res = cls()
        res.lap_number = lap_time.lap
        res.seconds = lap_time.time_milli / 1000
        return res

    class Config:
        schema_extra = {
            "lap_number": 1,
            "seconds": 100.573
        }


class DriverLapTimeResponseBase(BaseModel):
    driver_id: int = 0
    laptimes: List[LapTimeResponseBase] = []


class DriverLapTimeResponse(DriverLapTimeResponseBase):
    class Config:
        schema_extra = {
            "driver_id": 1,
            "laptimes": [{"lap_number": 1,  "seconds": 100.573}]
        }


class DriverLapTimeResList(BaseCollectionModel[DriverLapTimeResponse]):
    pass
