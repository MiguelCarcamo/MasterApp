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
-- Create date: <Create Date, 2/15/2022>
-- Description:	<Description,>
-- =============================================
ALTER PROCEDURE SP_Style_GeneralInfo_Action
	-- Add the parameters for the stored procedure here
	 @Id_Style_GeneralInfo int
	,@Id_Style_WorkCenter int
	,@StyleName varchar(150)
	,@UserUpdate int
	,@TypeStyle int
	,@LeadTime_days int
	,@WorkFlow varchar(550)
	,@Comments varchar(550)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	declare @StyleName_ varchar(150)
	declare @TypeStyle_ int
	declare @LeadTime_days_ int
	declare @WorkFlow_ varchar(550)
	declare @Comments_ varchar(550)
	BEGIN TRY
		IF (@Id_Style_GeneralInfo = 0 AND (select count(*) from Style_GeneralInfo where StyleName = @StyleName) = 0)
		BEGIN
			EXECUTE SP_Style_GeneralInfo_Create  @Id_Style_WorkCenter, @StyleName, @UserUpdate, @TypeStyle, @LeadTime_days, @WorkFlow, @Comments
		END
		ELSE
		BEGIN
			SELECT @StyleName_ = StyleName, @TypeStyle_ = TypeStyle, @LeadTime_days_ = LeadTime_days, @WorkFlow_ = WorkFlow, @Comments_ = Comments 
			FROM Style_GeneralInfo WHERE Id_Style_GeneralInfo = @Id_Style_GeneralInfo
			IF(@StyleName <> @StyleName_ OR @TypeStyle <> @TypeStyle_ OR @LeadTime_days <> @LeadTime_days_ OR @WorkFlow <> @WorkFlow_ OR @Comments <> @Comments_)
			BEGIN
				EXECUTE SP_Style_GeneralInfo_Update @Id_Style_GeneralInfo, @Id_Style_WorkCenter, @StyleName, @UserUpdate, @TypeStyle, @LeadTime_days, @WorkFlow, @Comments
			END
		END
	END TRY
	BEGIN CATCH
	END CATCH
END
GO
