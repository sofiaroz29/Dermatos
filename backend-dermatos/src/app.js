import express from "express";
import morgan from "morgan";
import multer from "multer";
import dotenv from 'dotenv';
import cors from 'cors';
dotenv.config()

const app = express();

app.use(cors({
    origin: 'http://localhost:5500',
    credentials: true
}));

app.use('/Images', express.static('./Images'))

import usuarioRoutes from "../routes/usuario.routes.js";
import reporteRoutes from "../routes/reporte.routes.js";


app.use(morgan("dev"));
app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.set('port', process.env.PORT || 3000);

app.use("/api/usuario", usuarioRoutes);
app.use ("/api", reporteRoutes);

app.use ("/images", express.static ("./images"));

export default app; 