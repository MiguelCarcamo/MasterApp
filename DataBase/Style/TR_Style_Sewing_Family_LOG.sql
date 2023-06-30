CREATE TRIGGER TR_Style_Sewing_Family_LOG
ON [dbo].[Style_Sewing_Family] AFTER INSERT, UPDATE
AS
	declare @Id_Style_Family int
	declare @Id_Style_WorkCenter int
	declare @Style_Family varchar(50)
	declare @UserUpdate int

SET @Id_Style_Family = (SELECT Id_Style_Family FROM inserted)
SET @Id_Style_WorkCenter = (SELECT Id_Style_WorkCenter FROM inserted)
SET @Style_Family = (SELECT Style_Family FROM inserted)
SET @UserUpdate = (SELECT UserUpdate FROM inserted)

INSERT INTO [dbo].[Style_General_Log]
           ([item]
           ,[TableName]
           ,[ID_TableName]
           ,[ID_User]
           ,[ChangeDescription])
     VALUES
           ((select isnull(max(item),0) + 1 from Style_General_Log)
           ,'Style_Sewing_Family'
           ,@Id_Style_Family
           ,@UserUpdate
           ,'WorkCenter:' + cast(@Id_Style_WorkCenter as varchar) + ' Family:' + @Style_Family)
