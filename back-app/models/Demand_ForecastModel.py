from database.db import conn
import asyncio

class Demand_ForecastModel():
    _loop2 = asyncio.get_event_loop()
    @classmethod
    def get_Demand_Forecast(self):
        try:
            textSQL = f"""
            SELECT [Id_Demand_ForecastHeader]
                ,[Id_Style_Customer]
                ,[Id_Demand_Cycle]
                ,[CustomerForecastDate]
                ,[CreateDate]
                ,[Status]
                ,[Id_User]
                ,[Comments]
            FROM [dbo].[Demand_ForecastHeader]
            """
            df = self._loop2.run_until_complete(conn.runServer(textSQL))
            if(len(df) > 0):
                return(df)
            else:
                return([])
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_Demand_Forecast(self, id, Id_Style_Customer, Id_Demand_Cycle, CustomerForecastDate, Status, Id_User, Comments):
        try:
            textSQL = f"execute SP_Demand_ForecastHeader_Action {id}, {Id_Style_Customer}, {Id_Demand_Cycle}, '{CustomerForecastDate}', {Status}, {Id_User}, '{Comments}' "
            df = 1
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_Demand_ForecastDetails(self, id):
        try:
            textSQL = f"""
            SELECT Id_Demand_ForecastDetail as id
                ,[Id_Demand_ForecastHeader]
                ,[Country]
                ,[StyleNumber]
                ,[StyleSeason]
                ,[StyleGender]
                ,[StyleColorWay]
                ,[StyleColorName]
                ,[ProductDescription]
                ,[IDPlant]
                ,[ProductType]
                ,[CustomerCategory]
                ,[BuyDateTentative]
                ,[CustomerPromisedDate]
                ,[CustomerOrderType]
                ,[CustomerLeadTime]
                ,[QuantityRequested]
            FROM [dbo].[Demand_ForecastDetail] WHERE Id_Demand_ForecastDetail = {id}
            """
            df = self._loop2.run_until_complete(conn.runServer(textSQL))
            if(len(df) > 0):
                return(df)
            else:
                return([])
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_Demand_ForecastDetails(self, Id_Demand_ForecastHeader, Country, StyleNumber, StyleSeason, StyleGender, StyleColorWay, StyleColorName, ProductDescription, IDPlant, ProductType, CustomerCategory, BuyDateTentative, CustomerPromisedDate, CustomerOrderType, CustomerLeadTime, QuantityRequested):
        try:
            textSQL = f""" 
            INSERT INTO [dbo].[Demand_ForecastDetail]
           ([Id_Demand_ForecastDetail]
           ,[Id_Demand_ForecastHeader]
           ,[Country]
           ,[StyleNumber]
           ,[StyleSeason]
           ,[StyleGender]
           ,[StyleColorWay]
           ,[StyleColorName]
           ,[ProductDescription]
           ,[IDPlant]
           ,[ProductType]
           ,[CustomerCategory]
           ,[BuyDateTentative]
           ,[CustomerPromisedDate]
           ,[CustomerOrderType]
           ,[CustomerLeadTime]
           ,[QuantityRequested])
     VALUES
           ((SELECT ISNULL(MAX([Id_Demand_ForecastDetail]), 0) + 1 FROM [Demand_ForecastDetail])
           ,{Id_Demand_ForecastHeader}
           ,'{Country}'
           ,'{StyleNumber}'
           ,'{StyleSeason}'
           ,'{StyleGender}'
           ,'{StyleColorWay}'
           ,'{StyleColorName}'
           ,'{ProductDescription}'
           ,{IDPlant}
           ,'{ProductType}'
           ,'{CustomerCategory}'
           ,'{BuyDateTentative}'
           ,'{CustomerPromisedDate}'
           ,'{CustomerOrderType}'
           ,{CustomerLeadTime}
           ,{QuantityRequested})
            """
            df = 1
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)