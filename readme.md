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
export FLASK_APP=server.py
export FLASK_ENV=development
flask run
```

### Formatter
```sh
black .
```

## Deployment

### Gunicorn
```sh
gunicorn server:app

# run in background
gunicorn -D server:app
```