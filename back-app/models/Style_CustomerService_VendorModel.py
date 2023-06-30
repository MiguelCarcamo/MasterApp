from database.db import conn
import asyncio

class Style_CustomerService_VendorModel():
    _loop2 = asyncio.get_event_loop()
    @classmethod
    def get_Style_CustomerService_Vendor(self):
        try:
            textSQL = f"""
            SELECT [Id_Style_Vendor] as id
                ,[Style_Vendor]
                ,[LastUpdateDate]
                ,[UserUpdate]
                ,[Comments]
            FROM [dbo].[Style_CustomerService_Vendor]
            """
            df = self._loop2.run_until_complete(conn.runServer(textSQL))
            if(len(df) > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_Style_CustomerService_Vendor(self, id, Style_Vendor, UserUpdate, Comments):
        try:
            textSQL = f"execute SP_Style_CustomerService_Vendor_Action {id}, '{Style_Vendor}', {UserUpdate}, '{Comments}' "
            df = 1
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)