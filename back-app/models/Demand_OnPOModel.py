from database.db import conn
import asyncio

class Demand_OnPOModel():
    _loop2 = asyncio.get_event_loop()
    @classmethod
    def get_Demand_OnPO(self):
        try:
            textSQL = f"""
            SELECT [ID_Demand_OnPOHeader]
                ,[IDPlant]
                ,[Id_Demand_Cycle]
                ,[LastDateBuy]
                ,[CreateDate]
                ,[Status]
                ,[Id_User]
                ,[Comments]
            FROM [dbo].[Demand_OnPOHeader]
            """
            df = self._loop2.run_until_complete(conn.runServer(textSQL))
            if(len(df) > 0):
                return(df)
            else:
                return([])
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_Demand_OnPO(self, id, IDPlant, Id_Demand_Cycle, LastDateBuy, Status, Id_User, Comments):
        try:
            textSQL = f"execute SP_Demand_OnPOHeader_Action {id}, {IDPlant}, {Id_Demand_Cycle}, '{LastDateBuy}', {Status}, {Id_User}, '{Comments}' "
            df = 1
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_Demand_OnPODetails(self, id):
        try:
            textSQL = f"""
            SELECT [Id_Demand_OnPODetail]
                ,[ID_Demand_OnPOHeader]
                ,[Country]
                ,[StyleNumber]
                ,[StyleSeason]
                ,[StyleGender]
                ,[StyleColorWay]
                ,[StyleColorName]
                ,[PlayerType]
                ,[ProductDescription]
                ,[IDPlant]
                ,[ProductType]
                ,[CustomerCategory]
                ,[BuyDateReal]
                ,[BuyStatus]
                ,[SerialNumber]
                ,[PurchaseOrder]
                ,[PurchaseOrderOld]
                ,[CurrentStatus]
                ,[CustomerPromisedDate]
                ,[PromisedDateSewing]
                ,[MaxPRD]
                ,[CustomerOrderType]
                ,[CustomerLeadTime]
                ,[QuantityRequested]
                ,[QuantitySewing]
            FROM [dbo].[Demand_OnPODetail] WHERE Id_Demand_OnPODetail = {id}
            """
            df = self._loop2.run_until_complete(conn.runServer(textSQL))
            if(len(df) > 0):
                return(df)
            else:
                return([])
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_Demand_OnPODetails(self, ID_Demand_OnPOHeader, Country, StyleNumber, StyleSeason, StyleGender, StyleColorWay, StyleColorName, PlayerType, ProductDescription, IDPlant, ProductType, CustomerCategory, BuyDateReal, BuyStatus, SerialNumber, PurchaseOrder, PurchaseOrderOld, CurrentStatus, CustomerPromisedDate, PromisedDateSewing, MaxPRD, CustomerOrderType, CustomerLeadTime, QuantityRequested, QuantitySewing ):
        try:
            textSQL = f""" 
            INSERT INTO [dbo].[Demand_OnPODetail]
                ([Id_Demand_OnPODetail]
                ,[ID_Demand_OnPOHeader]
                ,[Country]
                ,[StyleNumber]
                ,[StyleSeason]
                ,[StyleGender]
                ,[StyleColorWay]
                ,[StyleColorName]
                ,[PlayerType]
                ,[ProductDescription]
                ,[IDPlant]
                ,[ProductType]
                ,[CustomerCategory]
                ,[BuyDateReal]
                ,[BuyStatus]
                ,[SerialNumber]
                ,[PurchaseOrder]
                ,[PurchaseOrderOld]
                ,[CurrentStatus]
                ,[CustomerPromisedDate]
                ,[PromisedDateSewing]
                ,[MaxPRD]
                ,[CustomerOrderType]
                ,[CustomerLeadTime]
                ,[QuantityRequested]
                ,[QuantitySewing])
            VALUES
                ((select isnull(max([Id_Demand_OnPODetail]), 0) + 1 from [Demand_OnPODetail])
                ,{ID_Demand_OnPOHeader}
                ,'{Country}'
                ,'{StyleNumber}'
                ,'{StyleSeason}'
                ,'{StyleGender}'
                ,'{StyleColorWay}'
                ,'{StyleColorName}'
                ,'{PlayerType}'
                ,'{ProductDescription}'
                ,{IDPlant}
                ,'{ProductType}'
                ,'{CustomerCategory}'
                ,'{BuyDateReal}'
                ,{BuyStatus}
                ,{SerialNumber}
                ,'{PurchaseOrder}'
                ,'{PurchaseOrderOld}'
                ,'{CurrentStatus}'
                ,'{CustomerPromisedDate}'
                ,'{PromisedDateSewing}'
                ,'{MaxPRD}'
                ,'{CustomerOrderType}'
                ,{CustomerLeadTime}
                ,{QuantityRequested}
                ,{QuantitySewing}
            """
            df = 1
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)