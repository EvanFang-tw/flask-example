FROM python:3.10.4-slim-buster

WORKDIR /app

# install cron
RUN apt-get update
RUN apt-get -y install cron

# setup cron
COPY cronjobs/cron /etc/cron.d/cron
RUN chmod 0644 /etc/cron.d/cron
RUN crontab /etc/cron.d/cron

COPY ./cronjobs/job.py .
RUN chmod +x ./*.py
# RUN pip install -r requirements.txt

RUN touch /var/log/cron.log
RUN touch /var/log/cron-error.log

CMD cron && tail -f /var/log/cron.log
