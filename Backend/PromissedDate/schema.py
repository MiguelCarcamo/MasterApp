from marshmallow import Schema, fields

class PromisedDate(Schema):
    Po = fields.Str
    Mo = fields.Str
    GruopPO = fields.Str
    CutNum = fields.Str
    Serial = fields.Int
    promised_date1 = fields.DateTime
    promised_date2 = fields.DateTime
    Assigned = fields.Int