USE [SUPPLYPLANNING_test]
GO
/****** Object:  Trigger [dbo].[TR_PromisedDate_Nameplate_LOG]    Script Date: 5/24/2023 10:11:10 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[TR_PromisedDate_Nameplate_LOG]
ON [dbo].[PromisedDate_Nameplate] AFTER INSERT, UPDATE
AS
DECLARE @IDPromisedDateNameplate INT
DECLARE @PromisedDateNameplate DATE
DECLARE @AdjustedPromisedDateNameplate DATE
DECLARE @OriginalPromisedDateNameplate DATE
DECLARE @AssignedDateNameplate DATE
DECLARE @AssignedWeeksNameplate INT
DECLARE @Comments  varchar(50)

SET @IDPromisedDateNameplate = (SELECT IDPromisedDateNameplate FROM inserted)
SET @PromisedDateNameplate = (SELECT PromisedDateNameplate FROM inserted)
SET @AdjustedPromisedDateNameplate = (SELECT AdjustedPromisedDateNameplate FROM inserted)
SET @AssignedDateNameplate = (SELECT AssignedDateNameplate FROM inserted)
SET @AssignedWeeksNameplate = (SELECT AssignedWeeksNameplate FROM inserted)
SET @Comments = (SELECT Comments FROM inserted)
SET @OriginalPromisedDateNameplate = (SELECT OriginalPromisedDateNameplate FROM PromisedDate_Nameplate WHERE IDPromisedDateNameplate = @IDPromisedDateNameplate)

INSERT INTO [dbo].[PromisedDate_NameplateLog]
		([ITEM]
		,[IDPromisedDateNameplate]
		,[OriginalPromisedDateNameplate]
		,[PromisedDateNameplate]
		,[AdjustedPromisedDateNameplate]
		,[AssignedDateNameplate]
		,[AssignedWeeksNameplate]
		,[Comments]
		,[TransactionType])
	VALUES
		((SELECT ISNULL(MAX(ITEM),0) + 1 FROM [PromisedDate_NameplateLog])
		,@IDPromisedDateNameplate
		,@PromisedDateNameplate
		,@PromisedDateNameplate
		,@AdjustedPromisedDateNameplate
		,@AssignedDateNameplate
		,@AssignedWeeksNameplate
		,@Comments
		,'Both')
