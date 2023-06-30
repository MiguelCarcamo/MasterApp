USE [SUPPLYPLANNING_test]
GO

/****** Object:  View [dbo].[PromisedDate_HN]    Script Date: 5/29/2023 7:24:31 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





--31997

CREATE VIEW [dbo].[AdjustedPromisedDate_HN]
AS
SELECT ISNULL(ISNULL(ISNULL(ISNULL(ISNULL(
		ISNULL(ISNULL(ISNULL(ISNULL(ISNULL(
			ISNULL(ISNULL(ISNULL(PromisedDate_Sew.PurchaseOrder,  PromisedDate_Cut.PurchaseOrder),PromisedDate_ScreenPrinting.PurchaseOrder), PromisedDate_ScreenPrintingFG.PurchaseOrder)
			,PromisedDate_Emb.PurchaseOrder), PromisedDate_EmbFG.PurchaseOrder), PromisedDate_Perf.PurchaseOrder), PromisedDate_Sub.PurchaseOrder) , PromisedDate_Plot.PurchaseOrder
		), PromisedDate_Carru.PurchaseOrder), PromisedDate_Twi.PurchaseOrder), PromisedDate_HeatTr.PurchaseOrder), PromisedDate_NameP.PurchaseOrder), PromisedDate_PadPr.PurchaseOrder) AS PurchaseOrder
	  ,ISNULL(ISNULL(ISNULL(ISNULL(ISNULL(
		ISNULL(ISNULL(ISNULL(ISNULL(ISNULL(
			ISNULL(ISNULL(ISNULL(PromisedDate_Sew.MO,  PromisedDate_Cut.MO),PromisedDate_ScreenPrinting.MO), PromisedDate_ScreenPrintingFG.MO)
			,PromisedDate_Emb.MO), PromisedDate_EmbFG.MO), PromisedDate_Perf.MO), PromisedDate_Sub.MO) , PromisedDate_Plot.MO
		), PromisedDate_Carru.MO), PromisedDate_Twi.MO), PromisedDate_HeatTr.MO), PromisedDate_NameP.MO), PromisedDate_PadPr.MO) AS MO
      ,ISNULL(ISNULL(ISNULL(ISNULL(ISNULL(
		ISNULL(ISNULL(ISNULL(ISNULL(ISNULL(
			ISNULL(ISNULL(ISNULL(PromisedDate_Sew.SerialNumber,  PromisedDate_Cut.SerialNumber),PromisedDate_ScreenPrinting.SerialNumber), PromisedDate_ScreenPrintingFG.SerialNumber)
			,PromisedDate_Emb.SerialNumber), PromisedDate_EmbFG.SerialNumber), PromisedDate_Perf.SerialNumber), PromisedDate_Sub.SerialNumber) , PromisedDate_Plot.SerialNumber
		), PromisedDate_Carru.SerialNumber), PromisedDate_Twi.SerialNumber), PromisedDate_HeatTr.SerialNumber), PromisedDate_NameP.SerialNumber), PromisedDate_PadPr.SerialNumber)  AS SerialNumber
      ,ISNULL(ISNULL(ISNULL(ISNULL(ISNULL(
		ISNULL(ISNULL(ISNULL(ISNULL(ISNULL(
			ISNULL(ISNULL(ISNULL(PromisedDate_Sew.GroupNum,  PromisedDate_Cut.GroupNum),PromisedDate_ScreenPrinting.GroupNum), PromisedDate_ScreenPrintingFG.GroupNum)
			,PromisedDate_Emb.GroupNum), PromisedDate_EmbFG.GroupNum), PromisedDate_Perf.GroupNum), PromisedDate_Sub.GroupNum) , PromisedDate_Plot.GroupNum
		), PromisedDate_Carru.GroupNum), PromisedDate_Twi.GroupNum), PromisedDate_HeatTr.GroupNum), PromisedDate_NameP.GroupNum), PromisedDate_PadPr.GroupNum) AS GroupNum
      ,ISNULL(ISNULL(ISNULL(ISNULL(ISNULL(
		ISNULL(ISNULL(ISNULL(ISNULL(ISNULL(
			ISNULL(ISNULL(ISNULL(PromisedDate_Sew.CuttingNum,  PromisedDate_Cut.CuttingNum),PromisedDate_ScreenPrinting.CuttingNum), PromisedDate_ScreenPrintingFG.CuttingNum)
			,PromisedDate_Emb.CuttingNum), PromisedDate_EmbFG.CuttingNum), PromisedDate_Perf.CuttingNum), PromisedDate_Sub.CuttingNum) , PromisedDate_Plot.CuttingNum
		), PromisedDate_Carru.CuttingNum), PromisedDate_Twi.CuttingNum), PromisedDate_HeatTr.CuttingNum), PromisedDate_NameP.CuttingNum), PromisedDate_PadPr.CuttingNum) AS CuttingNum
      ,'ARN' AS Plant
      ,ISNULL(ISNULL(ISNULL(ISNULL(ISNULL(
		ISNULL(ISNULL(ISNULL(ISNULL(ISNULL(
			ISNULL(ISNULL(ISNULL(PromisedDate_Sew.PromisedDate,  PromisedDate_Cut.PromisedDate),PromisedDate_ScreenPrinting.PromisedDate), PromisedDate_ScreenPrintingFG.PromisedDate)
			,PromisedDate_Emb.PromisedDate), PromisedDate_EmbFG.PromisedDate), PromisedDate_Perf.PromisedDate), PromisedDate_Sub.PromisedDate) , PromisedDate_Plot.PromisedDate
		), PromisedDate_Carru.PromisedDate), PromisedDate_Twi.PromisedDate), PromisedDate_HeatTr.PromisedDate), PromisedDate_NameP.PromisedDate), PromisedDate_PadPr.PromisedDate) AS PromisedDate
      ,PromisedDate_Sew.AdjustedPromisedDateSewing, PromisedDate_Sew.SewingLocation
      ,PromisedDate_Cut.AdjustedPromisedDateCutting, PromisedDate_Cut.CuttingLocation
      ,PromisedDate_ScreenPrinting.AdjustedPromisedDateScreePrintingCP, PromisedDate_ScreenPrinting.ScreenPrintingLocation as SPLocation
      ,PromisedDate_ScreenPrintingFG.AdjustedPromisedDateScreePrintingFG, PromisedDate_ScreenPrintingFG.ScreenPrintingLocation as SPFGLocation
      ,PromisedDate_Emb.AdjustedPromisedDateEmbroideryCP, PromisedDate_Emb.EmbroideryLocation as EmbLocation
      ,PromisedDate_EmbFG.AdjustedPromisedDateEmbroideryFG AS PromisedDateEmbroideryFG, PromisedDate_EmbFG.EmbroideryFGLocation as EmbFGLocation
	  ,PromisedDate_Perf.AdjustedPromisedDatePerforation, PromisedDate_Perf.PerforationLocation as PerforationLocation
	  ,PromisedDate_Sub.AdjustedPromisedDateSublimated, PromisedDate_Sub.SublimatedLocation as SublimatedLocation
	  ,PromisedDate_Plot.AdjustedPromisedDatePlotter, PromisedDate_Plot.PlotterLocation as PlotterLocation
	  ,PromisedDate_Carru.AdjustedPromisedDateCarrusel, PromisedDate_Carru.CarruselLocation as CarruselLocation
	  ,PromisedDate_Twi.AdjustedPromisedDateTwill, PromisedDate_Twi.TwillLocation as TwillLocation
	  ,PromisedDate_HeatTr.AdjustedPromisedDateHeatTransfer, PromisedDate_HeatTr.HeatTransferLocation as HeatTransferLocation
	  ,PromisedDate_NameP.AdjustedPromisedDateNameplate, PromisedDate_NameP.NameplateLocation as NameplateLocation
	  ,PromisedDate_PadPr.AdjustedPromisedDatePadPrint, PromisedDate_PadPr.PadPrintLocation as PadPrintLocation
FROM PromisedDate_Sew
FULL OUTER JOIN PromisedDate_Cut ON PromisedDate_Sew.MO = PromisedDate_Cut.MO AND PromisedDate_Sew.CuttingNum = PromisedDate_Cut.CuttingNum
FULL OUTER JOIN PromisedDate_ScreenPrinting ON PromisedDate_Cut.MO = PromisedDate_ScreenPrinting.MO AND PromisedDate_Cut.CuttingNum = PromisedDate_ScreenPrinting.CuttingNum
FULL OUTER JOIN PromisedDate_ScreenPrintingFG ON PromisedDate_Cut.MO = PromisedDate_ScreenPrintingFG.MO AND PromisedDate_Cut.CuttingNum = PromisedDate_ScreenPrintingFG.CuttingNum
FULL OUTER JOIN PromisedDate_Emb ON PromisedDate_Cut.MO = PromisedDate_Emb.MO AND PromisedDate_Cut.CuttingNum = PromisedDate_Emb.CuttingNum
FULL OUTER JOIN PromisedDate_EmbFG ON PromisedDate_Cut.MO = PromisedDate_EmbFG.MO AND PromisedDate_Cut.CuttingNum = PromisedDate_EmbFG.CuttingNum
FULL OUTER JOIN PromisedDate_Perf ON PromisedDate_Cut.MO = PromisedDate_Perf.MO AND PromisedDate_Cut.CuttingNum = PromisedDate_Perf.CuttingNum
FULL OUTER JOIN PromisedDate_Sub ON PromisedDate_Cut.MO = PromisedDate_Sub.MO AND PromisedDate_Cut.CuttingNum = PromisedDate_Sub.CuttingNum
FULL OUTER JOIN PromisedDate_Plot ON PromisedDate_Cut.MO = PromisedDate_Plot.MO AND PromisedDate_Cut.CuttingNum = PromisedDate_Plot.CuttingNum
FULL OUTER JOIN PromisedDate_Carru ON PromisedDate_Cut.MO = PromisedDate_Carru.MO AND PromisedDate_Cut.CuttingNum = PromisedDate_Carru.CuttingNum
FULL OUTER JOIN PromisedDate_Twi ON PromisedDate_Cut.MO = PromisedDate_Twi.MO AND PromisedDate_Cut.CuttingNum = PromisedDate_Twi.CuttingNum
FULL OUTER JOIN PromisedDate_HeatTr ON PromisedDate_Cut.MO = PromisedDate_HeatTr.MO AND PromisedDate_Cut.CuttingNum = PromisedDate_HeatTr.CuttingNum
FULL OUTER JOIN PromisedDate_NameP ON PromisedDate_Cut.MO = PromisedDate_NameP.MO AND PromisedDate_Cut.CuttingNum = PromisedDate_NameP.CuttingNum
FULL OUTER JOIN PromisedDate_PadPr ON PromisedDate_Cut.MO = PromisedDate_PadPr.MO AND PromisedDate_Cut.CuttingNum = PromisedDate_PadPr.CuttingNum
GO


