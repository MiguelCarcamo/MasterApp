from database.db import conn
import asyncio

class Demand_CycleModel():
    _loop2 = asyncio.get_event_loop()
    @classmethod
    def get_Demand_Cycle(self):
        try:
            textSQL = f"""
            SELECT [Id_Demand_Cycle] as id
                ,[Name]
                ,[CreateDate]
                ,[Status]
                ,[Id_User]
                ,[StartDate]
                ,[EndDate]
                ,[Comments]
            FROM [dbo].[Demand_Cycle]
            """
            df = self._loop2.run_until_complete(conn.runServer(textSQL))
            if(len(df) > 0):
                return(df)
            else:
                return([])
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_Demand_Cycle(self, id, Name, Status, Id_User, StartDate, EndDate, Comments):
        try:
            textSQL = f"execute SP_Demand_Cycle_Action {id}, '{Name}', {Status}, {Id_User}, '{StartDate}', '{EndDate}', '{Comments}' "
            df = 1
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            print(ex)
            raise Exception(ex)