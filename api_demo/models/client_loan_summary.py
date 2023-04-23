from marshmallow import Schema, fields, EXCLUDE

# create a class for the schema of client_loan_summary table created by table_create_script/client_loan_summary.sql
class ClientLoanSummarySchema(Schema):
    client_id = fields.Str(required=True)
    month_id = fields.Int(required=True)
    number_of_loans = fields.Int(allow_none=True)
    total_loan_amount = fields.Float(allow_none=True)
    class Meta:
        unknown = EXCLUDE