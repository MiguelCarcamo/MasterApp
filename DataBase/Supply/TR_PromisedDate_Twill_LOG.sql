USE [SUPPLYPLANNING_test]
GO
/****** Object:  Trigger [dbo].[TR_PromisedDate_Twill_LOG]    Script Date: 5/24/2023 1:47:51 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[TR_PromisedDate_Twill_LOG]
ON [dbo].[PromisedDate_Twill] AFTER INSERT, UPDATE
AS
DECLARE @IDPromisedDateTwill INT
DECLARE @PromisedDateTwill DATE
DECLARE @AdjustedPromisedDateTwill DATE
DECLARE @OriginalPromisedDateTwill DATE
DECLARE @AssignedDateTwill DATE
DECLARE @AssignedWeeksTwill INT
DECLARE @Comments  varchar(50)

SET @IDPromisedDateTwill = (SELECT IDPromisedDateTwill FROM inserted)
SET @PromisedDateTwill = (SELECT PromisedDateTwill FROM inserted)
SET @AdjustedPromisedDateTwill = (SELECT AdjustedPromisedDateTwill FROM inserted)
SET @AssignedDateTwill = (SELECT AssignedDateTwill FROM inserted)
SET @AssignedWeeksTwill = (SELECT AssignedWeeksTwill FROM inserted)
SET @Comments = (SELECT Comments FROM inserted)
SET @OriginalPromisedDateTwill = (SELECT OriginalPromisedDateTwill FROM PromisedDate_Twill WHERE IDPromisedDateTwill = @IDPromisedDateTwill)

INSERT INTO [dbo].[PromisedDate_TwillLog]
		([ITEM]
		,[IDPromisedDateTwill]
		,[OriginalPromisedDateTwill]
		,[PromisedDateTwill]
		,[AdjustedPromisedDateTwill]
		,[AssignedDateTwill]
		,[AssignedWeeksTwill]
		,[Comments]
		,[TransactionType])
	VALUES
		((SELECT ISNULL(MAX(ITEM),0) + 1 FROM [PromisedDate_TwillLog])
		,@IDPromisedDateTwill
		,@PromisedDateTwill
		,@PromisedDateTwill
		,@AdjustedPromisedDateTwill
		,@AssignedDateTwill
		,@AssignedWeeksTwill
		,@Comments
		,'Both')
