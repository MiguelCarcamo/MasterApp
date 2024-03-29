USE [SUPPLYPLANNING_test]
GO
/****** Object:  StoredProcedure [dbo].[SP_Style_Sewing_Update]    Script Date: 2/13/2023 1:09:09 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,Miguel De Jesus Carcamo>
-- Create date: <Create Date, 02/09/2023>
-- Description:	<Description, Actualizacion de Customers>
-- =============================================
CREATE PROCEDURE [dbo].[SP_Style_Sewing_LayoutConfiguration_Update]
	-- Add the parameters for the stored procedure here
	 @Id_Style_LayoutConfiguration int
	,@Id_Style_Family int
	,@LayoutConfiguration varchar(50)
	,@UserUpdate int
	,@Comments varchar(550)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	
	UPDATE [dbo].[Style_Sewing_LayoutConfiguration]
	   SET [Id_Style_Family] = @Id_Style_Family
		  ,[LayoutConfiguration] = @LayoutConfiguration
		  ,[LastUpdateDate] = GETDATE()
		  ,[UserUpdate] = @UserUpdate
		  ,[Comments] = @Comments
	 WHERE [Id_Style_LayoutConfiguration] = @Id_Style_LayoutConfiguration
END
