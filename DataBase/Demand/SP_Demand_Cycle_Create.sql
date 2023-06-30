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
-- Create date: <Create Date, 3/7/2023>
-- Description:	<Description, >
-- =============================================
ALTER PROCEDURE SP_Demand_Cycle_Create
	-- Add the parameters for the stored procedure here
	@Name varchar(100),
	@Status int,
	@Id_User int,
	@StartDate date,
	@EndDate date,
	@Comments varchar(350)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	INSERT INTO [dbo].[Demand_Cycle]
			   ([Id_Demand_Cycle]
			   ,[Name]
			   ,[Status]
			   ,[Id_User]
			   ,[StartDate]
			   ,[EndDate]
			   ,[Comments])
		 VALUES
			   ((SELECT ISNULL(MAX([Id_Demand_Cycle]),0) + 1 FROM Demand_Cycle)
			   ,@Name
			   ,@Status
			   ,@Id_User
			   ,@StartDate
			   ,@EndDate
			   ,@Comments)
END
GO
