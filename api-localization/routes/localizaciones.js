const express = require("express");
const { Localizacion, Disponibilidad } = require("../models/localizacion");
const router = express.Router();

// Obtenemos todas las localizaciones
router.get("/", async (req, res) => {
  try {
    const localizaciones = await Localizacion.find();
    res.json(localizaciones);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
});

// Agregamos una nueva localización
router.post("/", async (req, res) => {
  const localizacion = new Localizacion({
    nombre: req.body.nombre,
    direccion: req.body.direccion,
  });

  try {
    const nuevaLocalizacion = await localizacion.save();
    res.status(201).json(nuevaLocalizacion);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

// Agregamos la disponibilidad de libros
router.post("/disponibilidad", async (req, res) => {
  const disponibilidad = new Disponibilidad({
    libro_id: req.body.libro_id,
    localizacion_id: req.body.localizacion_id,
    cantidad: req.body.cantidad,
  });

  try {
    const nuevaDisponibilidad = await disponibilidad.save();
    res.status(201).json(nuevaDisponibilidad);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
});

module.exports = router;
