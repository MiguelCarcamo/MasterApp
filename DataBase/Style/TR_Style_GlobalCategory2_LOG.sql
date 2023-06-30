CREATE TRIGGER TR_Style_GlobalCategory2_LOG
ON [dbo].[Style_GlobalCategory2] AFTER INSERT, UPDATE
AS
	declare @Id_Style_GlobalCategory int
	declare @Id_Style_Customer int
	declare @GlobalCategory varchar(150)
	declare @UserUpdate int
	declare @Comments varchar(550)

SET @Id_Style_GlobalCategory = (SELECT Id_Style_GlobalCategory FROM inserted)
SET @Id_Style_Customer = (SELECT Id_Style_Customer FROM inserted)
SET @GlobalCategory = (SELECT GlobalCategory FROM inserted)
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
           ,'Style_GlobalCategory2'
           ,@Id_Style_GlobalCategory
           ,@UserUpdate
           ,'Customer:'+ cast(@Id_Style_Customer as varchar) + ' GlobalCategory:' + @GlobalCategory)
