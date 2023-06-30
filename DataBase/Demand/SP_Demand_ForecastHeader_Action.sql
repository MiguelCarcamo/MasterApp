-- ================================================
-- Template generated from Template Explorer using:
-- Create Procedure (New Menu).SQL
--
-- Use the Specify Values for Template Parameters 
-- command (Ctrl-Shift-M) to fill in the parameter 
-- values below.
--
-- This block of comments will not be included in
-- the definition of the procedure.
-- ================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
ALTER PROCEDURE SP_Demand_ForecastHeader_Action
	-- Add the parameters for the stored procedure here
	@Id_Demand_ForecastHeader int,
	@Id_Style_Customer int,
	@Id_Demand_Cycle int,
	@CustomerForecastDate date,
	@Status int,
	@Id_User int,
	@Comments varchar(350)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	IF(@Id_Demand_ForecastHeader = 0)
	BEGIN
		EXECUTE SP_Demand_ForecastHeader_Create @Id_Style_Customer, @Id_Demand_Cycle, @CustomerForecastDate, 1, @Id_User, @Comments
	END
	ELSE
	BEGIN
		EXECUTE SP_Demand_ForecastHeader_Update @Id_Demand_ForecastHeader, @Id_Style_Customer, @Id_Demand_Cycle, @CustomerForecastDate, @Status, @Id_User, @Comments
	END
END
GO
