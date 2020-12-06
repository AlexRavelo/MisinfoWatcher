FROM ubuntu:20.04

RUN apt update -y
RUN apt upgrade -y
RUN apt-get install -y curl python3 python3-pip
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
ENV PATH = "${PATH}:/root/.poetry/bin"
EXPOSE 8000
COPY . .
RUN poetry install

CMD ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]