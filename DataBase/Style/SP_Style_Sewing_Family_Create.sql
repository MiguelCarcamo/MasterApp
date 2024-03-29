USE [SUPPLYPLANNING_test]
GO
/****** Object:  StoredProcedure [dbo].[SP_Style_WorkCenter_Create]    Script Date: 2/13/2023 11:13:31 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,Miguel De Jesus Carcamo>
-- Create date: <Create Date, 02/09/2023>
-- Description:	<Description, Creacion de WorkCenter>
-- =============================================
CREATE PROCEDURE [dbo].[SP_Style_Sewing_Family_Create]
	-- Add the parameters for the stored procedure here
	 @Id_Style_WorkCenter int
	,@Style_Family varchar(50)
	,@UserUpdate int
	,@Comments varchar(550)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	Declare @Id_Style_Family int

    -- Insert statements for procedure here
	select @Id_Style_Family =  isnull(max([Id_Style_Family]),0) + 1 from Style_Sewing_Family
	INSERT INTO [dbo].[Style_Sewing_Family]
			   ([Id_Style_Family]
			   ,[Id_Style_WorkCenter]
			   ,[Style_Family]
			   ,[LastUpdateDate]
			   ,[UserUpdate]
			   ,[Comments])
		 VALUES
			   (@Id_Style_Family
			   ,@Id_Style_WorkCenter
			   ,@Style_Family
			   ,GETDATE()
			   ,@UserUpdate
			   ,@Comments)
END
