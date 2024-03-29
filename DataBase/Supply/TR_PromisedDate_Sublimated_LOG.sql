USE [SUPPLYPLANNING_test]
GO
/****** Object:  Trigger [dbo].[TR_PromisedDate_Sublimated_LOG]    Script Date: 5/24/2023 11:31:11 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[TR_PromisedDate_Sublimated_LOG]
ON [dbo].[PromisedDate_Sublimated] AFTER INSERT, UPDATE
AS
DECLARE @IDPromisedDateSublimated INT
DECLARE @PromisedDateSublimated DATE
DECLARE @AdjustedPromisedDateSublimated DATE
DECLARE @OriginalPromisedDateSublimated DATE
DECLARE @AssignedDateSublimated DATE
DECLARE @AssignedWeeksSublimated INT
DECLARE @Comments  varchar(50)

SET @IDPromisedDateSublimated = (SELECT IDPromisedDateSublimated FROM inserted)
SET @PromisedDateSublimated = (SELECT PromisedDateSublimated FROM inserted)
SET @AdjustedPromisedDateSublimated = (SELECT AdjustedPromisedDateSublimated FROM inserted)
SET @AssignedDateSublimated = (SELECT AssignedDateSublimated FROM inserted)
SET @AssignedWeeksSublimated = (SELECT AssignedWeeksSublimated FROM inserted)
SET @Comments = (SELECT Comments FROM inserted)
SET @OriginalPromisedDateSublimated = (SELECT OriginalPromisedDateSublimated FROM PromisedDate_Sublimated WHERE IDPromisedDateSublimated = @IDPromisedDateSublimated)

INSERT INTO [dbo].[PromisedDate_SublimatedLog]
		([ITEM]
		,[IDPromisedDateSublimated]
		,[OriginalPromisedDateSublimated]
		,[PromisedDateSublimated]
		,[AdjustedPromisedDateSublimated]
		,[AssignedDateSublimated]
		,[AssignedWeeksSublimated]
		,[Comments]
		,[TransactionType])
	VALUES
		((SELECT ISNULL(MAX(ITEM),0) + 1 FROM [PromisedDate_SublimatedLog])
		,@IDPromisedDateSublimated
		,@PromisedDateSublimated
		,@PromisedDateSublimated
		,@AdjustedPromisedDateSublimated
		,@AssignedDateSublimated
		,@AssignedWeeksSublimated
		,@Comments
		,'Both')
