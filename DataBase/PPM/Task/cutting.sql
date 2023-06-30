SELECT 
	WorkTransactions.ManufactureSerialNumber
	,WorkTransactions.WarehouseName
	,WorkTransactions.Title
	,WorkTransactions.TaskName
	,WorkTransactions.OperatorName
	,WorkTransactions.OperatorNumber
	,WorkTransactions.TransactionDate
	,WorkTransactions.TransactionTime
	,case when WorkTransactions.TransactionTime < '06:00:00' then DATEADD(day,-1, WorkTransactions.TransactionDate) else WorkTransactions.TransactionDate END AS TransactionDate2
	,SUM(WorkTransactions.Quantity) As Quantity
FROM
(
	SELECT  
		RTrim(Case When ManufactureOrders.ManufactureID<=999999 Then 
						Replicate('0',6-Len(Cast(ManufactureOrders.ManufactureID As Nchar))) 
					Else '' 
					End + Cast(ManufactureOrders.ManufactureID As Nchar)) As ManufactureSerialNumber,
		Addresses5.ContactTitle As Title,
		Addresses5.CompanyName As OperatorName,
		Addresses5.CompanyNumber As OperatorNumber,
		WorkTasks.TaskName As TaskName,
		WorkTasks.Sequence,
		Warehouses.WarehouseName,
		CONVERT(DATE,ChangeLog.ChangeDate) As TransactionDate,
		CONVERT(TIME,ChangeLog.ChangeDate) As TransactionTime,
		WorkTransactions.Quantity
	FROM WorkTransactions 
		Left Outer Join WorkTasks 
		Left Outer Join WorkFlows
				On WorkTasks.WorkFlowID=WorkFlows.WorkFlowID
				On WorkTransactions.TaskID=WorkTasks.TaskID
		Left Outer Join Bundles 
		Left Outer Join ManufactureOrders 
				On Bundles.ManufactureID=ManufactureOrders.ManufactureID				
				On WorkTransactions.BundleID=Bundles.BundleID
		Left Outer Join StatusNames
				On WorkTasks.StatusID=StatusNames.StatusID
		Left Outer Join StatusNames StatusMO
				On ManufactureOrders.StatusID=StatusMO.StatusID
		Left Outer Join Warehouses
				On ManufactureOrders.WarehouseID=Warehouses.WarehouseID
		Left Outer Join Addresses As Addresses5
				On WorkTransactions.OperatorID=Addresses5.AddressID
		Left Outer Join WorkTasks As LastTask ON Workflows.LastTaskID=LastTask.TaskID
		Left Outer Join ChangeLog
				On WorkTransactions.ChangeLogID=ChangeLog.ChangeLogID
	WHERE CONVERT(DATE,ChangeLog.ChangeDate) >= {d '2022-01-01'} AND CONVERT(DATE,ChangeLog.ChangeDate) <=  eomonth(GETDATE())
		And (WorkTransactions.ChangeLogID Is Not Null)
		And StatusMO.StatusName<>'Void' And StatusMO.StatusName<>'Forecast'
		And WorkTransactions.Archived=0
		and WorkTasks.TaskName LIKE '%Cutting Ready%' AND Addresses5.ContactTitle LIKE '%1.0- Cortado%'
	) AS WorkTransactions	
GROUP BY WorkTransactions.ManufactureSerialNumber
	,WorkTransactions.Title
	,WorkTransactions.TaskName
	,WorkTransactions.OperatorName
	,WorkTransactions.OperatorNumber
	,WorkTransactions.TransactionTime
	,WorkTransactions.WarehouseName
	,WorkTransactions.TransactionDate
	,TransactionDate