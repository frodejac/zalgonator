FROM python:3.7.3-stretch

RUN pip install gunicorn

WORKDIR /opt/zalgonator
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY entrypoint.sh .

ENV PYTHONPATH /opt/zalgonator:/opt/zalgonator/zalgonator
ENTRYPOINT ["./entrypoint.sh"]
