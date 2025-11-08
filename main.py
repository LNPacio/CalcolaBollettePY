from datetime import datetime, timedelta
import funzioniCalendario
import funcioniCalcoli
import interfacciaGrafica

if __name__ == "__main__":

    dateStart, dateEnd, strCoinqInput, imp, comm = interfacciaGrafica.avvia_interfaccia()
    arrayCoinquilini = strCoinqInput.replace(" ", "").replace("\n", "").split(',')
    totBolletta = float(imp.replace(',', '.'))
    commissione = float(comm.replace(',', '.'))


    url_calendario = "" #inserire url qui
    ical_file = "mio_calendario.ics"
    funzioniCalendario.scarica_calendario_da_url(url_calendario, ical_file)
    # dateStart = datetime(2023, 12, 7).date()
    # dateEnd = datetime(2024, 2, 6).date()
    # arrayCoinquilini = ['Luca', 'Giacomo', 'Enrico']
    # totBolletta = 74.04
    # commissione = 1.30
    eventi = funzioniCalendario.eventi_in_periodo(ical_file, dateStart, dateEnd)
    # print(f"EVENTI TOTALI:")
    # for evento in eventi:
    #     print(f"Titolo: {evento[4]}, InizoEvento: {evento[0]},FineEvento: {evento[1]}, InizioInteresse: {evento[2]}, FineInteresse: {evento[3]}, GiorniCompresiInteresse: {evento[5]},")

    numeroGiorniBolletta = funzioniCalendario.numero_giorni_compresi(dateStart, dateEnd)
    numeroGiorniBolletta += 1 ###calcolo differenza giorni eg.(25/01/2024 - 24/01/2024 + 1 gg e non 2 gg)
    # print(f"Numero giorni bolletta: {numeroGiorniBolletta}\n")

    # print(f"EVENTI SMISTATI:")
    oggettoEventiSmistati = funzioniCalendario.smistaEventi(eventi, arrayCoinquilini)
    # for coinq in oggettoEventiSmistati:
    #     print(f"{coinq}:{oggettoEventiSmistati[coinq]}")
    if len(oggettoEventiSmistati['error']) == 0:

        # print(f"\n\nGIORNI TOTALI PRESENZA: ")
        objGionriPerCoinq = funcioniCalcoli.calcolaTotaliGiorniInquilini (oggettoEventiSmistati, numeroGiorniBolletta)
        # for coinq in objGionriPerCoinq:
        #     print(f"{coinq}:{objGionriPerCoinq[coinq]}")

        print(f"\n\nBolletta da   {dateStart.strftime('%d/%m/%Y')}   a    {dateEnd.strftime('%d/%m/%Y')}")
        print(f"Tot.Bolletta:   {totBolletta}€   Commissioni:    {commissione}€\nTOTALE DOVUTO DA OGNI INQUILINO: ")
        objTotaliDovuti = funcioniCalcoli.calcolaTotalDovutoePerCoinquilino(totBolletta, objGionriPerCoinq)
        for coinq in objTotaliDovuti:
            print(f"{coinq}:{objTotaliDovuti[coinq]} + {commissione/len(arrayCoinquilini)}(commissione) = {round(objTotaliDovuti[coinq] + (commissione/len(arrayCoinquilini)),2)}€\n  ASSENZE:")
            for e in oggettoEventiSmistati[coinq]:
                print(f"        {e[4]}: dal {e[2].strftime('%d/%m/%Y')}  al  {(e[3] - timedelta(days=1)).strftime('%d/%m/%Y')}  GG: {e[5]}")
            print(f"\n")

    else:
        print(f"SONO PRESENTI EVENTI ERRATI:")
        for e in oggettoEventiSmistati['error']:
            print(f"        {e[4]}: dal {e[2].strftime('%d/%m/%Y')}  al  {(e[3] - timedelta(days=1)).strftime('%d/%m/%Y')}  GG: {e[5]}")