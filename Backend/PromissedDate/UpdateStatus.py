from StatusSerial import MainStatusSerial
from database import conn as db
import asyncio
import pandas as pd
import time
import threading


start = time.time()
textSQL1 = """
SELECT * FROM 
(
SELECT  
	 Warehouses.WarehouseName AS [Goods Warehouse]
    ,RTrim(Case When ManufactureOrders.ManufactureID<=999999 Then 
            Replicate('0', 6-Len(Cast(ManufactureOrders.ManufactureID As Nchar))) 
        Else '' End
        + Cast(ManufactureOrders.ManufactureID As Nchar)) As [Serial Number]
	,ManufactureOrders.ManufactureNumber AS MO
	,Orders.PONumber As [PO Number]
    ,ManufactureOrders.CutNumber AS [Cut Number]
	,StatusNames.StatusName AS [Status]
	,CONVERT(DATE, Orders.RequiredDate) AS GAC
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
) AS B1
LEFT OUTER JOIN
(
SELECT Orders.PONumber, MAX(Shipments.ShipDate) as ShipDate, SUM(Shipments.ShipCount) as ShipCount
FROM Shipments
LEFT OUTER JOIN Orders ON Shipments.OrderID = Orders.OrderID
WHERE Shipments.ShipDate > '2021-06-01 00:00:00'
AND Shipments.ShipCount > 0
GROUP BY Orders.PONumber
) AS B2 ON B1.[PO Number] = B2.PONumber
UNION
SELECT * FROM 
(
SELECT  
	 Warehouses.WarehouseName AS [Goods Warehouse]
    ,RTrim(Case When ManufactureOrders.ManufactureID<=999999 Then 
            Replicate('0', 6-Len(Cast(ManufactureOrders.ManufactureID As Nchar))) 
        Else '' End
        + Cast(ManufactureOrders.ManufactureID As Nchar)) As [Serial Number]
	,ManufactureOrders.ManufactureNumber AS MO
	,Orders.PONumber As [PO Number]
    ,ManufactureOrders.CutNumber AS [Cut Number]
	,StatusNames.StatusName AS [Status]
	,CONVERT(DATE, Orders.RequiredDate) AS GAC
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

) AS B1
LEFT OUTER JOIN
(
SELECT Orders.PONumber, MAX(Shipments.ShipDate) as ShipDate, SUM(Shipments.ShipCount) as ShipCount
FROM Shipments
LEFT OUTER JOIN Orders ON Shipments.OrderID = Orders.OrderID
WHERE Shipments.ShipDate > '2021-06-01 00:00:00'
AND Shipments.ShipCount > 0
GROUP BY Orders.PONumber
) AS B2 ON B1.[PO Number] = B2.PONumber
"""

loop2 = asyncio.get_event_loop()
z = MainStatusSerial()

data = pd.json_normalize(loop2.run_until_complete(db.runServer3(textSQL1)))


def Update1(fd):
    SerialError = []
    for i in range(len(fd)):
        try:
            z._serial = int(fd.iloc[i, 1])
            if(str(fd.iloc[i, 5]) == 'Stage'):
                textSQL3 = f"execute [SP_PromisedDate_MOStatus_Action] {int(fd.iloc[i, 1])}, '{fd.iloc[i,2]}', '{str(fd.iloc[i, 4]) if str(fd.iloc[i, 4]) != 'None' else '001'}', 'Ready to Cut', 'Ready to Cut', 'Ready to Cut','WAREHOUSE','PRD' "
            elif(str(fd.iloc[i, 5]) == 'Released'):
                textSQL3 = f"execute [SP_PromisedDate_MOStatus_Action] {int(fd.iloc[i, 1])}, '{fd.iloc[i,2]}', '{str(fd.iloc[i, 4]) if str(fd.iloc[i, 4]) != 'None' else '001'}', 'Not Cut', 'Not Cut', 'Not Cut','WAREHOUSE','PRD' "
            else:
                p = z.GetStatus()
                if (p == 'x'):
                    p = z.GetStatus()
                if (p == ''):
                    textSQL3 = f"execute [SP_PromisedDate_MOStatus_Action] {int(fd.iloc[i, 1])}, '{fd.iloc[i,2]}', '{str(fd.iloc[i, 4]) if str(fd.iloc[i, 4]) != 'None' else '001'}', 'Not Cut', 'Not Cut', 'Not Cut','WAREHOUSE','PRD' "
                elif (p == 'x'):
                    textSQL3 = "Select 1"
                else:
                    textSQL3 = f"execute [SP_PromisedDate_MOStatus_Action] {int(fd.iloc[i, 1])}, '{fd.iloc[i,2]}', '{str(fd.iloc[i, 4]) if str(fd.iloc[i, 4]) != 'None' else '001'}', '{z._GeneralStatus}', '{z._DetailStatus}', '{z._RunnningTask}', '{z._Responsible}', '{z._SwivelBucket}' "
            # print(textSQL3)
            loop2.run_until_complete(db.runServer2(textSQL3))
        except:
            SerialError.append(int(fd.iloc[i, 2]))
        print(str(i) + '/' + str(len(fd)))
    end = time.time()
    print((end - start) / 60)
    print(SerialError)

