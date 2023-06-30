from database.db import conn
import asyncio

class Style_SewingModel():
    _loop2 = asyncio.get_event_loop()
    @classmethod
    def get_Style_Sewing(self):
        try:
            textSQL = f"""
            SELECT  Style_Sewing.Id_Style_Sewing AS id, Style_Sewing.Id_Style_GeneralInfo, Style_Sewing.NumOperators, Style_Sewing.SAM, Style_Sewing.GOAL, Style_Sewing.PE, Style_Sewing.LastUpdateDate, Style_Sewing.UserUpdate, 
                    Style_GeneralInfo.Id_Style_WorkCenter, Style_GeneralInfo.StyleName, Style_WorkCenter.Id_Style_GlobalCategory, Style_WorkCenter.Style_WorkCenter, Style_GlobalCategory2.Id_Style_Customer, 
                    Style_GlobalCategory2.GlobalCategory, Style_Customer.Style_Customer, Style_Sewing.Id_Style_LayoutConfiguration, Style_Sewing_LayoutConfiguration.LayoutConfiguration, 
                    Style_Sewing_LayoutConfiguration.Id_Style_Family, Style_Sewing_Family.Style_Family
            FROM Style_Sewing 
            INNER JOIN Style_GeneralInfo ON Style_Sewing.Id_Style_GeneralInfo = Style_GeneralInfo.Id_Style_GeneralInfo 
            INNER JOIN Style_WorkCenter ON Style_GeneralInfo.Id_Style_WorkCenter = Style_WorkCenter.Id_Style_WorkCenter 
            INNER JOIN Style_GlobalCategory2 ON Style_WorkCenter.Id_Style_GlobalCategory = Style_GlobalCategory2.Id_Style_GlobalCategory 
            INNER JOIN Style_Customer ON Style_GlobalCategory2.Id_Style_Customer = Style_Customer.Id_Style_Customer 
            INNER JOIN Style_Sewing_LayoutConfiguration ON Style_Sewing.Id_Style_LayoutConfiguration = Style_Sewing_LayoutConfiguration.Id_Style_LayoutConfiguration 
            INNER JOIN Style_Sewing_Family ON Style_Sewing_LayoutConfiguration.Id_Style_Family = Style_Sewing_Family.Id_Style_Family
            """
            df = self._loop2.run_until_complete(conn.runServer(textSQL))
            if(len(df) > 0):
                return(df)
            else:
                return([])
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_Style_Sewing(self, id, id_Style_GeneralInfo, id_Style_LayoutConfiguration, NumOperator, SAM, GOAL, PE, UserUpdate):
        try:
            textSQL = f"execute SP_Style_Sewing_Action {id}, {id_Style_GeneralInfo}, {id_Style_LayoutConfiguration}, {NumOperator}, {SAM}, {GOAL}, {PE}, {UserUpdate} "
            # textSQL = f"execute SP_Style_Sewing_Action 0, 1, 18, 30.50, 550, 80.50, 1 "
            df = 1
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)