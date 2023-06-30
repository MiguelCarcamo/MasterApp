USE [SUPPLYPLANNING_test]
GO

/****** Object:  View [dbo].[PromisedDate_Sew]    Script Date: 5/23/2023 2:25:50 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



--31997

ALTER VIEW [dbo].[PromisedDate_Sew]
AS
SELECT  PromisedDate.PurchaseOrder, PromisedDate.MO, PromisedDate_Sewing.SerialNumber, PromisedDate.GroupNum, PromisedDate_Sewing.CuttingNum,
		PromisedDate.PromisedDate, PromisedDate_Sewing.PromisedDateSewing, PLANT_SEWING.Plant AS SewingLocation, AdjustedPromisedDateSewing,
		AssignedDateSewing
FROM PromisedDate_Sewing
LEFT OUTER JOIN PromisedDate ON PromisedDate_Sewing.IDPromisedDate = PromisedDate.IDPromisedDate
LEFT OUTER JOIN General_Plant AS PLANT_SEWING  ON PromisedDate_Sewing.IDSuprocessPlant = PLANT_SEWING.IDPlant
WHERE not (PromisedDate.MO = 'NULL' OR PromisedDate.MO IS NULL)
GO


