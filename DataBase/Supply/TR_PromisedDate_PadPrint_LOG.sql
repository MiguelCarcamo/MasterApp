USE [SUPPLYPLANNING_test]
GO
/****** Object:  Trigger [dbo].[TR_PromisedDate_PadPrint_LOG]    Script Date: 5/24/2023 10:37:45 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[TR_PromisedDate_PadPrint_LOG]
ON [dbo].[PromisedDate_PadPrint] AFTER INSERT, UPDATE
AS
DECLARE @IDPromisedDatePadPrint INT
DECLARE @PromisedDatePadPrint DATE
DECLARE @AdjustedPromisedDatePadPrint DATE
DECLARE @OriginalPromisedDatePadPrint DATE
DECLARE @AssignedDatePadPrint DATE
DECLARE @AssignedWeeksPadPrint INT
DECLARE @Comments  varchar(50)

SET @IDPromisedDatePadPrint = (SELECT IDPromisedDatePadPrint FROM inserted)
SET @PromisedDatePadPrint = (SELECT PromisedDatePadPrint FROM inserted)
SET @AdjustedPromisedDatePadPrint = (SELECT AdjustedPromisedDatePadPrint FROM inserted)
SET @AssignedDatePadPrint = (SELECT AssignedDatePadPrint FROM inserted)
SET @AssignedWeeksPadPrint = (SELECT AssignedWeeksPadPrint FROM inserted)
SET @Comments = (SELECT Comments FROM inserted)
SET @OriginalPromisedDatePadPrint = (SELECT OriginalPromisedDatePadPrint FROM PromisedDate_PadPrint WHERE IDPromisedDatePadPrint = @IDPromisedDatePadPrint)

INSERT INTO [dbo].[PromisedDate_PadPrintLog]
		([ITEM]
		,[IDPromisedDatePadPrint]
		,[OriginalPromisedDatePadPrint]
		,[PromisedDatePadPrint]
		,[AdjustedPromisedDatePadPrint]
		,[AssignedDatePadPrint]
		,[AssignedWeeksPadPrint]
		,[Comments]
		,[TransactionType])
	VALUES
		((SELECT ISNULL(MAX(ITEM),0) + 1 FROM [PromisedDate_PadPrintLog])
		,@IDPromisedDatePadPrint
		,@PromisedDatePadPrint
		,@PromisedDatePadPrint
		,@AdjustedPromisedDatePadPrint
		,@AssignedDatePadPrint
		,@AssignedWeeksPadPrint
		,@Comments
		,'Both')
