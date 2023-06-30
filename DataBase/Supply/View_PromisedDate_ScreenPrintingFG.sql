USE [SUPPLYPLANNING_test]
GO

/****** Object:  View [dbo].[PromisedDate_ScreenPrintingFG]    Script Date: 5/24/2023 8:27:44 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO




--31997

ALTER VIEW [dbo].[PromisedDate_ScreenPrintingFG]
AS
SELECT  PromisedDate.PurchaseOrder, PromisedDate.MO, PromisedDate_ScreePrintingFG.SerialNumber, PromisedDate.GroupNum, PromisedDate_ScreePrintingFG.CuttingNum,
		PromisedDate.PromisedDate, PromisedDate_ScreePrintingFG.PromisedDateScreePrintingFG, PLANT_SP.Plant AS ScreenPrintingLocation, AdjustedPromisedDateScreePrintingFG
FROM PromisedDate_ScreePrintingFG
LEFT OUTER JOIN PromisedDate ON PromisedDate_ScreePrintingFG.IDPromisedDate = PromisedDate.IDPromisedDate
LEFT OUTER JOIN General_Plant AS PLANT_SP  ON PromisedDate_ScreePrintingFG.IDSuprocessPlant = PLANT_SP.IDPlant
WHERE not (PromisedDate.MO = 'NULL' OR PromisedDate.MO IS NULL)
GO


