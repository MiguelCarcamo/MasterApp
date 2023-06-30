USE SUPPLYPLANNING_test
go
CREATE VIEW PromisedDate_HN
AS
SELECT  PromisedDate.PurchaseOrder, PromisedDate.MO, PromisedDate_Sewing.SerialNumber, PromisedDate.GroupNum, PromisedDate_Sewing.CuttingNum, PLANT.Plant,
		PromisedDate.PromisedDate, PromisedDate_Sewing.PromisedDateSewing, PLANT_SEWING.Plant AS SewingLocation, PromisedDate_Cutting.PromisedDateCutting , PLANT_CUTTING.Plant as CuttingLocation, 
		PromisedDate_ScreePrintingCP.PromisedDateScreePrintingCP, PLANT_SP.Plant AS SPLocation
FROM PromisedDate_Sewing
LEFT OUTER JOIN General_Plant AS PLANT_SEWING  ON PromisedDate_Sewing.IDSuprocessPlant = PLANT_SEWING.IDPlant
LEFT OUTER JOIN PromisedDate ON PromisedDate_Sewing.IDPromisedDate = PromisedDate.IDPromisedDate
LEFT OUTER JOIN General_Plant AS PLANT  ON PromisedDate.IDPlant = PLANT.IDPlant
LEFT OUTER JOIN PromisedDate_Cutting ON PromisedDate_Sewing.IDPromisedDate = PromisedDate_Cutting.IDPromisedDate AND PromisedDate_Sewing.CuttingNum = PromisedDate_Cutting.CuttingNum
LEFT OUTER JOIN General_Plant AS PLANT_CUTTING  ON PromisedDate_Cutting.IDSuprocessPlant = PLANT_CUTTING.IDPlant
LEFT OUTER JOIN PromisedDate_ScreePrintingCP ON PromisedDate_Sewing.IDPromisedDate = PromisedDate_ScreePrintingCP.IDPromisedDate AND PromisedDate_Sewing.CuttingNum = PromisedDate_ScreePrintingCP.CuttingNum
LEFT OUTER JOIN General_Plant AS PLANT_SP  ON PromisedDate_ScreePrintingCP.IDSuprocessPlant = PLANT_SP.IDPlant
WHERE not (PromisedDate.MO = 'NULL' OR PromisedDate.MO IS NULL)