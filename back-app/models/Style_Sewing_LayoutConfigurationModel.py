from database.db import conn
import asyncio

class Style_Sewing_LayoutConfigurationModel():
    _loop2 = asyncio.get_event_loop()
    @classmethod
    def get_Style_Sewing_LayoutConfiguration(self):
        try:
            textSQL = f"""
            SELECT  Style_Sewing_LayoutConfiguration.Id_Style_LayoutConfiguration as id, Style_Sewing_LayoutConfiguration.Id_Style_Family, Style_Sewing_LayoutConfiguration.LayoutConfiguration, 
                    Style_Sewing_LayoutConfiguration.LastUpdateDate, Style_Sewing_LayoutConfiguration.UserUpdate, Style_Sewing_LayoutConfiguration.Comments, Style_Sewing_Family.Id_Style_WorkCenter, 
                    Style_Sewing_Family.Style_Family, Style_WorkCenter.Style_WorkCenter, Style_Customer.Style_Customer, Style_GlobalCategory2.Id_Style_Customer, Style_GlobalCategory2.GlobalCategory
            FROM Style_Sewing_LayoutConfiguration 
            INNER JOIN Style_Sewing_Family ON Style_Sewing_LayoutConfiguration.Id_Style_Family = Style_Sewing_Family.Id_Style_Family 
            INNER JOIN Style_WorkCenter ON Style_Sewing_Family.Id_Style_WorkCenter = Style_WorkCenter.Id_Style_WorkCenter 
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
    def add_Style_Sewing_LayoutConfiguration(self, id, Id_Style_Family, LayoutConfiguration, UserUpdate, Comments):
        try:
            textSQL = f"execute SP_Style_Sewing_LayoutConfiguration_Action {id}, {Id_Style_Family}, '{LayoutConfiguration}', {UserUpdate}, '{Comments}' "
            # textSQL = f"EXECUTE SP_Style_Sewing_LayoutConfiguration_Action 0, 1, 'DX-DA01', 1, 'TEST MIGUEL' "
            df = 1
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)