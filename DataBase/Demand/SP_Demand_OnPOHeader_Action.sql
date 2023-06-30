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
-- Create date: <Create Date, 3/15/2023>
-- Description:	<Description,>
-- =============================================
CREATE PROCEDURE SP_Demand_OnPOHeader_Action
	-- Add the parameters for the stored procedure here
	@ID_Demand_OnPOHeader int,
	@IDPlant int,
	@Id_Demand_Cycle int,
	@LastDateBuy date,
	@Status int,
	@Id_User int,
	@Comments varchar(350)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	IF(@ID_Demand_OnPOHeader = 0)
	BEGIN
		EXECUTE SP_Demand_OnPOHeader_Create @IDPlant, @Id_Demand_Cycle, @LastDateBuy, @Status, @Id_User, @Comments
	END
	ELSE
	BEGIN
		EXECUTE SP_Demand_OnPOHeader_Update @ID_Demand_OnPOHeader, @IDPlant, @Id_Demand_Cycle, @LastDateBuy, @Status, @Id_User, @Comments
	END
END
GO
