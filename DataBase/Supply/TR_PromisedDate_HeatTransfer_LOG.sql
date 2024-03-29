USE [SUPPLYPLANNING_test]
GO
/****** Object:  Trigger [dbo].[TR_PromisedDate_HeatTransfer_LOG]    Script Date: 5/24/2023 10:21:59 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[TR_PromisedDate_HeatTransfer_LOG]
ON [dbo].[PromisedDate_HeatTransfer] AFTER INSERT, UPDATE
AS
DECLARE @IDPromisedDateHeatTransfer INT
DECLARE @PromisedDateHeatTransfer DATE
DECLARE @AdjustedPromisedDateHeatTransfer DATE
DECLARE @OriginalPromisedDateHeatTransfer DATE
DECLARE @AssignedDateHeatTransfer DATE
DECLARE @AssignedWeeksHeatTransfer INT
DECLARE @Comments  varchar(50)

SET @IDPromisedDateHeatTransfer = (SELECT IDPromisedDateHeatTransfer FROM inserted)
SET @PromisedDateHeatTransfer = (SELECT PromisedDateHeatTransfer FROM inserted)
SET @AdjustedPromisedDateHeatTransfer = (SELECT AdjustedPromisedDateHeatTransfer FROM inserted)
SET @AssignedDateHeatTransfer = (SELECT AssignedDateHeatTransfer FROM inserted)
SET @AssignedWeeksHeatTransfer = (SELECT AssignedWeeksHeatTransfer FROM inserted)
SET @Comments = (SELECT Comments FROM inserted)
SET @OriginalPromisedDateHeatTransfer = (SELECT OriginalPromisedDateHeatTransfer FROM PromisedDate_HeatTransfer WHERE IDPromisedDateHeatTransfer = @IDPromisedDateHeatTransfer)

INSERT INTO [dbo].[PromisedDate_HeatTransferLog]
		([ITEM]
		,[IDPromisedDateHeatTransfer]
		,[OriginalPromisedDateHeatTransfer]
		,[PromisedDateHeatTransfer]
		,[AdjustedPromisedDateHeatTransfer]
		,[AssignedDateHeatTransfer]
		,[AssignedWeeksHeatTransfer]
		,[Comments]
		,[TransactionType])
	VALUES
		((SELECT ISNULL(MAX(ITEM),0) + 1 FROM [PromisedDate_HeatTransferLog])
		,@IDPromisedDateHeatTransfer
		,@PromisedDateHeatTransfer
		,@PromisedDateHeatTransfer
		,@AdjustedPromisedDateHeatTransfer
		,@AssignedDateHeatTransfer
		,@AssignedWeeksHeatTransfer
		,@Comments
		,'Both')
