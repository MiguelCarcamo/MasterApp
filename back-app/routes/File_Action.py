from flask import Blueprint, jsonify, request
import asyncio
from database.db import conn
import pandas as pd
from pandas import json_normalize
import json

from models.Style_CustomerModel import Style_CustomerModel
from models.Style_GlobalCategoryModel import Style_GlobalCategoryModel
from models.Style_WorkcenterModel import Style_WorkcenterModel
from models.Style_GeneralInfoModel import Style_GeneralInfoModel
from models.Style_SewingModel import Style_SewingModel
from models.Style_Sewing_FamilyModel import Style_Sewing_FamilyModel
from models.Style_Sewing_LayoutConfigurationModel import Style_Sewing_LayoutConfigurationModel

main=Blueprint('FileAction_blueprint', __name__)

from flask import request, send_from_directory
import os
from os import getcwd
from werkzeug.utils import secure_filename

PATH_FILES = getcwd() + '\\Files'
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) + '\\Files'
loop2 = asyncio.get_event_loop()

@main.route('/<id>')
def get_file(id):
    return send_from_directory(PATH_FILES, path=id, as_attachment=True)
    
@main.route('/add', methods=['POST'])
def add_file():
    try:
        x = request.files['File']
        ext = x.filename.split(".")[len(x.filename.split(".")) - 1]
        Process = request.form['Process']
        Plant = request.form['Plant']
        filename = Plant + "-"+ Process +"."+ ext
        x.save(os.path.join(PATH_FILES, secure_filename(filename)))
        url = PATH_FILES + "\\" + filename
        z1 = pd.read_excel(open(url, 'rb'), sheet_name='Sheet1', dtype={'Cut': str, 'Po_Number': str})
        textSQL = """
            SELECT  
                        --*
                Warehouses.WarehouseName AS [Goods Warehouse]
                ,RTrim(Case When ManufactureOrders.ManufactureID<=999999 Then 
                        Replicate('0', 6-Len(Cast(ManufactureOrders.ManufactureID As Nchar))) 
                    Else '' End
                    + Cast(ManufactureOrders.ManufactureID As Nchar)) As [Serial Number]
                ,ManufactureOrders.ManufactureNumber AS MO
                ,Orders.PONumber As [PO Number]
                ,ISNULL(ManufactureOrders.CutNumber,'001') AS [Cut Number]
                ,StatusNames.StatusName AS [Status]
                ,DropDownValues2.DropDownValue
                ,Orders.Comments4
                ,ManufactureOrders.QuantityOrdered
            FROM ManufactureOrders
            LEFT OUTER JOIN Warehouses ON ManufactureOrders.WarehouseID = Warehouses.WarehouseID
                LEFT OUTER JOIN Orders ON ManufactureOrders.OrderID = Orders.OrderID
                LEFT OUTER JOIN Addresses ON ManufactureOrders.CustomerID = Addresses.AddressID
                LEFT OUTER JOIN OrderItems ON ManufactureOrders.FirstOrderItemID = OrderItems.OrderItemID
                LEFT OUTER JOIN StyleColors ON OrderItems.StyleColorID = StyleColors.StyleColorID
                LEFT OUTER JOIN Styles ON OrderItems.StyleID = Styles.StyleID
                LEFT OUTER JOIN Divisions ON Styles.DivisionID = Divisions.DivisionID
                LEFT OUTER JOIN StyleCategories ON Styles.StyleCategoryID = StyleCategories.StyleCategoryID
                LEFT OUTER JOIN Seasons ON Styles.SeasonID = Seasons.SeasonID
                LEFT OUTER JOIN StatusNames ON ManufactureOrders.StatusID = StatusNames.StatusID
                LEFT OUTER JOIN DropDownValues2 ON Orders.OrderTypeID3 = DropDownValues2.DropDownValueID


            WHERE ManufactureOrders.StatusID NOT IN (95,20)
                AND ManufactureOrders.MfgOrderTypeID IN (SELECT EnumValueID FROM EnumValues WHERE EnumName='MfgOrderType' AND EnumValue In('New','Cut'))
                AND ( Orders.RequiredDate  > { d '2022-01-01' } OR ManufactureOrders.TargetDate > { d '2022-01-01' })
                AND ManufactureOrders.Archived = 0
                --AND (StyleCategories.StyleCategoryName <> 'Sub Assembly' OR Addresses.CompanyNumber NOT IN ('NHL', 'IKC'))
                AND (StyleCategories.StyleCategoryName <> 'Sub Assembly')
                AND Addresses.CompanyNumber NOT IN ('IKC')
                AND     Warehouses.WarehouseName in
                ('FGW-27 Calle',
                'FGW-Southern',
                'FGW-Arena',
                'FGW-Arena-Stock',
                'FGW-Arena-RQT'
                ,'FGW-Arena-Modified'
                --,'FGW-Decotex',
                )
            UNION
            SELECT  
                --*
                Warehouses.WarehouseName AS [Goods Warehouse]
                ,RTrim(Case When ManufactureOrders.ManufactureID<=999999 Then 
                        Replicate('0', 6-Len(Cast(ManufactureOrders.ManufactureID As Nchar))) 
                    Else '' End
                    + Cast(ManufactureOrders.ManufactureID As Nchar)) As [Serial Number]
                ,ManufactureOrders.ManufactureNumber AS MO
                ,Orders.PONumber As [PO Number]
                ,ISNULL(ManufactureOrders.CutNumber,'001') AS [Cut Number]
                ,StatusNames.StatusName AS [Status]
                ,DropDownValues2.DropDownValue
                ,Orders.Comments4
                ,ManufactureOrders.QuantityOrdered
            FROM ManufactureOrders
            LEFT OUTER JOIN Warehouses ON ManufactureOrders.WarehouseID = Warehouses.WarehouseID
                LEFT OUTER JOIN Orders ON ManufactureOrders.OrderID = Orders.OrderID
                LEFT OUTER JOIN Addresses ON ManufactureOrders.CustomerID = Addresses.AddressID
                LEFT OUTER JOIN OrderItems ON ManufactureOrders.FirstOrderItemID = OrderItems.OrderItemID
                LEFT OUTER JOIN StyleColors ON OrderItems.StyleColorID = StyleColors.StyleColorID
                LEFT OUTER JOIN Styles ON OrderItems.StyleID = Styles.StyleID
                LEFT OUTER JOIN Divisions ON Styles.DivisionID = Divisions.DivisionID
                LEFT OUTER JOIN StyleCategories ON Styles.StyleCategoryID = StyleCategories.StyleCategoryID
                LEFT OUTER JOIN Seasons ON Styles.SeasonID = Seasons.SeasonID
                LEFT OUTER JOIN StatusNames ON ManufactureOrders.StatusID = StatusNames.StatusID
                LEFT OUTER JOIN DropDownValues2 ON Orders.OrderTypeID3 = DropDownValues2.DropDownValueID


            WHERE ManufactureOrders.StatusID NOT IN (95,20)
                AND ManufactureOrders.MfgOrderTypeID IN (SELECT EnumValueID FROM EnumValues WHERE EnumName='MfgOrderType' AND EnumValue In('New','Standard'))
                AND ( Orders.RequiredDate  > { d '2022-01-01' } OR ManufactureOrders.TargetDate > { d '2022-01-01' })
                AND ManufactureOrders.Archived = 0
                AND     Warehouses.WarehouseName = 'FGW-Arena-Modified'
            UNION
            SELECT  
                --*
                Warehouses.WarehouseName AS [Goods Warehouse]
                ,RTrim(Case When ManufactureOrders.ManufactureID<=999999 Then 
                        Replicate('0', 6-Len(Cast(ManufactureOrders.ManufactureID As Nchar))) 
                    Else '' End
                    + Cast(ManufactureOrders.ManufactureID As Nchar)) As [Serial Number]
                ,ManufactureOrders.ManufactureNumber AS MO
                ,Orders.PONumber As [PO Number]
                ,ISNULL(ManufactureOrders.CutNumber,'001') AS [Cut Number]
                ,StatusNames.StatusName AS [Status]
                ,DropDownValues2.DropDownValue
                ,Orders.Comments4
                ,ManufactureOrders.QuantityOrdered
            FROM ManufactureOrders
            LEFT OUTER JOIN Warehouses ON ManufactureOrders.WarehouseID = Warehouses.WarehouseID
                LEFT OUTER JOIN Orders ON ManufactureOrders.OrderID = Orders.OrderID
                LEFT OUTER JOIN Addresses ON ManufactureOrders.CustomerID = Addresses.AddressID
                LEFT OUTER JOIN OrderItems ON ManufactureOrders.FirstOrderItemID = OrderItems.OrderItemID
                LEFT OUTER JOIN StyleColors ON OrderItems.StyleColorID = StyleColors.StyleColorID
                LEFT OUTER JOIN Styles ON OrderItems.StyleID = Styles.StyleID
                LEFT OUTER JOIN Divisions ON Styles.DivisionID = Divisions.DivisionID
                LEFT OUTER JOIN StyleCategories ON Styles.StyleCategoryID = StyleCategories.StyleCategoryID
                LEFT OUTER JOIN Seasons ON Styles.SeasonID = Seasons.SeasonID
                LEFT OUTER JOIN StatusNames ON ManufactureOrders.StatusID = StatusNames.StatusID
                LEFT OUTER JOIN DropDownValues2 ON Orders.OrderTypeID3 = DropDownValues2.DropDownValueID
            WHERE ManufactureOrders.StatusID NOT IN (95,20) 
                    AND ManufactureOrders.MfgOrderTypeID IN (SELECT EnumValueID FROM EnumValues WHERE EnumName='MfgOrderType' AND EnumValue In('New','Cut'))
                    AND StyleCategories.StyleCategoryName = 'Jersey'
                    AND ( Case When Exists((
                    Select * From ManufactureDetails
                    Where ManufactureID=ManufactureOrders.ManufactureID And RawMaterialID Is Not Null
                    )) Then 1 Else 0 End ) = 1
        """
        df_mo = pd.json_normalize(loop2.run_until_complete(conn.runServer3(textSQL)))
        df_mo[['PO Number','Cut Number']] = df_mo[['PO Number','Cut Number']].astype(str)
        z1[['Po_Number', 'Cut']] = z1[['Po_Number', 'Cut']].astype(str)
        merge1 = z1.merge(df_mo, how='inner', left_on=['Po_Number', 'Cut'], right_on=['PO Number','Cut Number'])
        merge2 = z1.merge(df_mo, how='inner', left_on=['Po_Number', 'Cut'], right_on=['MO','Cut Number'])
        z = pd.concat([merge1, merge2], ignore_index=True)
        z = z.drop(columns=['Goods Warehouse','DropDownValue','PromisedDate','Comments','PromisedDateProcess', 'Assigned_Date', 'NumAssigned','Cut Number','AdjustedPromisedDateProcess'])
        z = z.drop_duplicates(['Po_Number','Cut'])
        z = z1.merge(z, how='left', left_on=['Po_Number', 'Cut'], right_on=['Po_Number', 'Cut'])
        z = z.drop_duplicates(['Po_Number','Cut'])
        z = z.fillna('NULL')
        # z = z[z.MO != 'NULL']
        z = z.astype({"PromisedDate":"str","PromisedDateProcess":"str","Assigned_Date":"str","AdjustedPromisedDateProcess":"str"})
        z = z.replace({"00:00:00": 'NULL'})
        z = z.rename_axis('id').reset_index()
        result = z.to_json(orient="records")
        return result
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500

