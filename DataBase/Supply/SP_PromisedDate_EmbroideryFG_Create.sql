USE [SUPPLYPLANNING_test]
GO
/****** Object:  StoredProcedure [dbo].[SP_PromisedDate_EmbroideryFG_Create]    Script Date: 11/16/2022 11:07:19 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author, Miguel de Jesus Carcamo Torres>
-- Create date: <Create Date, 21/4/2022>
-- Description:	<Description, Controla la creacion de fechas promesas EmbroideryFG>
-- =============================================
ALTER PROCEDURE [dbo].[SP_PromisedDate_EmbroideryFG_Create]
	-- Add the parameters for the stored procedure here
	@MO varchar(100),
	@CuttingNum varchar(10),
	@SerialNumber bigint,
	@IDSuprocessPlant int,
	@IDUser int,
	@PromisedDateEmbroideryFG date,
	@AdjustedPromisedDateEmbroideryFG date,
	@AssignedDateEmbroideryFG date,
	@AssignedWeeksEmbroideryFG int,
	@Comments varchar(50)

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	Declare @IDPromisedDateEmbroideryFG int
	Declare @IDPromisedDate int
	Declare @ITEM int
	Declare @RESULT INT
	Declare @MSJ VARCHAR(350)

	BEGIN TRANSACTION T_TRANSAC
		BEGIN TRY
		SELECT @IDPromisedDateEmbroideryFG = ISNULL(MAX([IDPromisedDateEmbroidery]),0) + 1 FROM [PromisedDate_EmbroideryFG]
		SELECT @IDPromisedDate = IDPromisedDate FROM PromisedDate WHERE MO = @MO
		IF (@IDPromisedDate <> '')
		BEGIN
			INSERT INTO [dbo].[PromisedDate_EmbroideryFG]
				   ([IDPromisedDateEmbroidery]
				   ,[IDPromisedDate]
				   ,[CuttingNum]
				   ,[SerialNumber]
				   ,[IDSuprocessPlant]
				   ,[IDUser]
				   ,[OriginalPromisedDateEmbroidery]
				   ,[PromisedDateEmbroidery]
				   ,AdjustedPromisedDateEmbroideryFG
				   ,[AssignedDateEmbroidery]
				   ,[AssignedWeeksEmbroidery]
				   ,[CreateDate]
				   ,[Comments])
			 VALUES
				   (@IDPromisedDateEmbroideryFG
				   ,@IDPromisedDate
				   ,@CuttingNum
				   ,@SerialNumber
				   ,@IDSuprocessPlant
				   ,@IDUser
				   ,@PromisedDateEmbroideryFG
				   ,@PromisedDateEmbroideryFG
				   ,@AdjustedPromisedDateEmbroideryFG
				   ,@AssignedDateEmbroideryFG
				   ,@AssignedWeeksEmbroideryFG
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
			   ,'PromisedDate_EmbroideryFG'
			   ,@MO
			   ,@IDUser
			   ,@MSJ)
	END
END
