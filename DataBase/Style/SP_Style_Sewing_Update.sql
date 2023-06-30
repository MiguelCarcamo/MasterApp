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
-- Description:	<Description, Actualizacion de Customers>
-- =============================================
ALTER PROCEDURE SP_Style_Sewing_Update
	-- Add the parameters for the stored procedure here
	 @Id_Style_Sewing int
	,@Id_Style_GeneralInfo int
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

    -- Insert statements for procedure here
	
	UPDATE [dbo].[Style_Sewing]
	   SET [NumOperators] = @NumOperators
		  ,[SAM] = @SAM
		  ,[GOAL] = @GOAL
		  ,[PE] = @PE
		  ,[LastUpdateDate] = GETDATE()
		  ,[UserUpdate] = @UserUpdate
	 WHERE [Id_Style_Sewing] = @Id_Style_Sewing
END
GO
