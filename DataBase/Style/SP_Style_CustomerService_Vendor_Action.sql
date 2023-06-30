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
-- Create date: <Create Date, 27/2/2023>
-- Description:	<Description,>
-- =============================================
alter PROCEDURE SP_Style_CustomerService_Vendor_Action 
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
	declare @Style_Vendor_ varchar(150)
	declare @User_ int
	declare @Comments_ varchar(550)

    -- Insert statements for procedure here
	IF (@Id_Style_Vendor = 0 and (select count(*) from Style_CustomerService_Vendor where Style_Vendor = @Style_Vendor) = 0)
	begin
		EXECUTE SP_Style_CustomerService_Vendor_Create @Style_Vendor, @User, @Comments
	end
	ELSE
	BEGIN
		select @Style_Vendor_ = Style_Vendor, @User_ = UserUpdate, @Comments_ = Comments from Style_CustomerService_Vendor where Id_Style_Vendor = @Id_Style_Vendor
		IF (@Style_Vendor_ <> @Style_Vendor OR @Comments_ <> @Comments)
		BEGIN
			EXECUTE SP_Style_CustomerService_Vendor_Update @Id_Style_Vendor, @Style_Vendor, @User, @Comments
		END
	END
END
GO