@main.route('/StyleCustumer', methods=['POST'])
def add_StyleCustumerFile():
    try:
        x = request.files['File']
        ext = x.filename.split(".")[len(x.filename.split(".")) - 1]
        filename = "StyleFile1."+ ext
        x.save(os.path.join(PATH_FILES, secure_filename(filename)))
        url = PATH_FILES + "\\" + filename
        file = open(url, "rb")
        z1 = pd.read_excel(file, sheet_name='StylesDatas', dtype={'Cut': str})
        file.close()
        Customer = z1.drop(['GlobalCategory','Costura_PE', 'WorkCenter', 'Costura_Familia','Costura_LayoutConfiguration','StyleNumber','Costura_Operators','Costura_SAM','Costura_Goal_Pcs','Style_Comments','Style_LeadTimeDays','Style_Workflow'], axis=1)
        Customer = Customer.drop_duplicates()
        Customer = Customer[Customer['Customer'].notna()]
        Customer['Customer'] = Customer['Customer'].str.rstrip()
        if(len(Customer) > 0):
            try:
                Style_Customer = Style_CustomerModel.get_Style_Customer()
                Style_Customer = json_normalize(Style_Customer)
                merge1_Customer = Customer.merge(Style_Customer, how='left', left_on=['Customer'], right_on=['Style_Customer'])
                merge1_Customer = merge1_Customer.fillna({'id':0})
            except Exception as ex:
                Customer = Customer.assign(id=0)
                merge1_Customer = Customer.assign(Comments="")
            result = merge1_Customer.to_json(orient="records")
            return result
        else:
            return jsonify({'message': 'No Data'}), 200
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500

