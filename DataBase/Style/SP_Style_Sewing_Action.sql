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
-- Author:		<Author, Miguel De Jesus Carcamo Torres>
-- Create date: <Create Date, 2/15/2023>
-- Description:	<Description,>
-- =============================================
ALTER PROCEDURE SP_Style_Sewing_Action
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
	Declare @NumOperators_ int
	Declare @SAM_ decimal(12,4)
	Declare @GOAL_ int
	Declare @PE_ decimal(12,4)
	Declare @UserUpdate_ int
	
	IF (@Id_Style_Sewing = 0 and (select COUNT(*) from Style_Sewing where Id_Style_GeneralInfo = @Id_Style_GeneralInfo) = 0)
	BEGIN
		EXECUTE SP_Style_Sewing_Create @Id_Style_GeneralInfo, @Id_Style_LayoutConfiguration, @NumOperators, @SAM, @GOAL, @PE, @UserUpdate
	END
	ELSE
	BEGIN
		SELECT @NumOperators_ = NumOperators, @SAM_ = SAM, @GOAL_ = GOAL, @PE_ = PE, @Id_Style_Sewing = Id_Style_Sewing
		FROM Style_Sewing WHERE (Id_Style_Sewing = @Id_Style_Sewing or Id_Style_GeneralInfo = @Id_Style_GeneralInfo)
		IF (@NumOperators_ <> @NumOperators OR @SAM_ <> @SAM OR @GOAL_ <> @GOAL OR @PE_ <> @PE)
		BEGIN
			EXECUTE SP_Style_Sewing_Update @Id_Style_Sewing, @Id_Style_GeneralInfo, @Id_Style_LayoutConfiguration, @NumOperators, @SAM, @GOAL, @PE, @UserUpdate
		END
	END
END
GO
