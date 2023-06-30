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
-- Create date: <Create Date, 16/2/2023>
-- Description:	<Description, >
-- =============================================
CREATE PROCEDURE SP_Style_Sewing_LayoutConfiguration_Action
	-- Add the parameters for the stored procedure here
	 @Id_Style_LayoutConfiguration int
	,@Id_Style_Family int
	,@LayoutConfiguration varchar(50)
	,@UserUpdate int
	,@Comments varchar(550)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @LayoutConfiguration_ varchar(50)
	DECLARE @Comments_ varchar(550)
    -- Insert statements for procedure here
	IF (@Id_Style_LayoutConfiguration = 0 and (select COUNT(*) from Style_Sewing_LayoutConfiguration where LayoutConfiguration = @LayoutConfiguration) = 0)
	begin
		EXECUTE SP_Style_Sewing_LayoutConfiguration_Create @Id_Style_Family, @LayoutConfiguration, @UserUpdate, @Comments
	end
	ELSE
	BEGIN
		SELECT @LayoutConfiguration_ = LayoutConfiguration, @Comments_ = Comments 
		FROM  Style_Sewing_LayoutConfiguration WHERE Id_Style_LayoutConfiguration = @Id_Style_LayoutConfiguration
		IF (@LayoutConfiguration_ <> @LayoutConfiguration OR @Comments_ <> @Comments)
		BEGIN
			EXECUTE SP_Style_Sewing_LayoutConfiguration_Update @Id_Style_LayoutConfiguration, @Id_Style_Family, @LayoutConfiguration, @UserUpdate, @Comments
		END
	END
END
GO
