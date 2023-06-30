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
ALTER PROCEDURE SP_Style_WorkCenter_Action
	-- Add the parameters for the stored procedure here
	 @Id_Style_WorkCenter int
	,@Id_Style_GlobalCategory int
	,@Style_WorkCenter varchar(150)
	,@UserUpdate int
	,@Comments varchar(550)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	Declare @Style_WorkCenter_ varchar(150)
	Declare @Comments_ varchar(550)
	declare @Id_Style_GlobalCategory_ int

	BEGIN TRY
		IF (@Id_Style_WorkCenter = 0 AND (SELECT COUNT(*) FROM Style_WorkCenter WHERE Style_WorkCenter = @Style_WorkCenter) = 0)
		BEGIN
			EXECUTE SP_Style_WorkCenter_Create @Id_Style_GlobalCategory, @Style_WorkCenter, @UserUpdate, @Comments
		END
		ELSE
		BEGIN 
			SELECT @Style_WorkCenter_ = Style_WorkCenter, @Comments_ = Comments, @Id_Style_GlobalCategory_ = Id_Style_GlobalCategory
			FROM Style_WorkCenter WHERE Id_Style_WorkCenter = @Id_Style_WorkCenter
			IF (@Style_WorkCenter <> @Style_WorkCenter_ OR @Comments <> @Comments_ OR @Id_Style_GlobalCategory_ <> @Id_Style_GlobalCategory)
			BEGIN
				EXECUTE SP_Style_WorkCenter_Update @Id_Style_WorkCenter, @Id_Style_GlobalCategory, @Style_WorkCenter, @UserUpdate, @Comments
			END
		END
	END TRY
	BEGIN CATCH
	END CATCH
END
GO
