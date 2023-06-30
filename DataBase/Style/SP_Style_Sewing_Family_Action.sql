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
-- Create date: <Create Date, 15/2/2023>
-- Description:	<Description, >
-- =============================================
alter PROCEDURE SP_Style_Sewing_Family_Action
	-- Add the parameters for the stored procedure here
	 @Id_Style_Family int
	,@Id_Style_WorkCenter int
	,@Style_Family varchar(50)
	,@UserUpdate int
	,@Comments varchar(550)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @Style_Family_ varchar(50)
	DECLARE @Comments_ varchar(550)
    -- Insert statements for procedure here
	IF (@Id_Style_Family = 0 AND (SELECT COUNT(*) FROM Style_Sewing_Family WHERE Style_Family = @Style_Family) = 0 )
	BEGIN
		EXECUTE SP_Style_Sewing_Family_Create @Id_Style_WorkCenter, @Style_Family, @UserUpdate, @Comments
	END
	ELSE
	BEGIN
		SELECT @Style_Family_ = Style_Family, @Comments_ = Comments FROM Style_Sewing_Family WHERE Id_Style_Family = @Id_Style_Family
		IF (@Style_Family_ <> @Style_Family OR @Comments_ <> @Comments)
		BEGIN
			EXECUTE SP_Style_Sewing_Family_Update @Id_Style_Family, @Id_Style_WorkCenter, @Style_Family, @UserUpdate, @Comments
		END
	END
END
GO
