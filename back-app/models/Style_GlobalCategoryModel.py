from database.db import conn
import asyncio

class Style_GlobalCategoryModel():
    _loop2 = asyncio.get_event_loop()
    @classmethod
    def get_Style_GlobalCategory(self):
        try:
            textSQL = f"""
            SELECT Style_GlobalCategory2.Id_Style_GlobalCategory as id, Style_GlobalCategory2.Id_Style_Customer, Style_Customer.Style_Customer, 
                    Style_GlobalCategory2.GlobalCategory, Style_GlobalCategory2.LastUpdateDate, Style_GlobalCategory2.UserUpdate, 
                    Style_GlobalCategory2.Comments
            FROM Style_GlobalCategory2 
            INNER JOIN Style_Customer ON Style_GlobalCategory2.Id_Style_Customer = Style_Customer.Id_Style_Customer
            """
            df = self._loop2.run_until_complete(conn.runServer(textSQL))
            if(len(df) > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_Style_GlobalCategory(self, id, id_Style_Customer, Style_GlobalCategory, UserUpdate, Comments):
        try:
            textSQL = f"execute SP_Style_GlobalCategory2_Action {id}, {id_Style_Customer}, '{Style_GlobalCategory}', {UserUpdate}, '{Comments}' "
            # textSQL = f"execute SP_Style_GlobalCategory2_Action 1, 1, 'LEGEND TEE 2.1', 1, 'Test de Actualizacion' "
            df = 1
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)