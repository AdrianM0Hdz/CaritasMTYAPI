CREATE TABLE Manager (
    ID INT IDENTITY(1, 1) PRIMARY KEY,
    UUID VARCHAR(40) UNIQUE,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(150) NOT NULL
);

CREATE TABLE Collector (
    ID INT IDENTITY(1, 1) PRIMARY KEY,
    UUID VARCHAR(40) UNIQUE,
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(100) NOT NULL,
    ManagerID VARCHAR(40),
    Fullname VARCHAR(50),
    FOREIGN KEY (ManagerID) REFERENCES Manager(ID)
);

CREATE TABLE Ticket (
    ID INT IDENTITY(1, 1) PRIMARY KEY,
    UUID VARCHAR(40) UNIQUE,
    ManagerID VARCHAR(40),
    CollectorID VARCHAR(40),
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