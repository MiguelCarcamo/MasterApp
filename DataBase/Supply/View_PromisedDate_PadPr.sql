USE [SUPPLYPLANNING_test]
GO

/****** Object:  View [dbo].[PromisedDate_PadPr]    Script Date: 5/24/2023 10:45:12 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO






--31997

ALTER VIEW [dbo].[PromisedDate_PadPr]
AS
SELECT  PromisedDate.PurchaseOrder, PromisedDate.MO, PromisedDate_PadPrint.SerialNumber, PromisedDate.GroupNum, PromisedDate_PadPrint.CuttingNum,
		PromisedDate.PromisedDate, PromisedDate_PadPrint.PromisedDatePadPrint, PLANT_SP.Plant AS PadPrintLocation, AdjustedPromisedDatePadPrint
FROM PromisedDate_PadPrint
LEFT OUTER JOIN PromisedDate ON PromisedDate_PadPrint.IDPromisedDate = PromisedDate.IDPromisedDate
LEFT OUTER JOIN General_Plant AS PLANT_SP  ON PromisedDate_PadPrint.IDSuprocessPlant = PLANT_SP.IDPlant
WHERE not (PromisedDate.MO = 'NULL' OR PromisedDate.MO IS NULL)
GO


