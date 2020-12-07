# MisinfoWatcher

Repo for CAP4932 final project

In order to run this project you need the following installed:
- Node
- npm
- Python 3+
- Docker


## Frontend
- run `npm install` then `npm start` in the frontend repo

## API

Building the API:
```
docker build -t docker-username/misinfowatcher .
```

Run the image
```
docker run -p 8000:8000 docker-username/misinfowatcher
```

### Dev only
To push the image to your docker repo use the command:
```
docker push docker-username/misinfowatcher
```