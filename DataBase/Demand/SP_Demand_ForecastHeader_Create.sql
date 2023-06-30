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
-- Author:		<Author, Miguel De Jesus Carcamo>
-- Create date: <Create Date, 3/13/2023>
-- Description:	<Description,>
-- =============================================
alter PROCEDURE SP_Demand_ForecastHeader_Create
	-- Add the parameters for the stored procedure here
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
	
	DECLARE @Id_Demand_ForecastHeader INT
	SELECT @Id_Demand_ForecastHeader = ISNULL(MAX(Id_Demand_ForecastHeader),0) + 1 FROM [Demand_ForecastHeader]
    -- Insert statements for procedure here
	INSERT INTO [dbo].[Demand_ForecastHeader]
			   ([Id_Demand_ForecastHeader]
			   ,[Id_Style_Customer]
			   ,[Id_Demand_Cycle]
			   ,[CustomerForecastDate]
			   ,[Status]
			   ,[Id_User]
			   ,[Comments])
		 VALUES
			   (@Id_Demand_ForecastHeader
			   ,@Id_Style_Customer
			   ,@Id_Demand_Cycle
			   ,@CustomerForecastDate
			   ,@Status
			   ,@Id_User
			   ,@Comments)
END
GO
