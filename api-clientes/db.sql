CREATE TABLE Clientes (
                          id SERIAL PRIMARY KEY,
                          nombre VARCHAR(100) NOT NULL,
                          correo_electronico VARCHAR(100) NOT NULL,
                          telefono VARCHAR(15) NOT NULL
);
