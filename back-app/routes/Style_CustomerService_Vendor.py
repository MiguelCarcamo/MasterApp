from flask import Blueprint, jsonify, request
from models.Style_CustomerService_VendorModel import Style_CustomerService_VendorModel
import pandas as pd
import asyncio
import json
from pandas import json_normalize
from database.db import conn

main=Blueprint('Style_CustomerService_Vendor_blueprint', __name__)
_loop2 = asyncio.get_event_loop()

@main.route('/')
def get_Style_CustomerService_Vendor():
    try:
        Style_Sewing = Style_CustomerService_VendorModel.get_Style_CustomerService_Vendor()
        if(len(Style_Sewing) > 0):
            return jsonify(Style_Sewing)
        else:
            return jsonify({'message': "No Data"}), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add/<User>', methods=['POST'])
def add_Style_CustomerService_Vendor(User):
    try:
        jsonPD = request.get_json()
        df = json_normalize(jsonPD)
        for x in range(len(df)):
            Style_CustomerService_VendorModel.add_Style_CustomerService_Vendor(df.id[x], df.Style_Vendor[x], User, df.Comments[x])
        return dict(msj='Accion Realizada Correctamente')
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500