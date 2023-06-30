from flask import Blueprint, jsonify, request
from models.Style_Sewing_FamilyModel import Style_Sewing_FamilyModel
import pandas as pd
import asyncio
import json
from pandas import json_normalize
from database.db import conn

main=Blueprint('Style_Sewing_Family_blueprint', __name__)
_loop2 = asyncio.get_event_loop()

@main.route('/')
def get_Style_Sewing_Family():
    try:
        Style_Sewing = Style_Sewing_FamilyModel.get_Style_Sewing_Family()
        if(len(Style_Sewing) > 0):
            return jsonify(Style_Sewing)
        else:
            return jsonify({'message': "No Data"}), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add/<User>', methods=['POST'])
def add_Style_Sewing_Family(User):
    try:
        jsonPD = request.get_json()
        df = json_normalize(jsonPD)
        df = df.assign(CommentsUpdate="True")
        # df.to_excel("Style_Family.xlsx", sheet_name='Sheet1', index=False)
        df['Costura_Familia'] = df['Costura_Familia'].str.replace("'","-",regex=True)
        df['Comments'] = df['Comments'].str.replace("'","-",regex=True)
        for x in range(len(df)):
            try:
                if not(df.Id_Style_WorkCenter[x] == 0 or df.Id_Style_WorkCenter[x] == None):
                    _loop2.run_until_complete(Style_Sewing_FamilyModel.add_Style_Sewing_Family(df.id[x], df.Id_Style_WorkCenter[x], df.Costura_Familia[x], User, df.Comments[x]))
                else:
                    df.CommentsUpdate[x] = "False"
            except Exception as ex:
                pass
        return dict(msj='Accion Realizada Correctamente')
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500