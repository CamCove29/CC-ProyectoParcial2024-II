const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const localizacionesRoutes = require("./routes/localizaciones");

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.json());

// Rutas
app.use("/localizaciones", localizacionesRoutes);

// Conexión a MongoDB
mongoose
  .connect("mongodb://localhost/localizacionDB", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("Conectado a MongoDB"))
  .catch((error) => console.error("Error conectando a MongoDB:", error));

app.listen(port, () => {
  console.log(`Servidor corriendo en http://localhost:${port}`);
});
