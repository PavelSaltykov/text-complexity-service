# text-complexity-service

## Setup
```sh
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
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
Navigate to http://localhost:8000/docs to see interactive API documentation.

