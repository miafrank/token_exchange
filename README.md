## Securing api with jwt tokens

## Setup 

## Create Auth0 account

Create Auto0 account and register an [API](https://auth0.com/docs/get-started/auth0-overview/set-up-apis)

## Install Python

If you do not have Python, please install the latest 3.x version from python.org. You can check this by running: 

```
$ python --version
```

## Install Pipenv

### Install pip 

Make sure you have pip available, you should if you are using Python downloaded from python.org.

Check this by running:

```
$ pip --version
```

If you do not have Pipenv installed already, install with [Homebrew](https://brew.sh/). [Pipenv](https://packaging.python.org/en/latest/tutorials/managing-dependencies/#managing-dependencies) is the offical package management tool reccomended by Python (similar to `npm`): 

```
$ brew install pipenv
```

Alternatively, you can install Pipenv with pip: 

```
$ pip install --user pipenv
```

## Install dependencies

```
$ pipenv install
```

## Run banking api server

```
# Runs on port localhost:5000

$ flask --app app run
```

## Run banking api server on port 8080

```
$ export FLASK_RUN_PORT=8000
$ export FLASK_RUN_HOST="127.0.0.1"

$ flask --app token_client.app run 
```

## Env variables
- Create .env file with the following variables
- Creds can be found in Auth0 dashboard under `Applications/APIs`

```
CLIENT_ID=
CLIENT_SECRET=
AUDIENCE=
AUTH_API_URI=
```

## API

- Retrieve token from `/api/token` 

```
# There are both incomes and expenses created in mock transactions
```
```
transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('Pizza', 50),
    Expense('Rock Concert', 100)
]
```

- Income transactions can be fetched at `api/income` 
- Expense transactions can be fetched at `api/expense`
- Add header: `Authorization` to request

- Successful response example: 
```
[
    {
        "amount": 5000,
        "description": "Salary",
        "type": "TransactionType.INCOME"
    },
    {
        "amount": 200,
        "description": "Dividends",
        "type": "TransactionType.INCOME"
    }
]
```
