from typing import Union

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from db.database import SessionLocal
import response_model as rm
import db_queries as dbq


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def make_internal_error(e: Exception) -> HTTPException:
    return HTTPException(
        status_code=500,
        detail=f"Couldn't fetch data; error: {type(e)};" +
        " args: {err.args}; error: {err}"
    )


app = FastAPI()


@app.get("/ping")
def ping():
    return {
        "name": "f1_data_service",
        "status": "ok",
        "version": "1.0.0"
    }


@app.get("/drivers/{driver_id}")
def read_item(driver_id: int, db: Session = Depends(get_db)):
    if driver_id is None:
        raise HTTPException(status_code=400, detail="Please provide a driver ID")
    try:
        driver = dbq.get_driver(driver_id, db)
    except Exception as err:
        raise make_internal_error(err)
    if driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return rm.DriverResponse(driver=driver)


@app.get("/race/{race_id}/results")
def race_results(race_id: int, db: Session = Depends(get_db)):
    if race_id is None:
        raise HTTPException(status_code=400, detail="Please provide a race ID")
    try:
        res = dbq.get_race_results(race_id, db)
    except Exception as err:
        raise make_internal_error(err)
    return res


@app.get("/race/{race_id}/laptimes")
def lap_times(
    race_id: int,
    driver_id: Union[list[int], None] = Query(default=None),
    db: Session = Depends(get_db)
):
    if race_id is None or driver_id is None:
        raise HTTPException(
            status_code=400,
            detail="Please provide a race ID and driver ID(s)"
        )
    try:
        res = dbq.get_lap_times(race_id, driver_id, db)
    except Exception as err:
        raise make_internal_error(err)
    return res
