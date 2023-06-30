from database.db import conn
import asyncio


class PromisedDateModel():
    _loop2 = asyncio.get_event_loop()
    @classmethod
    def add_PromisedDate(self, type2, Process, Plant, Comments, Po, Mo, Serial, GruopPO, CutNum, Date1, DateAdj, Date2, Assigned):
        try:
            if(type2 == 1):
                textSQL = f"EXECUTE SP_PromisedDate_Action {Plant}, 1, '{Po}', '{Mo}', '{Comments}', '{GruopPO}' "
            else:
                textSQL = f"EXECUTE SP_PromisedDate_{Process}_Action '{Mo}', '{CutNum}', {Serial}, {Plant}, 1, '{Date1}', '{DateAdj}', '{Date2}', {Assigned}, '{Comments}' "
            df = 1
            # print(textSQL)
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)
