USE [SUPPLYPLANNING_test]
GO
/****** Object:  StoredProcedure [dbo].[SP_PromisedDate_ScreePrintingFG_Create]    Script Date: 11/16/2022 1:54:23 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author, Miguel de Jesus Carcamo Torres>
-- Create date: <Create Date, 21/4/2022>
-- Description:	<Description, Controla la creacion de fechas promesas ScreePrintingFG>
-- =============================================
CREATE PROCEDURE [dbo].[SP_PromisedDate_ScreePrintingFG_Create]
	-- Add the parameters for the stored procedure here
	@MO varchar(100),
	@CuttingNum varchar(10),
	@SerialNumber bigint,
	@IDSuprocessPlant int,
	@IDUser int,
	@PromisedDateScreePrintingFG date,
	@AdjustedPromisedDateScreePrintingFG date,
	@AssignedDateScreePrintingFG date,
	@AssignedWeeksScreePrintingFG int,
	@Comments varchar(50)

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	Declare @IDPromisedDateScreePrintingFG int
	Declare @IDPromisedDate int
	Declare @ITEM int
	Declare @RESULT INT
	Declare @MSJ VARCHAR(350)

	BEGIN TRANSACTION T_TRANSAC
		BEGIN TRY
		SELECT @IDPromisedDateScreePrintingFG = ISNULL(MAX([IDPromisedDateScreePrintingFG]),0) + 1 FROM [PromisedDate_ScreePrintingFG]
		SELECT @IDPromisedDate = IDPromisedDate FROM PromisedDate WHERE MO = @MO
		IF (@IDPromisedDate <> '')
		BEGIN
			INSERT INTO [dbo].[PromisedDate_ScreePrintingFG]
				   ([IDPromisedDateScreePrintingFG]
				   ,[IDPromisedDate]
				   ,[CuttingNum]
				   ,[SerialNumber]
				   ,[IDSuprocessPlant]
				   ,[IDUser]
				   ,[OriginalPromisedDateScreePrintingFG]
				   ,[PromisedDateScreePrintingFG]
				   ,[AdjustedPromisedDateScreePrintingFG]
				   ,[AssignedDateScreePrintingFG]
				   ,[AssignedWeeksScreePrintingFG]
				   ,[CreateDate]
				   ,[Comments])
			 VALUES
				   (@IDPromisedDateScreePrintingFG
				   ,@IDPromisedDate
				   ,@CuttingNum
				   ,@SerialNumber
				   ,@IDSuprocessPlant
				   ,@IDUser
				   ,@PromisedDateScreePrintingFG
				   ,@PromisedDateScreePrintingFG
				   ,@AdjustedPromisedDateScreePrintingFG
				   ,@AssignedDateScreePrintingFG
				   ,@AssignedWeeksScreePrintingFG
				   ,GETDATE()
				   ,@Comments)

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
			   ,'PromisedDate_SceenPrinting'
			   ,@MO
			   ,@IDUser
			   ,@MSJ)
	END
END
