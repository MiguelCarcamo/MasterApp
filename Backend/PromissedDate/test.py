
# from StatusSerial import MainStatusSerial
# from database import conn as db
# import asyncio
# import pandas as pd
# import time

# # start = time.time()
# textSQL1 = """
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
#     ,ManufactureOrders.QuantityOrdered
# FROM ManufactureOrders
# 	LEFT OUTER JOIN Warehouses ON ManufactureOrders.WarehouseID = Warehouses.WarehouseID
# 	LEFT OUTER JOIN Orders ON ManufactureOrders.OrderID = Orders.OrderID
# 	LEFT OUTER JOIN StatusNames ON ManufactureOrders.StatusID = StatusNames.StatusID
# 	--LEFT OUTER JOIN ReceivableLog ON Orders.OrderID = ReceivableLog.OrderID
# 	LEFT OUTER JOIN DropDownValues2 ON Orders.OrderTypeID3 = DropDownValues2.DropDownValueID

# WHERE ManufactureOrders.StatusID NOT IN (95,20)
# 	AND ManufactureOrders.MfgOrderTypeID IN (SELECT EnumValueID FROM EnumValues WHERE EnumName='MfgOrderType' AND EnumValue In('New','Cut'))
# 	AND ( Orders.RequiredDate  > { d '2021-06-30' } OR ManufactureOrders.TargetDate > { d '2022-01-01' })
# 	AND ManufactureOrders.Archived = 0
# 	AND (DropDownValues2.DropDownValue NOT LIKE '%SO-Packing Order%' or DropDownValues2.DropDownValue is null)
# """
# textSQL2 = "SELECT top 50 PurchaseOrder as [PO Number] FROM PromisedDate"
# loop2 = asyncio.get_event_loop()
# z = MainStatusSerial()

# df_pd = pd.json_normalize(loop2.run_until_complete(db.runServer(textSQL2)))
# df_mo = pd.json_normalize(loop2.run_until_complete(db.runServer3(textSQL1)))

# print(df_pd)
# print(df_mo)
# merge1 = df_mo.merge(df_pd, how='inner', on='PO Number')
# df_pd.columns = ['MO']
# merge2 = df_mo.merge(df_pd, how='inner', on='MO')
# merge2['PO Number'] = merge2['PO Number'] == None
# fd = merge1.append(merge2).reset_index()
# SerialError = []
# for i in range(len(fd)):
#         z._serial = int(fd.iloc[i, 2])
#         z.GetStatus()
#         print(z._GeneralStatus +  z._DetailStatus + z._RunnningTask)
# end = time.time()
# print((end - start) / 60)


# from TypePromissedDate import TypePD

# x = TypePD('0127725327','1174535','','','','2022-03-11 00:00:00','','')
# print(str(x._Po))
# print(str(x._Mo))
# print(str(x._Serial))
# print(str(x._promised_date))
# print(str(x._promised_date2))
# print(str(x._Assigned))

from StatusSerial import MainStatusSerial
from database import conn as db
import asyncio
import pandas as pd
import time

# # start = time.time()
# textSQL1 = """
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
#     ,ManufactureOrders.QuantityOrdered
# FROM ManufactureOrders
# 	LEFT OUTER JOIN Warehouses ON ManufactureOrders.WarehouseID = Warehouses.WarehouseID
# 	LEFT OUTER JOIN Orders ON ManufactureOrders.OrderID = Orders.OrderID
# 	LEFT OUTER JOIN StatusNames ON ManufactureOrders.StatusID = StatusNames.StatusID
# 	--LEFT OUTER JOIN ReceivableLog ON Orders.OrderID = ReceivableLog.OrderID
# 	LEFT OUTER JOIN DropDownValues2 ON Orders.OrderTypeID3 = DropDownValues2.DropDownValueID

