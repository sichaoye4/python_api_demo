#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
import atexit, json
from flask_restful import Resource, Api, abort
import jaydebeapi
from persistent import get_all_by_client_id, get_all_from_summary_by_month_id, get_all_by_client_id_and_month_id, close_connection
from models.loan_details import LoanDetailsSchema
from models.client_loan_summary import ClientLoanSummarySchema
from models.transaction_details import TransactionDetailsSchema
from models.client_trans_summary import ClientTransSummarySchema
from models.constants import *
from utils.decrypt_util import decrypt_db_password
from utils.utils import read_txt_file_as_single_line, CustomJsonEncoder

app = Flask(__name__)
api = Api(app)
# get path to encrypted password file
pwd = decrypt_db_password(read_txt_file_as_single_line(app, "static/encrypted.txt"))
connection = jaydebeapi.connect(
            "org.h2.Driver",
            DB_URL,
            [DB_USER, pwd],
            H2_DRIVER)
def on_exit_app(connection: jaydebeapi.Connection) -> None:
    close_connection(connection)
    print("H2 connection closed successfully")

atexit.register(on_exit_app, connection=connection)

class ClientLoanMonthlySummary(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.tb_name = CLIENT_LOAN_SUMMARY_NAME
        self.schema = ClientLoanSummarySchema

    def get(self, month_id: str) -> list:
        if month_id is None:
            abort(404, errors={"message": "Month ID is required"})
        loan_summary = get_all_from_summary_by_month_id(connection, month_id, self.tb_name, self.schema)
        if not loan_summary:
            abort(404, errors={"message": f"No loan summary found for the given month ID {month_id}"})
        return loan_summary
    
class ClientLoanDetails(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.tb_name = LOAN_DETAILS_NAME
        self.schema = LoanDetailsSchema
    
    def get(self, client_id: str, month_id: str) -> list:
        if client_id is None:
            abort(404, errors={"message": "Client ID is required"})
        loan_details = None
        if not month_id:
            loan_details = get_all_by_client_id(connection, client_id, self.tb_name, self.schema)
        else:
            loan_details = get_all_by_client_id_and_month_id(connection, client_id, month_id, self.tb_name, self.schema)
        if not loan_details:
            abort(404, errors={"message": f"No loan details found for the given client ID {client_id} & month_id {month_id}"})
        loan_details = json.loads(json.dumps(loan_details, cls=CustomJsonEncoder))
        return loan_details
    
class ClientTransMonthlySummary(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.tb_name = CLIENT_TRANS_SUMMARY_NAME
        self.schema = ClientTransSummarySchema

    def get(self, month_id: str) -> list:
        if month_id is None:
            abort(404, errors={"message": "Month ID is required"})
        trans_summary = get_all_from_summary_by_month_id(connection, month_id, self.tb_name, self.schema)
        if not trans_summary:
            abort(404, errors={"message": f"No trans summary found for the given month ID {month_id}"})
        return trans_summary
    
class ClientTransDetails(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.tb_name = TRANSACTION_DETAILS_NAME
        self.schema = TransactionDetailsSchema

    def get(self, client_id: str, month_id: str) -> list:
        if client_id is None:
            abort(404, errors={"message": "Client ID is required"})
        trans_details = None
        if not month_id:
            trans_details = get_all_by_client_id(connection, client_id, self.tb_name, self.schema)
        else:
            trans_details = get_all_by_client_id_and_month_id(connection, client_id, month_id, self.tb_name, self.schema)
        if not trans_details:
            abort(404, errors={"message": f"No trans details found for the given client ID {client_id} & month_id {month_id}"})
        trans_details = json.loads(json.dumps(trans_details, cls=CustomJsonEncoder))
        return trans_details


api.add_resource(ClientLoanMonthlySummary, "/loan-monthly-summary/<month_id>")
api.add_resource(ClientLoanDetails, "/client-loan-details/<client_id>", "/client-loan-details/<client_id>/<month_id>")
api.add_resource(ClientTransMonthlySummary, "/trans-monthly-summary/<month_id>")
api.add_resource(ClientTransDetails, "/client-trans-details/<client_id>", "/client-trans-details/<client_id>/<month_id>")
