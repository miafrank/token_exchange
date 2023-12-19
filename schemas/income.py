from marshmallow import post_load

from enums.transaction_type import TransactionType
from schemas.transaction import Transaction, TransactionSchema


class Income(Transaction):
    def __init__(self, description, amount):
        super(Income, self).__init__(
            description, amount, TransactionType.INCOME)

    def __repr__(self):
        return '<Income(name={self.description!r})>'.format(self=self)


class IncomeSchema(TransactionSchema):
    @post_load
    def make_income(self, data, **kwargs):
        return Income(**data)
