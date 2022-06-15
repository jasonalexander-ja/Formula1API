## F1 API 

To start:
```
    ProjectRoot>python -m venv .
    ProjectRoot>.\Scipts\activate
    ProjectRoot>pip install -r requirements.txt
```

To test:
```
    ProjectRoot>pytest
```

To generate coverage documentation:
```
    ProjectRoot>coverage run -m pytest
```

To view coverage report as a HTML document:
```
    ProjectRoot>coverage html
```

Remember when revisiting after the IDE or terminal has been restarted, restart the env;
```
    ProjectRoot>.\Scipts\activate
```
When the env is active you should see the project name before the directory in ther terminal;
```
    (ProjectName) ProjectName>
```

To restore packages after pulling from a repo, use;
```
    Formula1API> pip install -r requirements.txt
```
(make sure virtual environment is active)

## SQL Config 

Once in virtual env, to create the database use;
```
    Formula1API> alembic revision --autogenerate -m "InitialCreate"
    Formula1API> alembic upgrade head
```

To seed the database, run;
```
    Formula1API> python db_seed.py
```


## API Server

To start the API server, with the virtual environment started and packages restores, use;
```
    Formula1API> uvicorn main:app --reload
```

To find the Swagger docs and test the API, navigate to the base URL + /docs, this will usually be `http://127.0.0.1:8000/docs` .
