from flask import Blueprint, jsonify, request
from models.Style_SewingModel import Style_SewingModel
import pandas as pd
import asyncio
import json
from pandas import json_normalize
from database.db import conn

main=Blueprint('Style_Sewing_blueprint', __name__)
_loop2 = asyncio.get_event_loop()

@main.route('/')
def get_Style_Sewing():
    try:
        Style_Sewing = Style_SewingModel.get_Style_Sewing()
        if(len(Style_Sewing) > 0):
            return jsonify(Style_Sewing)
        else:
            return jsonify({'message': "No Data"}), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add/<User>', methods=['POST'])
def add_Style_GlobalCategory(User):
    try:
        jsonPD = request.get_json()
        df = json_normalize(jsonPD)
        df = df.assign(CommentsUpdate="True")
        df['Costura_PE'].fillna("Null", inplace=True)
        df['Costura_Operators'].fillna("Null", inplace=True)
        df['Costura_SAM'].fillna("Null", inplace=True)
        df['Costura_Goal_Pcs'].fillna("Null", inplace=True)
        # df.to_excel("Style_Sewing.xlsx", sheet_name='Sheet1', index=False)
        for x in range(len(df)):
            try:
                if not( df.Id_Style_GeneralInfo[x] == 0 or df.Id_Style_GeneralInfo[x] == None or df.Id_Style_LayoutConfiguration[x] == 0 or df.Id_Style_LayoutConfiguration[x] == None):
                    _loop2.run_until_complete(Style_SewingModel.add_Style_Sewing(df.id[x], df.Id_Style_GeneralInfo[x], df.Id_Style_LayoutConfiguration[x], df.Costura_Operators[x], df.Costura_SAM[x], df.Costura_Goal_Pcs[x], df.Costura_PE[x], User))
                else:
                    df.CommentsUpdate[x] = "False"
            except Exception as ex:
                pass
        return dict(msj='Accion Realizada Correctamente')
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500