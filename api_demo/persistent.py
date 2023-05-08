import jaydebeapi, marshmallow

def convert_to_schema(cursor: jaydebeapi.Cursor, Schema: marshmallow.Schema) -> list:
    column_names = [record[0].lower() for record in cursor.description]
    column_and_values = [dict(zip(column_names, record)) for record in cursor.fetchall()]

    return Schema().load(column_and_values, many=True)

def execute(query: str, connection: jaydebeapi.Connection, Schema: marshmallow.Schema, return_result: any = True) -> any:
    cursor = connection.cursor()
    cursor.execute(query)
    if Schema and return_result:
        returnResult = convert_to_schema(cursor, Schema)
    elif return_result:
        returnResult = cursor.fetchall()
    cursor.close()
    return returnResult

# get all by client_id
def get_all_by_client_id(connection: jaydebeapi.Connection, client_id: str, table_name: str, schema: marshmallow.Schema) -> list:
    query = f"SELECT * FROM {table_name} WHERE client_id = '{client_id}'"
    return execute(query, connection, schema)

# get all by client_id and month_id
def get_all_by_client_id_and_month_id(connection: jaydebeapi.Connection, client_id: str, month_id: str, table_name: str, schema: marshmallow.Schema) -> list:
    if not month_id.isdigit():
        raise ValueError("Month ID must be a Integer")
    query = f"SELECT * FROM {table_name} WHERE client_id = '{client_id}' AND month_id = {int(month_id)}"
    return execute(query, connection, schema)

# get all from summary tables by month_id
def get_all_from_summary_by_month_id(connection: jaydebeapi.Connection, month_id: str, table_name: str, schema: marshmallow.Schema) -> list:
    if not month_id.isdigit():
        raise ValueError("Month ID must be a Integer")
    query = f"SELECT * FROM {table_name} WHERE month_id = {int(month_id)}"
    print(query)
    return execute(query, connection, schema)

# get count of a table
def get_count(connection: jaydebeapi.Connection, table_name: str) -> int:
    query = f"SELECT COUNT(*) FROM {table_name}"
    return execute(query, connection, None)[0][0]

# get record detail of a loan or transaction by id
def get_record_by_id(connection: jaydebeapi.Connection, id: str, id_col: str, table_name: str, schema: marshmallow.Schema) -> list:
    query = f"SELECT * FROM {table_name} WHERE {id_col} = '{id}'"
    return execute(query, connection, schema)

def close_connection(connection: jaydebeapi.Connection):
    connection.close()