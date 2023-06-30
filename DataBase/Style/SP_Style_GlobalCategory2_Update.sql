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
-- Description:	<Description, Actualizacion de GlobalCategory>
-- =============================================
CREATE PROCEDURE SP_Style_GlobalCategory2_Update
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

    -- Insert statements for procedure here
	UPDATE [dbo].[Style_GlobalCategory2]
	   SET [Id_Style_Customer] = @Id_Style_Customer
		  ,[GlobalCategory] = @GlobalCategory
		  ,[LastUpdateDate] = GETDATE()
		  ,[UserUpdate] = @UserUpdate
		  ,[Comments] = @Comments
	 WHERE [Id_Style_GlobalCategory] = @Id_Style_GlobalCategory

END
GO