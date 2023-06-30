USE [SUPPLYPLANNING_test]
GO

/****** Object:  View [dbo].[PromisedDate_Carru]    Script Date: 5/24/2023 2:08:57 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





--31997

ALTER VIEW [dbo].[PromisedDate_Carru]
AS
SELECT  PromisedDate.PurchaseOrder, PromisedDate.MO, PromisedDate_Carrusel.SerialNumber, PromisedDate.GroupNum, PromisedDate_Carrusel.CuttingNum,
		PromisedDate.PromisedDate, PromisedDate_Carrusel.PromisedDateCarrusel, PLANT_SP.Plant AS CarruselLocation, AdjustedPromisedDateCarrusel
FROM PromisedDate_Carrusel
LEFT OUTER JOIN PromisedDate ON PromisedDate_Carrusel.IDPromisedDate = PromisedDate.IDPromisedDate
LEFT OUTER JOIN General_Plant AS PLANT_SP  ON PromisedDate_Carrusel.IDSuprocessPlant = PLANT_SP.IDPlant
WHERE not (PromisedDate.MO = 'NULL' OR PromisedDate.MO IS NULL)
GO


