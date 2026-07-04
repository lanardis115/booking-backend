import express from 'express';
import Database from 'better-sqlite3';

const app = express();
app.use(express.json());

// 1. Connessione al database reale (creerà un file chiamato hotel.db)
const db = new Database('hotel.db');

// 2. Creazione della tabella in SQL puro
db.prepare(`
    CREATE TABLE IF NOT EXISTS prenotazioni (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        data TEXT,
        stanza TEXT
    )
`).run();

// Inseriamo due dati di prova se la tabella è completamente vuota
const controllo = db.prepare("SELECT COUNT(*) as totale FROM prenotazioni").get();
if (controllo.totale === 0) {
    const inserisciIniziale = db.prepare("INSERT INTO prenotazioni (nome, data, stanza) VALUES (?, ?, ?)");
    inserisciIniziale.run("Mario Rossi", "2026-07-15", "101");
    inserisciIniziale.run("Luigi Bianchi", "2026-07-16", "102");
}

// -----------------------------------------------------------------
// LE API REST CHE PARLANO IN SQL
// -----------------------------------------------------------------

// GET - Recupera tutte le prenotazioni con un SELECT
app.get('/api/prenotazioni', (req, res) => {
    const query = db.prepare("SELECT * FROM prenotazioni");
    const listaPrenotazioni = query.all(); // .all() prende tutte le righe della tabella
    res.json(listaPrenotazioni);
});

// POST - Inserisce una nuova prenotazione con un INSERT INTO
app.post('/api/prenotazioni', (req, res) => {
    const { nome, data, stanza } = req.body; // Estraiamo i dati da Postman
    
    // Prepariamo l'INSERT usando i "?" per evitare problemi di sicurezza (SQL Injection)
    const query = db.prepare("INSERT INTO prenotazioni (nome, data, stanza) VALUES (?, ?, ?)");
    const risultato = query.run(nome, data, stanza); // Eseguiamo l'inserimento sul DB
    
    // Rispondiamo inviando l'oggetto creato con il suo VERO ID incrementato dal database
    res.status(201).json({
        id: risultato.lastInsertRowid, // Recupera l'ultimo ID generato automaticamente
        nome,
        data,
        stanza
    });
});

app.listen(3001, () => {
    console.log("🚀 Server con VERO Database SQL attivo sulla porta 3001");
});