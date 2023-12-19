from flask import Flask, jsonify, request
from enums.transaction_type import TransactionType
from schemas.expense import Expense, ExpenseSchema
from schemas.income import Income, IncomeSchema

from token_validator import validate_jwt_token

app = Flask(__name__)

transactions = [
    Income('Salary', 5000),
    Income('Dividends', 200),
    Expense('Pizza', 50),
    Expense('Rock Concert', 100)
]


@app.route("/api/incomes")
def get_incomes():
    auth_token = request.headers.get("Authorization")
    print(auth_token)
    validate_jwt_token(auth_token)

    schema = IncomeSchema(many=True)
    incomes = schema.dump(
        filter(lambda t: t.type == TransactionType.INCOME, transactions)
    )

    return jsonify(incomes)


@app.route("/api/expenses")
def get_expenses():
    auth_token = request.headers.get("Authorization")
    validate_jwt_token(auth_token)

    schema = ExpenseSchema(many=True)
    expenses = schema.dump(
        filter(lambda t: t.type == TransactionType.EXPENSE, transactions)
    )

    return jsonify(expenses)
