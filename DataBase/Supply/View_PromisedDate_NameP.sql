USE [SUPPLYPLANNING_test]
GO

/****** Object:  View [dbo].[PromisedDate_NameP]    Script Date: 5/24/2023 10:44:48 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO






--31997

ALTER VIEW [dbo].[PromisedDate_NameP]
AS
SELECT  PromisedDate.PurchaseOrder, PromisedDate.MO, PromisedDate_Nameplate.SerialNumber, PromisedDate.GroupNum, PromisedDate_Nameplate.CuttingNum,
		PromisedDate.PromisedDate, PromisedDate_Nameplate.PromisedDateNameplate, PLANT_SP.Plant AS NameplateLocation, AdjustedPromisedDateNameplate
FROM PromisedDate_Nameplate
LEFT OUTER JOIN PromisedDate ON PromisedDate_Nameplate.IDPromisedDate = PromisedDate.IDPromisedDate
LEFT OUTER JOIN General_Plant AS PLANT_SP  ON PromisedDate_Nameplate.IDSuprocessPlant = PLANT_SP.IDPlant
WHERE not (PromisedDate.MO = 'NULL' OR PromisedDate.MO IS NULL)
GO


