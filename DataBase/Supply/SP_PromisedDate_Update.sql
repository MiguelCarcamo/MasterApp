USE [SUPPLYPLANNING_test]
GO
/****** Object:  StoredProcedure [dbo].[SP_PromisedDate_Update]    Script Date: 11/16/2022 9:48:44 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author, Miguel de Jesus Carcamo Torres>
-- Create date: <Create Date, 19/4/2022>
-- Description:	<Description, Controla la ACTUALIZACION de fechas promesas>
-- =============================================
ALTER PROCEDURE [dbo].[SP_PromisedDate_Update]
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
	Declare @IDPromisedDate int
	Declare @ITEM int
	Declare @RESULT INT
	Declare @MSJ VARCHAR(350)
	DECLARE @OriginalPromisedDate Date
	DECLARE @PromisedDate_ Date

	BEGIN TRANSACTION T_TRANSAC
		BEGIN TRY
		SELECT @IDPromisedDate = IDPromisedDate, @PromisedDate_ = PromisedDate FROM PromisedDate WHERE [PurchaseOrder] = @PurchaseOrder
		UPDATE [dbo].[PromisedDate]
		   SET [IDPlant] = @IDPlant
			  ,[IDUser] = @IDUser
			  --,[PromisedDate] = @PromisedDate
			  ,[MO] = @MO
			  ,[Comments] = @Comments
			  ,[GroupNum] = @GroupNum
		 WHERE [IDPromisedDate] = @IDPromisedDate
		SET @RESULT = 1
		COMMIT TRAN T_TRANSAC;
	END TRY
	BEGIN CATCH
		SET @RESULT = 0
		SET @MSJ = ERROR_MESSAGE();
		ROLLBACK TRAN T_TRANSAC;
	END CATCH
	IF @RESULT = 0
	BEGIN
	DECLARE @ITEMERROR INT
	SELECT @ITEMERROR = ISNULL(MAX([ITEM]),0) + 1 FROM [PromisedDate_Error]
		INSERT INTO [dbo].[PromisedDate_Error]
			   ([ITEM]
			   ,[TABLE]
			   ,[PurchaseOrder]
			   ,[User]
			   ,[MsjError])
		 VALUES
			   (@ITEMERROR
			   ,'PromisedDate'
			   ,@PurchaseOrder
			   ,@IDUser
			   ,@MSJ)
	END
END
