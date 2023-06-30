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
-- Create date: <Create Date, 2-13-2023>
-- Description:	<Description, Accion para crear un cliente>
-- =============================================
ALTER PROCEDURE SP_Style_Customer_Action
	-- Add the parameters for the stored procedure here
	@Id_Style_Customer int,
	@Style_Customer varchar(150),
	@User int,
	@Comments varchar(550),
	@RETURN varchar(5) output
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @Id_Style_Customer_ int
	DECLARE @Style_Customer_ varchar(150)
	DECLARE @User_ int
	DECLARE @Comments_ varchar(550)

    -- Insert statements for procedure here
	BEGIN TRY
		IF (@Id_Style_Customer = 0 and (select count(*) from Style_Customer where Style_Customer = @Style_Customer) = 0)
		BEGIN
			EXECUTE SP_Style_Customer_Create @Style_Customer, @User, @Comments
		END
		ELSE
		BEGIN
			SELECT @Style_Customer_ = Style_Customer, @Comments_ = Comments FROM Style_Customer WHERE Id_Style_Customer = @Id_Style_Customer
			IF (@Style_Customer_ <> @Style_Customer or @Comments <> @Comments_)
			BEGIN
				EXECUTE [SP_Style_Customer_Update] @Id_Style_Customer, @Style_Customer, @User, @Comments
			END
		END
		SET @RETURN = 'YES'
	END TRY
	BEGIN CATCH
		SET @RETURN = 'NO'
	END CATCH
END
GO
