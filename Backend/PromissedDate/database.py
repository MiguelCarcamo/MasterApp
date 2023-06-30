import asyncio
import aioodbc

# con esta clase nos permite realizar las conexiones de forma asincrona con los servidores requeridos
class conn: 
    async def runServer(text):
        loop = asyncio.get_event_loop()
        # dsn = r'Driver=SQL Server;Server=10.48.26.25;Database=SUPPLYPLANNING_test;Trusted_Connection=yes;'
        dsn = r'Driver=SQL Server;Server=10.48.26.25;Database=SUPPLYPLANNING_test;UID=supply_planning;PWD=ibUpBdG5K?k!;'
        conn = await aioodbc.connect(dsn=dsn, loop=loop)
        cur = await conn.cursor()
        await cur.execute(text)
        rows = await cur.fetchall()
        dic = [dict(line) for line in [zip([ column[0] for column in cur.description], row) for row in rows]]
        await cur.close()
        await conn.close()
        return dic

    async def runServer2(text):
        loop = asyncio.get_event_loop()
        # dsn = r'Driver=SQL Server;Server=10.48.26.25;Database=SUPPLYPLANNING_test;Trusted_Connection=yes;'
        dsn = r'Driver=SQL Server;Server=10.48.26.25;Database=SUPPLYPLANNING_test;UID=supply_planning;PWD=ibUpBdG5K?k!;'
        conn = await aioodbc.connect(dsn=dsn, loop=loop)
        cur = await conn.cursor()
        await cur.execute(text)
        rows = await cur.commit()
        await cur.close()
        await conn.close()
    
    async def runServer3(text):
        loop = asyncio.get_event_loop()
        # dsn = r'Driver=SQL Server;Server=10.28.1.8\POLYSQL2019;Database=Tegra_Production;Trusted_Connection=yes;'
        dsn = r'Driver=SQL Server;Server=10.28.1.8\POLYSQL2019;Database=Tegra_Production;UID=svc_polyreporting;PWD=P0lyPM2021!!;'
        conn = await aioodbc.connect(dsn=dsn, loop=loop)
        cur = await conn.cursor()
        await cur.execute(text)
        rows = await cur.fetchall()
        dic = [dict(line) for line in [zip([ column[0] for column in cur.description], row) for row in rows]]
        await cur.close()
        await conn.close()
        return dic   

