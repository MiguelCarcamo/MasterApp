from flask import Blueprint, jsonify, request
from models.Demand_ForecastModel import Demand_ForecastModel
import pandas as pd
import asyncio
import json
from pandas import json_normalize
from database.db import conn

main=Blueprint('Demand_Forecast_blueprint', __name__)
_loop2 = asyncio.get_event_loop()

@main.route('/')
def get_Demand_Forecast():
    try:
        Demand_Forecast = Demand_ForecastModel.get_Demand_Forecast()
        if(len(Demand_Forecast) > 0):
            return jsonify(Demand_Forecast)
        else:
            return jsonify({'message': str(ex)}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add/<User>', methods=['POST'])
def add_Demand_Forecast(User):
    try:
        jsonPD = request.get_json()
        df = json_normalize(jsonPD)
        for x in range(len(df)):
            try:
                # id, Id_Style_Customer, Id_Demand_Cycle, CustomerForecastDate, Status, Id_User, Comments
                _loop2.run_until_complete(Demand_ForecastModel.add_Demand_Forecast(df.id[x], df.Id_Style_Customer[x], df.Id_Demand_Cycle[x], df.CustomerForecastDate[x], df.Status[x], User, df.Comments[x]))
            except Exception as ex:
                pass
        return dict(msj='Accion Realizada Correctamente')
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500

@main.route('/Details/<id>')
def get_Demand_ForecastDetails(id):
    try:
        Demand_Forecast = Demand_ForecastModel.get_Demand_ForecastDetails(id)
        if(len(Demand_Forecast) > 0):
            return jsonify(Demand_Forecast)
        else:
            return jsonify({'message': str(ex)}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/Details/add/<User>', methods=['POST'])
def add_Demand_ForecastDetails(User):
    try:
        jsonPD = request.get_json()
        df = json_normalize(jsonPD)
        for x in range(len(df)):
            try:
                _loop2.run_until_complete(Demand_ForecastModel.add_Demand_ForecastDetails(df.Id_Demand_ForecastHeader[x], df.Country[x], df.StyleNumber[x], df.StyleSeason[x], df.StyleGender[x], df.StyleColorWay[x], df.StyleColorName[x], df.ProductDescription[x], df.IDPlant[x], df.ProductType[x], df.CustomerCategory[x], df.BuyDateTentative[x], df.CustomerPromisedDate[x], df.CustomerOrderType[x], df.CustomerLeadTime[x], df.QuantityRequested[x]))
            except Exception as ex:
                pass
        return dict(msj='Accion Realizada Correctamente')
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500