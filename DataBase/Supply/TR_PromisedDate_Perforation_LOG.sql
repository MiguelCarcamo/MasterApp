USE [SUPPLYPLANNING_test]
GO
/****** Object:  Trigger [dbo].[TR_PromisedDate_Perforation_LOG]    Script Date: 5/24/2023 1:58:56 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[TR_PromisedDate_Perforation_LOG]
ON [dbo].[PromisedDate_Perforation] AFTER INSERT, UPDATE
AS
DECLARE @IDPromisedDatePerforation INT
DECLARE @PromisedDatePerforation DATE
DECLARE @AdjustedPromisedDatePerforation DATE
DECLARE @OriginalPromisedDatePerforation DATE
DECLARE @AssignedDatePerforation DATE
DECLARE @AssignedWeeksPerforation INT
DECLARE @Comments  varchar(50)

SET @IDPromisedDatePerforation = (SELECT IDPromisedDatePerforation FROM inserted)
SET @PromisedDatePerforation = (SELECT PromisedDatePerforation FROM inserted)
SET @AdjustedPromisedDatePerforation = (SELECT AdjustedPromisedDatePerforation FROM inserted)
SET @AssignedDatePerforation = (SELECT AssignedDatePerforation FROM inserted)
SET @AssignedWeeksPerforation = (SELECT AssignedWeeksPerforation FROM inserted)
SET @Comments = (SELECT Comments FROM inserted)
SET @OriginalPromisedDatePerforation = (SELECT OriginalPromisedDatePerforation FROM PromisedDate_Perforation WHERE IDPromisedDatePerforation = @IDPromisedDatePerforation)

INSERT INTO [dbo].[PromisedDate_PerforationLog]
		([ITEM]
		,[IDPromisedDatePerforation]
		,[OriginalPromisedDatePerforation]
		,[PromisedDatePerforation]
		,[AdjustedPromisedDatePerforation]
		,[AssignedDatePerforation]
		,[AssignedWeeksPerforation]
		,[Comments]
		,[TransactionType])
	VALUES
		((SELECT ISNULL(MAX(ITEM),0) + 1 FROM [PromisedDate_PerforationLog])
		,@IDPromisedDatePerforation
		,@PromisedDatePerforation
		,@PromisedDatePerforation
		,@AdjustedPromisedDatePerforation
		,@AssignedDatePerforation
		,@AssignedWeeksPerforation
		,@Comments
		,'Both')
