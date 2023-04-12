USE [Combine]
GO

/****** Object:  Table [dbo].[Options_API]    Script Date: 08-Apr-2023 6:34:03 pm ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Options_API](
	[volume] [decimal](8, 4) NULL,
	[btc_price] [nchar](10) NULL,
	[open_interest] [nchar](10) NULL,
	[mark_price] [nchar](10) NULL,
	[instrument_name] [nchar](40) NULL,
	[date1] [date] NULL,
	[time1] [time](7) NULL
) ON [PRIMARY]
GO

CREATE DATABASE [Combine]
GO

CREATE TABLE [dbo].[Options_API]([volume] [decimal](8, 4) NULL,	[btc_price] [nchar](10) NULL, [open_interest] [nchar](10) NULL, [mark_price] [nchar](10) NULL, [instrument_name] [nchar](40) NULL, [date1] [date] NULL, [time1] [time](7) NULL) ON [PRIMARY]


/opt/mssql-tools/bin/sqlcmd -S sql-server-db -U sa -P MyPassword123!      

SELECT * FROM [dbo].[Options_API];