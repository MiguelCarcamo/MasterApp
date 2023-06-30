
--drop table Style_Sewing_LayoutConfiguration
--drop table Style_Sewing_Family
--drop table Style_Sewing
--drop table Style_GeneralInfo
--drop table Style_WorkCenter
----drop table Style_ProductType
--drop table Style_GlobalCategory2
--drop table Style_Customer
CREATE TABLE Style_Customer(
	Id_Style_Customer int Primary key,
	Style_Customer varchar(150),
	LastUpdateDate datetime,
	UserUpdate int,
	Comments varchar(550)
)

CREATE TABLE Style_GlobalCategory2(
	Id_Style_GlobalCategory int Primary Key,
	Id_Style_Customer int,
	GlobalCategory varchar(150),
	LastUpdateDate datetime,
	UserUpdate int,
	Comments varchar(550),
	CONSTRAINT fk_Style_Customer_GlobalCategory FOREIGN KEY (Id_Style_Customer) REFERENCES Style_Customer (Id_Style_Customer)
)
--CREATE TABLE Style_ProductType(
--	Id_Style_ProductType int Primary Key,
--	Id_Style_GlobalCategory int,
--	CategoryRamp varchar(150),
--	CreateDate datetime default GETDATE(),
--	UserCreate int,
--	Comments varchar(550),
--	CONSTRAINT fk_Style_GlobalCategory_ProductType FOREIGN KEY (Id_Style_GlobalCategory) REFERENCES Style_GlobalCategory2 (Id_Style_GlobalCategory)
--)
CREATE TABLE Style_WorkCenter(
	Id_Style_WorkCenter int Primary Key,
	Id_Style_ProductType int,
	Style_WorkCenter varchar(150),
	LastUpdateDate datetime,
	UserUpdate int,
	Comments varchar(550),
	CONSTRAINT fk_Style_GlobalCategory_WorkCenter FOREIGN KEY (Id_Style_ProductType) REFERENCES Style_GlobalCategory2 (Id_Style_GlobalCategory)
)
CREATE TABLE Style_GeneralInfo(
	Id_Style_GeneralInfo int Primary Key,
	Id_Style_WorkCenter int,
	StyleName varchar(150),
	LastUpdateDate datetime,
	UserUpdate int,
	TypeStyle int,--1 Verified, 2 Forecast, 3 Not Verified
	LeadTime_days int,
	WorkFlow varchar(550),
	Comments varchar(550),
	CONSTRAINT fk_Style_WorkCenter_GeneralInfo FOREIGN KEY (Id_Style_WorkCenter) REFERENCES Style_WorkCenter (Id_Style_WorkCenter)
)

--COSTURA
CREATE TABLE Style_Sewing(
	Id_Style_Sewing int Primary Key,
	Id_Style_GeneralInfo int,
	NumOperators int,
	SAM decimal(12,4),
	GOAL int,
	PE decimal(12,4),
	LastUpdateDate datetime,
	UserUpdate int,
	CONSTRAINT fk_Style_GeneralInfo_Style_Sewing FOREIGN KEY (Id_Style_GeneralInfo) REFERENCES Style_GeneralInfo (Id_Style_GeneralInfo)
)
CREATE TABLE Style_Sewing_Family(
	Id_Style_Family int Primary Key,
	Id_Style_WorkCenter int,
	Style_Family varchar(50),
	LastUpdateDate datetime,
	UserUpdate int,
	Comments varchar(550),
	CONSTRAINT fk_Style_WorkCenter_Sewing_Family FOREIGN KEY (Id_Style_WorkCenter) REFERENCES Style_WorkCenter (Id_Style_WorkCenter)
)
CREATE TABLE Style_Sewing_LayoutConfiguration(
	Id_Style_LayoutConfiguration int Primary Key,
	Id_Style_Family int,
	LayoutConfiguration varchar(50),
	LastUpdateDate datetime,
	UserUpdate int,
	Comments varchar(550),
	CONSTRAINT fk_Style_Sewing_LayoutConfiguration_Sewing_Family FOREIGN KEY (Id_Style_Family) REFERENCES Style_Sewing_Family (Id_Style_Family)
)
CREATE TABLE Style_General_Log(
	item int primary key,
	TableName varchar(150),
	ID_TableName int,
	ID_User int,
	ChangeDescription varchar(2500),
	DateChange date default GETDATE()
)

--CUSTOMER SERVICE DATOS
CREATE TABLE Style_CustomerService_ProductType(
	Id_Style_ProductType int Primary key,
	Style_ProductType varchar(150),
	LastUpdateDate datetime,
	UserUpdate int,
	Comments varchar(550)
)
CREATE TABLE Style_CustomerService_Vendor(
	Id_Style_Vendor int Primary key,
	Style_Vendor varchar(150),
	LastUpdateDate datetime,
	UserUpdate int,
	Comments varchar(550)
)
CREATE TABLE Style_CustomerService_LT(
	Id_Style_CustomerService_LT int Primary Key,
	Id_Style_GeneralInfo int,
	Id_Style_ProductType int,
	Id_Style_Vendor int,
	Colorway varchar(50),
	Procurement int,
	Mfg int,
	GIPT int,
	Comments varchar(550),
	LastUpdateDate datetime,
	UserUpdate int,
	CONSTRAINT fk_Style_GeneralInfo_Style_CustomerService_LT FOREIGN KEY (Id_Style_GeneralInfo) REFERENCES Style_GeneralInfo (Id_Style_GeneralInfo),
	CONSTRAINT fk_Style_GeneralInfo_Style_CustomerService_ProductType FOREIGN KEY (Id_Style_ProductType) REFERENCES Style_CustomerService_ProductType (Id_Style_ProductType),
	CONSTRAINT fk_Style_GeneralInfo_Style_CustomerService_Vendor FOREIGN KEY (Id_Style_Vendor) REFERENCES Style_CustomerService_Vendor (Id_Style_Vendor)
)