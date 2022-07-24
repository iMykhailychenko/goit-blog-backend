FROM python:3.9-buster
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat \
  && apt-get clean

COPY requirements.txt .
COPY scripts /app/scripts
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["./scripts/run-app.sh"]