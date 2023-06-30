from flask import Blueprint, jsonify, request
import asyncio
from database.db import conn
import pandas as pd
import json

import os
from os import getcwd
from werkzeug.utils import secure_filename

loop2 = asyncio.get_event_loop()

main=Blueprint('FileActionForecast_blueprint', __name__)

@main.route('/NIKE/<year>', methods=['POST'])
def add_file(year):
    try:
        parent_dir = "D:\\Apps\\MasterApp\\back-app\\Files\\Cycle\\Forecast"
        v_path = os.path.join(parent_dir, str(year))
        contenido = os.listdir(parent_dir)
        if(len(contenido) == 0):
            os.mkdir(v_path)
        else:
            for fichero in contenido:
                if not str(year) in fichero:
                    os.mkdir(v_path)
        x = request.files['File']
        filename = x.filename
        url = os.path.join(v_path, secure_filename(filename))
        x.save(url)
        with open('D:\\Apps\\MasterApp\\back-app\\routes\\File_ForecastName.json') as file:
            data = json.load(file)

        df = pd.DataFrame()
        for a in range(len(data)):
            if data[a]['Customer'] == 'NIKE':
                for b in  range(len(data[a]['Container']['Sheets'])):
                    dct = {v: k for k, v in data[a]['Container']['Sheets'][b]['Column'].items()}
                    file = open(url, "rb")
                    z1 = pd.read_excel(file, sheet_name=data[a]['Container']['Sheets'][b]['Name'], header=data[a]['Container']['Sheets'][b]['PositionTitle'], usecols=list(data[a]['Container']['Sheets'][b]['Column'].values()) )
                    file.close()
                    z1 = z1.rename(dct, axis=1)  
                    if (len(df) == 0):
                        df = z1
                    else:
                        df = pd.concat([df, z1], ignore_index=True)
        df = df.fillna({'QuantityRequested':0})
        df.drop(df[(df['QuantityRequested'] == 0)].index, inplace=True)
        textSQL = """
                SELECT Style_GeneralInfo.StyleName, Style_WorkCenter.Style_WorkCenter, Style_GlobalCategory2.GlobalCategory, Style_Customer.Style_Customer
                FROM Style_GlobalCategory2
                INNER JOIN Style_Customer ON Style_GlobalCategory2.Id_Style_Customer = Style_Customer.Id_Style_Customer
                INNER JOIN Style_WorkCenter ON Style_GlobalCategory2.Id_Style_GlobalCategory = Style_WorkCenter.Id_Style_GlobalCategory
                INNER JOIN Style_GeneralInfo ON Style_WorkCenter.Id_Style_WorkCenter = Style_GeneralInfo.Id_Style_WorkCenter
                """
        df_style = pd.json_normalize(loop2.run_until_complete(conn.runServer(textSQL)))
        df_style['StyleName'] = df_style['StyleName'].astype(str)
        df['StyleNumber'] = df['StyleNumber'].astype(str)
        merge1 = df.merge(df_style, how='left', left_on=['StyleNumber'], right_on=['StyleName'])               
        merge1.to_excel(v_path + "\\NIKE-Model.xlsx", sheet_name='Sheet1', index=False)
        result = merge1.to_json(orient="records")
        return result
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500