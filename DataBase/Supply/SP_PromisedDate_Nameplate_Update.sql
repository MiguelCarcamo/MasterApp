USE [SUPPLYPLANNING_test]
GO
/****** Object:  StoredProcedure [dbo].[SP_PromisedDate_Nameplate_Update]    Script Date: 11/16/2022 11:07:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author, Miguel de Jesus Carcamo Torres>
-- Create date: <Create Date, 21/4/2022>
-- Description:	<Description, Controla la creacion de fechas promesas Nameplate>
-- =============================================
ALTER PROCEDURE [dbo].[SP_PromisedDate_Nameplate_Update]
	-- Add the parameters for the stored procedure here
	@MO varchar(100),
	@CuttingNum varchar(10),
	@SerialNumber bigint,
	@IDSuprocessPlant int,
	@IDUser int,
	@PromisedDateNameplate date,
	@AdjustedPromisedDateNameplate date,
	@AssignedDateNameplate date,
	@AssignedWeeksNameplate int,
	@Comments varchar(50)

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	Declare @IDPromisedDateNameplate int
	Declare @IDPromisedDate int
	Declare @ITEM int
	Declare @RESULT INT
	Declare @MSJ VARCHAR(350)
	declare @OriginalPromisedDateNameplate date
	declare @TransactionType varchar(50)
	declare @PromisedDateNameplate_ date
	declare @AssignedDateNameplate_ date


	BEGIN TRANSACTION T_TRANSAC
		BEGIN TRY
		SELECT @IDPromisedDate = IDPromisedDate FROM PromisedDate WHERE MO = @MO
		SELECT @IDPromisedDateNameplate = [IDPromisedDateNameplate] FROM [PromisedDate_Nameplate] WHERE IDPromisedDate = @IDPromisedDate and CuttingNum = @CuttingNum
		IF (@IDPromisedDate is not null and @IDPromisedDateNameplate is not null)
		BEGIN
			UPDATE [dbo].[PromisedDate_Nameplate]
			   SET [IDSuprocessPlant] = @IDSuprocessPlant
				  ,[IDUser] = @IDUser
				  ,[SerialNumber] = @SerialNumber
				  ,[PromisedDateNameplate] = @PromisedDateNameplate
				  ,[AdjustedPromisedDateNameplate] = @AdjustedPromisedDateNameplate
				  ,[AssignedDateNameplate] = @AssignedDateNameplate
				  ,[AssignedWeeksNameplate] = @AssignedWeeksNameplate
				  ,[Comments] = @Comments
			 WHERE [IDPromisedDateNameplate] = @IDPromisedDateNameplate
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
			   ,'PromisedDate_Nameplate'
			   ,@MO
			   ,@IDUser
			   ,@MSJ)
	END
END
