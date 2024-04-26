def totaleGiorniInquilino (totaleGiorniBolletta, arrayEventi):

    giorniAssenzaInquilino = 0
    for e in arrayEventi:
        giorniAssenzaInquilino += e[5]
        ##giorniAssenzaInquilino += 1 ###calcolo differenza giorni eg.(25/01/2024 - 24/01/2024 + 1 gg e non 2 gg)

    return totaleGiorniBolletta - giorniAssenzaInquilino

def calcolaTotaliGiorniInquilini (eventiSmistati, totaleGiorniBolletta):
    objGionriPerCoinq = {}
    for coinq in eventiSmistati:
        if coinq != "error":
            totGGCoinq = totaleGiorniInquilino(totaleGiorniBolletta, eventiSmistati[coinq])
            objGionriPerCoinq[coinq] = totGGCoinq
    return objGionriPerCoinq

def calcolaTotaleTuttiCoinquilini (objGionriPerCoinq):
    totaleTuttiCoinquilini = 0
    for c in objGionriPerCoinq:
        totaleTuttiCoinquilini += objGionriPerCoinq[c]
    return totaleTuttiCoinquilini

def calcolaTotalDovutoePerCoinquilino (totBolletta,objGionriPerCoinq):
    objTotaliPerCoinq = {}
    totGGTuttiCoinq = calcolaTotaleTuttiCoinquilini(objGionriPerCoinq)
    for coinq in objGionriPerCoinq:
        objTotaliPerCoinq[coinq] = totBolletta*(objGionriPerCoinq[coinq]/totGGTuttiCoinq)

    return objTotaliPerCoinq


