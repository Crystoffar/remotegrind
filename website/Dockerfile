FROM python:3.12-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY migrations migrations
COPY remotegrind.py config.py boot.sh ./
COPY vibrant-reach-416423-16001b68a39a.json ./
RUN chmod a+x boot.sh

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]