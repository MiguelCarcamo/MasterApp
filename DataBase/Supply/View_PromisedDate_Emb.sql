USE [SUPPLYPLANNING_test]
GO

/****** Object:  View [dbo].[PromisedDate_Emb]    Script Date: 5/24/2023 9:49:13 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





--31997

ALTER VIEW [dbo].[PromisedDate_Emb]
AS
SELECT  PromisedDate.PurchaseOrder, PromisedDate.MO, PromisedDate_Embroidery.SerialNumber, PromisedDate.GroupNum, PromisedDate_Embroidery.CuttingNum,
		PromisedDate.PromisedDate, PromisedDate_Embroidery.PromisedDateEmbroidery, PLANT_SP.Plant AS EmbroideryLocation, AdjustedPromisedDateEmbroideryCP
FROM PromisedDate_Embroidery
LEFT OUTER JOIN PromisedDate ON PromisedDate_Embroidery.IDPromisedDate = PromisedDate.IDPromisedDate
LEFT OUTER JOIN General_Plant AS PLANT_SP  ON PromisedDate_Embroidery.IDSuprocessPlant = PLANT_SP.IDPlant
WHERE not (PromisedDate.MO = 'NULL' OR PromisedDate.MO IS NULL)
GO


