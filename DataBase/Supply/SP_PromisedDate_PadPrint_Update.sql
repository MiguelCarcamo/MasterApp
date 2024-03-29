USE [SUPPLYPLANNING_test]
GO
/****** Object:  StoredProcedure [dbo].[SP_PromisedDate_PadPrint_Update]    Script Date: 11/16/2022 11:07:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author, Miguel de Jesus Carcamo Torres>
-- Create date: <Create Date, 21/4/2022>
-- Description:	<Description, Controla la creacion de fechas promesas PadPrint>
-- =============================================
alter PROCEDURE [dbo].[SP_PromisedDate_PadPrint_Update]
	-- Add the parameters for the stored procedure here
	@MO varchar(100),
	@CuttingNum varchar(10),
	@SerialNumber bigint,
	@IDSuprocessPlant int,
	@IDUser int,
	@PromisedDatePadPrint date,
	@AdjustedPromisedDatePadPrint date,
	@AssignedDatePadPrint date,
	@AssignedWeeksPadPrint int,
	@Comments varchar(50)

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	Declare @IDPromisedDatePadPrint int
	Declare @IDPromisedDate int
	Declare @ITEM int
	Declare @RESULT INT
	Declare @MSJ VARCHAR(350)
	declare @OriginalPromisedDatePadPrint date
	declare @TransactionType varchar(50)
	declare @PromisedDatePadPrint_ date
	declare @AssignedDatePadPrint_ date


	BEGIN TRANSACTION T_TRANSAC
		BEGIN TRY
		SELECT @IDPromisedDate = IDPromisedDate FROM PromisedDate WHERE MO = @MO
		SELECT @IDPromisedDatePadPrint = [IDPromisedDatePadPrint] FROM [PromisedDate_PadPrint] WHERE IDPromisedDate = @IDPromisedDate and CuttingNum = @CuttingNum
		IF (@IDPromisedDate is not null and @IDPromisedDatePadPrint is not null)
		BEGIN
			UPDATE [dbo].[PromisedDate_PadPrint]
			   SET [IDSuprocessPlant] = @IDSuprocessPlant
				  ,[IDUser] = @IDUser
				  ,[SerialNumber] = @SerialNumber
				  ,[PromisedDatePadPrint] = @PromisedDatePadPrint
				  ,[AdjustedPromisedDatePadPrint] = @AdjustedPromisedDatePadPrint
				  ,[AssignedDatePadPrint] = @AssignedDatePadPrint
				  ,[AssignedWeeksPadPrint] = @AssignedWeeksPadPrint
				  ,[Comments] = @Comments
			 WHERE [IDPromisedDatePadPrint] = @IDPromisedDatePadPrint
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
			   ,'PromisedDate_PadPrint'
			   ,@MO
			   ,@IDUser
			   ,@MSJ)
	END
END
