import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Avviamo Firefox controllato da Python
print("🦊 Avvio di Firefox controllato da Python...")
driver = webdriver.Firefox()

try:
    # 2. Apriamo la pagina del nostro sito
    driver.get("http://localhost:3001")
    print("🌍 Pagina caricata con successo.")
    time.sleep(2)  # Pausa di 2 secondi per farti vedere la pagina vuota

    # Dati da inserire
    nome_test = "Marco Viola (Firefox Test)"
    # Su Firefox, digitiamo la data come stringa continua di numeri: giorno, mese, anno (DDMMYYYY)
    data_test = "15082026"  # 15 Agosto 2026

    print(f"✍ Digito il nome: {nome_test}")
    # 3. Troviamo il campo Nome e digitiamo il testo
    campo_nome = driver.find_element(By.ID, "nome")
    campo_nome.send_keys(nome_test)
    time.sleep(1.5)  # Pausa visiva

    print("📅 Seleziono la data...")
    # 4. Troviamo il campo Data e inseriamo la data
    campo_data = driver.find_element(By.ID, "data")
    campo_data.send_keys(data_test)
    time.sleep(1.5)  # Pausa visiva

    print("🏨 Seleziono la Stanza 102...")
    # 5. Troviamo il menu a tendina e selezioniamo la stanza 102
    campo_stanza = driver.find_element(By.ID, "stanza")
    campo_stanza.send_keys("Stanza 102")
    time.sleep(1.5)  # Pausa visiva

    print("👆 Clicco sul pulsante 'Prenota Ora'!")
    # 6. Troviamo il pulsante di invio e lo clicchiamo
    pulsante_invia = driver.find_element(
        By.XPATH, "//button[@type='submit']"
    )
    pulsante_invia.click()

    # 7. Aspettiamo per vedere il risultato apparire a schermo
    print("⏳ Attendo la conferma visiva...")
    time.sleep(4)  # Ti lascia 4 secondi per vedere la riga aggiunta a destra!

    # 8. Verifichiamo se il messaggio di successo è comparso
    messaggio = driver.find_element(By.ID, "messaggio").text
    print(f"🎉 Risultato sul browser: '{messaggio}'")

except Exception as e:
    print(f"❌ Si è verificato un errore durante il test: {e}")

finally:
    # Chiudiamo il browser automatico alla fine del test
    print("🔒 Chiudo Firefox.")
    driver.quit()