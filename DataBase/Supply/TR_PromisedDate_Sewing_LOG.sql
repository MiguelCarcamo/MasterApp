USE [SUPPLYPLANNING_test]
GO
/****** Object:  Trigger [dbo].[TR_PromisedDate_Sewing_LOG]    Script Date: 5/23/2023 2:09:58 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[TR_PromisedDate_Sewing_LOG]
ON [dbo].[PromisedDate_Sewing] AFTER INSERT, UPDATE
AS
DECLARE @IDPromisedDateSewing INT
DECLARE @PromisedDateSewing DATE
DECLARE @OriginalPromisedDateSewing DATE
DECLARE @AdjustedPromisedDateSewing DATE
DECLARE @AssignedDateSewing DATE
DECLARE @AssignedWeeksSewing INT
DECLARE @Comments  varchar(50)

SET @IDPromisedDateSewing = (SELECT IDPromisedDateSewing FROM inserted)
SET @PromisedDateSewing = (SELECT PromisedDateSewing FROM inserted)
SET @AdjustedPromisedDateSewing = (SELECT AdjustedPromisedDateSewing FROM inserted)
SET @AssignedDateSewing = (SELECT AssignedDateSewing FROM inserted)
SET @AssignedWeeksSewing = (SELECT AssignedWeeksSewing FROM inserted)
SET @Comments = (SELECT Comments FROM inserted)
SET @OriginalPromisedDateSewing = (SELECT OriginalPromisedDateSewing FROM PromisedDate_Sewing WHERE IDPromisedDateSewing = @IDPromisedDateSewing)

INSERT INTO [dbo].[PromisedDate_SewingLog]
		([ITEM]
		,[IDPromisedDateSewing]
		,[OriginalPromisedDateSewing]
		,[PromisedDateSewing]
		,[AdjustedPromisedDateSewing]
		,[AssignedDateSewing]
		,[AssignedWeeksSewing]
		,[Comments]
		,[TransactionType])
	VALUES
		((SELECT ISNULL(MAX(ITEM),0) + 1 FROM [PromisedDate_SewingLog])
		,@IDPromisedDateSewing
		,@PromisedDateSewing
		,@PromisedDateSewing
		,@AdjustedPromisedDateSewing
		,@AssignedDateSewing
		,@AssignedWeeksSewing
		,@Comments
		,'Both')
