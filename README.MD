# Hardmob Scrapper

## You can run locally like this:

```
pipenv install
pipenv shell

export FLASK_APP=api.py
flask run
```

## Or using Docker (Local)

```
docker build -t api:local .
docker run -d -p 5000:5000 api:local
```
