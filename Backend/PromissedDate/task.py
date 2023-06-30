import time
from threading import Thread
from database import conn as db
import asyncio
import pandas as pd

loop2 = asyncio.get_event_loop()
# a custom function that blocks for a moment
def task():
    # block for a moment
    time.sleep(2.4)
    # display a message
    print('This is from another thread')
    textSQL3 = f""" 
        INSERT INTO [dbo].[General_WorkTransactions]
            ([ManufactureSerialNumber]
            ,[Title]
            ,[TaskName]
            ,[OperatorName]
            ,[OperatorNumber]
            ,[Sequence]
            ,[MIN_TransactionDate]
            ,[MAX_TransactionDate]
            ,[Quantity])
        VALUES
    """
    loop2.run_until_complete(db.runServer2(textSQL3))

# create a thread
thread = Thread(target=task)
print("1")
# run the thread
thread.start()
print("2")