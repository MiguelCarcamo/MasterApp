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
-- Description:	<Description, Creacion de Customers>
-- =============================================
ALTER PROCEDURE [dbo].[SP_Style_Sewing_Create]
	-- Add the parameters for the stored procedure here
	 @Id_Style_GeneralInfo int
	,@Id_Style_LayoutConfiguration int
	,@NumOperators int
	,@SAM decimal(12,4)
	,@GOAL int
	,@PE decimal(12,4)
	,@UserUpdate int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	Declare @Id_Style_Sewing int

    -- Insert statements for procedure here
	select @Id_Style_Sewing =  isnull(max([Id_Style_Sewing]),0) + 1 from Style_Sewing
	INSERT INTO [dbo].[Style_Sewing]
			   ([Id_Style_Sewing]
			   ,[Id_Style_GeneralInfo]
			   ,[Id_Style_LayoutConfiguration]
			   ,[NumOperators]
			   ,[SAM]
			   ,[GOAL]
			   ,[PE]
			   ,[LastUpdateDate]
			   ,[UserUpdate])
		 VALUES
			   (@Id_Style_Sewing
			   ,@Id_Style_GeneralInfo
			   ,@Id_Style_LayoutConfiguration
			   ,@NumOperators
			   ,@SAM
			   ,@GOAL
			   ,@PE
			   ,GETDATE()
			   ,@UserUpdate)
END
