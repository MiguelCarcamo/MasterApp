-- ================================================
-- Template generated from Template Explorer using:
-- Create Procedure (New Menu).SQL
--
-- Use the Specify Values for Template Parameters 
-- command (Ctrl-Shift-M) to fill in the parameter 
-- values below.
--
-- This block of comments will not be included in
-- the definition of the procedure.
-- ================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,Miguel De Jesus Carcamo>
-- Create date: <Create Date, 02/09/2023>
-- Description:	<Description, Creacion de GeneralInfo>
-- =============================================
CREATE PROCEDURE SP_Style_GeneralInfo_Create
	-- Add the parameters for the stored procedure here
	 @Id_Style_WorkCenter int
	,@StyleName varchar(150)
	,@UserUpdate int
	,@TypeStyle int
	,@LeadTime_days int
	,@WorkFlow varchar(550)
	,@Comments varchar(550)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	Declare @Id_Style_GeneralInfo int

    -- Insert statements for procedure here
	select @Id_Style_GeneralInfo =  isnull(max([Id_Style_GeneralInfo]),0) + 1 from [Style_GeneralInfo]
	INSERT INTO [dbo].[Style_GeneralInfo]
			   ([Id_Style_GeneralInfo]
			   ,[Id_Style_WorkCenter]
			   ,[StyleName]
			   ,[LastUpdateDate]
			   ,[UserUpdate]
			   ,[TypeStyle]
			   ,[LeadTime_days]
			   ,[WorkFlow]
			   ,[Comments])
		 VALUES
			   (@Id_Style_GeneralInfo
			   ,@Id_Style_WorkCenter
			   ,@StyleName
			   ,GETDATE()
			   ,@UserUpdate
			   ,@TypeStyle
			   ,@LeadTime_days
			   ,@WorkFlow
			   ,@Comments)
END
GO