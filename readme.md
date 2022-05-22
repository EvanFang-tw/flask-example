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

### Type Check
```sh
mypy .
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

## Debug

### Debug with VSCode

Select `Local` configuration to debug flask app locally.

If you want to debug flask app running in the container, you need select `Remote Attach(Container)` configuration and modify the `docker-compose.yml`:
```yaml
environment:
      - FLASK_ENV=development
    #   - DEBUG=True
    # ports:
    #   - "5678:5678"
```
change to:
```yaml
environment:
    #   - FLASK_ENV=development
      - DEBUG=True
    ports:
      - "5678:5678"
```

## Deployment

### Gunicorn
```sh
gunicorn server:app

# run in background
gunicorn -D server:app
```

### Cronjobs

Using crontab to schedule jobs.

Cronjob image is described in `cronjobs/Dockerfile`.

Cronjob setting is described in `cronjobs/cron`.

An example job is located in `cronjobs/job.py`.
