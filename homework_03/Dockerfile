FROM python:3.9-buster

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
ENV PATH="${PATH}:/root/.poetry/bin"
RUN poetry config virtualenvs.create false

WORKDIR /var/app
COPY app .

RUN pip install poetry==1.1.11
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD uvicorn app:app --host=0.0.0.0

EXPOSE 8000
