Create database DB_Prueba;

USE DB_Prueba;

CREATE TABLE Manager (
    ID INT IDENTITY(1, 1) PRIMARY KEY,
    UUID VARCHAR(40) UNIQUE,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(150) NOT NULL,
    FullName VARCHAR(50)
);

CREATE TABLE Collector (
    ID INT IDENTITY(1, 1) PRIMARY KEY,
    UUID VARCHAR(40) UNIQUE,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(150) NOT NULL,
    ManagerID INT,
    Fullname VARCHAR(50),
    CollectorZone VARCHAR(50),
    FOREIGN KEY (ManagerID) REFERENCES Manager(ID)
);

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

INSERT INTO Manager (UUID,Username,Password,Fullname) VALUES
	  ('1','manager','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f','Jaime López');
 
 INSERT INTO Collector (UUID,Username,Password,ManagerID,Fullname, CollectorZone) VALUES
	  ('1','collector1','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,'Manuel Gutiérrez', 'Monterrey'),
      ('2','collector2','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,'Rogelio Reyes', 'Guadalupe'),
	  ('3','collector3','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,'Jonathan Smith', 'Apodaca'),
	  ('4','collector4','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,'Enrique García', 'San Pedro'),
	  ('5','collector5','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,'Adrian Cantú', 'Santa Catarina'),
	  ('6','collector6','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,'Efraín Martínez', 'San Nicolás'),
      ('7','collector7','bf2121ff91f6981ec3563732c5449209d504b6036a4d924e71dd4262d4eb770554f1641a20d72cf3b02cc8e914fc1ec36ef8a36b9e4092db0340b664cee6648f',1,'Rodrigo Vizcaino', 'Cumbres');
 
 INSERT INTO Ticket (UUID,ManagerID,CollectorID,HousingReference,Street, HouseNumber, Municipality, Suburb, ReceiptComments,ReprogrammationComments,HousePhoneNumber,Cellphone,State,TicketDate,CollectorComments,DonationAmount,DonorName) VALUES
	  ('1111',1,1,'Casa Roja', 'Av. Junco de la Vega', 12, 'Monterrey', 'Altavista', 'Venir antes de las 2pm','','6731479311','6741479311','PENDING','2016-10-25','',200,'Jaime López'),
	  ('2222',1,1,'Casa es una esquina', 'Pedregal de la Bahia', 6700, 'Monterrey', 'Predio Creplan', 'Tocar fuerte','','6731479311','6741479311','PENDING','2016-10-25','',500,'Abner Martínez'),
	  ('3333',1,1,'Casa Azul', 'Valle de Mexico', 4307, 'Monterrey', 'Ejidal Los Remates', 'Ser puntuales','','6731479311','6741479311','PENDING','2016-10-25','',800,'Adrián García'),
	  ('4444',1,1,'Casa Blanca', 'Los Angeles', 2305, 'Monterrey', 'Sierra Ventana', 'El perro es bravo','','6731479311','6741479311','PENDING','2016-10-25','',1200,'Alan Sánchez'),
	  ('5555',1,1,'Casa Menta', 'Rotterdam', 5212, 'Monterrey', 'Las Torres', 'Recoge la esposa','','6731479311','6741479311','PENDING','2016-10-25','',600,'Alberto Pérez'),
		  ('6666',1,2,'Casa Roja', 'Juan Perez', 833, 'Monterrey', 'Independencia', 'Venir antes de las 2pm','','6731479311','6741479311','PENDING','2016-10-25','',200,'Jaime López'),
		  ('7777',1,2,'Casa es una esquina', 'Yucatan', 1005, 'Monterrey', 'Independencia', 'Tocar fuerte','','6731479311','6741479311','PENDING','2016-10-25','',500,'Abner Martínez'),
		  ('8888',1,2,'Casa Azul', 'Vicente Suarez', 303, 'Monterrey', 'Obrera', 'Ser puntuales','','6731479311','6741479311','PENDING','2016-10-25','',800,'Adrián García'),
		  ('9999',1,2,'Casa Blanca', 'Albino Espinosa', 221, 'Monterrey', 'Centro', 'El perro es bravo','','6731479311','6741479311','PENDING','2016-10-25','',1200,'Alan Sánchez'),
	  ('1010',1,3,'Casa Roja', 'Ruperto Martínez', 1200, 'Monterrey', 'Centro', 'Venir antes de las 2pm','','6731479311','6741479311','PENDING','2016-10-25','',200,'Jaime López'),
	  ('1111111',1,4,'Casa es una esquina', 'Ruperto Martínez', 1200, 'Monterrey', 'Centro', 'Tocar fuerte','','6731479311','6741479311','PENDING','2016-10-25','',500,'Abner Martínez'),
	  ('121212',1,5,'Casa Azul', 'Ruperto Martínez', 1200, 'Monterrey', 'Centro', 'Ser puntuales','','6731479311','6741479311','PENDING','2016-10-25','',800,'Adrián García');
 