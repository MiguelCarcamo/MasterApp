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
-- Description:	<Description, Actualizacion de WorkCenter>
-- =============================================
CREATE PROCEDURE SP_Style_GeneralInfo_Update
	-- Add the parameters for the stored procedure here
	 @Id_Style_GeneralInfo int
	,@Id_Style_WorkCenter int
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

    -- Insert statements for procedure here
	UPDATE [dbo].[Style_GeneralInfo]
	   SET [Id_Style_WorkCenter] = @Id_Style_WorkCenter
		  ,[StyleName] = @StyleName
		  ,[LastUpdateDate] = GETDATE()
		  ,[UserUpdate] = @UserUpdate
		  ,[TypeStyle] = @TypeStyle
		  ,[LeadTime_days] = @LeadTime_days
		  ,[WorkFlow] = @WorkFlow
		  ,[Comments] = @Comments
	 WHERE [Id_Style_GeneralInfo] = @Id_Style_GeneralInfo

END
GO