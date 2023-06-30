import json
from flask import Flask

from PromissedDate.PromissedData import MainPromissedDate
from PromissedDate.database import conn as db
import asyncio

path1 = "C:\\Users\\Miguel.Carcamo\\Desktop\\app\\MasterApp\\Backend\\PromissedDate\\File\\SewingOrdersData27ST - Planner1.xlsx"
SheetName = "Master"
Plant = None
Promissed = "Promised Date"
Assigned = "Assigned Date Sewing"
AssignedWeeks = "Assigned Weeks Sewing"

loop2 = asyncio.get_event_loop()
app = Flask(__name__)
@app.route('/')
def index():
    return"HELLO WORD"
    # x = MainPromissedDate(path1, SheetName, Plant, Promissed, Assigned, AssignedWeeks)
    # z = loop2.run_until_complete(x.ModelData())
    # for x in range(len(z.index)):
    #     loop2.run_until_complete(db.runServer2(f"EXECUTE SP_PromisedDate_Action 1,1,'{z.iloc[x,0]}','{z.iloc[x,1]}','Test Miguel Carcamo'"))
    # return z.to_json(orient='records')
app.run(debug=True)