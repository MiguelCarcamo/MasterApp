from flask import Blueprint, jsonify, request
from models.Style_GlobalCategoryModel import Style_GlobalCategoryModel
import pandas as pd
import asyncio
import json
from pandas import json_normalize
from database.db import conn

main=Blueprint('Style_GlobalCategory_blueprint', __name__)
_loop2 = asyncio.get_event_loop()
@main.route('/')
def get_Style_GlobalCategory():
    try:
        Style_GlobalCategory = Style_GlobalCategoryModel.get_Style_GlobalCategory()
        if(len(Style_GlobalCategory) > 0):
            return jsonify(Style_GlobalCategory)
        else:
            return jsonify({'message': str(ex)}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add/<User>', methods=['POST'])
def add_Style_GlobalCategory(User):
    try:
        jsonPD = request.get_json()
        df = json_normalize(jsonPD)
        df = df.assign(CommentsUpdate="True")
        df['GlobalCategory'] = df['GlobalCategory'].str.replace("'","-",regex=True)
        df['Comments'] = df['Comments'].str.replace("'","-",regex=True)
        for x in range(len(df)):
            try:
                if not(df.Id_Style_Customer[x] == 0 or df.Id_Style_Customer[x] == None):
                    _loop2.run_until_complete(Style_GlobalCategoryModel.add_Style_GlobalCategory(df.id[x], df.Id_Style_Customer[x], df.GlobalCategory[x], User, df.Comments[x]))
                else:
                    df.CommentsUpdate[x] = "False"
            except Exception as ex:
                pass
        return dict(msj='Accion Realizada Correctamente')
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500