CREATE TRIGGER TR_Style_GeneralInfo_LOG
ON [dbo].[Style_GeneralInfo] AFTER INSERT, UPDATE
AS
	declare @Id_Style_GeneralInfo int
	declare @Id_Style_WorkCenter int
	declare @StyleName varchar(150)
	declare @UserUpdate int
	declare @TypeStyle int
	declare @LeadTime_days int
	declare @WorkFlow varchar(550)
	declare @Comments varchar(550)

SET @Id_Style_GeneralInfo = (SELECT Id_Style_GeneralInfo FROM inserted)
SET @Id_Style_WorkCenter = (SELECT Id_Style_WorkCenter FROM inserted)
SET @StyleName = (SELECT StyleName FROM inserted)
SET @TypeStyle = (SELECT TypeStyle FROM inserted)
SET @LeadTime_days = (SELECT LeadTime_days FROM inserted)
SET @WorkFlow = (SELECT WorkFlow FROM inserted)
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
           ,'Style_GeneralInfo'
           ,@Id_Style_GeneralInfo
           ,@UserUpdate
           ,'WorkCenter:'+ cast(@Id_Style_WorkCenter as varchar) + ' StyleName:' + @StyleName + ' TypeStyle:' + cast(@TypeStyle as varchar) + ' LeadTime_days:' + cast(@LeadTime_days as varchar) + ' WorkFlow:' + @WorkFlow)
