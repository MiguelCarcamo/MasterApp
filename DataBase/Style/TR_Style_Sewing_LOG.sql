ALTER TRIGGER TR_Style_Sewing_LOG
ON [dbo].[Style_Sewing] AFTER INSERT, UPDATE
AS
	DECLARE @Id_Style_Sewing int
	DECLARE @Id_Style_GeneralInfo int
	DECLARE @Id_Style_LayoutConfiguration int
	DECLARE @NumOperators int
	DECLARE @SAM decimal(12,4)
	DECLARE @GOAL int
	DECLARE @PE decimal(12,4)
	DECLARE @UserUpdate int

SET @Id_Style_Sewing = (SELECT Id_Style_Sewing FROM inserted)
SET @Id_Style_GeneralInfo = (SELECT Id_Style_Sewing FROM inserted)
SET @NumOperators = (SELECT NumOperators FROM inserted)
SET @SAM = (SELECT SAM FROM inserted)
SET @GOAL = (SELECT GOAL FROM inserted)
SET @PE = (SELECT PE FROM inserted)
SET @UserUpdate = (SELECT UserUpdate FROM inserted)
SET @Id_Style_LayoutConfiguration = (SELECT Id_Style_LayoutConfiguration FROM inserted)

INSERT INTO [dbo].[Style_General_Log]
           ([item]
           ,[TableName]
           ,[ID_TableName]
           ,[ID_User]
           ,[ChangeDescription])
     VALUES
           ((select isnull(max(item),0) + 1 from Style_General_Log)
           ,'Style_Sewing'
           ,@Id_Style_Sewing
           ,@UserUpdate
           ,'LayoutConfiguration' + CAST(@Id_Style_LayoutConfiguration as varchar) + 'NumOperators' + CAST(@NumOperators as varchar) + ' SAM:' + CAST(@SAM as varchar) + ' GOAL:' + CAST(@GOAL as varchar) + ' PE:' + CAST(@PE as varchar))