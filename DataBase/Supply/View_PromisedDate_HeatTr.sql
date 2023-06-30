USE [SUPPLYPLANNING_test]
GO

/****** Object:  View [dbo].[PromisedDate_HeatTr]    Script Date: 5/24/2023 10:45:35 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO






--31997

ALTER VIEW [dbo].[PromisedDate_HeatTr]
AS
SELECT  PromisedDate.PurchaseOrder, PromisedDate.MO, PromisedDate_HeatTransfer.SerialNumber, PromisedDate.GroupNum, PromisedDate_HeatTransfer.CuttingNum,
		PromisedDate.PromisedDate, PromisedDate_HeatTransfer.PromisedDateHeatTransfer, PLANT_SP.Plant AS HeatTransferLocation, AdjustedPromisedDateHeatTransfer
FROM PromisedDate_HeatTransfer
LEFT OUTER JOIN PromisedDate ON PromisedDate_HeatTransfer.IDPromisedDate = PromisedDate.IDPromisedDate
LEFT OUTER JOIN General_Plant AS PLANT_SP  ON PromisedDate_HeatTransfer.IDSuprocessPlant = PLANT_SP.IDPlant
WHERE not (PromisedDate.MO = 'NULL' OR PromisedDate.MO IS NULL)
GO