def Update2(fd):
    # print(fd)
    SerialError = []
    for i in range(len(fd)):
        try:
            textSQL3 = f"execute [SP_PromisedDate_MOStatus_Action] {int(fd.iloc[i, 1])}, '{fd.iloc[i,2]}', '{str(fd.iloc[i, 4]) if str(fd.iloc[i, 4]) != 'None' else '001'}', 'In Packing', 'In Packing', 'In Packing','PACKING','SHIPPING' "
            loop2.run_until_complete(db.runServer2(textSQL3))
        except:
            SerialError.append(int(fd.iloc[i, 2]))
        print(str(i) + '/' + str(len(fd)))
    end = time.time()
    print((end - start) / 60)
    print(SerialError)

def Update3(fd):
    # print(fd)
    SerialError = []
    for i in range(len(fd)):
        try:
            textSQL3 = f"execute [SP_PromisedDate_MOStatus_Action] {int(fd.iloc[i, 1])}, '{fd.iloc[i,2]}', '{str(fd.iloc[i, 4]) if str(fd.iloc[i, 4]) != 'None' else '001'}', 'Shipped', 'Shipped', 'Shipped','SHIPPED','SHIPPED' "
            loop2.run_until_complete(db.runServer2(textSQL3))
        except:
            SerialError.append(int(fd.iloc[i, 2]))
        print(str(i) + '/' + str(len(fd)))
    end = time.time()
    print((end - start) / 60)
    print(SerialError)

def Update4(fd):
    # print(fd)
    SerialError = []
    for i in range(len(fd)):
        try:
            textSQL3 = f"execute [SP_PromisedDate_MOStatus_Action] {int(fd.iloc[i, 1])}, '{fd.iloc[i,2]}', '{str(fd.iloc[i, 4]) if str(fd.iloc[i, 4]) != 'None' else '001'}', 'Shipped(issues)', 'Shipped(issues)', 'Shipped(issues)','SHIPPED','SHIPPED' "
            loop2.run_until_complete(db.runServer2(textSQL3))
        except:
            SerialError.append(int(fd.iloc[i, 2]))
        print(str(i) + '/' + str(len(fd)))
    end = time.time()
    print((end - start) / 60)
    print(SerialError)

writer = pd.ExcelWriter('StatusExcel.xlsx')
data[(data['ShipDate'].isnull()) & (data['Status'] != 'Complete')].to_excel(writer, sheet_name='Sheet1', index=False)
data[(data['ShipDate'].isnull()) & (data['Status'] == 'Complete')].to_excel(writer, sheet_name='Sheet2', index=False)
data[(~data['ShipDate'].isnull()) & (data['Status'] == 'Complete')].to_excel(writer, sheet_name='Sheet3', index=False)
data[(~data['ShipDate'].isnull()) & (data['Status'] != 'Complete')].to_excel(writer, sheet_name='Sheet4', index=False)
writer.save()

Update1(data[(data['ShipDate'].isnull()) & (data['Status'] != 'Complete')])
Update2(data[(data['ShipDate'].isnull()) & (data['Status'] == 'Complete')])
Update3(data[(~data['ShipDate'].isnull()) & (data['Status'] == 'Complete')])
Update4(data[(~data['ShipDate'].isnull()) & (data['Status'] != 'Complete')])
