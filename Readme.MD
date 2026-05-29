# Expense Tracker API

A personal finance management API built with Django REST Framework.

## Features

* User Registration
* JWT Authentication
* Wallet Management
* Income & Expense Tracking
* Automatic Balance Updates
* Transaction Validation
* Protected Endpoints

## Tech Stack

* Python
* Django
* Django REST Framework
* Simple JWT
* SQLite

## API Endpoints

### Authentication

* `/api/register/`
* `/api/token/`
* `/api/token/refresh/`

### Wallets

* `/api/wallets/`

### Transactions

* `/api/transactions/`

## Installation

```bash
git clone https://github.com/Dilshodbek-Ilhomov/Expense-Tracker.git

cd Expense-Tracker

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## Future Improvements

* Analytics Dashboard
* Docker Support
* PostgreSQL
* AWS Deployment
* API Documentation

## Author

Dilshodbek Ilhomov
