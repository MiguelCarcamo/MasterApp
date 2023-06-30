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
-- Create date: <Create Date, 2/27/2023>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE SP_Style_CustomerService_ProductType_Create
	-- Add the parameters for the stored procedure here
	@Style_ProductType varchar(150),
	@User int,
	@Comments varchar(550)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	declare @Id_Style_ProductType int

	SELECT @Id_Style_ProductType = ISNULL(MAX(Id_Style_ProductType),0) + 1 FROM Style_CustomerService_ProductType
	INSERT INTO [dbo].[Style_CustomerService_ProductType]
           ([Id_Style_ProductType]
           ,[Style_ProductType]
           ,[LastUpdateDate]
           ,[UserUpdate]
           ,[Comments])
     VALUES
           (@Id_Style_ProductType
           ,@Style_ProductType
           ,GETDATE()
           ,@User
           ,@Comments)
END
GO
