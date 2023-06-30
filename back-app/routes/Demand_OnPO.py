from flask import Blueprint, jsonify, request
from models.Demand_OnPOModel import Demand_OnPOModel
import pandas as pd
import asyncio
import json
from pandas import json_normalize
from database.db import conn

main=Blueprint('Demand_OnPO_blueprint', __name__)
_loop2 = asyncio.get_event_loop()

@main.route('/')
def get_Demand_OnPO():
    try:
        Demand_OnPO = Demand_OnPOModel.get_Demand_OnPO()
        if(len(Demand_OnPO) > 0):
            return jsonify(Demand_OnPO)
        else:
            return jsonify({'message': str(ex)}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add/<User>', methods=['POST'])
def add_Demand_OnPO(User):
    try:
        jsonPD = request.get_json()
        df = json_normalize(jsonPD)
        for x in range(len(df)):
            try:
                # id, IDPlant, Id_Demand_Cycle, LastDateBuy, Status, Id_User, Comments
                _loop2.run_until_complete(Demand_OnPOModel.add_Demand_OnPO(df.id[x], df.IDPlant[x], df.Id_Demand_Cycle[x], df.LastDateBuy[x], df.Status[x], User, df.Comments[x]))
            except Exception as ex:
                pass
        return dict(msj='Accion Realizada Correctamente')
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500
    
@main.route('/Details/<id>')
def get_Demand_OnPODetails(id):
    try:
        Demand_Forecast = Demand_OnPOModel.get_Demand_OnPODetails(id)
        if(len(Demand_Forecast) > 0):
            return jsonify(Demand_Forecast)
        else:
            return jsonify({'message': str(ex)}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
    
@main.route('/Details/add/<User>', methods=['POST'])
def add_Demand_OnPODetails(User):
    try:
        jsonPD = request.get_json()
        df = json_normalize(jsonPD)
        for x in range(len(df)):
            try:
                #                                                                   ID_Demand_OnPOHeader, Country, StyleNumber, StyleSeason,                        StyleGender,        StyleColorWay,      StyleColorName, PlayerType,             ProductDescription,             IDPlant, ProductType,        CustomerCategory,          BuyDateReal,    BuyStatus,      SerialNumber, PurchaseOrder,            PurchaseOrderOld,         CurrentStatus,       CustomerPromisedDate,        PromisedDateSewing,         MaxPRD, CustomerOrderType, CustomerLeadTime, QuantityRequested, QuantitySewing
                _loop2.run_until_complete(Demand_OnPOModel.add_Demand_OnPODetails(df.ID_Demand_OnPOHeader[x], df.Country[x], df.StyleNumber[x], df.StyleSeason[x], df.StyleGender[x], df.StyleColorWay[x], df.StyleColorName[x], df.PlayerType[x], df.ProductDescription[x], df.IDPlant[x], df.ProductType[x], df.CustomerCategory[x], df.BuyDateReal[x], df.BuyStatus[x], df.SerialNumber[x], df.PurchaseOrder[x], df.PurchaseOrderOld[x], df.CurrentStatus[x], df.CustomerPromisedDate[x], df.PromisedDateSewing[x], df.MaxPRD[x], df.CustomerOrderType[x], df.CustomerLeadTime[x], df.QuantityRequested[x], df.QuantitySewing[x]))
            except Exception as ex:
                pass
        return dict(msj='Accion Realizada Correctamente')
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500