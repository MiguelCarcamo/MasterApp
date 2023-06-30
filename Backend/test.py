# from PromissedDate.PromissedData import MainPromissedDate
# from PromissedDate.database import conn as db
# import asyncio

# path1 = "C:\\Users\\Miguel.Carcamo\\Desktop\\app\\MasterApp\\Backend\\PromissedDate\\File\\SewingOrdersData27ST - Planner1.xlsx"
# SheetName = "Master"
# Plant = None
# Promissed = "Promised Date"
# Assigned = "Assigned Date Sewing"
# AssignedWeeks = "Assigned Weeks Sewing"

# Error = []
# loop2 = asyncio.get_event_loop()
# x = MainPromissedDate(path1, SheetName, Plant, Promissed, Assigned, AssignedWeeks)
# z = loop2.run_until_complete(x.ModelData())
# for x in range(len(z.index)):
#     try:
#             loop2.run_until_complete(db.runServer2(f"EXECUTE SP_PromisedDate_Sewing_Action '{z.iloc[x,0]}','{z.iloc[x,1]}',{Plant},1,'{z.iloc[x,2]}','{z.iloc[x,3]}',{z.iloc[x,4]},'Test Miguel Carcamo'"))
#         # loop2.run_until_complete(db.runServer2(f"EXECUTE SP_PromisedDate_Action 1,1,'{z.iloc[x,0]}','{z.iloc[x,1]}','Test Miguel Carcamo'"))
#     except:
#         Error.append(z.iloc[x,0]+'|'+z.iloc[x,1])
# print(Error)

# import asyncio
# with open("C:\\Users\\Miguel.Carcamo\\Desktop\\app\\MasterApp\\DataBase\\Task\\sewing.sql", 'r') as myfile:
#     textSQL = myfile.read()
# text2 = """
# SELECT 
# 	WorkTransactions.ManufactureSerialNumber
# 	,WorkTransactions.WarehouseName
# 	,WorkTransactions.Title
# 	,WorkTransactions.TaskName
# 	,WorkTransactions.OperatorName
# 	,WorkTransactions.OperatorNumber
# 	,WorkTransactions.TransactionDate
# 	,WorkTransactions.TransactionTime
# 	,case when WorkTransactions.TransactionTime < '06:00:00' then DATEADD(day,-1, WorkTransactions.TransactionDate) else WorkTransactions.TransactionDate END AS TransactionDate2
# 	,SUM(WorkTransactions.Quantity) As Quantity
# FROM
# (
# 	SELECT  
# 		RTrim(Case When ManufactureOrders.ManufactureID<=999999 Then 
# 						Replicate('0',6-Len(Cast(ManufactureOrders.ManufactureID As Nchar))) 
# 					Else '' 
# 					End + Cast(ManufactureOrders.ManufactureID As Nchar)) As ManufactureSerialNumber,
# 		Addresses5.ContactTitle As Title,
# 		Addresses5.CompanyName As OperatorName,
# 		Addresses5.CompanyNumber As OperatorNumber,
# 		WorkTasks.TaskName As TaskName,
# 		WorkTasks.Sequence,
# 		Warehouses.WarehouseName,
# 		CONVERT(DATE,ChangeLog.ChangeDate) As TransactionDate,
# 		CONVERT(TIME,ChangeLog.ChangeDate) As TransactionTime,
# 		WorkTransactions.Quantity
# 	FROM WorkTransactions 
# 		Left Outer Join WorkTasks 
# 		Left Outer Join WorkFlows
# 				On WorkTasks.WorkFlowID=WorkFlows.WorkFlowID
# 				On WorkTransactions.TaskID=WorkTasks.TaskID
# 		Left Outer Join Bundles 
# 		Left Outer Join ManufactureOrders 
# 				On Bundles.ManufactureID=ManufactureOrders.ManufactureID				
# 				On WorkTransactions.BundleID=Bundles.BundleID
# 		Left Outer Join StatusNames
# 				On WorkTasks.StatusID=StatusNames.StatusID
# 		Left Outer Join StatusNames StatusMO
# 				On ManufactureOrders.StatusID=StatusMO.StatusID
# 		Left Outer Join Warehouses
# 				On ManufactureOrders.WarehouseID=Warehouses.WarehouseID
# 		Left Outer Join Addresses As Addresses5
# 				On WorkTransactions.OperatorID=Addresses5.AddressID
# 		Left Outer Join WorkTasks As LastTask ON Workflows.LastTaskID=LastTask.TaskID
# 		Left Outer Join ChangeLog
# 				On WorkTransactions.ChangeLogID=ChangeLog.ChangeLogID
# 	WHERE CONVERT(DATE,ChangeLog.ChangeDate) >= dateadd(DAY, 1, eomonth(GETDATE(), -1)) AND CONVERT(DATE,ChangeLog.ChangeDate) <=  eomonth(GETDATE())
# 		And (WorkTransactions.ChangeLogID Is Not Null)
# 		And StatusMO.StatusName<>'Void' And StatusMO.StatusName<>'Forecast'
# 		And WorkTransactions.Archived=0
# 		and WorkTasks.TaskName LIKE '%Sewing Production%' AND Addresses5.ContactTitle LIKE '%6.6- Costura%'
# 	) AS WorkTransactions	
# GROUP BY WorkTransactions.ManufactureSerialNumber
# 	,WorkTransactions.Title
# 	,WorkTransactions.TaskName
# 	,WorkTransactions.OperatorName
# 	,WorkTransactions.OperatorNumber
# 	,WorkTransactions.TransactionTime
# 	,WorkTransactions.WarehouseName
# 	,WorkTransactions.TransactionDate
# 	,TransactionDate
# """
# loop = asyncio.get_event_loop()
# async def runServer(text):
#     dsn = r'Driver=SQL Server;Server=10.48.26.25;Database=SUPPLYPLANNING_test;Trusted_Connection=yes;'
#     conn = await aioodbc.connect(dsn=dsn, loop=loop)
#     cur = await conn.cursor()
#     await cur.execute(text)
#     rows = await cur.fetchall()
#     x = [ column[0] for column in cur.description]
#     dic = [dict(line) for line in [zip([ column[0] for column in cur.description], row) for row in rows]]
#     await cur.close()
#     await conn.close()
#     return dic

