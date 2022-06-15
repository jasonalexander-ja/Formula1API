from typing import Optional, List

from sqlalchemy.orm import Session

from db import database as sch
import models


def get_driver(id: int, db: Session) -> Optional[sch.Driver]:
    return db.query(sch.Driver).filter(sch.Driver.id == id).first()


def get_statuses(db: Session) -> List[sch.Status]:
    return db.query(sch.Status).all()


def find_status(status_list: List[sch.Status], id: int) -> str:
    for stat in status_list:
        if stat.id == id:
            return stat.status_name
    return ""


def get_race_results(id: int, db: Session) -> List[models.ResultResponse]:
    results: List[sch.Results] = db.query(sch.Results).filter(
        sch.Results.race_id == id
    ).all()
    status_list = get_statuses(db)
    results_mapped = map(
        lambda r: models.ResultResponse.from_db_class(
            r,
            find_status(status_list, r.race_id)
        ),
        results
    )
    return list(results_mapped)


def get_lap_time(
    race_id: int,
    driver_id: int,
    db: Session
) -> models.DriverLapTimeResponse:
    results: List[sch.LapTime] = db.query(sch.LapTime).filter(
        sch.LapTime.race_id == race_id
    ).filter(
        sch.LapTime.driver_id == driver_id
    ).all()
    lap_times = map(
        lambda l: models.LapTimeResponse.from_db_class(l),
        results
    )
    driver_laps = models.DriverLapTimeResponse()
    driver_laps.driver_id = driver_id
    driver_laps.laptimes = list(lap_times)
    return driver_laps


def get_lap_times(
    race_id: int,
    driver_ids: List[int],
    db: Session
) -> List[models.DriverLapTimeResponse]:
    results = map(
        lambda dId: get_lap_time(race_id, dId, db),
        driver_ids
    )
    return list(results)
