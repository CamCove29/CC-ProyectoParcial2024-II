const mongoose = require("mongoose");

// Definimos el esquema para ver las localizaciones
const localizacionSchema = new mongoose.Schema({
  nombre: {
    type: String,
    required: true,
  },
  direccion: {
    type: String,
    required: true,
  },
});

// Definimos el esquema para visualizar la disponibilidad
const disponibilidadSchema = new mongoose.Schema({
  libro_id: {
    type: Number,
    required: true,
  },
  localizacion_id: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "Localizacion",
    required: true,
  },
  cantidad: {
    type: Number,
    required: true,
  },
});

const Localizacion = mongoose.model("Localizacion", localizacionSchema);
const Disponibilidad = mongoose.model("Disponibilidad", disponibilidadSchema);

module.exports = { Localizacion, Disponibilidad };
