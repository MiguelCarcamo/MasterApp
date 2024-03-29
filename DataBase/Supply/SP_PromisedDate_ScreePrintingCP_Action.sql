USE [SUPPLYPLANNING_test]
GO
/****** Object:  StoredProcedure [dbo].[SP_PromisedDate_ScreePrintingCP_Action]    Script Date: 11/16/2022 1:54:21 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,Miguel De Jesus Carcamo Torres>
-- Create date: <Create Date, 22/4/2022>
-- Description:	<Description, Controla la ACTUALIZACION de fechas promesas de Costura>
-- =============================================
ALTER PROCEDURE [dbo].[SP_PromisedDate_ScreePrintingCP_Action]
	-- Add the parameters for the stored procedure here
	@MO varchar(100),
	@CuttingNum varchar(10),
	@SerialNumber bigint,
	@IDSuprocessPlant int,
	@IDUser int,
	@PromisedDateScreePrintingCP date,
	@AdjustedPromisedDateScreePrintingCP date,
	@AssignedDateScreePrintingCP varchar(100),
	@AssignedWeeksScreePrintingCP int,
	@Comments varchar(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	BEGIN TRY 
		Declare @IDPromisedDate int
		Declare @IDPromisedDateScreePrintingCP int
		Declare @check1 int
		Declare @check2 int
		IF(@AssignedDateScreePrintingCP = 'NULL')
		BEGIN
			SET @AssignedDateScreePrintingCP = NULL
		END
		-- Insert statements for procedure here
	
		IF(EXISTS(SELECT IDPromisedDate FROM PromisedDate WHERE MO = @MO ))
		BEGIN
			SELECT @IDPromisedDate = IDPromisedDate FROM PromisedDate WHERE MO = @MO
			SELECT @check1 = COUNT(*) FROM PromisedDate_ScreePrintingCP WHERE IDPromisedDate = @IDPromisedDate AND CuttingNum = @CuttingNum
			IF (@check1 = 0)
			BEGIN
				EXECUTE SP_PromisedDate_ScreePrintingCP_Create @MO, @CuttingNum, @SerialNumber, @IDSuprocessPlant, @IDUser, @PromisedDateScreePrintingCP, @AdjustedPromisedDateScreePrintingCP, @AssignedDateScreePrintingCP, @AssignedWeeksScreePrintingCP, @Comments
			END
			ELSE
			BEGIN
				SELECT @check2 = COUNT(*) FROM PromisedDate_ScreePrintingCP WHERE IDPromisedDate = @IDPromisedDate AND CuttingNum = @CuttingNum AND PromisedDateScreePrintingCP = @PromisedDateScreePrintingCP and AdjustedPromisedDateScreePrintingCP = @AdjustedPromisedDateScreePrintingCP
				IF (@check2 = 0)
				BEGIN
					SELECT @check2
					EXECUTE SP_PromisedDate_ScreePrintingCP_Update @MO, @CuttingNum, @SerialNumber, @IDSuprocessPlant, @IDUser, @PromisedDateScreePrintingCP, @AdjustedPromisedDateScreePrintingCP, @AssignedDateScreePrintingCP, @AssignedWeeksScreePrintingCP, @Comments
				END
			END
		END
	END TRY  
	BEGIN CATCH
	END CATCH 
END
