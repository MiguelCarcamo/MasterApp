CREATE TRIGGER TR_Style_CustomerService_LT_LOG
ON [dbo].[Style_CustomerService_LT] AFTER INSERT, UPDATE
AS
	declare @Id_Style_CustomerService_LT int 
	declare @Id_Style_GeneralInfo int
	declare @Id_Style_ProductType int
	declare @Id_Style_Vendor int
	declare @Colorway varchar(50)
	declare @Procurement int
	declare @Mfg int
	declare @GIPT int
	declare @user varchar(550)

SET @Id_Style_CustomerService_LT = (SELECT Id_Style_CustomerService_LT FROM inserted)
SET @Id_Style_GeneralInfo = (SELECT Id_Style_GeneralInfo FROM inserted)
SET @Id_Style_ProductType = (SELECT Id_Style_ProductType FROM inserted)
SET @Id_Style_Vendor = (SELECT Id_Style_Vendor FROM inserted)
SET @Colorway = (SELECT Colorway FROM inserted)
SET @Procurement = (SELECT Procurement FROM inserted)
SET @Mfg = (SELECT Mfg FROM inserted)
SET @GIPT = (SELECT GIPT FROM inserted)
SET @user = (SELECT UserUpdate FROM inserted)

INSERT INTO [dbo].[Style_General_Log]
           ([item]
           ,[TableName]
           ,[ID_TableName]
           ,[ID_User]
           ,[ChangeDescription])
     VALUES
           ((select isnull(max(item),0) + 1 from Style_General_Log)
           ,'Style_CustomerService_LT'
           ,@Id_Style_CustomerService_LT
           ,@User
           ,'Id_Style_CustomerService_LT:' + cast(@Id_Style_CustomerService_LT as varchar) + 'Id_Style_GeneralInfo:' + cast(@Id_Style_GeneralInfo as varchar) + 'Id_Style_ProductType:' + cast(@Id_Style_ProductType as varchar) + 'Id_Style_Vendor:' + cast(@Id_Style_Vendor as varchar))