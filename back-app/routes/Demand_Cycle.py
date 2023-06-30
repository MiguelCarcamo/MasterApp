from flask import Blueprint, jsonify, request
from models.Demand_CycleModel import Demand_CycleModel
import pandas as pd
import asyncio
import json
from pandas import json_normalize
from database.db import conn

main=Blueprint('Demand_Cycle_blueprint', __name__)
_loop2 = asyncio.get_event_loop()

@main.route('/')
def get_Demand_Cycle():
    try:
        Demand_Cycle = Demand_CycleModel.get_Demand_Cycle()
        if(len(Demand_Cycle) > 0):
            return jsonify(Demand_Cycle)
        else:
            return jsonify({'message': str(ex)}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add/<User>', methods=['POST'])
def add_Demand_Cycle(User):
    try:
        jsonPD = request.get_json()
        df = json_normalize(jsonPD)
        df['Name'] = df['Name'].str.replace("'","-",regex=True)
        df['Comments'] = df['Comments'].str.replace("'","-",regex=True)
        print(df)
        for x in range(len(df)):
            try:
                _loop2.run_until_complete(Demand_CycleModel.add_Demand_Cycle(df.id[x], df.Name[x], 1, User, df.StartDate[x], df.EndDate[x], df.Comments[x]))
            except Exception as ex:
                pass
        return dict(msj='Accion Realizada Correctamente')
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500