from database import conn as db
import pandas as pd
import asyncio
from threading import Thread
import asyncio

class MainStatusSerial:
    _serial = None
    __loop = None
    _GeneralStatus = None
    _DetailStatus = None
    _RunnningTask = None
    _Responsible = None
    _SwivelBucket = None
    _GlobalData1 = None
    _GlobalData2 = None

    def __init__(self):
        self.__loop = asyncio.get_event_loop()
        self._GlobalData1 = self.GetGeneralStatus()
        self._GlobalData2 = self.GetStatusDetail()

    def GetDataPPM(self):
        text1 = f"""
                SELECT *
                FROM (	
                SELECT  
                    RTrim(Case When ManufactureOrders.ManufactureID<=999999 Then 
                                    Replicate('0',6-Len(Cast(ManufactureOrders.ManufactureID As Nchar))) 
                                Else '' 
                                End + Cast(ManufactureOrders.ManufactureID As Nchar)) As ManufactureSerialNumber,
                    Addresses5.ContactTitle As Title,
                    WorkTasks.TaskName As TaskName,
                    Addresses5.CompanyName As OperatorName,
                    Addresses5.CompanyNumber As OperatorNumber,
                    WorkTasks.Sequence,
                    MIN(CONVERT(DATE,ChangeLog.ChangeDate)) As MIN_TransactionDate,
                    MAX(CONVERT(DATE,ChangeLog.ChangeDate)) As MAX_TransactionDate,
                    SUM(WorkTransactions.Quantity) as Quantity
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
                    Left Outer Join Addresses As Addresses5
                            On WorkTransactions.OperatorID=Addresses5.AddressID
                    Left Outer Join WorkTasks As LastTask ON Workflows.LastTaskID=LastTask.TaskID
                    Left Outer Join ChangeLog
                            On WorkTransactions.ChangeLogID=ChangeLog.ChangeLogID
                WHERE ManufactureOrders.ManufactureID = {self._serial} AND NOT ChangeLog.ChangeDate IS NULL
                GROUP BY ManufactureOrders.ManufactureID, Addresses5.ContactTitle, Addresses5.CompanyName, Addresses5.CompanyNumber, WorkTasks.TaskName, WorkTasks.Sequence, Addresses5.ContactTitle, Addresses5.CompanyName, Addresses5.CompanyNumber
                ) AS B1 
                WHERE B1.Quantity <> 0
                ORDER BY B1.Sequence
                        """
        task = self.__loop.run_until_complete(db.runServer3(text1))
        df_task = pd.json_normalize(task)
        return df_task.fillna(0)
    
    def SaveTask2(self, Where, Serial, Process):
        TextSql = f""" SELECT
                            WorkTransactions.ManufactureSerialNumber
                            ,WorkTransactions.Title
                            ,WorkTransactions.TaskName
                            ,WorkTransactions.OperatorName
                            ,WorkTransactions.OperatorNumber
                            ,WorkTransactions.TransactionDate
                            ,CASE LEN(DATEPART(iso_week, WorkTransactions.TransactionDate)) 
                                        WHEN 1 THEN 'WK-0' + CONVERT(VARCHAR, DATEPART(iso_week, WorkTransactions.TransactionDate)) + '-' + CONVERT(VARCHAR, DATEPART(YEAR, WorkTransactions.TransactionDate))
                                        WHEN 2 THEN 'WK-' + CONVERT(VARCHAR, DATEPART(iso_week, WorkTransactions.TransactionDate)) + '-' + CONVERT(VARCHAR, DATEPART(YEAR, WorkTransactions.TransactionDate))
                                    END AS Wk_YEAR
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
                                CONVERT(DATE,ChangeLog.ChangeDate) As TransactionDate,
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
                            WHERE (WorkTransactions.ChangeLogID Is Not Null)
                                And StatusMO.StatusName<>'Void' And StatusMO.StatusName<>'Forecast'
                                And WorkTransactions.Archived=0
                                {Where}
                                and ManufactureOrders.ManufactureID  = {Serial}
                            ) AS WorkTransactions	
                        GROUP BY WorkTransactions.ManufactureSerialNumber
                            ,WorkTransactions.Title
                            ,WorkTransactions.TaskName
                            ,WorkTransactions.OperatorName
                            ,WorkTransactions.OperatorNumber
                            ,WorkTransactions.TransactionDate
                            ,TransactionDate """
        task = self.__loop.run_until_complete(db.runServer3(TextSql))
        df = pd.json_normalize(task)
        TextSql = f""" DELETE FROM PromisedDate_{Process} WHERE ManufactureSerialNumber = {df.iloc[0, 0]} """
        self.__loop.run_until_complete(db.runServer2(TextSql))
        try:
            for i in range(len(df)):
                TextSql = f""" execute SP_PromisedDate_{Process}_Create {df.iloc[i, 0]}, '{df.iloc[i, 1]}','{df.iloc[i, 2]}','{df.iloc[i, 3]}','{df.iloc[i, 4]}', '{df.iloc[i, 5]}','{df.iloc[i, 6]}', {int(df.iloc[i, 7])} """
                self.__loop.run_until_complete(db.runServer2(TextSql))
        except:
            TextSql = f""" DELETE FROM PromisedDate_{Process} WHERE ManufactureSerialNumber = {df.iloc[0, 0]} """
            self.__loop.run_until_complete(db.runServer2(TextSql))

    def SaveTask(self, df):
        TextSql = f""" delete from General_WorkTransactions where ManufactureSerialNumber = {df.iloc[0, 0]} """
        self.__loop.run_until_complete(db.runServer2(TextSql))
        try:
            for i in range(len(df)):
                TextSql = f""" execute SP_General_WorkTransactions_Create {df.iloc[i, 0]}, '{df.iloc[i, 1]}','{df.iloc[i, 2]}','{df.iloc[i, 3]}','{df.iloc[i, 4]}', '{df.iloc[i, 5]}','{df.iloc[i, 6]}','{df.iloc[i, 7]}',{int(df.iloc[i, 8])} """
                self.__loop.run_until_complete(db.runServer2(TextSql))
        except:
            TextSql = f""" delete from General_WorkTransactions where ManufactureSerialNumber = {df.iloc[0, 0]} """
            self.__loop.run_until_complete(db.runServer2(TextSql))

    def GetGeneralStatus(self):
        text2 = """SELECT General_StatusDetailSub.IDStatusDetailSub, General_Status.StatusName, General_StatusDetail.StatusDetailName, General_StatusDetailSub.StatusDetailNameSub, General_StatusDetailSub.valueif
                        ,General_StatusDetail.Responsible, General_StatusDetail.SwivelBucket
                    FROM General_Status
                    LEFT JOIN General_StatusDetail ON General_Status.IDStatus = General_StatusDetail.IDStatus
                    LEFT JOIN General_StatusDetailSub ON General_StatusDetail.IDStatusDetail = General_StatusDetailSub.IDStatusDetail
                    WHERE General_Status.Active = 1 AND General_StatusDetailSub.Filter = 'WIP'
                    ORDER BY General_Status.Sequence, General_StatusDetailSub.Sequence
                """
        data = self.__loop.run_until_complete(db.runServer(text2))
        df_data = pd.json_normalize(data)
        return(df_data)

    def GetStatusDetail(self):
        text3 = """
        SELECT        General_StatusDetailWip.Item, General_StatusDetailWip.IDStatusDetailSub, General_StatusDetailWip.NamePPMWIP, General_StatusDetailWip.LookField, General_StatusDetailWip.IDOperatorType, 
                         General_StatusOperator.IDOperatorType AS Expr1, General_StatusOperator.OperatorType
        FROM            General_StatusDetailWip LEFT OUTER JOIN
                                General_StatusOperator ON General_StatusDetailWip.IDOperatorType = General_StatusOperator.IDOperatorType
        """
        data = self.__loop.run_until_complete(db.runServer(text3))
        df_data = pd.json_normalize(data)
        return(df_data)
    
    def GetStatus(self):
        try:
            self._GeneralStatus = ""
            self._DetailStatus = ""
            self._RunnningTask = ""
            df_task = self.GetDataPPM()
            df_data = self._GlobalData1
            df_data2 = self._GlobalData2
            # print(df_data)
            if(len(df_task) > 0):
                thread = Thread(target=self.SaveTask(df_task))
                thread.start()
                df_data = df_data.assign(Cant=0)
                df_data = df_data.assign(Date="")
                for i in range(len(df_data)):
                    if int(df_data.iloc[i, 4]) > 0:
                        Where = []
                        for j in range(len(df_data2)):
                            if int(df_data.iloc[i, 0]) == int(df_data2.iloc[j,1]):
                                Where.append([df_data2.iloc[j, 3], df_data2.iloc[j, 2], df_data2.iloc[j, 6]])
                        for k in range(len(df_task)):
                            cadena = ''
                            cant = 0
                            for l in range(len(Where)):
                                col = 2
                                if(Where[l][0] == 'Title'):
                                    col = 1
                                if cadena == '':
                                    if(Where[l][2] == 'NOT LIKE'):
                                        cadena += " not ('" + str(Where[l][1]) + "' in '" + str(df_task.iloc[k, col]) + "')"
                                    else:
                                        cadena += " ('" + str(Where[l][1]) + "' in '" + str(df_task.iloc[k, col]) + "')"
                                else:
                                    if(Where[l][2] == 'NOT LIKE'):
                                        cadena += " and not ('" + str(Where[l][1]) + "' in '" + str(df_task.iloc[k, col]) + "')"
                                    else:
                                        cadena += " and ('" + str(Where[l][1]) + "' in '" + str(df_task.iloc[k, col]) + "')"
                            cant = int(df_task.iloc[k, 8])
                            date = str(df_task.iloc[k, 7])
                            if len(str(cadena)) > 0:
                                if eval(str(cadena)):
                                    # print(str(cadena))
                                    df_data.iloc[i, 7] = int(df_data.iloc[i, 7]) + cant
                                    df_data.iloc[i, 8] = date
                df = df_data[df_data.Cant > 0]
                # print(df)
                if len(df) > 0:
                    CutCant = int(df.iloc[0, 7])
                    # ESTE CODIGO LO DEJO POR SI DECIDEN REGRESAR A COMO ESTABA ANTES
                    lastStatus = str(df.loc[df.index[-1], "StatusName"])
                    lastResponsible = str(df.loc[df.index[-1], "Responsible"])
                    lastSwivelBucket = str(df.loc[df.index[-1], "SwivelBucket"])
                    # ESTE ES EL NUEVO CODIGO
                    # for h in range(len(df))[::-1]:
                    #     if df.iloc[h, 7] > CutCant:
                    #         lastStatus = df.iloc[h, 1]
                    #         lastResponsible = df.iloc[h, 5]
                    #         lastSwivelBucket = df.iloc[h, 6]
                    df = df[df.StatusName == lastStatus]
                    df1 = df.StatusDetailName
                    df2 = df.Cant
                    df3 = str(df.loc[df.index[-1], "StatusDetailNameSub"])
                    lista = list(df1.drop_duplicates())
                    lista2 = df2.tolist()
                    detailStatus = ''
                    if len(lista) == 1:
                        detailStatus ='[' +  lista[0] + ']' + '(' +  df3 + ')'
                    else:
                        ss = 0
                        for m in lista:
                            varpass = ''
                            if ('IN' in str(m)) or ('ON' in str(m)) or ('OUT' in str(m)):
                                if(int(lista2[ss]) >= int(CutCant)):
                                    detailStatus = str(m)
                                else:
                                    varpass = str(m) + '[' + str(lista2[ss]) +']'
                                detailStatus += "(" + varpass + ")"
                            else:
                                for n in range(len(df)):
                                    if str(m) in str(df.iloc[n, 2]):
                                        varpass = df.iloc[n, 3]
                                detailStatus += "(" + varpass + ")"
                            ss += 1
                    # print(lastStatus + ' -> ' + detailStatus)
                    self._GeneralStatus = lastStatus
                    if('Sew OUT' in detailStatus):
                        thread2 = Thread(target=self.SaveTask2(" and (WorkTasks.TaskName LIKE '%Shipping Area%' or WorkTasks.TaskName LIKE '%In Packing Area%' or WorkTasks.TaskName LIKE '%TW Shipping%') ",self._serial, 'Sewing_OUT'))
                        thread2.start()
                    if('Sew ON' in detailStatus):
                        thread2 = Thread(target=self.SaveTask2(" and WorkTasks.TaskName LIKE '%Sewing Production%' AND Addresses5.ContactTitle LIKE '%6.6- Costura%' ",self._serial, 'Sewing_ON'))
                        thread2.start()
                    self._DetailStatus = detailStatus
                    self._Responsible = lastResponsible
                    self._SwivelBucket = lastSwivelBucket
                    dx = df_task.sort_values(['MAX_TransactionDate','Sequence'],ascending=False)
                    self._RunnningTask = '('+str(dx.iloc[0,1]) + ')(' + str(dx.iloc[0,2]) + ')'
                else:
                    self._GeneralStatus = ""
                    self._DetailStatus = ""
                    self._RunnningTask = ""
                    self._Responsible = ""
                    self._SwivelBucket = ""
                    lastStatus = "x"
            else:
                self._GeneralStatus = ""
                self._DetailStatus = ""
                self._RunnningTask = ""
                self._Responsible = ""
                self._SwivelBucket = ""
        except Exception as err:
            print(f"Serial:{self._serial} Unexpected {err=}, {type(err)=}")
            self._GeneralStatus = ""
            self._DetailStatus = ""
            self._RunnningTask = ""
            self._Responsible = ""
            self._SwivelBucket = ""
            lastStatus = "x"
        return lastStatus