# dependencies

- [docker](https://docs.docker.com/engine/install/)
- [docker-compose](https://docs.docker.com/compose/install/)

# Getting started

This project use docker to build the dependencies and isolate it in a container, so docker and docker-compose need to be instaled.

In the first time running this project run the buld command:
```
docker-compose build
```

After that you can run the project by running:
```
docker-compose up
```

after that the API will be listening at http://localhost:8000/search

# Limitations

letter index that also are roman number will not be considered as a index and will be considered as a roman number.
For example this input will throw an error:
```json
{
    "text":"CXXX"
}
```