@main.route('/StyleGlobalCategory', methods=['POST'])
def add_StyleGlobalCategoryFile():
    try:
        x = request.files['File']
        ext = x.filename.split(".")[len(x.filename.split(".")) - 1]
        filename = "StyleFile2."+ ext
        x.save(os.path.join(PATH_FILES, secure_filename(filename)))
        url = PATH_FILES + "\\" + filename
        file = open(url, "rb")
        z1 = pd.read_excel(file, sheet_name='StylesDatas', dtype={'Cut': str})
        file.close()
        GlobalCategory = z1.drop(['WorkCenter', 'Costura_PE', 'Costura_Familia','Costura_LayoutConfiguration','StyleNumber','Costura_Operators','Costura_SAM','Costura_Goal_Pcs','Style_Comments','Style_LeadTimeDays','Style_Workflow'], axis=1)
        GlobalCategory = GlobalCategory.drop_duplicates()
        GlobalCategory = GlobalCategory[GlobalCategory['GlobalCategory'].notna()]
        GlobalCategory['GlobalCategory'] = GlobalCategory['GlobalCategory'].str.rstrip()
        GlobalCategory['Customer'] = GlobalCategory['Customer'].str.rstrip()
        if(len(GlobalCategory) > 0):
            try:
                Style_GlobalCategory = Style_GlobalCategoryModel.get_Style_GlobalCategory()
                Style_GlobalCategory = json_normalize(Style_GlobalCategory)
                Style_GlobalCategory.drop(['LastUpdateDate','UserUpdate'], axis = 'columns', inplace=True)
                merge1_Customer = GlobalCategory.merge(Style_GlobalCategory, how='left', left_on=['GlobalCategory'], right_on=['GlobalCategory'])
                merge1_Customer.drop(['Id_Style_Customer','Style_Customer'], axis = 'columns', inplace=True)
            except Exception as ex:
                merge1_Customer = GlobalCategory.assign(id=0)
                merge1_Customer = merge1_Customer.assign(Comments="")
            Style_Customer = Style_CustomerModel.get_Style_Customer()
            Style_Customer = json_normalize(Style_Customer)
            Style_Customer.drop(['LastUpdateDate','UserUpdate','Comments'], axis = 'columns', inplace=True)
            Style_Customer = Style_Customer.rename(columns={'id':'Id_Style_Customer'})
            merge1_Customer = merge1_Customer.merge(Style_Customer, how='left', left_on=['Customer'], right_on=['Style_Customer'])
            merge1_Customer = merge1_Customer.fillna({'id':0, 'Id_Style_Customer':0})
            result = merge1_Customer.to_json(orient="records")
            return result
        else:
            return jsonify({'message': 'No Data'}), 200
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500
    
