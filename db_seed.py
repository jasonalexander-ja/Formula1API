from db.database import SessionLocal
from db import importers as imp


db = SessionLocal()


circuits = imp.extract_circuit('.\\challenge\\data\\circuits.csv')
db.add_all(circuits)
db.commit()

constructors = imp.extract_constructors('.\\challenge\\data\\constructors.csv')
db.add_all(constructors)
db.commit()

drivers = imp.extract_driver('.\\challenge\\data\\drivers.csv')
db.add_all(drivers)
db.commit()

lap_times = imp.extract_lap_time('.\\challenge\\data\\lap_times.csv')
db.add_all(lap_times)
db.commit()

races = imp.extract_races('.\\challenge\\data\\races.csv')
db.add_all(races)
db.commit()

results = imp.extract_results('.\\challenge\\data\\results.csv')
db.add_all(results)
db.commit()

status = imp.extract_statuses('.\\challenge\\data\\status.csv')
db.add_all(status)
db.commit()

db.close()
