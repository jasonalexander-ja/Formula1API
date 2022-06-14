from typing import List, Union
import csv

from db.database import Status
from models.Status import Status as PdStatus

from db.database import Constructor
from models.Constructor import Constructor as PdConstructor

from db.database import Circuit
from models.Circuit import Circuit as PdCircuit

from db.database import Driver
from models.Driver import Driver as PdDriver

from db.database import LapTime
from models.LapTime import LapTime as PdLapTime

from db.database import Results
from models.Results import Results as PdResults

from db.database import Race
from models.Race import Race as PdRace


def sanitise_value(value: str) -> Union[str, None]:
    return value if value != '\\N' else None


def extract_statuses(filepath: str) -> List[Status]:
    with open(filepath, newline='', encoding="utf8") as file:
        data: csv._reader = csv.reader(file)
        next(data)
        pydantics = map(
            lambda row: PdStatus(
                given_id=sanitise_value(row[0]),
                status_name=sanitise_value(row[1])
            ),
            data
        )
        orm_models = map(
            lambda s: Status(given_id=s.given_id, status_name=s.status_name),
            pydantics
        )
        return list(orm_models)


def extract_constructors(filepath: str) -> List[Constructor]:
    with open(filepath, newline='', encoding="utf8") as file:
        data: csv._reader = csv.reader(file)
        next(data)
        pydantics = map(
            lambda row: PdConstructor(
                given_id=sanitise_value(row[0]),
                reference=sanitise_value(row[1]),
                name=sanitise_value(row[2]),
                nationality=sanitise_value(row[3]),
                url=sanitise_value(row[4])
            ),
            data
        )
        orm_models = map(
            lambda s: Constructor(
                given_id=s.given_id,
                reference=s.reference,
                name=s.name,
                nationality=s.nationality,
                url=s.url
            ),
            pydantics
        )
        return list(orm_models)


def extract_circuit(filepath: str) -> List[Circuit]:
    with open(filepath, newline='', encoding="utf8") as file:
        data: csv._reader = csv.reader(file)
        next(data)
        pydantics = map(
            lambda row: PdCircuit(
                given_id=sanitise_value(row[0]),
                circuit_ref=sanitise_value(row[1]),
                name=sanitise_value(row[2]),
                location=sanitise_value(row[3]),
                country=sanitise_value(row[4]),
                latitude=sanitise_value(row[5]),
                longitude=sanitise_value(row[6]),
                alt=sanitise_value(row[7]),
                url=sanitise_value(row[8])
            ),
            data
        )
        orm_models = map(
            lambda s: Circuit(
                given_id=s.given_id,
                circuit_ref=s.circuit_ref,
                name=s.name,
                location=s.location,
                country=s.country,
                latitude=s.latitude,
                longitude=s.longitude,
                alt=s.alt,
                url=s.url
            ),
            pydantics
        )
        return list(orm_models)


def extract_driver(filepath: str) -> List[Driver]:
    with open(filepath, newline='', encoding="utf8") as file:
        data: csv._reader = csv.reader(file)
        next(data)
        pydantics = map(
            lambda row: PdDriver(
                given_id=sanitise_value(row[0]),
                driver_ref=sanitise_value(row[1]),
                number=sanitise_value(row[2]),
                code=sanitise_value(row[3]),
                forename=sanitise_value(row[4]),
                surname=sanitise_value(row[5]),
                date_of_birth=sanitise_value(row[6]),
                nationality=sanitise_value(row[7]),
                url=sanitise_value(row[8])
            ),
            data
        )
        orm_models = map(
            lambda s: Driver(
                given_id=s.given_id,
                driver_ref=s.driver_ref,
                number=s.number,
                code=s.code,
                forename=s.forename,
                surname=s.surname,
                date_of_birth=s.date_of_birth,
                nationality=s.nationality,
                url=s.url
            ),
            pydantics
        )
        return list(orm_models)


def extract_lap_time(filepath: str) -> List[LapTime]:
    with open(filepath, newline='', encoding="utf8") as file:
        data: csv._reader = csv.reader(file)
        next(data)
        pydantics = map(
            lambda row: PdLapTime(
                race_id=sanitise_value(row[0]),
                driver_id=sanitise_value(row[1]),
                lap=sanitise_value(row[2]),
                position=sanitise_value(row[3]),
                time_str=sanitise_value(row[4]),
                time_milli=sanitise_value(row[5])
            ),
            data
        )
        orm_models = map(
            lambda s: LapTime(
                race_id=s.race_id,
                driver_id=s.driver_id,
                lap=s.lap,
                position=s.position,
                time_str=s.time_str,
                time_milli=s.time_milli
            ),
            pydantics
        )
        return list(orm_models)


def extract_results(filepath: str) -> List[Results]:
    with open(filepath, newline='', encoding="utf8") as file:
        data: csv._reader = csv.reader(file)
        next(data)
        pydantics = map(
            lambda row: PdResults(
                given_id=sanitise_value(row[0]),
                race_id=sanitise_value(row[1]),
                driver_id=sanitise_value(row[2]),
                constructor_id=sanitise_value(row[3]),
                number=sanitise_value(row[4]),
                grid=sanitise_value(row[5]),
                position=sanitise_value(row[6]),
                position_text=sanitise_value(row[7]),
                position_order=sanitise_value(row[8]),
                points=sanitise_value(row[9]),
                laps=sanitise_value(row[10]),
                time_str=sanitise_value(row[11]),
                time_milli=sanitise_value(row[12]),
                rank=sanitise_value(row[13]),
                fastest_lap=sanitise_value(row[14]),
                fastest_time=sanitise_value(row[15]),
                fastest_speed=sanitise_value(row[16]),
                status_id=sanitise_value(row[17])
            ),
            data
        )
        orm_models = map(
            lambda s: Results(
                given_id=s.given_id,
                race_id=s.race_id,
                driver_id=s.driver_id,
                constructor_id=s.constructor_id,
                number=s.number,
                grid=s.grid,
                position=s.position,
                position_text=s.position_text,
                position_order=s.position_order,
                points=s.points,
                laps=s.laps,
                time_str=s.time_str,
                time_milli=s.time_milli,
                rank=s.rank,
                fastest_lap=s.fastest_lap,
                fastest_time=s.fastest_time,
                fastest_speed=s.fastest_speed,
                status_id=s.status_id
            ),
            pydantics
        )
        return list(orm_models)


def extract_races(filepath: str) -> List[Race]:
    with open(filepath, newline='', encoding="utf8") as file:
        data: csv._reader = csv.reader(file)
        next(data)
        pydantics = map(
            lambda row: PdRace(
                given_id=sanitise_value(row[0]),
                year=sanitise_value(row[1]),
                round=sanitise_value(row[2]),
                circuit_id=sanitise_value(row[3]),
                name=sanitise_value(row[4]),
                date=sanitise_value(row[5]),
                time=sanitise_value(row[6]),
                url=sanitise_value(row[7])
            ),
            data
        )
        orm_models = map(
            lambda s: Race(
                given_id=s.given_id,
                year=s.year,
                round=s.round,
                name=s.name,
                date=s.date,
                time=s.time,
                url=s.url
            ),
            pydantics
        )
        return list(orm_models)