@main.route('/StyleWorkcenter', methods=['POST'])
def add_StyleWorkcenterFile():
    try:
        x = request.files['File']
        ext = x.filename.split(".")[len(x.filename.split(".")) - 1]
        filename = "StyleFile3."+ ext
        x.save(os.path.join(PATH_FILES, secure_filename(filename)))
        url = PATH_FILES + "\\" + filename
        file = open(url, "rb")
        z1 = pd.read_excel(file, sheet_name='StylesDatas', dtype={'Cut': str})
        file.close()
        Workcenter = z1.drop(['Customer', 'Costura_Familia','Costura_LayoutConfiguration','StyleNumber','Costura_Operators','Costura_SAM','Costura_Goal_Pcs','Style_Comments','Style_LeadTimeDays','Style_Workflow'], axis=1)
        Workcenter = Workcenter.drop_duplicates()
        Workcenter = Workcenter[Workcenter['WorkCenter'].notna()]
        Workcenter['GlobalCategory'] = Workcenter['GlobalCategory'].str.rstrip()
        Workcenter['WorkCenter'] = Workcenter['WorkCenter'].str.rstrip()
        Workcenter['WorkCenter'] = Workcenter['WorkCenter'].astype(str)
        if(len(Workcenter) > 0):
            try:
                Style_Workcenter = Style_WorkcenterModel.get_Style_Workcenter()
                Style_Workcenter = json_normalize(Style_Workcenter)
                Style_Workcenter.drop(['LastUpdateDate','UserUpdate','GlobalCategory'], axis = 'columns', inplace=True)
                merge1_Customer = Workcenter.merge(Style_Workcenter, how='left', left_on=['WorkCenter'], right_on=['Style_WorkCenter'])
                merge1_Customer.drop(['Style_WorkCenter','Id_Style_Customer','Style_Customer','Id_Style_GlobalCategory'], axis = 'columns', inplace=True)
            except Exception as ex:
                merge1_Customer = Workcenter.assign(id=0)
                merge1_Customer = merge1_Customer.assign(Comments="")
            Style_GlobalCategory = Style_GlobalCategoryModel.get_Style_GlobalCategory()
            Style_GlobalCategory = json_normalize(Style_GlobalCategory)
            Style_GlobalCategory = Style_GlobalCategory.rename(columns={'id':'Id_Style_GlobalCategory'})
            Style_GlobalCategory.drop(['LastUpdateDate','UserUpdate','Comments'], axis = 'columns', inplace=True)
            merge1_Customer = merge1_Customer.merge(Style_GlobalCategory, how='left', left_on=['GlobalCategory'], right_on=['GlobalCategory'])
            merge1_Customer = merge1_Customer.fillna({'id':0, 'Id_Style_GlobalCategory':0})
            result = merge1_Customer.to_json(orient="records")
            return result
        else:
            return jsonify({'message': 'No Data'}), 200
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500

