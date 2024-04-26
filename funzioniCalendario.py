from icalendar import Calendar
from datetime import datetime
import requests

def eventi_in_periodo(ical_file, dateStart, dateEnd):
    eventi = []
    with open(ical_file, 'rb') as f:
        cal = Calendar.from_ical(f.read())
        for componente in cal.walk():
            if componente.name == "VEVENT":
                start = componente.get('dtstart').dt
                end = componente.get('dtend').dt
                if start <= dateEnd and end >= dateStart:
                    startInteresse, endInteresse = estraiPeriodoInteresse(start, end, dateStart, dateEnd)
                    giorniCompresi = numero_giorni_compresi(startInteresse, endInteresse)
                    titolo = componente.get('summary').to_ical().decode()
                    eventi.append((start, end, startInteresse, endInteresse, titolo, giorniCompresi))
    return eventi

def estraiPeriodoInteresse(start, end, dateStart, dateEnd):
    startInteresse = start
    endInteresse = end
    if start < dateStart:
        startInteresse = dateStart
    if end > dateEnd:
        endInteresse = dateEnd
    return startInteresse, endInteresse

def numero_giorni_compresi(dateStart, dateEnd):
    differenza = dateEnd - dateStart
    numero_giorni = differenza.days
    ##numero_giorni += 1 ###calcolo differenza giorni eg.(25/01/2024 - 24/01/2024 + 1 gg e non 2 gg)
    return numero_giorni

def smistaEventi(eventi, arrayCoinquilini):
    obj = {"error":[]}
    for coinq in arrayCoinquilini:
        obj[coinq] = []
    for e in eventi:
        titoloEve = e[4]
        if titoloEve in obj:
            obj[titoloEve].append(e)
        else:
            trovato = False
            for coinq in arrayCoinquilini:
                if coinq in titoloEve:
                    trovato = True
                    obj[coinq].append(e)
            if not trovato:
                obj["error"].append(e)
    return obj

def scarica_calendario_da_url(url, nome_file):
    response = requests.get(url)
    if response.status_code == 200:
        with open(nome_file, 'wb') as f:
            f.write(response.content)
        print(f"File {nome_file} scaricato correttamente.")
    else:
        print("Errore durante il download del file.")