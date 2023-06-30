from database.db import conn
import asyncio

class Style_CustomerService_LTModel():
    _loop2 = asyncio.get_event_loop()
    @classmethod
    def get_Style_CustomerService_LT(self):
        try:
            textSQL = f"""
            SELECT        Style_CustomerService_LT.Id_Style_CustomerService_LT as id, Style_CustomerService_LT.Id_Style_GeneralInfo , Style_GeneralInfo.StyleName, Style_CustomerService_LT.Id_Style_ProductType, Style_CustomerService_ProductType.Style_ProductType, 
                                    Style_CustomerService_LT.Id_Style_Vendor, Style_CustomerService_Vendor.Style_Vendor, Style_CustomerService_LT.Colorway, Style_CustomerService_LT.Procurement, Style_CustomerService_LT.Mfg, 
                                    Style_CustomerService_LT.GIPT, Style_CustomerService_LT.Comments, Style_CustomerService_LT.LastUpdateDate, Style_CustomerService_LT.UserUpdate
            FROM            Style_CustomerService_LT INNER JOIN
                                    Style_CustomerService_ProductType ON Style_CustomerService_LT.Id_Style_ProductType = Style_CustomerService_ProductType.Id_Style_ProductType INNER JOIN
                                    Style_CustomerService_Vendor ON Style_CustomerService_LT.Id_Style_Vendor = Style_CustomerService_Vendor.Id_Style_Vendor INNER JOIN
                                    Style_GeneralInfo ON Style_CustomerService_LT.Id_Style_GeneralInfo = Style_GeneralInfo.Id_Style_GeneralInfo
            """
            df = self._loop2.run_until_complete(conn.runServer(textSQL))
            if(len(df) > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def add_Style_CustomerService_LT(self, id, Id_Style_GeneralInfo, Id_Style_ProductType, Id_Style_Vendor, Colorway, Procurement, Mfg, GIPT, UserUpdate, Comments):
        try:
            textSQL = f"execute SP_Style_CustomerService_LT_Action {id}, {Id_Style_GeneralInfo}, {Id_Style_ProductType}, {Id_Style_Vendor}, '{Colorway}', {Procurement}, {Mfg}, {GIPT}, '{Comments}' ,{UserUpdate}, "
            df = 1
            self._loop2.run_until_complete(conn.runServer2(textSQL))
            if(df > 0):
                return(df)
        except Exception as ex:
            raise Exception(ex)