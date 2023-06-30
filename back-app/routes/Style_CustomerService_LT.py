from flask import Blueprint, jsonify, request
from models.Style_CustomerService_LTModel import Style_CustomerService_LTModel
import pandas as pd
import asyncio
import json
from pandas import json_normalize
from database.db import conn

main=Blueprint('Style_CustomerService_LT_blueprint', __name__)
_loop2 = asyncio.get_event_loop()

@main.route('/')
def get_Style_CustomerService_LT():
    try:
        Style_Sewing = Style_CustomerService_LTModel.get_Style_CustomerService_LT()
        if(len(Style_Sewing) > 0):
            return jsonify(Style_Sewing)
        else:
            return jsonify({'message': "No Data"}), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add/<User>', methods=['POST'])
def add_Style_CustomerService_LT(User):
    try:
        jsonPD = request.get_json()
        df = json_normalize(jsonPD)
        for x in range(len(df)):
            Style_CustomerService_LTModel.add_Style_CustomerService_LT(df.id[x], df.Id_Style_GeneralInfo[x], df.Id_Style_ProductType[x], df.Id_Style_Vendor[x] , df.Colorway[x], df.Procurement[x], df.Mfg[x], df.GIPT[x], df.Comments[x], User)
        return dict(msj='Accion Realizada Correctamente')
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500