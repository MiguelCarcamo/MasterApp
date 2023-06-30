from database.db import conn
import asyncio

class Style_CustomerService_ProductTypeModel():
    _loop2 = asyncio.get_event_loop()
    @classmethod
    def get_Style_CustomerService_ProductType(self):
        try:
            textSQL = f"""
            SELECT [Id_Style_ProductType] as id
                ,[Style_ProductType]
                ,[LastUpdateDate]
                ,[UserUpdate]
                ,[Comments]
            FROM [dbo].[Style_CustomerService_ProductType]
            """
            df = self._loop2.run_until_complete(conn.runServer(textSQL))
            if(len(df) > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_Style_CustomerService_ProductType(self, id, Style_ProductType, UserUpdate, Comments):
        try:
            textSQL = f"execute SP_Style_CustomerService_ProductType_Action {id}, '{Style_ProductType}', {UserUpdate}, '{Comments}' "
            df = 1
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)