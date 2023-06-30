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
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE SP_Style_CustomerService_LT_Action 
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
	DECLARE @Colorway_ varchar(50)
    DECLARE @Procurement_ int
    DECLARE @Mfg_ int
    DECLARE @GIPT_ int
    -- Insert statements for procedure here
	IF(@Id_Style_CustomerService_LT = 0 AND (select count(*) from Style_CustomerService_LT where Id_Style_GeneralInfo = @Id_Style_GeneralInfo) = 0)
	BEGIN
		EXECUTE SP_Style_CustomerService_LT_Create @Id_Style_GeneralInfo, @Id_Style_ProductType, @Id_Style_Vendor, @Colorway, @Procurement, @Mfg, @GIPT, @Comments, @UserUpdate
	END
	ELSE
	BEGIN
		SELECT @Colorway_ = Colorway, @Procurement_ = Procurement, @Mfg_ = Mfg, @GIPT_ = GIPT FROM [Style_CustomerService_LT] WHERE Id_Style_CustomerService_LT = @Id_Style_CustomerService_LT
		IF(@Colorway_ <> @Colorway OR @Procurement_ <> @Procurement OR @Mfg_ <> @Mfg OR @GIPT_ <> @GIPT)
		BEGIN
			EXECUTE SP_Style_CustomerService_LT_Update @Id_Style_CustomerService_LT, @Id_Style_GeneralInfo, @Id_Style_ProductType, @Id_Style_Vendor, @Colorway, @Procurement, @Mfg, @GIPT, @Comments, @UserUpdate
		END
	END
END
GO
