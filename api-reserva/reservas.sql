CREATE TABLE Reservas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  cliente_id INT,
  libro_id INT,
  fecha_reserva DATE,
  estado VARCHAR(50),
  FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
  FOREIGN KEY (libro_id) REFERENCES Libros(id)
);
