from datetime import datetime, timedelta
import funzioniCalendario
import funcioniCalcoli
import interfacciaGrafica
import funzioniPdf

if __name__ == "__main__":

    dateStart, dateEnd, strCoinqInput, imp, comm = interfacciaGrafica.avvia_interfaccia()
    arrayCoinquilini = strCoinqInput.replace(" ", "").replace("\n", "").split(',')
    totBolletta = float(imp.replace(',', '.'))
    commissione = float(comm.replace(',', '.'))

    url_calendario = None;
    with open('calendar_url.txt', 'r') as f:
        url_calendario = f.read().strip()

    ical_file = "mio_calendario.ics"
    funzioniCalendario.scarica_calendario_da_url(url_calendario, ical_file)

    eventi = funzioniCalendario.eventi_in_periodo(ical_file, dateStart, dateEnd)

    numeroGiorniBolletta = funzioniCalendario.numero_giorni_compresi(dateStart, dateEnd)
    numeroGiorniBolletta += 1

    
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

        funzioniPdf.crea_ricevuta_pdf(dateStart, dateEnd, totBolletta, commissione,
                          objGionriPerCoinq, objTotaliDovuti,
                          oggettoEventiSmistati, arrayCoinquilini)

    else:
        print(f"SONO PRESENTI EVENTI ERRATI:")
        for e in oggettoEventiSmistati['error']:
            print(f"        {e[4]}: dal {e[2].strftime('%d/%m/%Y')}  al  {(e[3] - timedelta(days=1)).strftime('%d/%m/%Y')}  GG: {e[5]}")
