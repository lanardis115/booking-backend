// -----------QUI NON USIAMO SQLite--------------

import express from 'express';
const app = express();
app.use(express.json());

// Database temporaneo in memoria
let prenotazioni = [
    { id: 1, nome: "Mario Rossi", data: "2026-07-15", stanza: "101" },
    { id: 2, nome: "Luigi Bianchi", data: "2026-07-16", stanza: "102" }
];

// 1. GET - Recupera tutte le prenotazioni
app.get('/api/prenotazioni', (req, res) => {
    res.json(prenotazioni);
});

// 2. POST - Crea una nuova prenotazione
app.post('/api/prenotazioni', (req, res) => {
    const nuovaPrenotazioni = {
        id: prenotazioni.length + 1,
        ...req.body
    };
    prenotazioni.push(nuovaPrenotazioni);
    res.status(201).json(nuovaPrenotazioni);
});

app.listen(3001, () => {
    console.log("🚀 Server di test attivo sulla porta 3001");
});