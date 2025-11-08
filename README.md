# 🏠 Divisione Bollette Coinquilini

> 🇬🇧 [English version available here](README_EN.md)

Un programma Python per dividere automaticamente le spese delle bollette in base ai giorni di presenza effettiva di ogni coinquilino, utilizzando Google Calendar per tracciare le assenze.

## 📋 Come Funziona

Il programma calcola quanto deve pagare ogni coinquilino in base ai giorni in cui è stato **effettivamente presente** nell'appartamento. Le assenze vengono tracciate tramite eventi in Google Calendar.

### Principio Base
- **Più giorni sei presente = più paghi**
- **Più giorni sei assente = meno paghi**
- Le commissioni vengono divise equamente tra tutti

## 🚀 Setup Iniziale

### 1️⃣ Crea il file `calendar_url.txt`

Nella root del progetto, crea un file chiamato `calendar_url.txt` contenente **solo** l'URL pubblico del tuo Google Calendar.

**Come ottenere l'URL:**

1. Apri [Google Calendar](https://calendar.google.com)
2. Vai su **Impostazioni** (⚙️) → **Impostazioni**
3. Nella barra laterale sinistra, clicca sul calendario che vuoi usare
4. Scorri fino a **"Integra calendario"**
5. Copia l'**indirizzo segreto in formato iCal**
6. Incollalo nel file `calendar_url.txt`

**Esempio di `calendar_url.txt`:**
```
https://calendar.google.com/calendar/ical/tu0kalendar1234567890%40group.calendar.google.com/private-abc123def456/basic.ics
```

### 2️⃣ Installa le dipendenze
```bash
pip install -r requirements.txt
```

### 3️⃣ Avvia il programma
```bash
python main.py
```

## 📅 Come Configurare il Calendario

### Registrare le Assenze

Per registrare un'assenza, crea un evento in Google Calendar con queste caratteristiche:

✅ **Il nome dell'evento DEVE contenere il nome del coinquilino**
   - Esempi: `Giovani a Londra`, `Chiara vacanza`, `Mario weekend fuori`
   
✅ **L'evento DEVE essere impostato come "Tutto il giorno"**
   - Quando crei l'evento, spunta la casella **"Tutto il giorno"**
   
✅ **La data di fine è ESCLUSA**
   - Se Mario è via dal 1 al 5 marzo, l'evento va impostato dal 1 marzo al 6 marzo
   - In questo modo conterà 5 giorni (1, 2, 3, 4, 5)

### ⚠️ Importante

- **Nome univoco**: Ogni coinquilino deve avere un nome univoco (no abbreviazioni ambigue)
- **Tutto il giorno**: Se non è spuntato "Tutto il giorno", l'evento viene ignorato
- **Calendario condiviso**: Assicurati che tutti i coinquilini abbiano accesso al calendario

### Esempio Pratico

**Scenario**: Luca va in vacanza dal 10 al 15 gennaio (5 giorni)

**Come creare l'evento:**
- Nome evento: `Luca vacanza Spagna` (o qualsiasi testo contenente "Luca")
- Data inizio: 10 gennaio
- Data fine: 16 gennaio (⚠️ importante: un giorno dopo l'ultimo giorno di assenza)
- Spunta: ✅ Tutto il giorno

## 🖥️ Utilizzo

1. **Avvia il programma**
```bash
   python main.py
```

2. **Compila il form** che si apre nel browser:
   - Data inizio bolletta
   - Data fine bolletta
   - Importo totale bolletta
   - Commissioni (spese bancarie, ecc.)
   - Nome dei coinquilini (separati da virgola)

3. **Il programma genera una ricevuta PDF** con:
   - Riepilogo dei pagamenti per ogni coinquilino
   - Dettaglio delle assenze
   - Totale da pagare (quota + commissione)

## 📊 Output

Il programma genera un file PDF chiamato `ricevuta_bolletta.pdf` contenente:

- 📅 Periodo di riferimento
- 💰 Totale bolletta e commissioni
- 📋 Tabella riepilogativa con:
  - Giorni di presenza per ogni coinquilino
  - Quota base calcolata proporzionalmente
  - Commissione divisa equamente
  - Totale da pagare
- 📝 Dettaglio di tutte le assenze per ogni persona

## 🛠️ Requisiti

- Python 3.7+
- Google Calendar pubblico o condiviso
- Connessione internet (per sincronizzare il calendario)

## 📁 Struttura File
```
progetto/
├── main.py                  # File principale
├── interfacciaGrafica.py    # Interfaccia HTML
├── funcioniCalcoli.py       # Logica di calcolo
├── calendar_url.txt         # ⚠️ URL del calendario (da creare)
├── requirements.txt         # Dipendenze
├── .gitignore              # File da ignorare in Git
└── ricevuta_bolletta.pdf   # Output generato
```

## ❓ FAQ

**Q: Posso usare più calendari?**  
A: Al momento il programma supporta un solo calendario. Tutti gli eventi devono essere nello stesso calendario.

**Q: Cosa succede se dimentico di mettere "Tutto il giorno"?**  
A: L'evento verrà ignorato e quei giorni verranno conteggiati come presenza.

**Q: E se due persone hanno lo stesso nome?**  
A: Usa nomi univoci o abbreviazioni diverse per ogni coinquilino.

## 📝 Licenza

Progetto personale per la gestione delle bollette condivise.

## 🤝 Contributi

Suggerimenti e miglioramenti sono benvenuti!

---

**Nota**: Ricordati di NON committare il file `calendar_url.txt` su GitHub (è già nel .gitignore) per proteggere la privacy del tuo calendario! 🔒