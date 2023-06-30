CREATE TRIGGER TR_Style_Customer_LOG
ON [dbo].[Style_Customer] AFTER INSERT, UPDATE
AS
	declare @Id_Style_Customer int
	declare @Style_Customer varchar(150)
	declare @User int

SET @Id_Style_Customer = (SELECT Id_Style_Customer FROM inserted)
SET @Style_Customer = (SELECT Style_Customer FROM inserted)
SET @User = (SELECT UserUpdate FROM inserted)

INSERT INTO [dbo].[Style_General_Log]
           ([item]
           ,[TableName]
           ,[ID_TableName]
           ,[ID_User]
           ,[ChangeDescription])
     VALUES
           ((select isnull(max(item),0) + 1 from Style_General_Log)
           ,'Style_Customer'
           ,@Id_Style_Customer
           ,@User
           ,'Style_Customer:' + @Style_Customer)
