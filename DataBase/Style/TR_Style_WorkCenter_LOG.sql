CREATE TRIGGER TR_Style_WorkCenter_LOG
ON [dbo].[Style_WorkCenter] AFTER INSERT, UPDATE
AS
	declare @Id_Style_WorkCenter int
	declare @Id_Style_GlobalCategory int
	declare @Style_WorkCenter varchar(150)
	declare @UserUpdate int
	declare @Comments varchar(550)

SET @Id_Style_WorkCenter = (SELECT Id_Style_WorkCenter FROM inserted)
SET @Id_Style_GlobalCategory = (SELECT Id_Style_GlobalCategory FROM inserted)
SET @Style_WorkCenter = (SELECT Style_WorkCenter FROM inserted)
SET @UserUpdate = (SELECT UserUpdate FROM inserted)
SET @Comments = (SELECT Comments FROM inserted)

INSERT INTO [dbo].[Style_General_Log]
           ([item]
           ,[TableName]
           ,[ID_TableName]
           ,[ID_User]
           ,[ChangeDescription])
     VALUES
           ((select isnull(max(item),0) + 1 from Style_General_Log)
           ,'Style_WorkCenter'
           ,@Id_Style_WorkCenter
           ,@UserUpdate
           ,'GlobalCategory:'+ cast(@Id_Style_GlobalCategory as varchar) + ' WorkCenter:' + @Style_WorkCenter)
