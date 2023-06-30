from database.db import conn
import asyncio

class Style_WorkcenterModel():
    _loop2 = asyncio.get_event_loop()
    @classmethod
    def get_Style_Workcenter(self):
        try:
            textSQL = f"""
            SELECT Style_WorkCenter.Id_Style_WorkCenter as id, Style_WorkCenter.Id_Style_GlobalCategory, Style_WorkCenter.Style_WorkCenter, 
                Style_WorkCenter.LastUpdateDate, Style_WorkCenter.UserUpdate, Style_WorkCenter.Comments, 
                Style_GlobalCategory2.GlobalCategory, Style_GlobalCategory2.Id_Style_Customer, Style_Customer.Style_Customer
            FROM Style_WorkCenter 
            INNER JOIN Style_GlobalCategory2 ON Style_WorkCenter.Id_Style_GlobalCategory = Style_GlobalCategory2.Id_Style_GlobalCategory 
            INNER JOIN Style_Customer ON Style_GlobalCategory2.Id_Style_Customer = Style_Customer.Id_Style_Customer
            """
            df = self._loop2.run_until_complete(conn.runServer(textSQL))
            if(len(df) > 0):
                return(df)
            else:
                return([])
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_Style_Workcenter(self, id, id_Style_GlobalCategory, Style_WorkCenter, UserUpdate, Comments):
        try:
            textSQL = f"execute SP_Style_WorkCenter_Action {id}, {id_Style_GlobalCategory}, '{Style_WorkCenter}', {UserUpdate}, '{Comments}' "
            # textSQL = f"execute SP_Style_GlobalCategory2_Action 1, 1, 'LEGEND TEE 2.1', 1, 'Test de Actualizacion' "
            df = 1
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)