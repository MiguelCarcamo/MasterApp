USE [SUPPLYPLANNING_test]
GO

/****** Object:  View [dbo].[PromisedDate_EmbFG]    Script Date: 5/24/2023 9:54:09 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





--31997

ALTER VIEW [dbo].[PromisedDate_EmbFG]
AS
SELECT  PromisedDate.PurchaseOrder, PromisedDate.MO, PromisedDate_EmbroideryFG.SerialNumber, PromisedDate.GroupNum, PromisedDate_EmbroideryFG.CuttingNum,
		PromisedDate.PromisedDate, PromisedDate_EmbroideryFG.PromisedDateEmbroidery, PLANT_SP.Plant AS EmbroideryFGLocation, AdjustedPromisedDateEmbroideryFG
FROM PromisedDate_EmbroideryFG
LEFT OUTER JOIN PromisedDate ON PromisedDate_EmbroideryFG.IDPromisedDate = PromisedDate.IDPromisedDate
LEFT OUTER JOIN General_Plant AS PLANT_SP  ON PromisedDate_EmbroideryFG.IDSuprocessPlant = PLANT_SP.IDPlant
WHERE not (PromisedDate.MO = 'NULL' OR PromisedDate.MO IS NULL)
GO


