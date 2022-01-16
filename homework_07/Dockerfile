FROM python:3.9-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY coverage_app /app/

RUN chmod +x setup.sh

ENTRYPOINT ["bash", "setup.sh"]
