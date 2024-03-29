USE [SUPPLYPLANNING_test]
GO
/****** Object:  StoredProcedure [dbo].[SP_Style_Sewing_Create]    Script Date: 2/13/2023 1:09:06 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,Miguel De Jesus Carcamo>
-- Create date: <Create Date, 02/09/2023>
-- Description:	<Description, Creacion de Customers>
-- =============================================
CREATE PROCEDURE [dbo].[SP_Style_Sewing_LayoutConfiguration_Create]
	-- Add the parameters for the stored procedure here
	 @Id_Style_Family int
	,@LayoutConfiguration varchar(50)
	,@UserUpdate int
	,@Comments varchar(550)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	Declare @Id_Style_LayoutConfiguration int

    -- Insert statements for procedure here
	select @Id_Style_LayoutConfiguration =  isnull(max([Id_Style_LayoutConfiguration]),0) + 1 from [Style_Sewing_LayoutConfiguration]
	INSERT INTO [dbo].[Style_Sewing_LayoutConfiguration]
			   ([Id_Style_LayoutConfiguration]
			   ,[Id_Style_Family]
			   ,[LayoutConfiguration]
			   ,[LastUpdateDate]
			   ,[UserUpdate]
			   ,[Comments])
		 VALUES
			   (@Id_Style_LayoutConfiguration
			   ,@Id_Style_Family
			   ,@LayoutConfiguration
			   ,GETDATE()
			   ,@UserUpdate
			   ,@Comments)
END
