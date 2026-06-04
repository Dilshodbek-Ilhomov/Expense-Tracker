# Expense Tracker API

A personal finance management API built with Django REST Framework.

## Features

* User Registration
* JWT Authentication
* Wallet Management
* Income & Expense Tracking
* Automatic Balance Updates
* Transaction Validation
* Basic Analytics
* Protected Endpoints

## Tech Stack

* Python
* Django
* Django REST Framework
* Simple JWT
* SQLite
* Docker

## API Endpoints

### Authentication

* `POST /api/register/`
* `POST /api/token/`
* `POST /api/token/refresh/`

### Wallets

* `GET /api/wallets/`
* `POST /api/wallets/`

### Transactions

* `GET /api/transactions/`
* `POST /api/transactions/`

### Analytics

* `GET /api/transactions/analytics/`

## Installation

```bash
git clone https://github.com/Dilshodbek-Ilhomov/Expense-Tracker.git

cd Expense-Tracker

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## Author

Dilshodbek Ilhomov
