FROM python:3.10

RUN pip install poetry
RUN poetry config virtualenvs.in-project true