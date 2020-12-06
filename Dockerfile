FROM ubuntu:20.04

RUN apt update -y
RUN apt upgrade -y


EXPOSE 8000
COPY . .


CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]