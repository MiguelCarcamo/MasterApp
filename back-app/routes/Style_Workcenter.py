from flask import Blueprint, jsonify, request
from models.Style_WorkcenterModel import Style_WorkcenterModel
import pandas as pd
import asyncio
import json
from pandas import json_normalize
from database.db import conn

main=Blueprint('Style_Workcenter_blueprint', __name__)
_loop2 = asyncio.get_event_loop()

@main.route('/')
def get_Style_Workcenter():
    try:
        Style_Workcenter = Style_WorkcenterModel.get_Style_Workcenter()
        if(len(Style_Workcenter) > 0):
            return jsonify(Style_Workcenter)
        else:
            return jsonify({'message': "No Data"}), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/add/<User>', methods=['POST'])
def add_Style_Workcenter(User):
    try:
        jsonPD = request.get_json()
        df = json_normalize(jsonPD)
        df = df.assign(CommentsUpdate="True")
        df['WorkCenter'] = df['WorkCenter'].str.replace("'","-",regex=True)
        df['Comments'] = df['Comments'].str.replace("'","-",regex=True)
        for x in range(len(df)):
            try:
                if not(df.Id_Style_GlobalCategory[x] == 0 or df.Id_Style_GlobalCategory[x] == None):
                    _loop2.run_until_complete(Style_WorkcenterModel.add_Style_Workcenter(df.id[x], df.Id_Style_GlobalCategory[x], df.WorkCenter[x], User, df.Comments[x]))
                else:
                    df.CommentsUpdate[x] = "False"
            except Exception as ex:
                pass
        return dict(msj='Accion Realizada Correctamente')
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500