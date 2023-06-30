USE [SUPPLYPLANNING_test]
GO

/****** Object:  View [dbo].[PromisedDate_Cut]    Script Date: 5/23/2023 9:43:05 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



--31997

ALTER VIEW [dbo].[PromisedDate_Cut]
AS
SELECT  PromisedDate.PurchaseOrder, PromisedDate.MO, PromisedDate_Cutting.SerialNumber, PromisedDate.GroupNum, PromisedDate_Cutting.CuttingNum,
		PromisedDate.PromisedDate, PromisedDate_Cutting.PromisedDateCutting, PLANT_CUTTING.Plant AS CuttingLocation, PromisedDate_Cutting.AdjustedPromisedDateCutting
FROM PromisedDate_Cutting
LEFT OUTER JOIN PromisedDate ON PromisedDate_Cutting.IDPromisedDate = PromisedDate.IDPromisedDate
LEFT OUTER JOIN General_Plant AS PLANT_CUTTING  ON PromisedDate_Cutting.IDSuprocessPlant = PLANT_CUTTING.IDPlant
WHERE not (PromisedDate.MO = 'NULL' OR PromisedDate.MO IS NULL)
GO