# data = loop.run_until_complete(db.runServer3(textSQL))
# print(data)
# var = "('Ship To ScreenPrint' in 'Ship To ScreenPrint - Left Insert Sleeve') and not ('Finished Goods' in 'Ship To ScreenPrint - Left Insert Sleeve')"
# var = "('ScreenPrinting - Right Shoulder' in 'ScreenPrinting -') and ('4.1- Serigrafiado' in '4.1- Serigrafiado') and not ('ScreenPrinting - Right Shoulder' in 'FG')"
# if eval(var):
#     print("s")
# x = 2
# eval('print(x+5)')
# if ('ScreenPrinting' in 'ScreenPrinting Process'):
# # if ('ScreenPrinting - Right Shoulder' in 'ScreenPrinting -') and ('4.1- Serigrafiado' in '4.1- Serigrafiado') and not ('ScreenPrinting - Right Shoulder' in 'FG'):
# # if ('ScreenPrinting - Right Shoulder' in 'ScreenPrinting -') and ('4.1- Serigrafiado' in '4.1- Serigrafiado') and not ('ScreenPrinting - Right Shoulder' in 'FG'):
#     print("test")
# import threading
# from PromissedDate.database import conn as db
# import asyncio
# import pandas as pd

# import time

# start = time.time()
# loop2 = asyncio.get_event_loop()
# def contar():
#     textSQL2 = """
# SELECT  
# 	--*
# 	 Warehouses.WarehouseName AS [Goods Warehouse]
#     ,RTrim(Case When ManufactureOrders.ManufactureID<=999999 Then 
#             Replicate('0', 6-Len(Cast(ManufactureOrders.ManufactureID As Nchar))) 
#         Else '' End
#         + Cast(ManufactureOrders.ManufactureID As Nchar)) As [Serial Number]
# 	,ManufactureOrders.ManufactureNumber AS MO
# 	,Orders.PONumber As [PO Number]
#     ,ManufactureOrders.CutNumber AS [Cut Number]
# 	,StatusNames.StatusName AS [Status]
# 	,DropDownValues2.DropDownValue
#     ,ManufactureOrders.QuantityOrdered
# FROM ManufactureOrders
# 	LEFT OUTER JOIN Warehouses ON ManufactureOrders.WarehouseID = Warehouses.WarehouseID
# 	LEFT OUTER JOIN Orders ON ManufactureOrders.OrderID = Orders.OrderID
# 	LEFT OUTER JOIN StatusNames ON ManufactureOrders.StatusID = StatusNames.StatusID
# 	--LEFT OUTER JOIN ReceivableLog ON Orders.OrderID = ReceivableLog.OrderID
# 	LEFT OUTER JOIN DropDownValues2 ON Orders.OrderTypeID3 = DropDownValues2.DropDownValueID
# --where Orders.PONumber = '3503021345-10'
# WHERE ManufactureOrders.StatusID NOT IN (95,20)
# 	AND DropDownValues2.DropDownValue LIKE '%SO-Packing Order%'
# 	AND ( Orders.RequiredDate  > { d '2021-06-30' } OR ManufactureOrders.TargetDate > { d '2022-01-01' })
# 	AND ManufactureOrders.Archived = 0
# """
#     for x in range(10):
#         df_mo = pd.json_normalize(loop2.run_until_complete(db.runServer3(textSQL2)))
#         # print(df_mo)


# # contar()
# # contar()
# hilo1 = threading.Thread(target=contar)
# hilo2 = threading.Thread(target=contar)
# hilo1.start()
# hilo1.join()
# hilo2.start()
# hilo2.join()

# end = time.time()
# print((end - start))

# var = 12
# print(type(var))
# print(var if type(var) == "int" else "0")

# from msgraph import api

# authority_host_uri = 'https://login.microsoftonline.com'
# tenant = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
# resource_uri = 'https://graph.microsoft.com'
# client_id = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
# client_thumbprint = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# client_certificate = ''
# api_instance = api.GraphAPI.from_certificate(authority_host_uri, tenant, resource_uri, client_id, client_certificate, client_thumbprint)


import requests

def get_token():
    url = 'https://login.microsoftonline.com/03fa6430-2a3b-4a59-b916-ffb7eb0b395c/oauth2/token'
    headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
    data = {
        'grant_type': 'password',
        'username': 'miguel.carcamo@tegraglobal.com',
        'password': 'Naruto04..',
        'client_id': '4e3ecd43-63b6-4504-a5f4-2b9639615dd0',
        'resource': 'https://analysis.windows.net/powerbi/api',
        'scope': 'openid'
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        access_token = response.json().get('access_token')
        print(access_token)
    else:
        print(response.text)

get_token()