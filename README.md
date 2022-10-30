# text-complexity-service

## Setup
```sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Run
* Uvicorn:
```sh
source venv/bin/activate
uvicorn src.app.api:app
```
* Docker:
```sh
docker build -t text-complexity-service .
docker run -p 8000:8000 text-complexity-service
```

