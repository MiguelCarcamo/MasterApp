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
CREATE PROCEDURE SP_Style_CustomerService_Vendor_Update
	-- Add the parameters for the stored procedure here
	@Id_Style_Vendor int,
	@Style_Vendor varchar(150),
	@User int,
	@Comments varchar(550)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	UPDATE [dbo].[Style_CustomerService_Vendor]
	   SET [Style_Vendor] = @Style_Vendor
		  ,[Comments] = @Comments
		  ,[UserUpdate] = @User
		  ,[LastUpdateDate] = GETDATE()
	 WHERE [Id_Style_Vendor] = @Id_Style_Vendor

END
GO
