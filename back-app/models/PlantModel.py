from database.db import conn
import asyncio


class PlantModel():
    _loop2 = asyncio.get_event_loop()
    @classmethod
    def get_Plant(self):
        try:
            textSQL = f"""
            SELECT [IDPlant] as id
                ,[Plant]
            FROM [SUPPLYPLANNING_test].[dbo].[General_Plant]
            """
            df = self._loop2.run_until_complete(conn.runServer(textSQL))
            if(len(df) > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)