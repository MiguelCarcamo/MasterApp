USE [SUPPLYPLANNING_test]
GO
/****** Object:  Trigger [dbo].[TR_PromisedDate_Embroidery_LOG]    Script Date: 5/24/2023 9:17:31 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[TR_PromisedDate_Embroidery_LOG]
ON [dbo].[PromisedDate_Embroidery] AFTER INSERT, UPDATE
AS
DECLARE @IDPromisedDateEmbroidery INT
DECLARE @PromisedDateEmbroidery DATE
DECLARE @AdjustedPromisedDateEmbroidery DATE
DECLARE @OriginalPromisedDateEmbroidery DATE
DECLARE @AssignedDateEmbroidery DATE
DECLARE @AssignedWeeksEmbroidery INT
DECLARE @Comments  varchar(50)

SET @IDPromisedDateEmbroidery = (SELECT IDPromisedDateEmbroidery FROM inserted)
SET @PromisedDateEmbroidery = (SELECT PromisedDateEmbroidery FROM inserted)
SET @AdjustedPromisedDateEmbroidery = (SELECT AdjustedPromisedDateEmbroideryCP FROM inserted)
SET @AssignedDateEmbroidery = (SELECT AssignedDateEmbroidery FROM inserted)
SET @AssignedWeeksEmbroidery = (SELECT AssignedWeeksEmbroidery FROM inserted)
SET @Comments = (SELECT Comments FROM inserted)
SET @OriginalPromisedDateEmbroidery = (SELECT OriginalPromisedDateEmbroidery FROM PromisedDate_Embroidery WHERE IDPromisedDateEmbroidery = @IDPromisedDateEmbroidery)

INSERT INTO [dbo].[PromisedDate_EmbroideryLog]
		([ITEM]
		,[IDPromisedDateEmbroidery]
		,[OriginalPromisedDateEmbroidery]
		,[PromisedDateEmbroidery]
		,[AdjustedPromisedDateEmbroideryCP]
		,[AssignedDateEmbroidery]
		,[AssignedWeeksEmbroidery]
		,[Comments]
		,[TransactionType])
	VALUES
		((SELECT ISNULL(MAX(ITEM),0) + 1 FROM [PromisedDate_EmbroideryLog])
		,@IDPromisedDateEmbroidery
		,@PromisedDateEmbroidery
		,@PromisedDateEmbroidery
		,@AdjustedPromisedDateEmbroidery
		,@AssignedDateEmbroidery
		,@AssignedWeeksEmbroidery
		,@Comments
		,'Both')
