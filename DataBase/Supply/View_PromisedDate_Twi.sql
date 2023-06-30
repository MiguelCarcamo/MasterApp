USE [SUPPLYPLANNING_test]
GO

/****** Object:  View [dbo].[PromisedDate_Twi]    Script Date: 5/24/2023 2:08:52 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





--31997

ALTER VIEW [dbo].[PromisedDate_Twi]
AS
SELECT  PromisedDate.PurchaseOrder, PromisedDate.MO, PromisedDate_Twill.SerialNumber, PromisedDate.GroupNum, PromisedDate_Twill.CuttingNum,
		PromisedDate.PromisedDate, PromisedDate_Twill.PromisedDateTwill, PLANT_SP.Plant AS TwillLocation, AdjustedPromisedDateTwill
FROM PromisedDate_Twill
LEFT OUTER JOIN PromisedDate ON PromisedDate_Twill.IDPromisedDate = PromisedDate.IDPromisedDate
LEFT OUTER JOIN General_Plant AS PLANT_SP  ON PromisedDate_Twill.IDSuprocessPlant = PLANT_SP.IDPlant
WHERE not (PromisedDate.MO = 'NULL' OR PromisedDate.MO IS NULL)
GO


