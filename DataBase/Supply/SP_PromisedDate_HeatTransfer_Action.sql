USE [SUPPLYPLANNING_test]
GO
/****** Object:  StoredProcedure [dbo].[SP_PromisedDate_HeatTransfer_Action]    Script Date: 11/16/2022 11:07:25 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,Miguel De Jesus Carcamo Torres>
-- Create date: <Create Date, 22/4/2022>
-- Description:	<Description, Controla la ACTUALIZACION de fechas promesas de Costura>
-- =============================================
ALTER PROCEDURE [dbo].[SP_PromisedDate_HeatTransfer_Action]
	-- Add the parameters for the stored procedure here
	@MO varchar(100),
	@CuttingNum varchar(10),
	@SerialNumber bigint,
	@IDSuprocessPlant int,
	@IDUser int,
	@PromisedDateHeatTransfer date,
	@AdjustedPromisedDateHeatTransfer date,
	@AssignedDateHeatTransfer varchar(100),
	@AssignedWeeksHeatTransfer int,
	@Comments varchar(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	BEGIN TRY 
		Declare @IDPromisedDate int
		Declare @IDPromisedDateHeatTransfer int
		Declare @check1 int
		Declare @check2 int
		IF(@AssignedDateHeatTransfer = 'NULL')
		BEGIN
			SET @AssignedDateHeatTransfer = NULL
		END
		-- Insert statements for procedure here
	
		IF(EXISTS(SELECT IDPromisedDate FROM PromisedDate WHERE MO = @MO ))
		BEGIN
			SELECT @IDPromisedDate = IDPromisedDate FROM PromisedDate WHERE MO = @MO
			SELECT @check1 = COUNT(*) FROM PromisedDate_HeatTransfer WHERE IDPromisedDate = @IDPromisedDate AND CuttingNum = @CuttingNum
			IF (@check1 = 0)
			BEGIN
				EXECUTE SP_PromisedDate_HeatTransfer_Create @MO, @CuttingNum, @SerialNumber, @IDSuprocessPlant, @IDUser, @PromisedDateHeatTransfer, @AdjustedPromisedDateHeatTransfer, @AssignedDateHeatTransfer, @AssignedWeeksHeatTransfer, @Comments
			END
			ELSE
			BEGIN
				SELECT @check2 = COUNT(*) FROM PromisedDate_HeatTransfer WHERE IDPromisedDate = @IDPromisedDate AND CuttingNum = @CuttingNum AND PromisedDateHeatTransfer = @PromisedDateHeatTransfer AND AssignedDateHeatTransfer = @AssignedDateHeatTransfer and AdjustedPromisedDateHeatTransfer = @AdjustedPromisedDateHeatTransfer
				IF (@check2 = 0)
				BEGIN
					--SELECT @check2
					EXECUTE SP_PromisedDate_HeatTransfer_Update @MO, @CuttingNum, @SerialNumber, @IDSuprocessPlant, @IDUser, @PromisedDateHeatTransfer, @AdjustedPromisedDateHeatTransfer, @AssignedDateHeatTransfer, @AssignedWeeksHeatTransfer, @Comments
				END
			END
		END
	END TRY  
	BEGIN CATCH
	END CATCH 
END
