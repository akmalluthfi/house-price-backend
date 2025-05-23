FROM python:3.11-slim-bookworm

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./database /code/database
COPY ./models /code/models

COPY alembic.ini .env.example /code

CMD ["fastapi", "run", "app/main.py", "--port", "80"]