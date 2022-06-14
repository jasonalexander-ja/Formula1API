from db import schema


class ResultResponse:
    def __init__(self, results: schema.Results, status: str) -> None:
        self.constructor_id = results.constructor_id
        self.driver_id = results.driver_id
        self.position = results.position
        self.status = status

    constructor_id: int
    driver_id: int
    position: int
    status: str


class DriverResponse:
    def __init__(self, driver: schema.Driver) -> None:
        self.code = driver.code
        self.dob = driver.date_of_birth
        self.driver_id = driver.id
        self.forename = driver.forename
        self.nationality = driver.nationality
        self.number = driver.number
        self.surname = driver.surname
        self.url = driver.url

    code: str
    dob: str
    driver_id: int
    forename: str
    nationality: str
    number: int
    surname: str
    url: str


class DriverLapTimeResponse:
    driver_id: int
    laptimes: float


class LapTimeResponse:
    def __init__(self, lap_time: schema.LapTime) -> None:
        self.lap_number = lap_time.lap
        self.seconds = lap_time.time_milli / 1000

    lap_number: int
    seconds: float