@main.route('/StyleGeneral', methods=['POST'])
def add_StyleGeneralFile():
    try:
        x = request.files['File']
        ext = x.filename.split(".")[len(x.filename.split(".")) - 1]
        filename = "StyleFile4."+ ext
        x.save(os.path.join(PATH_FILES, secure_filename(filename)))
        url = PATH_FILES + "\\" + filename
        file = open(url, "rb")
        z1 = pd.read_excel(file, sheet_name='StylesDatas', dtype={'Cut': str})
        file.close()
        GeneralInfo = z1.drop(['Customer', 'GlobalCategory', 'Costura_Familia','Costura_LayoutConfiguration','Costura_Operators','Costura_SAM','Costura_Goal_Pcs'], axis=1)
        GeneralInfo = GeneralInfo.drop_duplicates()
        GeneralInfo = GeneralInfo[GeneralInfo['StyleNumber'].notna()]
        GeneralInfo['StyleNumber'] = GeneralInfo['StyleNumber'].astype(str)
        GeneralInfo['WorkCenter'] = GeneralInfo['WorkCenter'].astype(str)
        GeneralInfo['StyleNumber'] = GeneralInfo['StyleNumber'].str.rstrip()
        GeneralInfo['WorkCenter'] = GeneralInfo['WorkCenter'].str.rstrip()
        if(len(GeneralInfo) > 0):
            try:
                Style_GeneralInfo = Style_GeneralInfoModel.get_Style_GeneralInfo()
                Style_GeneralInfo = json_normalize(Style_GeneralInfo)
                Style_GeneralInfo.drop(['Style_WorkCenter','Id_Style_Customer','Style_Customer','Id_Style_GlobalCategory','Id_Style_WorkCenter','Style_WorkCenter','GlobalCategory'], axis = 'columns', inplace=True)
                merge1_Customer = GeneralInfo.merge(Style_GeneralInfo, how='left', left_on=['StyleNumber'], right_on=['StyleName'])
            except Exception as ex:
                merge1_Customer = GeneralInfo.assign(id=0, TypeStyle=1, Comments="" )
            Style_Workcenter = Style_WorkcenterModel.get_Style_Workcenter()
            Style_Workcenter = json_normalize(Style_Workcenter)
            Style_Workcenter.drop(['LastUpdateDate','UserUpdate','GlobalCategory','Id_Style_GlobalCategory','Comments','Id_Style_Customer','Style_Customer'], axis = 'columns', inplace=True)
            Style_Workcenter = Style_Workcenter.rename(columns={'id':'Id_Style_WorkCenter'})
            merge1_Customer = merge1_Customer.merge(Style_Workcenter, how='left', left_on=['WorkCenter'], right_on=['Style_WorkCenter'])
            merge1_Customer = merge1_Customer.fillna({'id':0, 'Id_Style_WorkCenter':0, 'Style_LeadTimeDays':0, 'TypeStyle':1})
            result = merge1_Customer.to_json(orient="records")
            return result
        else:
            return jsonify({'message': 'No Data'}), 200
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500

