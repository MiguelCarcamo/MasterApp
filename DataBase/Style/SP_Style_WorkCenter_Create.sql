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
-- Description:	<Description, Creacion de WorkCenter>
-- =============================================
CREATE PROCEDURE SP_Style_WorkCenter_Create
	-- Add the parameters for the stored procedure here
	 @Id_Style_GlobalCategory int
	,@Style_WorkCenter varchar(150)
	,@UserUpdate int
	,@Comments varchar(550)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	Declare @Id_Style_WorkCenter int

    -- Insert statements for procedure here
	select @Id_Style_WorkCenter =  isnull(max([Id_Style_WorkCenter]),0) + 1 from [Style_WorkCenter]
	INSERT INTO [dbo].[Style_WorkCenter]
			   ([Id_Style_WorkCenter]
			   ,[Id_Style_GlobalCategory]
			   ,[Style_WorkCenter]
			   ,[LastUpdateDate]
			   ,[UserUpdate]
			   ,[Comments])
		 VALUES
			   (@Id_Style_WorkCenter
			   ,@Id_Style_GlobalCategory
			   ,@Style_WorkCenter
			   ,GETDATE()
			   ,@UserUpdate
			   ,@Comments)
END
GO