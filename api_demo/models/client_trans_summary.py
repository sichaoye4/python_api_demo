from marshmallow import Schema, fields, EXCLUDE

# create a class for the schema of client_trans_summary table created by table_create_script/client_trans_summary.sql
class ClientTransSummarySchema(Schema):
    client_id = fields.Str(required=True)
    month_id = fields.Int(required=True)
    operation = fields.Str(allow_none=True)
    number_of_trans = fields.Int(allow_none=True)
    total_trans_amount = fields.Float(allow_none=True)
    class Meta:
        unknown = EXCLUDE