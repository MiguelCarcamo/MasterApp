from flask import Blueprint, jsonify, request
from models.Style_CustomerModel import Style_CustomerModel
import pandas as pd
import asyncio
import json
from pandas import json_normalize
from database.db import conn

main=Blueprint('Style_Customer_blueprint', __name__)
_loop2 = asyncio.get_event_loop()

@main.route('/')
def get_Style_Customer():
    try:
        Style_Customer = Style_CustomerModel.get_Style_Customer()
        if(len(Style_Customer) > 0):
            return jsonify(Style_Customer)
        else:
            return jsonify({'message': str(ex)}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add/<User>', methods=['POST'])
def add_Style_Customer(User):
    try:
        jsonPD = request.get_json()
        df = json_normalize(jsonPD)
        df = df.assign(CommentsUpdate="True")
        df['Customer'] = df['Customer'].str.replace("'","-",regex=True)
        df['Comments'] = df['Comments'].str.replace("'","-",regex=True)
        for x in range(len(df)):
            try:
                _loop2.run_until_complete(Style_CustomerModel.add_Style_Customer(df.id[x], df.Customer[x], User, df.Comments[x]))
            except Exception as ex:
                pass
        return dict(msj='Accion Realizada Correctamente')
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500
