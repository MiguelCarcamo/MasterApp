from schema import PromisedDate as bx

class TypePD():
    _Po = None
    _Mo = None
    _GruopPO = None
    _Serial = None
    _CutNum = None
    _promised_date = None
    _promised_date2 = None
    _Assigned = None
    
    def __init__(self, Po, Mo, Serial, GruopPO, CutNum, Date1, Date2, Assigned):
        self._Po = Po
        self._Mo = Mo
        self._Serial = Serial
        self._GruopPO = GruopPO
        self._CutNum = CutNum
        self._promised_date = Date1
        self._promised_date2 = Date2
        self._Assigned = Assigned
        self.GetData()

    def GetData(self):
        try:
            bx.Mo = str(self._Mo)
            if bx.Mo == '':
                self._Mo = 'NULL'
            else:
                self._Mo = self._Mo
        except:
            self._Mo = 'NULL'
        try:
            bx.GruopPO = str(self._GruopPO)
            if bx.GruopPO == '':
                self._GruopPO = 'NULL'
            else:
                self._GruopPO = "'" + self._GruopPO + "'"
        except:
            self._GruopPO = 'NULL'
        try:
            bx.Serial = int(self._Serial)
        except:
            self._Serial = 'NULL'
        try:
            bx.promised_date1 = self._promised_date
            if bx.promised_date1 == '':
                self._promised_date = 'NULL'
            else:
                self._promised_date = "'" + self._promised_date + "'"
        except:
            self._promised_date = 'NULL'
        try:
            bx.promised_date2 = self._promised_date2
            if bx.promised_date2 == '':
                self._promised_date2 = 'NULL'
            else:
                self._promised_date2 = "'" + self._promised_date2 + "'"
        except:
            self._promised_date2 = 'NULL'
        try:
            bx.Assigned = int(self._Assigned)
        except:
            self._Assigned = 'NULL'