import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

def ottieni_valori():
    global data_inizio_bolletta, data_fine_bolletta, stringaCoinquilini, importo, commissioni
    data_inizio_bolletta = cal_inizio.get_date()
    data_fine_bolletta = cal_fine.get_date()
    stringaCoinquilini = campo_testuale.get("1.0", tk.END)
    importo = campo_importo.get()
    commissioni = campo_commissioni.get()
    root.destroy()

def crea_interfaccia():
    global root, cal_inizio, cal_fine, campo_testuale, campo_importo, campo_commissioni


    root = tk.Tk()
    root.title("Interfaccia Utente")

    frame_date = ttk.Frame(root)
    frame_date.pack(padx=40, pady=40)

    ttk.Label(frame_date, text="Data di inizio:").grid(row=0, column=0)
    cal_inizio = DateEntry(frame_date, width=12, background='darkblue', foreground='white', borderwidth=2)
    cal_inizio.grid(row=0, column=1)

    ttk.Label(frame_date, text="Data di fine:").grid(row=1, column=0)
    cal_fine = DateEntry(frame_date, width=12, background='darkblue', foreground='white', borderwidth=2)
    cal_fine.grid(row=1, column=1)

    ttk.Label(frame_date, text="Importo:").grid(row=2, column=0)
    campo_importo = ttk.Entry(frame_date, width=15)
    campo_importo.grid(row=2, column=1)

    ttk.Label(frame_date, text="Commissioni:").grid(row=3, column=0)
    campo_commissioni = ttk.Entry(frame_date, width=15)
    campo_commissioni.grid(row=3, column=1)

    ttk.Label(root, text="Coinquilini (separati da ','):").pack(pady=(5,0))
    campo_testuale = tk.Text(root, height=2, width=20)
    campo_testuale.pack()

    bottone_conferma = ttk.Button(root, text="Conferma", command=ottieni_valori)
    bottone_conferma.pack(pady=10)

    root.mainloop()

    return data_inizio_bolletta, data_fine_bolletta, stringaCoinquilini, importo, commissioni

def avvia_interfaccia():
    data_inizio_bolletta, data_fine_bolletta, stringaCoinquilini, importo, commissioni = crea_interfaccia()
    ##inserire controlli in futuro
    return data_inizio_bolletta, data_fine_bolletta, stringaCoinquilini, importo, commissioni