@main.route('/StyleSewFamily', methods=['POST'])
def add_StyleSewFamilyFile():
    try:
        x = request.files['File']
        ext = x.filename.split(".")[len(x.filename.split(".")) - 1]
        filename = "StyleFile6."+ ext
        x.save(os.path.join(PATH_FILES, secure_filename(filename)))
        url = PATH_FILES + "\\" + filename
        file = open(url, "rb")
        z1 = pd.read_excel(file, sheet_name='StylesDatas', dtype={'Cut': str})
        file.close()
        Family = z1.drop(['Customer', 'GlobalCategory', 'Costura_LayoutConfiguration','StyleNumber','Costura_Operators','Costura_SAM','Costura_Goal_Pcs','Style_Comments','Style_LeadTimeDays','Style_Workflow'], axis=1)
        Family = Family.drop_duplicates()
        Family = Family[Family['Costura_Familia'].notna()]
        Family['Costura_Familia'] = Family['Costura_Familia'].str.rstrip()
        Family['WorkCenter'] = Family['WorkCenter'].str.rstrip()
        if(len(Family) > 0):
            try:
                Style_SewFamily = Style_Sewing_FamilyModel.get_Style_Sewing_Family()
                Style_SewFamily = json_normalize(Style_SewFamily)
                merge1_Customer = Family.merge(Style_SewFamily, how='left', left_on=['Costura_Familia'], right_on=['Style_Family'])
                merge1_Customer.drop(['LastUpdateDate','UserUpdate','Id_Style_GlobalCategory','Style_WorkCenter','GlobalCategory','Id_Style_Customer','Style_Customer','Id_Style_WorkCenter'], axis = 'columns', inplace=True)
            except Exception as ex:
                merge1_Customer = Family.assign(id=0, Comments="" )
            Style_Workcenter = Style_WorkcenterModel.get_Style_Workcenter()
            Style_Workcenter = json_normalize(Style_Workcenter)
            Style_Workcenter.drop(['LastUpdateDate','UserUpdate','GlobalCategory','Id_Style_GlobalCategory','Comments','Id_Style_Customer','Style_Customer'], axis = 'columns', inplace=True)
            Style_Workcenter = Style_Workcenter.rename(columns={'id':'Id_Style_WorkCenter'})
            merge1_Customer = merge1_Customer.merge(Style_Workcenter, how='left', left_on=['WorkCenter'], right_on=['Style_WorkCenter'])
            merge1_Customer = merge1_Customer.fillna({'id':0, 'Id_Style_WorkCenter':0})
            result = merge1_Customer.to_json(orient="records")
            return result
        else:
            return jsonify({'message': 'No Data'}), 200
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500

