FROM python:3.10.4

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

ENV FLASK_APP=server.py

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8888"]
