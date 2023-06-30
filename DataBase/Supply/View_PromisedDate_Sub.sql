USE [SUPPLYPLANNING_test]
GO

/****** Object:  View [dbo].[PromisedDate_Sub]    Script Date: 5/24/2023 11:41:40 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





--31997

create VIEW [dbo].[PromisedDate_Sub]
AS
SELECT  PromisedDate.PurchaseOrder, PromisedDate.MO, PromisedDate_Sublimated.SerialNumber, PromisedDate.GroupNum, PromisedDate_Sublimated.CuttingNum,
		PromisedDate.PromisedDate, PromisedDate_Sublimated.PromisedDateSublimated, PLANT_SP.Plant AS SublimatedLocation, AdjustedPromisedDateSublimated
FROM PromisedDate_Sublimated
LEFT OUTER JOIN PromisedDate ON PromisedDate_Sublimated.IDPromisedDate = PromisedDate.IDPromisedDate
LEFT OUTER JOIN General_Plant AS PLANT_SP  ON PromisedDate_Sublimated.IDSuprocessPlant = PLANT_SP.IDPlant
WHERE not (PromisedDate.MO = 'NULL' OR PromisedDate.MO IS NULL)
GO


