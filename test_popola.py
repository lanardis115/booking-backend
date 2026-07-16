import datetime
import random
import requests

# L'indirizzo del tuo server Express locale
URL_API = "http://localhost:3001/api/prenotazioni"

# Liste di dati fittizi
NOMI = [
    "Giuseppe Verdi",
    "Francesca Neri",
    "Alessandro Viola",
    "Elena Bianchi",
    "Roberto Bruno",
    "Sofia Esposito",
]
STANZE = ["101", "102", "201"]


def genera_e_invia_test():
    print("⚡ Avvio inserimento automatico da Python...")

    for i in range(5):
        # 1. Scegliamo dati a caso
        nome_casuale = random.choice(NOMI)
        stanza_casuale = random.choice(STANZE)

        # 2. Generiamo una data a partire da oggi (+ i giorni)
        oggi = datetime.date.today()
        data_casuale = (oggi + datetime.timedelta(days=i)).isoformat()

        # 3. Prepariamo il dizionario (che Python trasformerà in JSON)
        dati_prenotazione = {
            "nome": f"{nome_casuale} (Python Test {i+1})",
            "stanza": stanza_casuale,
            "data": data_casuale,
        }

        # 4. Spediamo la richiesta POST al server Express
        try:
            risposta = requests.post(url=URL_API, json=dati_prenotazione)

            if risposta.status_code in [200, 201]:
                print(
                    f"✓ [Test {i+1}] Inserito con successo: {dati_prenotazione['nome']}"
                )
            else:
                # Se il server risponde con errore (es. stanza già occupata)
                dettaglio_errore = risposta.json().get(
                    "errore", "Errore sconosciuto"
                )
                print(
                    f"✗ [Test {i+1}] Server rifiutato ({risposta.status_code}): {dettaglio_errore}"
                )

        except requests.exceptions.ConnectionError:
            print(
                "⚠ Errore: Impossibile connettersi al server. Assicurati che Express sia attivo!"
            )
            break

    print("\nFine del test automatico.")


if __name__ == "__main__":
    genera_e_invia_test()