USE [SUPPLYPLANNING_test]
GO

/****** Object:  View [dbo].[PromisedDate_Plot]    Script Date: 5/24/2023 11:38:08 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





--31997

ALTER VIEW [dbo].[PromisedDate_Plot]
AS
SELECT  PromisedDate.PurchaseOrder, PromisedDate.MO, PromisedDate_Plotter.SerialNumber, PromisedDate.GroupNum, PromisedDate_Plotter.CuttingNum,
		PromisedDate.PromisedDate, PromisedDate_Plotter.PromisedDatePlotter, PLANT_SP.Plant AS PlotterLocation, AdjustedPromisedDatePlotter
FROM PromisedDate_Plotter
LEFT OUTER JOIN PromisedDate ON PromisedDate_Plotter.IDPromisedDate = PromisedDate.IDPromisedDate
LEFT OUTER JOIN General_Plant AS PLANT_SP  ON PromisedDate_Plotter.IDSuprocessPlant = PLANT_SP.IDPlant
WHERE not (PromisedDate.MO = 'NULL' OR PromisedDate.MO IS NULL)
GO


