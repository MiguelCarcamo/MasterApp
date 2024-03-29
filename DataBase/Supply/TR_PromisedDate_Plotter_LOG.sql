USE [SUPPLYPLANNING_test]
GO
/****** Object:  Trigger [dbo].[TR_PromisedDate_Plotter_LOG]    Script Date: 5/24/2023 11:26:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER TRIGGER [dbo].[TR_PromisedDate_Plotter_LOG]
ON [dbo].[PromisedDate_Plotter] AFTER INSERT, UPDATE
AS
DECLARE @IDPromisedDatePlotter INT
DECLARE @PromisedDatePlotter DATE
DECLARE @AdjustedPromisedDatePlotter DATE
DECLARE @OriginalPromisedDatePlotter DATE
DECLARE @AssignedDatePlotter DATE
DECLARE @AssignedWeeksPlotter INT
DECLARE @Comments  varchar(50)

SET @IDPromisedDatePlotter = (SELECT IDPromisedDatePlotter FROM inserted)
SET @PromisedDatePlotter = (SELECT PromisedDatePlotter FROM inserted)
SET @AdjustedPromisedDatePlotter = (SELECT AdjustedPromisedDatePlotter FROM inserted)
SET @AssignedDatePlotter = (SELECT AssignedDatePlotter FROM inserted)
SET @AssignedWeeksPlotter = (SELECT AssignedWeeksPlotter FROM inserted)
SET @Comments = (SELECT Comments FROM inserted)
SET @OriginalPromisedDatePlotter = (SELECT OriginalPromisedDatePlotter FROM PromisedDate_Plotter WHERE IDPromisedDatePlotter = @IDPromisedDatePlotter)

INSERT INTO [dbo].[PromisedDate_PlotterLog]
		([ITEM]
		,[IDPromisedDatePlotter]
		,[OriginalPromisedDatePlotter]
		,[PromisedDatePlotter]
		,[AdjustedPromisedDatePlotter]
		,[AssignedDatePlotter]
		,[AssignedWeeksPlotter]
		,[Comments]
		,[TransactionType])
	VALUES
		((SELECT ISNULL(MAX(ITEM),0) + 1 FROM [PromisedDate_PlotterLog])
		,@IDPromisedDatePlotter
		,@PromisedDatePlotter
		,@PromisedDatePlotter
		,@AdjustedPromisedDatePlotter
		,@AssignedDatePlotter
		,@AssignedWeeksPlotter
		,@Comments
		,'Both')
