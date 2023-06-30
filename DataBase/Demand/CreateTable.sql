USE [SUPPLYPLANNING_test]
GO

/****** Object:  Table [dbo].[Demand_Cycle]    Script Date: 3/3/2023 11:40:31 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Demand_Cycle](
	[Id_Demand_Cycle] [int] NOT NULL,
	[Name] [varchar](100) NULL,
	[CreateDate] [datetime] NULL,
	[Status] [int] NULL,
	[StartDate] [date] NULL,
	[EndDate] [date] NULL,
	[Comments] [varchar](350) NULL,
 CONSTRAINT [PK_Demand_Cycle] PRIMARY KEY CLUSTERED 
(
	[Id_Demand_Cycle] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Demand_Cycle] ADD  CONSTRAINT [DF_Demand_Cycle_CreateDate]  DEFAULT (getdate()) FOR [CreateDate]
GO


CREATE TABLE [dbo].[Demand_ForecastHeader](
	[Id_Demand_ForecastHeader] [int] NOT NULL,
	[Id_Style_Customer] [int] NULL,
	[Id_Demand_Cycle] [int] NULL,
	[CustomerForecastDate] [date] NULL,
	[CreateDate] [datetime] NULL,
	[Status] [int] NULL,
	[Comments] [varchar](350) NULL,
 CONSTRAINT [PK_Demand_ForecastHeader] PRIMARY KEY CLUSTERED 
(
	[Id_Demand_ForecastHeader] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Demand_ForecastHeader] ADD  CONSTRAINT [DF_Demand_ForecastHeader_CreateDate]  DEFAULT (getdate()) FOR [CreateDate]
GO

ALTER TABLE [dbo].[Demand_ForecastHeader]  WITH CHECK ADD  CONSTRAINT [FK_Demand_ForecastHeader_Demand_Cycle] FOREIGN KEY([Id_Demand_Cycle])
REFERENCES [dbo].[Demand_Cycle] ([Id_Demand_Cycle])
GO

ALTER TABLE [dbo].[Demand_ForecastHeader] CHECK CONSTRAINT [FK_Demand_ForecastHeader_Demand_Cycle]
GO

ALTER TABLE [dbo].[Demand_ForecastHeader]  WITH CHECK ADD  CONSTRAINT [FK_Demand_ForecastHeader_Style_Customer] FOREIGN KEY([Id_Style_Customer])
REFERENCES [dbo].[Style_Customer] ([Id_Style_Customer])
GO

ALTER TABLE [dbo].[Demand_ForecastHeader] CHECK CONSTRAINT [FK_Demand_ForecastHeader_Style_Customer]
GO

CREATE TABLE [dbo].[Demand_ForecastDetail](
	[Id_Demand_ForecastDetail] [int] NOT NULL,
	[Id_Demand_ForecastHeader] [int] NULL,
	[Country] [varchar](50) NULL,
	[StyleNumber] [varchar](150) NULL,
	[StyleSeason] [varchar](100) NULL,
	[StyleGender] [nchar](10) NULL,
	[ProductDescription] [varchar](350) NULL,
	[IDPlant] [int] NULL,
	[ProductType] [varchar](150) NULL,
	[CustomerCategory] [varchar](150) NULL,
	[BuyDateTentative] [date] NULL,
	[CustomerPromisedDate] [date] NULL,
	[CustumerLeadTime] [int] NULL,
	[QuantityRequested] [int] NULL,
 CONSTRAINT [PK_Demand_ForecastDetail] PRIMARY KEY CLUSTERED 
(
	[Id_Demand_ForecastDetail] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Demand_ForecastDetail]  WITH CHECK ADD  CONSTRAINT [FK_Demand_ForecastDetail_Demand_ForecastHeader] FOREIGN KEY([Id_Demand_ForecastHeader])
REFERENCES [dbo].[Demand_ForecastHeader] ([Id_Demand_ForecastHeader])
GO

ALTER TABLE [dbo].[Demand_ForecastDetail] CHECK CONSTRAINT [FK_Demand_ForecastDetail_Demand_ForecastHeader]
GO

ALTER TABLE [dbo].[Demand_ForecastDetail]  WITH CHECK ADD  CONSTRAINT [FK_Demand_ForecastDetail_General_Plant] FOREIGN KEY([IDPlant])
REFERENCES [dbo].[General_Plant] ([IDPlant])
GO

ALTER TABLE [dbo].[Demand_ForecastDetail] CHECK CONSTRAINT [FK_Demand_ForecastDetail_General_Plant]
GO
