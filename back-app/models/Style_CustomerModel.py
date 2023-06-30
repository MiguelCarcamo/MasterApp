from database.db import conn
import asyncio

class Style_CustomerModel():
    _loop2 = asyncio.get_event_loop()
    @classmethod
    def get_Style_Customer(self):
        try:
            textSQL = f"""
            SELECT [Id_Style_Customer] as id
                ,[Style_Customer]
                ,[LastUpdateDate]
                ,[UserUpdate]
                ,[Comments]
            FROM [dbo].[Style_Customer]
            """
            df = self._loop2.run_until_complete(conn.runServer(textSQL))
            if(len(df) > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_Style_Customer(self, id, Style_Customer, UserUpdate, Comments):
        try:
            textSQL = f"execute SP_Style_Customer_Action {id}, '{Style_Customer}', {UserUpdate}, '{Comments}' "
            # textSQL = f"execute SP_Style_Customer_Action 1, 'NIKE', 1, 'Test de Actualizacion' "
            df = 1
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)