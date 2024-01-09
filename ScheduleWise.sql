-- Crear la base de datos
DROP database schedulewise;
CREATE DATABASE IF NOT EXISTS schedulewise;
USE schedulewise;

-- Crear la tabla User
CREATE TABLE IF NOT EXISTS User (
    email VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255),
    firstName VARCHAR(255),
    lastName VARCHAR(255)
);

-- Crear la tabla Horary
CREATE TABLE IF NOT EXISTS Horary (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    description TEXT,
    userfk VARCHAR(255),
    FOREIGN KEY (userfk) REFERENCES User(email)
);

-- Crear la tabla Hour
CREATE TABLE IF NOT EXISTS Hour (
    id INT PRIMARY KEY AUTO_INCREMENT,
    startDate DATETIME,
    finalDate DATETIME,
    title VARCHAR(255),
    description TEXT,
    horaryfk INT,
    FOREIGN KEY (horaryfk) REFERENCES Horary(id)
);

-- Crear la tabla Integrant
CREATE TABLE IF NOT EXISTS Integrant (
    id INT PRIMARY KEY AUTO_INCREMENT,
    userfk VARCHAR(255),
    description TEXT,
    horaryfk INT,
    FOREIGN KEY (userfk) REFERENCES User(email),
    FOREIGN KEY (horaryfk) REFERENCES Horary(id)
);

-- Insertar datos de ejemplo en la tabla User
INSERT INTO User (email, password, firstName, lastName)
VALUES
    ('usuario1@example.com', 'contraseña1', 'Juan', 'Pérez'),
    ('usuario2@example.com', 'contraseña2', 'María', 'López'),
    ('usuario3@example.com', 'contraseña1', 'Manuel', 'Domingo'),
    ('usuario4@example.com', 'contraseña2', 'Lucas', 'López');

-- Insertar datos de ejemplo en la tabla Horary
INSERT INTO Horary (id, title, description, userfk)
VALUES
    ('Horario 1', 'Descripción del horario 1', 'usuario1@example.com'),
    ('Horario 2', 'Descripción del horario 2', 'usuario2@example.com'),
    ('Horario 3', 'Descripción del horario 3', 'usuario1@example.com'),
    ('Horario 4', 'Descripción del horario 4', 'usuario1@example.com');

-- Insertar datos de ejemplo en la tabla Hour
INSERT INTO Hour (startDate, finalDate, title, description, horaryfk)
VALUES
    ('2023-01-01 08:00:00', '2023-01-01 12:00:00', 'Clase 1', 'Descripción de la clase 1', 1),
    ('2023-01-02 14:00:00', '2023-01-02 17:00:00', 'Clase 2', 'Descripción de la clase 2', 2),
    ('2023-01-04 09:00:00', '2023-01-04 15:00:00', 'Clase 3', 'Descripción de la clase 3', 3),
    ('2023-01-05 18:00:00', '2023-01-05 19:00:00', 'Clase 4', 'Descripción de la clase 4', 4);

-- Insertar datos de ejemplo en la tabla Integrant
INSERT INTO Integrant (userfk, horaryfk, description)
VALUES
    ('usuario1@example.com', '1',''),
    ('usuario3@example.com', '1',''),
    ('usuario4@example.com', '1',''),
    
    ('usuario2@example.com', '2',''),
    ('usuario1@example.com', '2',''),
    
    ('usuario1@example.com', '3',''),
    ('usuario2@example.com', '3',''),
    ('usuario3@example.com', '3','');