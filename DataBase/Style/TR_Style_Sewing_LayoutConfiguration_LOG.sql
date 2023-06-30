CREATE TRIGGER TR_Style_Sewing_LayoutConfiguration_LOG
ON [dbo].[Style_Sewing_LayoutConfiguration] AFTER INSERT, UPDATE
AS
	declare @Id_Style_LayoutConfiguration int
	declare @Id_Style_Family int
	declare @LayoutConfiguration varchar(50)
	declare @UserUpdate int

SET @Id_Style_LayoutConfiguration = (SELECT Id_Style_LayoutConfiguration FROM inserted)
SET @Id_Style_Family = (SELECT Id_Style_Family FROM inserted)
SET @LayoutConfiguration = (SELECT LayoutConfiguration FROM inserted)
SET @UserUpdate = (SELECT UserUpdate FROM inserted)

INSERT INTO [dbo].[Style_General_Log]
           ([item]
           ,[TableName]
           ,[ID_TableName]
           ,[ID_User]
           ,[ChangeDescription])
     VALUES
           ((select isnull(max(item),0) + 1 from Style_General_Log)
           ,'Style_Sewing_LayoutConfiguration'
           ,@Id_Style_LayoutConfiguration
           ,@UserUpdate
           ,'Family:' + cast(@Id_Style_Family as varchar) + ' LayoutConfiguration:' + @LayoutConfiguration)
