from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from datetime import timedelta


def crea_ricevuta_pdf(dateStart, dateEnd, totBolletta, commissione, objGionriPerCoinq,
                      objTotaliDovuti, oggettoEventiSmistati, arrayCoinquilini,
                      nome_file="ricevuta_bolletta.pdf"):
    """
    Crea un PDF con la ricevuta della bolletta
    """
    doc = SimpleDocTemplate(nome_file, pagesize=A4,
                            rightMargin=2 * cm, leftMargin=2 * cm,
                            topMargin=2 * cm, bottomMargin=2 * cm)

    story = []
    styles = getSampleStyleSheet()

    # Stile personalizzato per il titolo
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=30,
        alignment=TA_CENTER
    )

    # Titolo
    story.append(Paragraph("📊 Ricevuta Bolletta Coinquilini", title_style))
    story.append(Spacer(1, 0.5 * cm))

    # Periodo
    periodo_text = f"<b>Periodo:</b> dal {dateStart.strftime('%d/%m/%Y')} al {dateEnd.strftime('%d/%m/%Y')}"
    story.append(Paragraph(periodo_text, styles['Normal']))
    story.append(Spacer(1, 0.3 * cm))

    # Totali
    totale_text = f"<b>Totale Bolletta:</b> €{totBolletta} | <b>Commissioni:</b> €{commissione}"
    story.append(Paragraph(totale_text, styles['Normal']))
    story.append(Spacer(1, 0.5 * cm))

    # Tabella riepilogo
    story.append(Paragraph("<b>RIEPILOGO PAGAMENTI</b>", styles['Heading2']))
    story.append(Spacer(1, 0.3 * cm))

    # Dati tabella
    data = [['Coinquilino', 'Giorni Presenza', 'Quota Base', 'Commissione', 'TOTALE']]

    commissione_per_persona = round(commissione / len(arrayCoinquilini), 2)

    for coinq in objTotaliDovuti:
        giorni = objGionriPerCoinq.get(coinq, 0)
        quota_base = objTotaliDovuti[coinq]
        totale = round(quota_base + commissione_per_persona, 2)
        data.append([
            coinq,
            str(giorni),
            f"€{quota_base}",
            f"€{commissione_per_persona}",
            f"€{totale}"
        ])

    # Crea tabella
    t = Table(data, colWidths=[4 * cm, 3 * cm, 3 * cm, 3 * cm, 3 * cm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))

    story.append(t)
    story.append(Spacer(1, 1 * cm))

    # Dettaglio assenze per ogni coinquilino
    story.append(Paragraph("<b>DETTAGLIO ASSENZE</b>", styles['Heading2']))
    story.append(Spacer(1, 0.5 * cm))

    for coinq in objTotaliDovuti:
        story.append(Paragraph(f"<b>{coinq}</b>", styles['Heading3']))

        if coinq in oggettoEventiSmistati and len(oggettoEventiSmistati[coinq]) > 0:
            assenze_data = [['Descrizione', 'Dal', 'Al', 'Giorni']]

            for e in oggettoEventiSmistati[coinq]:
                assenze_data.append([
                    e[4],
                    e[2].strftime('%d/%m/%Y'),
                    (e[3] - timedelta(days=1)).strftime('%d/%m/%Y'),
                    str(e[5])
                ])

            t_assenze = Table(assenze_data, colWidths=[5 * cm, 3 * cm, 3 * cm, 2 * cm])
            t_assenze.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#764ba2')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
            ]))

            story.append(t_assenze)
        else:
            story.append(Paragraph("<i>Nessuna assenza</i>", styles['Italic']))

        story.append(Spacer(1, 0.5 * cm))

    # Build PDF
    doc.build(story)
    print(f"\n✅ Ricevuta PDF creata: {nome_file}")