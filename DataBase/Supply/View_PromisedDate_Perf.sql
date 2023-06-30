USE [SUPPLYPLANNING_test]
GO

/****** Object:  View [dbo].[PromisedDate_Perf]    Script Date: 5/24/2023 2:08:47 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





--31997

ALTER VIEW [dbo].[PromisedDate_Perf]
AS
SELECT  PromisedDate.PurchaseOrder, PromisedDate.MO, PromisedDate_Perforation.SerialNumber, PromisedDate.GroupNum, PromisedDate_Perforation.CuttingNum,
		PromisedDate.PromisedDate, PromisedDate_Perforation.PromisedDatePerforation, PLANT_SP.Plant AS PerforationLocation, AdjustedPromisedDatePerforation
FROM PromisedDate_Perforation
LEFT OUTER JOIN PromisedDate ON PromisedDate_Perforation.IDPromisedDate = PromisedDate.IDPromisedDate
LEFT OUTER JOIN General_Plant AS PLANT_SP  ON PromisedDate_Perforation.IDSuprocessPlant = PLANT_SP.IDPlant
WHERE not (PromisedDate.MO = 'NULL' OR PromisedDate.MO IS NULL)
GO


