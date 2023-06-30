from database.db import conn
import asyncio

class Style_GeneralInfoModel():
    _loop2 = asyncio.get_event_loop()
    @classmethod
    def get_Style_GeneralInfo(self):
        try:
            textSQL = f"""
            SELECT Style_GeneralInfo.Id_Style_GeneralInfo as id, Style_GeneralInfo.Id_Style_WorkCenter, Style_GeneralInfo.StyleName, Style_GeneralInfo.LastUpdateDate, Style_GeneralInfo.UserUpdate, Style_GeneralInfo.TypeStyle, 
                Style_GeneralInfo.LeadTime_days, Style_GeneralInfo.WorkFlow, Style_GeneralInfo.Comments, Style_WorkCenter.Id_Style_GlobalCategory, Style_WorkCenter.Style_WorkCenter, Style_GlobalCategory2.GlobalCategory, 
                Style_GlobalCategory2.Id_Style_Customer, Style_Customer.Style_Customer
            FROM Style_GlobalCategory2 
            INNER JOIN Style_Customer ON Style_GlobalCategory2.Id_Style_Customer = Style_Customer.Id_Style_Customer 
            INNER JOIN Style_WorkCenter ON Style_GlobalCategory2.Id_Style_GlobalCategory = Style_WorkCenter.Id_Style_GlobalCategory 
            INNER JOIN Style_GeneralInfo ON Style_WorkCenter.Id_Style_WorkCenter = Style_GeneralInfo.Id_Style_WorkCenter
            """
            df = self._loop2.run_until_complete(conn.runServer(textSQL))
            if(len(df) > 0):
                return(df)
            else:
                return([])
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_Style_GeneralInfo(self, id, id_Style_WorkCenter, StyleName, UserUpdate, TypeStyle, LeadTime_days, WorkFlow, Comments):
        try:
            textSQL = f"execute SP_Style_GeneralInfo_Action {id}, {id_Style_WorkCenter}, '{StyleName}', {UserUpdate}, {TypeStyle}, {LeadTime_days}, '{WorkFlow}', '{Comments}' "
            # textSQL = f"EXECUTE SP_Style_GeneralInfo_Action 1,1,'DX42789',1,1,30,'CUT-SP-SEW-SP-SHIP', 'TEST MIGUEL' "
            df = 1
            # print(textSQL)
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            print(textSQL)
            raise Exception(ex)