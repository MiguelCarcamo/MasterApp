# 
from database.db import conn
import asyncio

class Style_Sewing_FamilyModel():
    _loop2 = asyncio.get_event_loop()
    @classmethod
    def get_Style_Sewing_Family(self):
        try:
            textSQL = f"""
            SELECT Style_Sewing_Family.Id_Style_Family as id, Style_Sewing_Family.Id_Style_WorkCenter, Style_Sewing_Family.Style_Family, Style_Sewing_Family.LastUpdateDate, 
                Style_Sewing_Family.UserUpdate, Style_Sewing_Family.Comments, Style_WorkCenter.Id_Style_GlobalCategory, Style_WorkCenter.Style_WorkCenter, 
                Style_GlobalCategory2.GlobalCategory, Style_GlobalCategory2.Id_Style_Customer, Style_Customer.Style_Customer
            FROM Style_Sewing_Family 
            INNER JOIN Style_WorkCenter ON Style_Sewing_Family.Id_Style_WorkCenter = Style_WorkCenter.Id_Style_WorkCenter 
            INNER JOIN Style_GlobalCategory2 
            INNER JOIN Style_Customer ON Style_GlobalCategory2.Id_Style_Customer = Style_Customer.Id_Style_Customer 
            ON Style_WorkCenter.Id_Style_GlobalCategory = Style_GlobalCategory2.Id_Style_GlobalCategory
            """
            df = self._loop2.run_until_complete(conn.runServer(textSQL))
            if(len(df) > 0):
                return(df)
            else:
                return([])
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_Style_Sewing_Family(self, id, id_Style_Workcenter, Sewing_Family, UserUpdate, Comments):
        try:
            textSQL = f"execute SP_Style_Sewing_Family_Action {id}, {id_Style_Workcenter}, '{Sewing_Family}', {UserUpdate}, '{Comments}' "
            # textSQL = f"EXECUTE SP_Style_Sewing_Family_Action 0, 1, 'DX-DA01', 1, 'TEST MIGUEL' "
            df = 1
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)