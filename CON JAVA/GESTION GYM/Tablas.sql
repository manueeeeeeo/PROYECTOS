/*Creamos tabla de Usuarios*/
CREATE TABLE Usuarios (
    id VARCHAR2(50) PRIMARY KEY,
    nombre VARCHAR2(100) NOT NULL,
    email VARCHAR2(100) UNIQUE NOT NULL,
    telefono VARCHAR2(20) NOT NULL
);

/*Creamos tabla de Clientes*/
CREATE TABLE Clientes (
    id VARCHAR2(50) PRIMARY KEY,
    cuenta_banco VARCHAR2(100) NOT NULL,
    FOREIGN KEY (id) REFERENCES Usuarios(id)
);

/*Creamos tabla de Empleados*/
CREATE TABLE Empleados (
    id VARCHAR2(50) PRIMARY KEY,
    puesto VARCHAR2(50) NOT NULL,
    FOREIGN KEY (id) REFERENCES Usuarios(id)
);

/*Creamos tabla de Accesos*/
CREATE TABLE Accesos (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cliente_id VARCHAR2(50) NOT NULL,
    fecha_acceso TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id) ON DELETE CASCADE
);

/*Creamos tabla de Items*/
CREATE TABLE Items (
    id VARCHAR2(50) PRIMARY KEY,
    nombre VARCHAR2(100) NOT NULL,
    precio NUMBER(10, 2) NOT NULL
);

/*Creamos tabla de Clases*/
CREATE TABLE Clases (
    id VARCHAR2(50) PRIMARY KEY,
    nombre VARCHAR2(100) NOT NULL,
    horario VARCHAR2(50) NOT NULL,
    instructor_id VARCHAR2(50) NOT NULL,
    FOREIGN KEY (instructor_id) REFERENCES Empleados(id)
);

/*Creamos tabla de Reservaciones*/
CREATE TABLE Reservaciones (
    id NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    cliente_id VARCHAR2(50) NOT NULL,
    clase_id VARCHAR2(50) NOT NULL,
    fecha_reservacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
    FOREIGN KEY (clase_id) REFERENCES Clases(id)
);

/*Creamos tabla de Turnos*/
CREATE TABLE Turnos (
    id VARCHAR2(50) PRIMARY KEY,
    dia VARCHAR2(50) NOT NULL,
    hora_inicio VARCHAR2(20) NOT NULL,
    hora_fin VARCHAR2(20) NOT NULL,
    empleado_id VARCHAR2(50) NOT NULL,
    FOREIGN KEY (empleado_id) REFERENCES Empleados(id)
);

/*Creamos tabla de Transacciones*/
CREATE TABLE Transacciones (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    cliente_id VARCHAR2(50) NOT NULL,
    empleado_id VARCHAR2(50) NOT NULL,
    item_id VARCHAR2(50) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
    FOREIGN KEY (empleado_id) REFERENCES Empleados(id),
    FOREIGN KEY (item_id) REFERENCES Items(id)
);

COMMIT;

/* INSERCCIONES EN LA TABLA DE ITEMS*/
INSERT INTO ITEMS VALUES('ZPH3', 'Coca-Cola',2.5);
INSERT INTO ITEMS VALUES('NDD9', 'Fanta',2.5);
INSERT INTO ITEMS VALUES('LAP9', 'Toalla',12);
INSERT INTO ITEMS VALUES('VJE0', 'Proteína 1 KG',13.5);
INSERT INTO ITEMS VALUES('AÑJ2', 'Proteína 2 KG',20.99);
INSERT INTO ITEMS VALUES('CJY1', 'Creatina 500 g',14.99);
INSERT INTO ITEMS VALUES('VBN7', 'Straps',5.99);
INSERT INTO ITEMS VALUES('MNY8', 'Guantes',12);
INSERT INTO ITEMS VALUES('FHC9', 'Banda Elastica 15 KG',10.99);
INSERT INTO ITEMS VALUES('HJD8', 'Banda Elastica 30 KG',14.99);
INSERT INTO ITEMS VALUES('CBD2', 'Banda Elastica 45 KG',21.99);

COMMIT;
