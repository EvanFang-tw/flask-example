# Flask Example

A quick start template with some examples.

## Development

### Env
```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Run
```sh
export FLASK_APP=src/server.py
export FLASK_ENV=development
flask run -h 127.0.0.1 -p 8888
```

### Formatter
```sh
black .
```

## Development with Docker Compose

Using docker compose to start all related services.

```sh
# build
docker-compose build

# run
docker-compose up

# or run in detached mode
docker-compose up -d

# logs
docker-compose logs -f

# tear down
docker-compose down
```

## Deployment

### Gunicorn
```sh
gunicorn server:app

# run in background
gunicorn -D server:app
```
