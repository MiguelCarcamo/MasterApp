USE [SUPPLYPLANNING_test]
GO
/****** Object:  StoredProcedure [dbo].[SP_Style_WorkCenter_Update]    Script Date: 2/13/2023 11:13:33 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,Miguel De Jesus Carcamo>
-- Create date: <Create Date, 02/09/2023>
-- Description:	<Description, Actualizacion de WorkCenter>
-- =============================================
CREATE PROCEDURE [dbo].[SP_Style_Sewing_Family_Update]
	-- Add the parameters for the stored procedure here
	 @Id_Style_Family int
	,@Id_Style_WorkCenter int
	,@Style_Family varchar(50)
	,@UserUpdate int
	,@Comments varchar(550)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	UPDATE [dbo].[Style_Sewing_Family]
	   SET [Id_Style_WorkCenter] = @Id_Style_WorkCenter
		  ,[Style_Family] = @Style_Family
		  ,[LastUpdateDate] = GETDATE()
		  ,[UserUpdate] = @UserUpdate
		  ,[Comments] = @Comments
	 WHERE [Id_Style_Family] = @Id_Style_Family

END
