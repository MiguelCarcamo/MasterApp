USE [SUPPLYPLANNING_test]
GO
/****** Object:  Trigger [dbo].[TR_PromisedDate_ScreePrintingFG_LOG]    Script Date: 5/23/2023 4:05:56 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER [dbo].[TR_PromisedDate_ScreePrintingFG_LOG]
ON [dbo].[PromisedDate_ScreePrintingFG] AFTER INSERT, UPDATE
AS
DECLARE @IDPromisedDateScreePrintingFG INT
DECLARE @PromisedDateScreePrintingFG DATE
DECLARE @OriginalPromisedDateScreePrintingFG DATE
DECLARE @AdjustedPromisedDateScreePrintingFG DATE
DECLARE @AssignedDateScreePrintingFG DATE
DECLARE @AssignedWeeksScreePrintingFG INT
DECLARE @Comments  varchar(50)

SET @IDPromisedDateScreePrintingFG = (SELECT IDPromisedDateScreePrintingFG FROM inserted)
SET @PromisedDateScreePrintingFG = (SELECT PromisedDateScreePrintingFG FROM inserted)
SET @AdjustedPromisedDateScreePrintingFG = (SELECT AdjustedPromisedDateScreePrintingFG FROM inserted)
SET @AssignedDateScreePrintingFG = (SELECT AssignedDateScreePrintingFG FROM inserted)
SET @AssignedWeeksScreePrintingFG = (SELECT AssignedWeeksScreePrintingFG FROM inserted)
SET @Comments = (SELECT Comments FROM inserted)
SET @OriginalPromisedDateScreePrintingFG = (SELECT OriginalPromisedDateScreePrintingFG FROM PromisedDate_ScreePrintingFG WHERE IDPromisedDateScreePrintingFG = @IDPromisedDateScreePrintingFG)

INSERT INTO [dbo].[PromisedDate_ScreePrintingFGLog]
		([ITEM]
		,[IDPromisedDateScreePrinting]
		,[OriginalPromisedDateScreePrintingFG]
		,[PromisedDateScreePrintingFG]
		,[AdjustedPromisedDateScreePrintingFG]
		,[AssignedDateScreePrintingFG]
		,[AssignedWeeksScreePrintingFG]
		,[Comments])
	VALUES
		((SELECT ISNULL(MAX(ITEM),0) + 1 FROM [PromisedDate_ScreePrintingFGLog])
		,@IDPromisedDateScreePrintingFG
		,@PromisedDateScreePrintingFG
		,@PromisedDateScreePrintingFG
		,@AdjustedPromisedDateScreePrintingFG
		,@AssignedDateScreePrintingFG
		,@AssignedWeeksScreePrintingFG
		,@Comments)
