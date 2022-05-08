# S3 Agent

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

## Docker
```sh
# build
docker build -t flask-example:1.0 .

# run
docker run -d -p 8888:8888 --name flask-app flask-example:1.0
```

### Dcoker Compose
```sh
# build
docker-compose build

# run
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
