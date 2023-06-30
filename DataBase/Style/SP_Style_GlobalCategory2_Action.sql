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
-- Author:		<Author, Miguel De Jesus Carcamo>
-- Create date: <Create Date, 2/14/2023>
-- Description:	<Description,>
-- =============================================
ALTER PROCEDURE SP_Style_GlobalCategory2_Action 
	-- Add the parameters for the stored procedure here
	@Id_Style_GlobalCategory int
	,@Id_Style_Customer int
	,@GlobalCategory varchar(150)
	,@UserUpdate int
	,@Comments varchar(550)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	declare @GlobalCategory_ varchar(150)
	declare @Comments_ varchar(550)
    -- Insert statements for procedure here
	BEGIN TRY
		IF(@Id_Style_GlobalCategory = 0 AND (Select COUNT(*) from Style_GlobalCategory2 where GlobalCategory = @GlobalCategory) = 0)
		BEGIN
			EXECUTE SP_Style_GlobalCategory2_Create @Id_Style_Customer, @GlobalCategory, @UserUpdate, @Comments
		END
		ELSE
		BEGIN
			SELECT @GlobalCategory_ = GlobalCategory, @Comments_ = Comments FROM Style_GlobalCategory2 WHERE Id_Style_GlobalCategory = @Id_Style_GlobalCategory
			IF(@GlobalCategory <> @GlobalCategory_ or @Comments <> @Comments_)
			BEGIN
				EXECUTE SP_Style_GlobalCategory2_Update @Id_Style_GlobalCategory, @Id_Style_Customer, @GlobalCategory, @UserUpdate, @Comments
			END
		END
	END TRY
	BEGIN CATCH
	END CATCH
END
GO
