from marshmallow import Schema, fields, EXCLUDE

# create a class for the schema of transaction_details table created by table_create_script/transaction_details.sql
class TransactionDetailsSchema(Schema):
    trans_id = fields.Str(required=True)
    client_id = fields.Str(required=True)
    account_id = fields.Str(required=True)
    date = fields.Date(allow_none=True)
    type = fields.Str(allow_none=True)
    operation = fields.Str(allow_none=True)
    amount = fields.Float(required=True)
    balance = fields.Float(allow_none=True)
    k_symbol = fields.Str(allow_none=True)
    bank = fields.Str(allow_none=True)
    account = fields.Str(allow_none=True)
    tran_desc = fields.Str(allow_none=True)
    month_id = fields.Int(required=True)
    class Meta:
        unknown = EXCLUDE
