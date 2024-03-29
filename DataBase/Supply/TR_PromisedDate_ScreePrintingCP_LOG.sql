USE [SUPPLYPLANNING_test]
GO
/****** Object:  Trigger [dbo].[TR_PromisedDate_ScreePrintingCP_LOG]    Script Date: 5/23/2023 4:05:56 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[TR_PromisedDate_ScreePrintingCP_LOG]
ON [dbo].[PromisedDate_ScreePrintingCP] AFTER INSERT, UPDATE
AS
DECLARE @IDPromisedDateScreePrintingCP INT
DECLARE @PromisedDateScreePrintingCP DATE
DECLARE @OriginalPromisedDateScreePrintingCP DATE
DECLARE @AdjustedPromisedDateScreePrintingCP DATE
DECLARE @AssignedDateScreePrintingCP DATE
DECLARE @AssignedWeeksScreePrintingCP INT
DECLARE @Comments  varchar(50)

SET @IDPromisedDateScreePrintingCP = (SELECT IDPromisedDateScreePrintingCP FROM inserted)
SET @PromisedDateScreePrintingCP = (SELECT PromisedDateScreePrintingCP FROM inserted)
SET @AdjustedPromisedDateScreePrintingCP = (SELECT AdjustedPromisedDateScreePrintingCP FROM inserted)
SET @AssignedDateScreePrintingCP = (SELECT AssignedDateScreePrintingCP FROM inserted)
SET @AssignedWeeksScreePrintingCP = (SELECT AssignedWeeksScreePrintingCP FROM inserted)
SET @Comments = (SELECT Comments FROM inserted)
SET @OriginalPromisedDateScreePrintingCP = (SELECT OriginalPromisedDateScreePrintingCP FROM PromisedDate_ScreePrintingCP WHERE IDPromisedDateScreePrintingCP = @IDPromisedDateScreePrintingCP)

INSERT INTO [dbo].[PromisedDate_ScreePrintingCPLog]
		([ITEM]
		,[IDPromisedDateScreePrinting]
		,[OriginalPromisedDateScreePrintingCP]
		,[PromisedDateScreePrintingCP]
		,[AdjustedPromisedDateScreePrintingCP]
		,[AssignedDateScreePrintingCP]
		,[AssignedWeeksScreePrintingCP]
		,[Comments]
		,[TransactionType])
	VALUES
		((SELECT ISNULL(MAX(ITEM),0) + 1 FROM [PromisedDate_ScreePrintingCPLog])
		,@IDPromisedDateScreePrintingCP
		,@PromisedDateScreePrintingCP
		,@PromisedDateScreePrintingCP
		,@AdjustedPromisedDateScreePrintingCP
		,@AssignedDateScreePrintingCP
		,@AssignedWeeksScreePrintingCP
		,@Comments
		,'Both')
