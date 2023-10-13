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
            Password VARCHAR(150) NOT NULL,
            FullName VARCHAR(50)
        );
        GO

        CREATE TABLE Collector (
            ID INT IDENTITY(1, 1) PRIMARY KEY,
            UUID VARCHAR(40) UNIQUE,
            Username VARCHAR(50) NOT NULL,
            Password VARCHAR(150) NOT NULL,
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
            Street VARCHAR(100),
            HouseNumber INT, 
            Municipality VARCHAR(100),
            Suburb VARCHAR(100),
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

--INSERT INTO Manager (UUID,Username,Password,Fullname) VALUES
--	('1','manager','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f','Jaime López');
--  GO

--INSERT INTO Collector (UUID,Username,Password,ManagerID,Fullname) VALUES
--    ('1','collector1','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,'Manuel Gutiérrez'),
--    ('2','collector2','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,'Rogelio Reyes'),
--    ('3','collector3','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,'Jonathan Smith'),
--    ('4','collector4','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,'Enrique García'),
--    ('5','collector5','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,'Adrian Cantú'),
--    ('6','collector6','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,'Efraín Martínez'),
--    ('7','collector7','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,'Rodrigo Vizcaino');
--  GO

--INSERT INTO Ticket (UUID,ManagerID,CollectorID,HousingReference,Street, HouseNumber, Municipality, Suburb, ReceiptComments,ReprogrammationComments,HousePhoneNumber,Cellphone,State,TicketDate,CollectorComments,DonationAmount,DonorName) VALUES
--    ('1',1,1,'Casa Roja', 'Garza Sada', 11, 'Monterrey', 'Tecnológico', 'Venir antes de las 2pm','','6731479311','6741479311','PENDING','2016-10-25','',200,'Jaime López'),
--    ('2',1,1,'Casa es una esquina', 'Independencia', 12, 'Monterrey', 'Tecnológico', 'Tocar fuerte','','6731479311','6741479311','PENDING','2016-10-25','',500,'Abner Martínez'),
--    ('3',1,1,'Casa Azul', 'Garza Sada', 11, 'Monterrey', 'Tecnológico', 'Ser puntuales','','6731479311','6741479311','PENDING','2016-10-25','',800,'Adrián García'),
--    ('4',1,1,'Casa Blanca', 'Independencia', 12, 'Monterrey', 'Tecnológico', 'El perro es bravo','','6731479311','6741479311','PENDING','2016-10-25','',1200,'Alan Sánchez'),
--    ('5',1,1,'Casa Menta', 'Garza Sada', 11, 'Monterrey', 'Tecnológico', 'Recoge la esposa','','6731479311','6741479311','PENDING','2016-10-25','',600,'Alberto Pérez'),
    --    ('6',1,2,'Casa Roja', 'Garza Sada', 11, 'Monterrey', 'Tecnológico', 'Venir antes de las 2pm','','6731479311','6741479311','PENDING','2016-10-25','',200,'Jaime López'),
    --    ('7',1,2,'Casa es una esquina', 'Independencia', 12, 'Monterrey', 'Tecnológico', 'Tocar fuerte','','6731479311','6741479311','PENDING','2016-10-25','',500,'Abner Martínez'),
    --    ('8',1,2,'Casa Azul', 'Garza Sada', 11, 'Monterrey', 'Tecnológico', 'Ser puntuales','','6731479311','6741479311','PENDING','2016-10-25','',800,'Adrián García'),
    --    ('9',1,2,'Casa Blanca', 'Independencia', 12, 'Monterrey', 'Tecnológico', 'El perro es bravo','','6731479311','6741479311','PENDING','2016-10-25','',1200,'Alan Sánchez'),
--    ('10',1,3,'Casa Roja', 'Garza Sada', 11, 'Monterrey', 'Tecnológico', 'Venir antes de las 2pm','','6731479311','6741479311','PENDING','2016-10-25','',200,'Jaime López'),
--    ('11',1,4,'Casa es una esquina', 'Independencia', 12, 'Monterrey', 'Tecnológico', 'Tocar fuerte','','6731479311','6741479311','PENDING','2016-10-25','',500,'Abner Martínez'),
--    ('12',1,5,'Casa Azul', 'Garza Sada', 11, 'Monterrey', 'Tecnológico', 'Ser puntuales','','6731479311','6741479311','PENDING','2016-10-25','',800,'Adrián García');
--  GO