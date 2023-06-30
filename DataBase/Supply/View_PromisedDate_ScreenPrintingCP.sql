USE [SUPPLYPLANNING_test]
GO

/****** Object:  View [dbo].[PromisedDate_ScreenPrinting]    Script Date: 5/23/2023 4:23:41 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



--31997

ALTER VIEW [dbo].[PromisedDate_ScreenPrinting]
AS
SELECT  PromisedDate.PurchaseOrder, PromisedDate.MO, PromisedDate_ScreePrintingCP.SerialNumber, PromisedDate.GroupNum, PromisedDate_ScreePrintingCP.CuttingNum,
		PromisedDate.PromisedDate, PromisedDate_ScreePrintingCP.PromisedDateScreePrintingCP, PLANT_SP.Plant AS ScreenPrintingLocation, AdjustedPromisedDateScreePrintingCP
FROM PromisedDate_ScreePrintingCP
LEFT OUTER JOIN PromisedDate ON PromisedDate_ScreePrintingCP.IDPromisedDate = PromisedDate.IDPromisedDate
LEFT OUTER JOIN General_Plant AS PLANT_SP  ON PromisedDate_ScreePrintingCP.IDSuprocessPlant = PLANT_SP.IDPlant
WHERE not (PromisedDate.MO = 'NULL' OR PromisedDate.MO IS NULL)
GO


