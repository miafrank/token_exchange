from marshmallow import Schema, fields


class Transaction:
    def __init__(self, description, amount, type):
        self.description = description
        self.amount = amount
        self.type = type

    def __repr__(self):
        return '<Transaction(name={self.description!r})>'.format(self=self)


class TransactionSchema(Schema):
    description = fields.Str(required=True)
    amount = fields.Int(required=True)
    type = fields.Str(required=True)
