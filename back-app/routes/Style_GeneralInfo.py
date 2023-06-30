from flask import Blueprint, jsonify, request
from models.Style_GeneralInfoModel import Style_GeneralInfoModel
import pandas as pd
import asyncio
import json
from pandas import json_normalize
from database.db import conn

main=Blueprint('Style_GeneralInfo_blueprint', __name__)
_loop2 = asyncio.get_event_loop()

@main.route('/')
def get_Style_GeneralInfo():
    try:
        Style_GeneralInfo = Style_GeneralInfoModel.get_Style_GeneralInfo()
        if(len(Style_GeneralInfo) > 0):
            return jsonify(Style_GeneralInfo)
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
        df['Style_LeadTimeDays'].fillna("Null", inplace=True)
        df['StyleNumber'] = df['StyleNumber'].str.replace("'","-",regex=True)
        df['Style_Comments'] = df['Style_Comments'].str.replace("'","-",regex=True)
        for x in range(len(df)):
            try:
                if not(df.Id_Style_WorkCenter[x] == 0 or df.Id_Style_WorkCenter[x] == None):
                    _loop2.run_until_complete(Style_GeneralInfoModel.add_Style_GeneralInfo(df.id[x], df.Id_Style_WorkCenter[x], df.StyleNumber[x], User, df.TypeStyle[x], df.Style_LeadTimeDays[x], df.Style_Workflow[x], df.Style_Comments[x]))
                else:
                    df.CommentsUpdate[x] = "False"
            except Exception as ex:
               pass
        return dict(msj='Accion Realizada Correctamente')
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500