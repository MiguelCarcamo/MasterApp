USE [SUPPLYPLANNING_test]
GO
/****** Object:  StoredProcedure [dbo].[SP_PromisedDate_Plotter_Update]    Script Date: 11/16/2022 11:07:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author, Miguel de Jesus Carcamo Torres>
-- Create date: <Create Date, 21/4/2022>
-- Description:	<Description, Controla la creacion de fechas promesas Plotter>
-- =============================================
ALTER PROCEDURE [dbo].[SP_PromisedDate_Plotter_Update]
	-- Add the parameters for the stored procedure here
	@MO varchar(100),
	@CuttingNum varchar(10),
	@SerialNumber bigint,
	@IDSuprocessPlant int,
	@IDUser int,
	@PromisedDatePlotter date,
	@AdjustedPromisedDatePlotter date,
	@AssignedDatePlotter date,
	@AssignedWeeksPlotter int,
	@Comments varchar(50)

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	Declare @IDPromisedDatePlotter int
	Declare @IDPromisedDate int
	Declare @ITEM int
	Declare @RESULT INT
	Declare @MSJ VARCHAR(350)
	declare @OriginalPromisedDatePlotter date
	declare @TransactionType varchar(50)
	declare @PromisedDatePlotter_ date
	declare @AssignedDatePlotter_ date


	BEGIN TRANSACTION T_TRANSAC
		BEGIN TRY
		SELECT @IDPromisedDate = IDPromisedDate FROM PromisedDate WHERE MO = @MO
		SELECT @IDPromisedDatePlotter = [IDPromisedDatePlotter] FROM [PromisedDate_Plotter] WHERE IDPromisedDate = @IDPromisedDate and CuttingNum = @CuttingNum
		IF (@IDPromisedDate is not null and @IDPromisedDatePlotter is not null)
		BEGIN
			UPDATE [dbo].[PromisedDate_Plotter]
			   SET [IDSuprocessPlant] = @IDSuprocessPlant
				  ,[IDUser] = @IDUser
				  ,[SerialNumber] = @SerialNumber
				  ,[PromisedDatePlotter] = @PromisedDatePlotter
				  ,[AdjustedPromisedDatePlotter] = @AdjustedPromisedDatePlotter
				  ,[AssignedDatePlotter] = @AssignedDatePlotter
				  ,[AssignedWeeksPlotter] = @AssignedWeeksPlotter
				  ,[Comments] = @Comments
			 WHERE [IDPromisedDatePlotter] = @IDPromisedDatePlotter
		END
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
			   ,'PromisedDate_Plotter'
			   ,@MO
			   ,@IDUser
			   ,@MSJ)
	END
END