@main.route('/StyleSewLayout', methods=['POST'])
def add_StyleSewLayoutFile():
    try:
        x = request.files['File']
        ext = x.filename.split(".")[len(x.filename.split(".")) - 1]
        filename = "StyleFile7."+ ext
        x.save(os.path.join(PATH_FILES, secure_filename(filename)))
        url = PATH_FILES + "\\" + filename
        file = open(url, "rb")
        z1 = pd.read_excel(file, sheet_name='StylesDatas', dtype={'Cut': str})
        file.close()
        Layout = z1.drop(['Customer', 'GlobalCategory', 'WorkCenter','StyleNumber','Costura_Operators','Costura_SAM','Costura_Goal_Pcs','Style_Comments','Style_LeadTimeDays','Style_Workflow'], axis=1)
        Layout = Layout.drop_duplicates()
        Layout = Layout[Layout['Costura_LayoutConfiguration'].notna()]
        Layout['Costura_LayoutConfiguration'] = Layout['Costura_LayoutConfiguration'].str.rstrip()
        Layout['Costura_Familia'] = Layout['Costura_Familia'].str.rstrip()
        if(len(Layout) > 0):
            try:
                Style_SewFamily = Style_Sewing_LayoutConfigurationModel.get_Style_Sewing_LayoutConfiguration()
                Style_SewFamily = json_normalize(Style_SewFamily)
                merge1_Customer = Layout.merge(Style_SewFamily, how='left', left_on=['Costura_LayoutConfiguration'], right_on=['LayoutConfiguration'])
                merge1_Customer.drop(['LastUpdateDate','UserUpdate','Id_Style_Family','LayoutConfiguration','Style_Family','Style_WorkCenter','GlobalCategory','Id_Style_Customer','Style_Customer','Id_Style_WorkCenter'], axis = 'columns', inplace=True)
            except Exception as ex:
                merge1_Customer = Layout.assign(id=0, Comments="" )
            Style_SewFamily = Style_Sewing_FamilyModel.get_Style_Sewing_Family()
            Style_SewFamily = json_normalize(Style_SewFamily)
            Style_SewFamily.drop(['LastUpdateDate','UserUpdate','Comments','Id_Style_GlobalCategory','Style_WorkCenter','GlobalCategory','Id_Style_Customer','Style_Customer','Id_Style_WorkCenter'], axis = 'columns', inplace=True)
            Style_SewFamily = Style_SewFamily.rename(columns={'id':'Id_Style_Family'})
            merge1_Customer = merge1_Customer.merge(Style_SewFamily, how='left', left_on=['Costura_Familia'], right_on=['Style_Family'])
            merge1_Customer = merge1_Customer.fillna({'id':0, 'Id_Style_Family':0})
            result = merge1_Customer.to_json(orient="records")
            return result
        else:
            return jsonify({'message': 'No Data'}), 200
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500