# WHERE ManufactureOrders.StatusID NOT IN (95,20)
# 	AND ManufactureOrders.MfgOrderTypeID IN (SELECT EnumValueID FROM EnumValues WHERE EnumName='MfgOrderType' AND EnumValue In('New','Cut'))
# 	AND ( Orders.RequiredDate  > { d '2021-06-30' } OR ManufactureOrders.TargetDate > { d '2022-01-01' })
# 	AND ManufactureOrders.Archived = 0
# 	AND (DropDownValues2.DropDownValue NOT LIKE '%SO-Packing Order%' or DropDownValues2.DropDownValue is null)
# """
# textSQL2 = "SELECT PurchaseOrder as [PO Number] FROM PromisedDate"
loop2 = asyncio.get_event_loop()
z = MainStatusSerial()
# df_pd = pd.json_normalize(loop2.run_until_complete(db.runServer(textSQL2)))
# df_mo = pd.json_normalize(loop2.run_until_complete(db.runServer3(textSQL1)))
# merge1 = df_mo.merge(df_pd, how='inner', on='PO Number')
# df_pd.columns = ['MO']
# merge2 = df_mo.merge(df_pd, how='inner', on='MO')
# merge2['PO Number'] = merge2['PO Number'] == None
# fd = merge1.append(merge2).reset_index()
# for i in range(100):
# print(fd.iloc[i, 2] +' - ' + fd.iloc[i, 6])
# CUT
# lista = [2340444]
# lista = [2352518]
# Serial:2292982 
lista = [2292982]
for x in lista:
    z._serial = int(x)
    # z._serial = int(2201674)
    # 2201674
    z.GetStatus()
    print( z._GeneralStatus +' - ' + z._DetailStatus + ' - ' + z._RunnningTask + ' - ' + z._Responsible + ' - ' + z._SwivelBucket)

# import webbrowser
# import msal
# from msal import PublicClientApplication

# Tenant_ID = '03fa6430-2a3b-4a59-b916-ffb7eb0b395c'
# Secret_key = 'VNE8Q~nbDUpJ6-O~cPmP2k_dlj-G5dOR9FlsWbYv'

# Authority_url = 'https://login.microsoftonline.com/consumers/'
# Base_url = 'https://graph.microsoft.com/v1.0/'
# End_Point = Base_url + 'me'
# SCOPES = ["https://graph.microsoft.com/.default"]

# x = msal.ConfidentialClientApplication(
#     client_id=Tenant_ID,
#     client_credential=Secret_key,
#     authority=Authority_url
# )
# z = x.get_authorization_request_url(SCOPES)
# print(z)
# import shutil

# from numpy import size
# from datetime import date

# today = date.today()
# print(today)
# var = "S:/El Baron/Production/Schedules - Nike Modified/Master Actualizados/Master Actual/SewingOrdersDataARENA - Planner1.xlsx"
# array = var.split("/")
# namevar = array[size(array)-1]
# print(namevar)
# shutil.copyfile(var, namevar)


# Python program to explain os.mkdir() method 
    
# importing os module 
# import os
# from datetime import date
# # Directory
# # directory = "GeeksForGeeks"
# today = date.today()
# # Parent Directory path
# parent_dir = "D:\Apps\MasterApp\Backend\File"
  
# # Path
# path = os.path.join(parent_dir, str(today))
# print(path)
# # Create the directory
# # 'GeeksForGeeks' in
# # '/home / User / Documents'
# os.mkdir(path)
# print("Directory '%s' created" %today)
  
  
# Directory
# directory = "ihritik"
  
# # Parent Directory path
# parent_dir = "/home/User/Documents"
  
# # mode
# mode = 0o666
  
# # Path
# path = os.path.join(parent_dir, directory)
  
# # Create the directory
# # 'GeeksForGeeks' in
# # '/home / User / Documents'
# # with mode 0o666
# os.mkdir(path, mode)
# print("Directory '%s' created" %directory)
# from datetime import date
# import os

# today = date.today()
# # Parent Directory path
# parent_dir = "D:\Apps\MasterApp\Backend\File\Cycle\Forecast"
# v_path = os.path.join(parent_dir, str(2024))
# contenido = os.listdir(parent_dir)
# cant = 1
# for fichero in contenido:
#     if not str(2024) in fichero:
#         os.mkdir(v_path)