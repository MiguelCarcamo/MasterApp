USE [SUPPLYPLANNING_test]
GO
/****** Object:  StoredProcedure [dbo].[SP_PromisedDate_Action]    Script Date: 11/16/2022 9:51:53 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author, Miguel de Jesus Carcamo Torres>
-- Create date: <Create Date, 19/4/2022>
-- Description:	<Description, Controla la ACTUALIZACION de fechas promesas>
-- =============================================
ALTER PROCEDURE [dbo].[SP_PromisedDate_Action]
	-- Add the parameters for the stored procedure here
	@IDPlant int,
	@IDUser int,
	@PurchaseOrder varchar(100),
	@MO varchar(100),
	--@PromisedDate date,
	@Comments varchar(50),
	@GroupNum varchar(100)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	BEGIN TRY 
		Declare @IDPromisedDate int
		Declare @check int
		--SELECT @check = COUNT(*) FROM PromisedDate WHERE [PurchaseOrder] = @PurchaseOrder 
		SELECT @IDPromisedDate = IDPromisedDate FROM PromisedDate WHERE MO = @MO
		IF( @IDPromisedDate IS NULL)
		BEGIN
			--EXECUTE SP_PromisedDate_Create @IDPlant, @IDUser, @PurchaseOrder, @MO, @PromisedDate, @Comments, @GroupNum
			EXECUTE SP_PromisedDate_Create @IDPlant, @IDUser, @PurchaseOrder, @MO, @Comments, @GroupNum
		END
		ELSE
		BEGIN
			--EXECUTE SP_PromisedDate_Update @IDPlant, @IDUser, @PurchaseOrder, @MO, @PromisedDate, @Comments, @GroupNum
			EXECUTE SP_PromisedDate_Update @IDPlant, @IDUser, @PurchaseOrder, @MO, @Comments, @GroupNum
		END
	END TRY  
	BEGIN CATCH
	END CATCH 
END
