from database import conn as db
import asyncio
import pandas as pd
import json
import requests

textSQL1 = """
SELECT  
    --*
    Warehouses.WarehouseName AS [Goods Warehouse]
	,case when ManufactureOrders.CutNumber IS NULL then 'MO' else 'Serial' end AS [UpdateType]
    ,RTrim(Case When ManufactureOrders.ManufactureID<=999999 Then 
            Replicate('0', 6-Len(Cast(ManufactureOrders.ManufactureID As Nchar))) 
        Else '' End
        + Cast(ManufactureOrders.ManufactureID As Nchar)) As [serialNumber]
    ,ManufactureOrders.ManufactureNumber AS moNumber
    ,Orders.PONumber As [PO Number]
    ,ISNULL(ManufactureOrders.CutNumber, '001') AS [Cut Number]
    ,StatusNames.StatusName AS [Status]
	,CAST(ManufactureOrders.WithdrawDateB2 AS DATE) AS [Plan_Cut_Date] 
	,(SELECT AddressesCUT.CompanyName FROM ManufactureOrders LEFT OUTER JOIN Addresses As AddressesCUT ON ManufactureOrders.CutLocationID = AddressesCUT.AddressID WHERE BlanketOrderID = ManufactureOrders.ManufactureID) as [Cut Location Name]
	,CAST(ManufactureOrders.UserPlanningDate AS DATE) as [Plan_Sew_Date]
	,(SELECT AddressesSEW.CompanyName FROM ManufactureOrders LEFT OUTER JOIN Addresses As AddressesSEW ON ManufactureOrders.SewLocationID = AddressesSEW.AddressID WHERE BlanketOrderID = ManufactureOrders.ManufactureID) as [Sew Location Name]
	,CAST(ManufactureOrders.UserDate2 AS DATE) As [Plan_ScreenPrint_Date]
	,(SELECT AddressesSP.CompanyName FROM ManufactureOrders LEFT OUTER JOIN Addresses As AddressesSP ON ManufactureOrders.ScreenPrintLocationID = AddressesSP.AddressID WHERE BlanketOrderID = ManufactureOrders.ManufactureID) AS [Screen Print Location]
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
	AND (StatusNames.StatusName <> 'Complete' and StatusNames.StatusName <> 'Hold')
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
UNION
SELECT  
    --*
    Warehouses.WarehouseName AS [Goods Warehouse]
	,case when ManufactureOrders.CutNumber IS NULL then 'MO' else 'Serial' end AS [UpdateType]
    ,RTrim(Case When ManufactureOrders.ManufactureID<=999999 Then 
            Replicate('0', 6-Len(Cast(ManufactureOrders.ManufactureID As Nchar))) 
        Else '' End
        + Cast(ManufactureOrders.ManufactureID As Nchar)) As [serialNumber]
    ,ManufactureOrders.ManufactureNumber AS moNumber
    ,Orders.PONumber As [PO Number]
    ,ISNULL(ManufactureOrders.CutNumber, '001') AS [Cut Number]
    ,StatusNames.StatusName AS [Status]
	,CAST(ManufactureOrders.WithdrawDateB2 AS DATE) AS [Plan_Cut_Date] 
	,(SELECT AddressesCUT.CompanyName FROM ManufactureOrders LEFT OUTER JOIN Addresses As AddressesCUT ON ManufactureOrders.CutLocationID = AddressesCUT.AddressID WHERE BlanketOrderID = ManufactureOrders.ManufactureID) as [Cut Location Name]
	,CAST(ManufactureOrders.UserPlanningDate AS DATE) as [Plan_Sew_Date]
	,(SELECT AddressesSEW.CompanyName FROM ManufactureOrders LEFT OUTER JOIN Addresses As AddressesSEW ON ManufactureOrders.SewLocationID = AddressesSEW.AddressID WHERE BlanketOrderID = ManufactureOrders.ManufactureID) as [Sew Location Name]
	,CAST(ManufactureOrders.UserDate2 AS DATE) As [Plan_ScreenPrint_Date]
	,(SELECT AddressesSP.CompanyName FROM ManufactureOrders LEFT OUTER JOIN Addresses As AddressesSP ON ManufactureOrders.ScreenPrintLocationID = AddressesSP.AddressID WHERE BlanketOrderID = ManufactureOrders.ManufactureID) AS [Screen Print Location]
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
	AND (StatusNames.StatusName <> 'Complete' and StatusNames.StatusName <> 'Hold')
    AND ManufactureOrders.MfgOrderTypeID IN (SELECT EnumValueID FROM EnumValues WHERE EnumName='MfgOrderType' AND EnumValue In('New','Standard'))
    AND ( Orders.RequiredDate  > { d '2022-01-01' } OR ManufactureOrders.TargetDate > { d '2022-01-01' })
    AND ManufactureOrders.Archived = 0
    AND     Warehouses.WarehouseName = 'FGW-Arena-Modified'
"""
textSQL2 = """
SELECT  MO as moNumber, SerialNumber, CuttingNum, 
		PromisedDateSewing as planSewDate, case SewingLocation when 'SAC' then 3276 when '27ST' then 369 when 'ARENA' then 508029 end as sewLocationId, 
		PromisedDateCutting as planCutDate, case CuttingLocation  when 'SAC' then 3276 when '27ST' then 369 when 'ARENA' then 508029 end as cutLocationId, 
		PromisedDateScreePrintingCP as planScreenPrintDate, case SPLocation when 'SAC' then 3276 when '27ST' then 369 when 'ARENA' then 508029 end as screenPrintLocationId
FROM [SUPPLYPLANNING_test].[dbo].[PromisedDate_HN]
--where MO = '1366093'
"""

