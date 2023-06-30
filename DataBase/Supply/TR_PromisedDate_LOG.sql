--CREATE TRIGGER TR_PromisedDate_LOG
ALTER TRIGGER TR_PromisedDate_LOG
ON [dbo].[PromisedDate] AFTER INSERT, UPDATE
AS
DECLARE @IDPromisedDate INT
DECLARE @PromisedDate DATE
--DECLARE @OriginalPromisedDate DATE
DECLARE @Comments  varchar(50)

SET @IDPromisedDate = (SELECT IDPromisedDate FROM inserted)
SET @PromisedDate = (SELECT PromisedDate FROM inserted)
--SET @OriginalPromisedDate = (SELECT OriginalPromisedDate FROM PromisedDate WHERE IDPromisedDate = @IDPromisedDate)
INSERT INTO [dbo].[PromisedDateLog]
		([ITEM]
		,[IDPromisedDate]
		,[OriginalPromisedDate]
		--,[PromisedDate]
		,[Comments])
	VALUES
		((SELECT ISNULL(MAX([ITEM]),0) + 1 FROM [PromisedDateLog])
		,@IDPromisedDate
		,@PromisedDate
		--,@OriginalPromisedDate
		,@Comments)
