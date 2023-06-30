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
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
alter PROCEDURE SP_Demand_Cycle_Update
	-- Add the parameters for the stored procedure here
	@Id_Demand_Cycle int,
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
	UPDATE [dbo].[Demand_Cycle]
	   SET [Name] = @Name
		  ,[Status] = @Status
		  ,[Id_User] = @Id_User
		  ,[StartDate] = @StartDate
		  ,[EndDate] = @EndDate
		  ,[Comments] = @Comments
	 WHERE [Id_Demand_Cycle] = @Id_Demand_Cycle
END
GO
