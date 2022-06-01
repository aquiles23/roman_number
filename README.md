this exercise is made with [fastAPI](https://fastapi.tiangolo.com), the solution code is on [app/main.py](./app/main.py) and its tests are on [app/test_main.py](./app/test_main.py) using parameterized tests with [pytest](https://docs.pytest.org/en/7.1.x/)

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

after that the API will be listening at http://localhost:8000/search with a POST endpoint

you can debug and know better about the endpoints at http://localhost:8000/docs

# Limitations

letter index that also are roman number will not be considered as a index and will be considered as a roman number.
For example this input will throw an error:
```json
{
    "text":"CXXX"
}
```