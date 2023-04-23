import sys
from pathlib import Path
from flask import Flask
import json
from datetime import date, datetime

# util function to get project root path
def get_project_root() -> Path:
    print(sys.argv)
    return Path(sys.argv[1]).parent.absolute()

# util function to read txt file
def read_txt_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()
    
# util function to read txt file as one signle line
def read_txt_file_as_single_line(app: Flask, file_path: str) -> str:
    with app.open_resource(file_path) as f:
        return ''.join([x.decode('utf-8') for x in f.readlines()])
    
# define custom JsonEncoder to handle date and datetime objects
class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)