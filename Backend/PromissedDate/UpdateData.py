from email.headerregistry import Group
from PromissedData import MainPromissedDate
from database import conn as db
import asyncio
from os import getcwd
import pandas as pd
from TypePromissedDate import TypePD
import json
from numpy import size
import shutil
import os
from datetime import date

today = date.today()
# Parent Directory path
parent_dir = "D:\Apps\MasterApp\Backend\File"
v_path = os.path.join(parent_dir, str(today))
contenido = os.listdir(parent_dir)
cant = 1
for fichero in contenido:
    if str(today) in fichero:
        cant += 1
v_path += '(' + str(cant) +')' 
os.mkdir(v_path)
with open('DataExcel.json') as file:
    data = json.load(file)
Error = []
for i in range(len(data)):
    try:
        loop2 = asyncio.get_event_loop()
        Error2 = []
        var = data[i]['PATH_FILES']
        array = var.split("/")
        
        namevar = array[size(array)-1]
        excelfile = v_path + "\(" + data[i]['Proceso'] + ")" + namevar
        preparefile = v_path + "\excel-("+data[i]['Proceso']+")"+namevar
        preparefile2 = v_path + "\PPM-("+data[i]['Proceso']+")"+namevar
        shutil.copyfile(var, excelfile)
        x = MainPromissedDate(excelfile, data[i]['SheetName'], data[i]['Plant'], data[i]['Promissed'], data[i]['Assigned'], data[i]['AssignedWeeks'])
        z1 = loop2.run_until_complete(x.ModelData())
        # print("Paso 1")
        z1.to_excel(preparefile, sheet_name='Sheet1', index=False)
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
            AND ManufactureOrders.OrderID IN (SELECT OrderID FROM Orders WHERE ((RequiredDate >= { d '2022-01-01'  })))
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
            --,'FGW-Decotex','FGW-Arena-Modified'
            )
        """
        textSQL2 = """
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
            AND ManufactureOrders.OrderID IN (SELECT OrderID FROM Orders WHERE ((RequiredDate >= { d '2022-01-01'  })))
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
            --,'FGW-Decotex','FGW-Arena-Modified'
            )
        """

        df_mo = pd.json_normalize(loop2.run_until_complete(db.runServer3(textSQL)))
        df_mo.to_excel("test2.xlsx", sheet_name='Sheet1', index=False)
        df_mo2 = pd.json_normalize(loop2.run_until_complete(db.runServer3(textSQL2)))
        # print("Paso 2")
        if data[i]['Proceso'] == '':
            df_mo.to_excel("test1.xlsx", sheet_name='Sheet1', index=False)
            merge1 = z1.merge(df_mo, how='inner', left_on=['po_nomber'], right_on=['PO Number'])
            merge2 = z1.merge(df_mo, how='inner', left_on=['po_nomber'], right_on=['MO'])
            merge3 = z1.merge(df_mo2, how='inner', left_on=['po_nomber'], right_on=['PO Number'])
            merge4 = z1.merge(df_mo2, how='inner', left_on=['po_nomber'], right_on=['MO'])
            z = pd.concat([merge1, merge2, merge3, merge4], ignore_index=True)
            z = z.drop(columns=['Goods Warehouse','Promised Date','Serial Number', 'Cut Number', 'QuantityOrdered'])
            z = z.drop_duplicates('po_nomber')
            z = z1.merge(z, how='left', left_on=['po_nomber'], right_on=['po_nomber'])
            z = z.fillna('NULL')
        else:
            merge1 = z1.merge(df_mo, how='inner', left_on=['po_nomber', 'Cut'], right_on=['PO Number','Cut Number'])
            merge2 = z1.merge(df_mo, how='inner', left_on=['po_nomber', 'Cut'], right_on=['MO','Cut Number'])
            merge3 = z1.merge(df_mo2, how='inner', left_on=['po_nomber', 'Cut'], right_on=['PO Number','Cut Number'])
            merge4 = z1.merge(df_mo2, how='inner', left_on=['po_nomber', 'Cut'], right_on=['MO','Cut Number'])
            z = pd.concat([merge1, merge2, merge3, merge4], ignore_index=True)
            z = z.drop(columns=['Goods Warehouse','Status','QuantityOrdered','DropDownValue',data[i]['Promissed'], 'assigned_date', 'NumAssigned','Cut Number','Comments4'])
            z = z.drop_duplicates(['po_nomber','Cut'])
            z = z1.merge(z, how='left', left_on=['po_nomber', 'Cut'], right_on=['po_nomber', 'Cut'])
            z = z.drop_duplicates(['po_nomber','Cut'])
            z = z.fillna('NULL')
        z = z[z.MO != 'NULL']
        z.to_excel(preparefile2, sheet_name='Sheet1', index=False)
        for m in range(len(z.index)):
            try:
                if data[i]['Proceso'] == '':
                    x = TypePD(z.iloc[m,0],z.iloc[m,2],'',z.iloc[m,6],'',z.iloc[m,1],'','')
                    loop2.run_until_complete(db.runServer2(f"EXECUTE SP_PromisedDate_Action {data[i]['Plant']},1,'{x._Po}',{x._Mo},{x._promised_date},'Test Miguel Carcamo', {x._GruopPO} "))
                elif data[i]['Proceso'] == 'Sewing':
                    x = TypePD(z.iloc[m,0],z.iloc[m,6],z.iloc[m,5],'',z.iloc[m,1],z.iloc[m,2],z.iloc[m,3],z.iloc[m,4])
                    loop2.run_until_complete(db.runServer2(f"EXECUTE SP_PromisedDate_Sewing_Action '{x._Mo}','{x._CutNum}',{x._Serial},{data[i]['Plant']},1, {x._promised_date}, {x._promised_date}, {x._Assigned},'Test Miguel Carcamo'"))
                elif data[i]['Proceso'] == 'Cutting':
                    x = TypePD(z.iloc[m,0],z.iloc[m,6],z.iloc[m,5],'',z.iloc[m,1],z.iloc[m,2],z.iloc[m,3],z.iloc[m,4])
                    loop2.run_until_complete(db.runServer2(f"EXECUTE SP_PromisedDate_Cutting_Action '{x._Mo}','{x._CutNum}',{x._Serial},{data[i]['Plant']},1, {x._promised_date}, {x._promised_date}, {x._Assigned},'Test Miguel Carcamo'"))
                elif data[i]['Proceso'] == 'EMBR':
                    x = TypePD(z.iloc[m,0],z.iloc[m,6],z.iloc[m,5],'',z.iloc[m,1],z.iloc[m,2],z.iloc[m,3],z.iloc[m,4])
                    loop2.run_until_complete(db.runServer2(f"EXECUTE SP_PromisedDate_Embroidery_Action '{x._Po}','{x._CutNum}',{x._Serial},{data[i]['Plant']},1, {x._promised_date}, {x._promised_date}, {x._Assigned},'Test Miguel Carcamo'"))
                elif data[i]['Proceso'] == 'EMBR-FG':
                    x = TypePD(z.iloc[m,0],z.iloc[m,6],z.iloc[m,5],'',z.iloc[m,1],z.iloc[m,2],z.iloc[m,3],z.iloc[m,4])
                    loop2.run_until_complete(db.runServer2(f"EXECUTE SP_PromisedDate_EmbroideryFG_Action '{x._Po}','{x._CutNum}',{x._Serial},{data[i]['Plant']},1, {x._promised_date}, {x._promised_date}, {x._Assigned},'Test Miguel Carcamo'"))
                elif data[i]['Proceso'] == 'SP':
                    x = TypePD(z.iloc[m,0],z.iloc[m,6],z.iloc[m,5],'',z.iloc[m,1],z.iloc[m,2],z.iloc[m,3],z.iloc[m,4])
                    loop2.run_until_complete(db.runServer2(f"EXECUTE SP_PromisedDate_ScreePrintingCP_Action '{x._Po}','{x._CutNum}',{x._Serial},{data[i]['Plant']},1, {x._promised_date}, {x._promised_date}, {x._Assigned},'Test Miguel Carcamo'"))
                elif data[i]['Proceso'] == 'SUB':
                    x = TypePD(z.iloc[m,0],z.iloc[m,6],z.iloc[m,5],'',z.iloc[m,1],z.iloc[m,2],z.iloc[m,3],z.iloc[m,4])
                    loop2.run_until_complete(db.runServer2(f"EXECUTE SP_PromisedDate_Sublimated_Action '{x._Po}','{x._CutNum}',{x._Serial},{data[i]['Plant']},1, {x._promised_date}, {x._promised_date}, {x._Assigned},'Test Miguel Carcamo'"))
                elif data[i]['Proceso'] == 'PLOTTER':
                    x = TypePD(z.iloc[m,0],z.iloc[m,6],z.iloc[m,5],'',z.iloc[m,1],z.iloc[m,2],z.iloc[m,3],z.iloc[m,4])
                    loop2.run_until_complete(db.runServer2(f"EXECUTE SP_PromisedDate_Plotter_Action '{x._Po}','{x._CutNum}',{x._Serial},{data[i]['Plant']},1, {x._promised_date}, {x._promised_date}, {x._Assigned},'Test Miguel Carcamo'"))
                elif data[i]['Proceso'] == 'Carrusel':
                    x = TypePD(z.iloc[m,0],z.iloc[m,6],z.iloc[m,5],'',z.iloc[m,1],z.iloc[m,2],z.iloc[m,3],z.iloc[m,4])
                    loop2.run_until_complete(db.runServer2(f"EXECUTE SP_PromisedDate_Carrusel_Action '{x._Po}','{x._CutNum}',{x._Serial},{data[i]['Plant']},1, {x._promised_date}, {x._promised_date}, {x._Assigned},'Test Miguel Carcamo'"))
                elif data[i]['Proceso'] == 'Perforation':
                    x = TypePD(z.iloc[m,0],z.iloc[m,6],z.iloc[m,5],'',z.iloc[m,1],z.iloc[m,2],z.iloc[m,3],z.iloc[m,4])
                    loop2.run_until_complete(db.runServer2(f"EXECUTE SP_PromisedDate_Perforation_Action '{x._Po}','{x._CutNum}',{x._Serial},{data[i]['Plant']},1, {x._promised_date}, {x._promised_date}, {x._Assigned},'Test Miguel Carcamo'"))
                elif data[i]['Proceso'] == 'Twill':
                    x = TypePD(z.iloc[m,0],z.iloc[m,6],z.iloc[m,5],'',z.iloc[m,1],z.iloc[m,2],z.iloc[m,3],z.iloc[m,4])
                    loop2.run_until_complete(db.runServer2(f"EXECUTE SP_PromisedDate_Twill_Action '{x._Po}','{x._CutNum}',{x._Serial},{data[i]['Plant']},1, {x._promised_date}, {x._promised_date}, {x._Assigned},'Test Miguel Carcamo'"))
            except:
                Error2.append(str(x._Po))
        print(Error2)
    except:
        Error.append(str(data[i]['Planta'] +'-'+ data[i]['Proceso']))
print(Error)