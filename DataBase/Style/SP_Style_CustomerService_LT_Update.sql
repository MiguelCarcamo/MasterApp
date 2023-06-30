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
-- Create date: <Create Date, 2/28/2023>
-- Description:	<Description,>
-- =============================================
CREATE PROCEDURE SP_Style_CustomerService_LT_Update
	-- Add the parameters for the stored procedure here
	@Id_Style_CustomerService_LT int,
    @Id_Style_GeneralInfo int,
    @Id_Style_ProductType int,
    @Id_Style_Vendor int,
    @Colorway varchar(50),
    @Procurement int,
    @Mfg int,
    @GIPT int,
    @Comments varchar(550),
    @UserUpdate int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	UPDATE [dbo].[Style_CustomerService_LT]
	   SET [Id_Style_GeneralInfo] = @Id_Style_GeneralInfo
		  ,[Id_Style_ProductType] = @Id_Style_ProductType
		  ,[Id_Style_Vendor] = @Id_Style_Vendor
		  ,[Colorway] = @Colorway
		  ,[Procurement] = @Procurement
		  ,[Mfg] = @Mfg
		  ,[GIPT] = @GIPT
		  ,[Comments] = @Comments
		  ,[LastUpdateDate] = GETDATE()
		  ,[UserUpdate] = @UserUpdate
	 WHERE [Id_Style_CustomerService_LT] = @Id_Style_CustomerService_LT
		  
END
GO
