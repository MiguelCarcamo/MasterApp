USE [SUPPLYPLANNING_test]
GO
/****** Object:  Trigger [dbo].[TR_PromisedDate_EmbroideryFG_LOG]    Script Date: 5/24/2023 9:47:50 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[TR_PromisedDate_EmbroideryFG_LOG]
ON [dbo].[PromisedDate_EmbroideryFG] AFTER INSERT, UPDATE
AS
DECLARE @IDPromisedDateEmbroideryFG INT
DECLARE @PromisedDateEmbroideryFG DATE
DECLARE @AdjustedPromisedDateEmbroideryFG DATE
DECLARE @OriginalPromisedDateEmbroideryFG DATE
DECLARE @AssignedDateEmbroideryFG DATE
DECLARE @AssignedWeeksEmbroideryFG INT
DECLARE @Comments  varchar(50)

SET @IDPromisedDateEmbroideryFG = (SELECT IDPromisedDateEmbroidery FROM inserted)
SET @PromisedDateEmbroideryFG = (SELECT PromisedDateEmbroidery FROM inserted)
SET @AdjustedPromisedDateEmbroideryFG = (SELECT AdjustedPromisedDateEmbroideryFG FROM inserted)
SET @AssignedDateEmbroideryFG = (SELECT AssignedDateEmbroidery FROM inserted)
SET @AssignedWeeksEmbroideryFG = (SELECT AssignedWeeksEmbroidery FROM inserted)
SET @Comments = (SELECT Comments FROM inserted)
SET @OriginalPromisedDateEmbroideryFG = (SELECT OriginalPromisedDateEmbroidery FROM PromisedDate_EmbroideryFG WHERE IDPromisedDateEmbroidery = @IDPromisedDateEmbroideryFG)

INSERT INTO [dbo].[PromisedDate_EmbroideryFGLog]
		([ITEM]
		,[IDPromisedDateEmbroidery]
		,[OriginalPromisedDateEmbroidery]
		,[PromisedDateEmbroidery]
		,[AdjustedPromisedDateEmbroideryFG]
		,[AssignedDateEmbroidery]
		,[AssignedWeeksEmbroidery]
		,[Comments]
		,[TransactionType])
	VALUES
		((SELECT ISNULL(MAX(ITEM),0) + 1 FROM [PromisedDate_EmbroideryFGLog])
		,@IDPromisedDateEmbroideryFG
		,@PromisedDateEmbroideryFG
		,@PromisedDateEmbroideryFG
		,@AdjustedPromisedDateEmbroideryFG
		,@AssignedDateEmbroideryFG
		,@AssignedWeeksEmbroideryFG
		,@Comments
		,'Both')
