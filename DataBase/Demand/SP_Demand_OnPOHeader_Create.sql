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
-- Author:		<Author, Miguel De Jesus Carcamo Torres>
-- Create date: <Create Date, 3/15/2023>
-- Description:	<Description,>
-- =============================================
CREATE PROCEDURE SP_Demand_OnPOHeader_Create
	-- Add the parameters for the stored procedure here
	@IDPlant int,
	@Id_Demand_Cycle int,
	@LastDateBuy date,
	@CreateDate datetime,
	@Status int,
	@Id_User int,
	@Comments varchar(350)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	DECLARE @ID_Demand_OnPOHeader int
	SELECT @ID_Demand_OnPOHeader = ISNULL(MAX(ID_Demand_OnPOHeader),0) + 1 FROM [Demand_OnPOHeader]
    -- Insert statements for procedure here
	INSERT INTO [dbo].[Demand_OnPOHeader]
           ([ID_Demand_OnPOHeader]
           ,[IDPlant]
           ,[Id_Demand_Cycle]
           ,[LastDateBuy]
           ,[Status]
           ,[Id_User]
           ,[Comments])
     VALUES
           (@ID_Demand_OnPOHeader
		   ,@IDPlant
		   ,@Id_Demand_Cycle
		   ,@LastDateBuy
		   ,@Status
		   ,@Id_User
		   ,@Comments)
END
GO
