IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'DB_INGRESOS')
    BEGIN
        CREATE DATABASE DB_INGRESOS;
        GO

        USE DB_INGRESOS;
        GO

        CREATE TABLE Manager (
            ID INT IDENTITY(1, 1) PRIMARY KEY,
            UUID VARCHAR(40) UNIQUE,
            Username VARCHAR(50) NOT NULL,
            Password VARCHAR(150) NOT NULL
        );
        GO

        CREATE TABLE Collector (
            ID INT IDENTITY(1, 1) PRIMARY KEY,
            UUID VARCHAR(40) UNIQUE,
            Username VARCHAR(50) NOT NULL,
            Password VARCHAR(100) NOT NULL,
            ManagerID INT,
            Fullname VARCHAR(50),
            FOREIGN KEY (ManagerID) REFERENCES Manager(ID)
        );
        GO

        CREATE TABLE Ticket (
            ID INT IDENTITY(1, 1) PRIMARY KEY,
            UUID VARCHAR(40) UNIQUE,
            ManagerID INT,
            CollectorID INT,
            HousingReference VARCHAR(200),
            ReceiptComments VARCHAR(200),
            ReprogrammationComments VARCHAR(200),
            HousePhoneNumber VARCHAR(20),
            Cellphone VARCHAR(20),
            State VARCHAR(20),
            TicketDate DATE,
            CollectorComments VARCHAR(200),
            DonationAmount INT,
            DonorName VARCHAR(50),
            FOREIGN KEY (ManagerID) REFERENCES Manager(ID),
            FOREIGN KEY (CollectorID) REFERENCES Collector(ID)
        );
        GO
    END;
    GO

-- INSERT INTO Manager (UUID,Username,Password,Fullname) VALUES
	--  (N'1',N'dummy_manager',N'bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',N'dummy perez');
-- GO
-- 
-- INSERT INTO Collector (UUID,Username,Password,ManagerID,Fullname) VALUES
	--  (N'2',N'dummy2',N'bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,N'dummy garcia'),
	--  (N'1',N'dummy',N'bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,N'dummy gonzalez');
-- GO
-- 
-- INSERT INTO Ticket (UUID,ManagerID,CollectorID,HousingReference,ReceiptComments,ReprogrammationComments,HousePhoneNumber,Cellphone,State,TicketDate,CollectorComments,DonationAmount,DonorName) VALUES
	--  (N'1',1,1,N'Casa Roja',N'Venir antes de las 2pm',N'',N'6731479311',N'6741479311',N'PENDING','2016-10-25',N'Si abrio la persona',200,N'donante lopez'),
	--  (N'2',1,1,N'Casa Blanca',N'Recoge la esposa',N'',N'6731479311',N'6741479311',N'PENDING','2016-10-25',N'',500,N'donante a la torre'),
	--  (N'3',1,2,N'Casa Amarilla',N'Tocar fuerte',N'',N'6731479311',N'6741479311',N'PENDING','2016-10-25',N'',1000,N'donante sada'),
	--  (N'4',1,2,N'Casa Azul',N'Pregunte por El Pollo',N'',N'6731479311',N'6741479311',N'PENDING','2016-10-25',N'',800,N'donante gonzalez');
-- GO