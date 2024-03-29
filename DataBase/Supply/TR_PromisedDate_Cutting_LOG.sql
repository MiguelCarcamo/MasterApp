USE [SUPPLYPLANNING_test]
GO
/****** Object:  Trigger [dbo].[TR_PromisedDate_Cutting_LOG]    Script Date: 5/22/2023 3:52:11 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[TR_PromisedDate_Cutting_LOG]
ON [dbo].[PromisedDate_Cutting] AFTER INSERT, UPDATE
AS
DECLARE @IDPromisedDateCutting INT
DECLARE @PromisedDateCutting DATE
DECLARE @AdjustedPromisedDateCutting DATE
DECLARE @OriginalPromisedDateCutting DATE
DECLARE @AssignedDateCutting DATE
DECLARE @AssignedWeeksCutting INT
DECLARE @Comments  varchar(50)

SET @IDPromisedDateCutting = (SELECT IDPromisedDateCutting FROM inserted)
SET @PromisedDateCutting = (SELECT PromisedDateCutting FROM inserted)
SET @AdjustedPromisedDateCutting = (SELECT AdjustedPromisedDateCutting FROM inserted)
SET @AssignedDateCutting = (SELECT AssignedDateCutting FROM inserted)
SET @AssignedWeeksCutting = (SELECT AssignedWeeksCutting FROM inserted)
SET @Comments = (SELECT Comments FROM inserted)
SET @OriginalPromisedDateCutting = (SELECT OriginalPromisedDateCutting FROM PromisedDate_Cutting WHERE IDPromisedDateCutting = @IDPromisedDateCutting)


INSERT INTO [dbo].[PromisedDate_CuttingLog]
		([ITEM]
		,[IDPromisedDateCutting]
		,[OriginalPromisedDateCutting]
		,[PromisedDateCutting]
		,[AdjustedPromisedDateCutting]
		,[AssignedDateCutting]
		,[AssignedWeeksCutting]
		,[Comments]
		,[TransactionType])
	VALUES
		((SELECT ISNULL(MAX(ITEM),0) + 1 FROM [PromisedDate_CuttingLog])
		,@IDPromisedDateCutting
		,@PromisedDateCutting
		,@PromisedDateCutting
		,@AdjustedPromisedDateCutting
		,@AssignedDateCutting
		,@AssignedWeeksCutting
		,@Comments
		,'Both')
