FROM python:3.10

WORKDIR /app
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip poetry==1.1.11 && poetry config virtualenvs.create false

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install --no-dev
COPY . .

CMD poetry run python app/app.py