loop2 = asyncio.get_event_loop()
dataPPM = pd.json_normalize(loop2.run_until_complete(db.runServer3(textSQL1)))
dataSupply = pd.json_normalize(loop2.run_until_complete(db.runServer(textSQL2)))

# print(dataPPM)
# merge1 = dataPPM.merge(dataSupply, how='inner', left_on=['moNumber', 'Cut Number'], right_on=['moNumber','CuttingNum'])
merge1 = dataSupply.merge(dataPPM, how='inner', left_on=['moNumber', 'CuttingNum'], right_on=['moNumber','Cut Number'])

data = merge1.drop(columns=['Goods Warehouse','PO Number','Cut Number', 'Cut Location Name', 'Sew Location Name', 'Screen Print Location', 'QuantityOrdered', 'SerialNumber', 'CuttingNum'])
data = data.assign(Cant=0)
for x in range(len(data)):
    if(data.UpdateType[x] == 'Serial'):
        data.at[x, 'moNumber'] = ""
    else:
        data.at[x, 'serialNumber'] = 0
    if ((data.planSewDate[x] == data.Plan_Sew_Date[x]) & (data.planCutDate[x] == data.Plan_Cut_Date[x]) & (data.planScreenPrintDate[x] == data.Plan_ScreenPrint_Date[x])):
        data.at[x, 'Cant'] = 1
data.to_excel("FileTestMiguel1.xlsx", sheet_name='Sheet1', index=False)
data = data[data.Cant == 0]

data = data.drop(columns=['Plan_Cut_Date', 'Plan_Sew_Date', 'Plan_ScreenPrint_Date', 'UpdateType','Cant'])
data = data.assign(cutUserId=1881)
data = data.assign(sewUserId=1881)
data = data.assign(screenPrintUserId=1881)
data = data.assign(notes="")
data['sewLocationId'] = data['sewLocationId'].fillna(0)
data['cutLocationId'] = data['cutLocationId'].fillna(0)
data['screenPrintLocationId'] = data['screenPrintLocationId'].fillna(0)
data = data.astype({"screenPrintLocationId":"int","cutLocationId":"int","sewLocationId":"int"})
data.to_excel("File.xlsx", sheet_name='Sheet1', index=False)
result = data.to_json(orient="records")
parsed = json.loads(result)

print("Enviado Datos")

with open('Subida.json', 'w') as json_file:
    json.dump(parsed, json_file)

api_url = "http://arnws001:9183/api/Po/updateProductionScheduleDatesWithList"
headers =  {"Content-Type":"application/json"}
response = requests.put(api_url, data=json.dumps(parsed, sort_keys=False, indent=4, separators=(',', ': ')), headers=headers)
x = response.json()

with open('Descarga.json', 'w') as json_file:
    json.dump(x, json_file)