@main.route('/StyleSewInfo', methods=['POST'])
def add_StyleSewInfoFile():
    try:
        x = request.files['File']
        ext = x.filename.split(".")[len(x.filename.split(".")) - 1]
        filename = "StyleFile5."+ ext
        x.save(os.path.join(PATH_FILES, secure_filename(filename)))
        url = PATH_FILES + "\\" + filename
        file = open(url, "rb")
        z1 = pd.read_excel(file, sheet_name='StylesDatas', dtype={'Cut': str})
        file.close()
        GeneralSewInfo = z1.drop(['Customer', 'GlobalCategory', 'Costura_Familia','Style_Comments','Style_LeadTimeDays','Style_Workflow'], axis=1)
        GeneralSewInfo = GeneralSewInfo.drop_duplicates()
        GeneralSewInfo = GeneralSewInfo[GeneralSewInfo['StyleNumber'].notna()]
        GeneralSewInfo['StyleNumber'] = GeneralSewInfo['StyleNumber'].astype(str)
        GeneralSewInfo['StyleNumber'] = GeneralSewInfo['StyleNumber'].str.rstrip()
        GeneralSewInfo['Costura_LayoutConfiguration'] = GeneralSewInfo['Costura_LayoutConfiguration'].str.rstrip()
        if(len(GeneralSewInfo) > 0):
            try:
                Style_GeneralSewInfo = Style_SewingModel.get_Style_Sewing()
                Style_GeneralSewInfo = json_normalize(Style_GeneralSewInfo)
                Style_GeneralSewInfo.drop(['NumOperators','SAM','GOAL','PE','LastUpdateDate','UserUpdate','Id_Style_LayoutConfiguration','LayoutConfiguration','Id_Style_Family','Style_Family','Style_WorkCenter','Id_Style_Customer','Style_Customer','Id_Style_GlobalCategory','Id_Style_WorkCenter','Style_WorkCenter','GlobalCategory','Id_Style_GeneralInfo'], axis = 'columns', inplace=True)
                merge1_Customer = GeneralSewInfo.merge(Style_GeneralSewInfo, how='left', left_on=['StyleNumber'], right_on=['StyleName'])
            except Exception as ex:
                merge1_Customer = GeneralSewInfo.assign(id=0, Comments="" )
            Style_GeneralInfo = Style_GeneralInfoModel.get_Style_GeneralInfo()
            Style_GeneralInfo = json_normalize(Style_GeneralInfo)
            Style_GeneralInfo.drop(['LastUpdateDate','UserUpdate','TypeStyle','LeadTime_days','WorkFlow','Comments','Style_WorkCenter','Id_Style_Customer','Style_Customer','Id_Style_GlobalCategory','Id_Style_WorkCenter','Style_WorkCenter','GlobalCategory'], axis = 'columns', inplace=True)
            Style_GeneralInfo = Style_GeneralInfo.rename(columns={'id':'Id_Style_GeneralInfo'})
            merge1_Customer = merge1_Customer.merge(Style_GeneralInfo, how='left', left_on=['StyleNumber'], right_on=['StyleName'])
            Style_SewLayout = Style_Sewing_LayoutConfigurationModel.get_Style_Sewing_LayoutConfiguration()
            Style_SewLayout = json_normalize(Style_SewLayout)
            Style_SewLayout.drop(['Id_Style_Family','Comments','Id_Style_WorkCenter','LastUpdateDate','UserUpdate','Style_Family','Style_WorkCenter','Style_Customer','Id_Style_Customer','GlobalCategory'], axis = 'columns', inplace=True)
            Style_SewLayout = Style_SewLayout.rename(columns={'id':'Id_Style_LayoutConfiguration'})
            merge1_Customer = merge1_Customer.merge(Style_SewLayout, how='left', left_on=['Costura_LayoutConfiguration'], right_on=['LayoutConfiguration'])
            merge1_Customer = merge1_Customer.fillna({'id':0, 'Id_Style_LayoutConfiguration':0, 'Id_Style_GeneralInfo':0})
            result = merge1_Customer.to_json(orient="records")
            return result
        else:
            return jsonify({'message': 'No Data'}), 200
    except Exception as ex:
        print(ex)
        return jsonify({'message': str(ex)}), 500
