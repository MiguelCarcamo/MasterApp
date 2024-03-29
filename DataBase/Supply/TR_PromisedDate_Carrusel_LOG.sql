USE [SUPPLYPLANNING_test]
GO
/****** Object:  Trigger [dbo].[TR_PromisedDate_Carrusel_LOG]    Script Date: 5/24/2023 1:39:34 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[TR_PromisedDate_Carrusel_LOG]
ON [dbo].[PromisedDate_Carrusel] AFTER INSERT, UPDATE
AS
DECLARE @IDPromisedDateCarrusel INT
DECLARE @PromisedDateCarrusel DATE
DECLARE @AdjustedPromisedDateCarrusel DATE
DECLARE @OriginalPromisedDateCarrusel DATE
DECLARE @AssignedDateCarrusel DATE
DECLARE @AssignedWeeksCarrusel INT
DECLARE @Comments  varchar(50)

SET @IDPromisedDateCarrusel = (SELECT IDPromisedDateCarrusel FROM inserted)
SET @PromisedDateCarrusel = (SELECT PromisedDateCarrusel FROM inserted)
SET @AdjustedPromisedDateCarrusel = (SELECT AdjustedPromisedDateCarrusel FROM inserted)
SET @AssignedDateCarrusel = (SELECT AssignedDateCarrusel FROM inserted)
SET @AssignedWeeksCarrusel = (SELECT AssignedWeeksCarrusel FROM inserted)
SET @Comments = (SELECT Comments FROM inserted)
SET @OriginalPromisedDateCarrusel = (SELECT OriginalPromisedDateCarrusel FROM PromisedDate_Carrusel WHERE IDPromisedDateCarrusel = @IDPromisedDateCarrusel)

INSERT INTO [dbo].[PromisedDate_CarruselLog]
		([ITEM]
		,[IDPromisedDateCarrusel]
		,[OriginalPromisedDateCarrusel]
		,[PromisedDateCarrusel]
		,[AdjustedPromisedDateCarrusel]
		,[AssignedDateCarrusel]
		,[AssignedWeeksCarrusel]
		,[Comments]
		,[TransactionType])
	VALUES
		((SELECT ISNULL(MAX(ITEM),0) + 1 FROM [PromisedDate_CarruselLog])
		,@IDPromisedDateCarrusel
		,@PromisedDateCarrusel
		,@PromisedDateCarrusel
		,@AdjustedPromisedDateCarrusel
		,@AssignedDateCarrusel
		,@AssignedWeeksCarrusel
		,@Comments
		,'Both')
