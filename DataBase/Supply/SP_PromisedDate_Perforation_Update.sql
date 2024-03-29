USE [SUPPLYPLANNING_test]
GO
/****** Object:  StoredProcedure [dbo].[SP_PromisedDate_Perforation_Update]    Script Date: 11/16/2022 11:07:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author, Miguel de Jesus Carcamo Torres>
-- Create date: <Create Date, 21/4/2022>
-- Description:	<Description, Controla la creacion de fechas promesas Perforation>
-- =============================================
ALTER PROCEDURE [dbo].[SP_PromisedDate_Perforation_Update]
	-- Add the parameters for the stored procedure here
	@MO varchar(100),
	@CuttingNum varchar(10),
	@SerialNumber bigint,
	@IDSuprocessPlant int,
	@IDUser int,
	@PromisedDatePerforation date,
	@AdjustedPromisedDatePerforation date,
	@AssignedDatePerforation date,
	@AssignedWeeksPerforation int,
	@Comments varchar(50)

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	Declare @IDPromisedDatePerforation int
	Declare @IDPromisedDate int
	Declare @ITEM int
	Declare @RESULT INT
	Declare @MSJ VARCHAR(350)
	declare @OriginalPromisedDatePerforation date
	declare @TransactionType varchar(50)
	declare @PromisedDatePerforation_ date
	declare @AssignedDatePerforation_ date


	BEGIN TRANSACTION T_TRANSAC
		BEGIN TRY
		SELECT @IDPromisedDate = IDPromisedDate FROM PromisedDate WHERE MO = @MO
		SELECT @IDPromisedDatePerforation = [IDPromisedDatePerforation] FROM [PromisedDate_Perforation] WHERE IDPromisedDate = @IDPromisedDate and CuttingNum = @CuttingNum
		IF (@IDPromisedDate is not null and @IDPromisedDatePerforation is not null)
		BEGIN
			UPDATE [dbo].[PromisedDate_Perforation]
			   SET [IDSuprocessPlant] = @IDSuprocessPlant
				  ,[IDUser] = @IDUser
				  ,[SerialNumber] = @SerialNumber
				  ,[PromisedDatePerforation] = @PromisedDatePerforation
				  ,[AdjustedPromisedDatePerforation] = @AdjustedPromisedDatePerforation
				  ,[AssignedDatePerforation] = @AssignedDatePerforation
				  ,[AssignedWeeksPerforation] = @AssignedWeeksPerforation
				  ,[Comments] = @Comments
			 WHERE [IDPromisedDatePerforation] = @IDPromisedDatePerforation
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
			   ,'PromisedDate_Perforation'
			   ,@MO
			   ,@IDUser
			   ,@MSJ)
	END
END
