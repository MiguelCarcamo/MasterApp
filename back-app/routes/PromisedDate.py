from flask import Blueprint, jsonify, request
from models.PromisedDateModel import PromisedDateModel
import pandas as pd
import json
from pandas import json_normalize
import asyncio
from database.db import conn
from datetime import datetime

main=Blueprint('PromisedDate_blueprint', __name__)
_loop2 = asyncio.get_event_loop()
@main.route('/add/<Plant>/<Process>', methods=['POST'])
def add_PromisedDate(Plant, Process):
    try:
        jsonPD = request.get_json()
        df = json_normalize(jsonPD)
        textSQL = """
            SELECT PurchaseOrder, MO, CuttingNum, 
                PromisedDateSewing, PromisedDateCutting, PromisedDateScreePrintingCP, PromisedDateScreePrintingFG, PromisedDateEmbroidery, PromisedDateEmbroideryFG, PromisedDateSublimated, PromisedDatePlotter, PromisedDateCarrusel, PromisedDateCarruselFG, PromisedDatePerforation, PromisedDateTwill, PromisedDateHeatTransfer, PromisedDateNameplate, PromisedDatePadPrint
            FROM PromisedDate_HN
        """
        df_pd = pd.json_normalize(_loop2.run_until_complete(conn.runServer(textSQL)))
        merge1 = df.merge(df_pd, how='left', left_on=['MO', 'Cut'], right_on=['MO','CuttingNum'])
        # merge1 = merge1.drop(columns=['id', 'PurchaseOrder','MO','CuttingNum', 'PromisedDateSewing', 'PromisedDateCutting','PromisedDateScreePrintingCP', 'PromisedDateEmbroideryCP','PromisedDateEmbroideryFG', 'PromisedDateSublimated', 'PromisedDatePlotter', 'PromisedDateCarrusel', 'PromisedDatePerforation', 'PromisedDateTwill'])
        if(Process == 'Sewing'):
            merge1 = merge1.drop(columns=['id', 'PurchaseOrder','PO Number','CuttingNum', 'PromisedDateCutting','PromisedDateScreePrintingCP', 'PromisedDateEmbroidery','PromisedDateEmbroideryFG', 'PromisedDateSublimated', 'PromisedDatePlotter', 'PromisedDateCarrusel', 'PromisedDatePerforation', 'PromisedDateTwill', 'PromisedDateHeatTransfer', 'PromisedDateNameplate', 'PromisedDatePadPrint' , 'PromisedDateScreePrintingFG','PromisedDateCarruselFG'])
        if(Process == 'Cutting'):
            merge1 = merge1.drop(columns=['id', 'PurchaseOrder','PO Number','CuttingNum', 'PromisedDateSewing', 'PromisedDateScreePrintingCP', 'PromisedDateEmbroidery','PromisedDateEmbroideryFG', 'PromisedDateSublimated', 'PromisedDatePlotter', 'PromisedDateCarrusel', 'PromisedDatePerforation', 'PromisedDateTwill', 'PromisedDateHeatTransfer', 'PromisedDateNameplate', 'PromisedDatePadPrint' , 'PromisedDateScreePrintingFG','PromisedDateCarruselFG'])
        if(Process == 'ScreePrintingCP'):
            merge1 = merge1.drop(columns=['id', 'PurchaseOrder','PO Number','CuttingNum', 'PromisedDateSewing', 'PromisedDateCutting', 'PromisedDateEmbroidery','PromisedDateEmbroideryFG', 'PromisedDateSublimated', 'PromisedDatePlotter', 'PromisedDateCarrusel', 'PromisedDatePerforation', 'PromisedDateTwill', 'PromisedDateHeatTransfer', 'PromisedDateNameplate', 'PromisedDatePadPrint' , 'PromisedDateScreePrintingFG','PromisedDateCarruselFG'])
        if(Process == 'ScreePrintingFG'):
            merge1 = merge1.drop(columns=['id', 'PurchaseOrder','PO Number','CuttingNum', 'PromisedDateSewing', 'PromisedDateCutting', 'PromisedDateEmbroidery','PromisedDateEmbroideryFG', 'PromisedDateSublimated', 'PromisedDatePlotter', 'PromisedDateCarrusel', 'PromisedDatePerforation', 'PromisedDateTwill', 'PromisedDateHeatTransfer', 'PromisedDateNameplate', 'PromisedDatePadPrint' , 'PromisedDateScreePrintingCP','PromisedDateCarruselFG'])
        if(Process == 'Embroidery'):
            merge1 = merge1.drop(columns=['id', 'PurchaseOrder','PO Number','CuttingNum', 'PromisedDateSewing', 'PromisedDateCutting', 'PromisedDateScreePrintingCP','PromisedDateEmbroideryFG', 'PromisedDateSublimated', 'PromisedDatePlotter', 'PromisedDateCarrusel', 'PromisedDatePerforation', 'PromisedDateTwill', 'PromisedDateHeatTransfer', 'PromisedDateNameplate', 'PromisedDatePadPrint' , 'PromisedDateScreePrintingFG','PromisedDateCarruselFG'])
        if(Process == 'EmbroideryFG'):
            merge1 = merge1.drop(columns=['id', 'PurchaseOrder','PO Number','CuttingNum', 'PromisedDateSewing', 'PromisedDateCutting', 'PromisedDateScreePrintingCP','PromisedDateEmbroidery', 'PromisedDateSublimated', 'PromisedDatePlotter', 'PromisedDateCarrusel', 'PromisedDatePerforation', 'PromisedDateTwill', 'PromisedDateHeatTransfer', 'PromisedDateNameplate', 'PromisedDatePadPrint' , 'PromisedDateScreePrintingFG','PromisedDateCarruselFG'])
        if(Process == 'Carrusel'):
            merge1 = merge1.drop(columns=['id', 'PurchaseOrder','PO Number','CuttingNum', 'PromisedDateSewing', 'PromisedDateCutting', 'PromisedDateScreePrintingCP','PromisedDateEmbroidery', 'PromisedDateSublimated', 'PromisedDatePlotter', 'PromisedDateEmbroideryFG', 'PromisedDatePerforation', 'PromisedDateTwill', 'PromisedDateHeatTransfer', 'PromisedDateNameplate', 'PromisedDatePadPrint' , 'PromisedDateScreePrintingFG','PromisedDateCarruselFG'])
        if(Process == 'CarruselFG'):
            merge1 = merge1.drop(columns=['id', 'PurchaseOrder','PO Number','CuttingNum', 'PromisedDateSewing', 'PromisedDateCutting', 'PromisedDateScreePrintingCP','PromisedDateEmbroidery', 'PromisedDateSublimated', 'PromisedDatePlotter', 'PromisedDateEmbroideryFG', 'PromisedDatePerforation', 'PromisedDateTwill', 'PromisedDateHeatTransfer', 'PromisedDateNameplate', 'PromisedDatePadPrint' , 'PromisedDateScreePrintingFG','PromisedDateCarrusel'])
        if(Process == 'Perforation'):
            merge1 = merge1.drop(columns=['id', 'PurchaseOrder','PO Number','CuttingNum', 'PromisedDateSewing', 'PromisedDateCutting', 'PromisedDateScreePrintingCP','PromisedDateEmbroidery', 'PromisedDateSublimated', 'PromisedDatePlotter', 'PromisedDateCarrusel', 'PromisedDateEmbroideryFG', 'PromisedDateTwill', 'PromisedDateHeatTransfer', 'PromisedDateNameplate', 'PromisedDatePadPrint' , 'PromisedDateScreePrintingFG','PromisedDateCarruselFG'])
        if(Process == 'Twill'):
            merge1 = merge1.drop(columns=['id', 'PurchaseOrder','PO Number','CuttingNum', 'PromisedDateSewing', 'PromisedDateCutting', 'PromisedDateScreePrintingCP','PromisedDateEmbroidery', 'PromisedDateSublimated', 'PromisedDatePlotter', 'PromisedDateCarrusel', 'PromisedDatePerforation', 'PromisedDateEmbroideryFG', 'PromisedDateHeatTransfer', 'PromisedDateNameplate', 'PromisedDatePadPrint' , 'PromisedDateScreePrintingFG','PromisedDateCarruselFG'])
        if(Process == 'Plotter'):
            merge1 = merge1.drop(columns=['id', 'PurchaseOrder','PO Number','CuttingNum', 'PromisedDateSewing', 'PromisedDateCutting', 'PromisedDateScreePrintingCP','PromisedDateEmbroidery', 'PromisedDateSublimated', 'PromisedDateTwill', 'PromisedDateCarrusel', 'PromisedDatePerforation', 'PromisedDateEmbroideryFG', 'PromisedDateHeatTransfer', 'PromisedDateNameplate', 'PromisedDatePadPrint' , 'PromisedDateScreePrintingFG','PromisedDateCarruselFG'])
        if(Process == 'Sublimated'):
            merge1 = merge1.drop(columns=['id', 'PurchaseOrder','PO Number','CuttingNum', 'PromisedDateSewing', 'PromisedDateCutting', 'PromisedDateScreePrintingCP','PromisedDateEmbroidery', 'PromisedDateTwill', 'PromisedDatePlotter', 'PromisedDateCarrusel', 'PromisedDatePerforation', 'PromisedDateEmbroideryFG', 'PromisedDateHeatTransfer', 'PromisedDateNameplate', 'PromisedDatePadPrint' , 'PromisedDateScreePrintingFG','PromisedDateCarruselFG'])
        if(Process == 'Nameplate'):
            merge1 = merge1.drop(columns=['id', 'PurchaseOrder','PO Number','CuttingNum', 'PromisedDateSewing', 'PromisedDateCutting', 'PromisedDateScreePrintingCP','PromisedDateEmbroidery','PromisedDateSublimated', 'PromisedDateTwill', 'PromisedDatePlotter', 'PromisedDateCarrusel', 'PromisedDatePerforation', 'PromisedDateEmbroideryFG', 'PromisedDateHeatTransfer', 'PromisedDatePadPrint' , 'PromisedDateScreePrintingFG','PromisedDateCarruselFG'])
        if(Process == 'PadPrint'):
            merge1 = merge1.drop(columns=['id', 'PurchaseOrder','PO Number','CuttingNum', 'PromisedDateSewing', 'PromisedDateCutting', 'PromisedDateScreePrintingCP','PromisedDateEmbroidery','PromisedDateSublimated', 'PromisedDateTwill', 'PromisedDatePlotter', 'PromisedDateCarrusel', 'PromisedDatePerforation', 'PromisedDateEmbroideryFG', 'PromisedDateHeatTransfer', 'PromisedDateNameplate', 'PromisedDateScreePrintingFG','PromisedDateCarruselFG'])
        if(Process == 'HeatTransfer'):
            merge1 = merge1.drop(columns=['id', 'PurchaseOrder','PO Number','CuttingNum', 'PromisedDateSewing', 'PromisedDateCutting', 'PromisedDateScreePrintingCP','PromisedDateEmbroidery','PromisedDateSublimated', 'PromisedDateTwill', 'PromisedDatePlotter', 'PromisedDateCarrusel', 'PromisedDatePerforation', 'PromisedDateEmbroideryFG', 'PromisedDateNameplate', 'PromisedDatePadPrint' , 'PromisedDateScreePrintingFG','PromisedDateCarruselFG'])
        data = merge1.assign(Cant=0)
        data = data.fillna('New')
        for x in range(len(data)):
            fecha_dt1 = data.iloc[x,3].split(" ")
            fecha_dt2 = data.iloc[x,4].split(" ")
            fecha_dt4 = data.iloc[x,5].split(" ")
            fecha_dt3 = data.iloc[x,2].split(" ")
            data.iloc[x,3] = fecha_dt1[0]
            data.iloc[x,4] = fecha_dt2[0]
            data.iloc[x,5] = fecha_dt4[0]
            data.iloc[x,2] = fecha_dt3[0]
            if (data.iloc[x,3] == data.iloc[x,12]):
                data.iloc[x,13] = 1
        data = data[data.Cant == 0]
        data.columns = ['Po_Number', 'Cut', 'PromisedDate', 'PromisedDateProcess', 'AdjustedPromisedDateProcess', 'Assigned_Date', 'NumAssigned', 'Comments', 'SerialNumber', 'MO', 'Status', 'Comments4', 'QuantityOrdered', 'PromisedDateOld', 'Cant']
        DataNew = data[data.PromisedDateOld == "New"]
        # print(DataNew)
        # print(data)
        # type2, Process, Plant, Comments, Po, Mo, Serial, GruopPO, CutNum, Date1, DateAdj, Date2, Assigned
        for x in range(len(DataNew)):
            PromisedDateModel.add_PromisedDate(1, Process, Plant, DataNew.iloc[x, 7], DataNew.iloc[x, 0], DataNew.iloc[x, 9], DataNew.iloc[x, 8], DataNew.iloc[x, 11], DataNew.iloc[x, 1], DataNew.iloc[x, 2], DataNew.iloc[x, 2], DataNew.iloc[x, 2], DataNew.iloc[x, 2])
        for x in range(len(data)):
            PromisedDateModel.add_PromisedDate(0, Process, Plant, data.iloc[x, 7], data.iloc[x, 0], data.iloc[x, 9], data.iloc[x, 8], data.iloc[x, 11], data.iloc[x, 1], data.iloc[x, 3], data.iloc[x, 4], data.iloc[x, 5], data.iloc[x, 6])
        return dict(msj='Accion Realizada Correctamente')
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500