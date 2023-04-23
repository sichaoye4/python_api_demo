from marshmallow import Schema, fields, EXCLUDE

# create a class for the schema of loan_details table created by table_create_script/loan_details.sql
class LoanDetailsSchema(Schema):
    loan_id = fields.Str(required=True)
    client_id = fields.Str(required=True)
    account_id = fields.Str(required=True)
    date = fields.Date(allow_none=True)
    amount = fields.Float(allow_none=True)
    duration = fields.Int(allow_none=True)
    payments = fields.Float(allow_none=True)
    due_date = fields.Date(allow_none=True)
    status = fields.Str(allow_none=True)
    month_id = fields.Int(required=True)
    class Meta:
        unknown = EXCLUDE
