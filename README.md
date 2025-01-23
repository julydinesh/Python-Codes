# Python Codes covering the below concepts 

* Data Science
* Mathematics
* Algorithms

# FastAPI Setup
Setting up FastAPI with JSON file

## Installation

Follow the below steps to setup

### Step 1 - Git clone

```
git clone https://github.com/saasscaleup/fastapi.git
```

```
cd fastapi
```

### Step 2 - Install required packages.

```
pip install fastapi uvicorn
```

## Run FastAPI locally

```
uvicorn main:app --reload
```

## Using the GUI

Invoke the below URL and passs the desired test data id to validate the prediction. In the below case 1 is the test id.

http://127.0.0.1:8000/pred/1
