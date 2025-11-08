import webview
import threading
from datetime import datetime


class API:
    def __init__(self):
        self.dati_form = None
        self.window = None

    def submit_form(self, data_inizio, data_fine, coinquilini, importo, commissioni):
        """Chiamata da JavaScript quando il form viene inviato"""
        self.dati_form = {
            'dataInizio': data_inizio,
            'dataFine': data_fine,
            'coinquilini': coinquilini,
            'importo': importo,
            'commissioni': commissioni
        }
        # Chiudi la finestra dopo aver salvato i dati
        if self.window:
            threading.Timer(0.5, lambda: self.window.destroy()).start()
        return True


HTML_CONTENT = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestione Bollette</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            max-width: 500px;
            width: 100%;
            animation: slideIn 0.5s ease-out;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        h1 {
            color: #333;
            margin-bottom: 30px;
            text-align: center;
            font-size: 28px;
        }

        .form-group {
            margin-bottom: 25px;
        }

        label {
            display: block;
            color: #555;
            font-weight: 600;
            margin-bottom: 8px;
            font-size: 14px;
        }

        input[type="date"],
        input[type="text"],
        input[type="number"],
        textarea {
            width: 100%;
            padding: 12px 15px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 15px;
            transition: all 0.3s ease;
            font-family: inherit;
        }

        input[type="date"]:focus,
        input[type="text"]:focus,
        input[type="number"]:focus,
        textarea:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }

        textarea {
            resize: vertical;
            min-height: 60px;
        }

        .date-group {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }

        .amount-group {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }

        button {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            margin-top: 10px;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        }

        button:active {
            transform: translateY(0);
        }

        .info-text {
            color: #888;
            font-size: 13px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Gestione Bollette</h1>
        <form id="bollettaForm" onsubmit="return submitForm(event)">
            <div class="date-group">
                <div class="form-group">
                    <label for="dataInizio">Data Inizio 📅</label>
                    <input type="date" id="dataInizio" name="dataInizio" required>
                </div>
                <div class="form-group">
                    <label for="dataFine">Data Fine 📅</label>
                    <input type="date" id="dataFine" name="dataFine" required>
                </div>
            </div>

            <div class="amount-group">
                <div class="form-group">
                    <label for="importo">Importo (€) 💰</label>
                    <input type="number" id="importo" name="importo" step="0.01" required>
                </div>
                <div class="form-group">
                    <label for="commissioni">Commissioni (€) 💳</label>
                    <input type="number" id="commissioni" name="commissioni" step="0.01" required>
                </div>
            </div>

            <div class="form-group">
                <label for="coinquilini">Coinquilini 👥</label>
                <textarea id="coinquilini" name="coinquilini" rows="3" placeholder="Mario, Luca, Sara..." required></textarea>
                <div class="info-text">Inserisci i nomi separati da virgola</div>
            </div>

            <button type="submit">Conferma e Continua ✓</button>
        </form>
    </div>

    <script>
        function submitForm(event) {
            event.preventDefault();

            const dataInizio = document.getElementById('dataInizio').value;
            const dataFine = document.getElementById('dataFine').value;
            const coinquilini = document.getElementById('coinquilini').value;
            const importo = document.getElementById('importo').value;
            const commissioni = document.getElementById('commissioni').value;

            // Chiama la funzione Python
            pywebview.api.submit_form(dataInizio, dataFine, coinquilini, importo, commissioni);

            return false;
        }
    </script>
</body>
</html>
"""


def avvia_interfaccia():
    """
    Avvia l'interfaccia grafica HTML e restituisce i dati inseriti dall'utente.

    Returns:
        tuple: (data_inizio, data_fine, stringaCoinquilini, importo, commissioni)
    """
    api = API()

    # Crea la finestra con l'HTML
    window = webview.create_window(
        'Gestione Bollette Coinquilini',
        html=HTML_CONTENT,
        js_api=api,
        width=600,
        height=700,
        resizable=True
    )

    api.window = window

    # Avvia la GUI (blocca fino alla chiusura della finestra)
    webview.start()

    # Quando la finestra si chiude, controlla se ci sono dati
    if api.dati_form is None:
        raise Exception("Finestra chiusa senza inserire dati")

    # Converti le date da stringa a datetime.date
    data_inizio = datetime.strptime(api.dati_form['dataInizio'], '%Y-%m-%d').date()
    data_fine = datetime.strptime(api.dati_form['dataFine'], '%Y-%m-%d').date()

    return (
        data_inizio,
        data_fine,
        api.dati_form['coinquilini'],
        api.dati_form['importo'],
        api.dati_form['commissioni']
    )


# Per test standalone
if __name__ == "__main__":
    risultato = avvia_interfaccia()
    print("Dati ricevuti:")
    print(f"Data inizio: {risultato[0]}")
    print(f"Data fine: {risultato[1]}")
    print(f"Coinquilini: {risultato[2]}")
    print(f"Importo: {risultato[3]}")
    print(f"Commissioni: {risultato[4]}")