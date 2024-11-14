import tkinter as tk
import webbrowser
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from actiuni import Actiuni
from portofoliu import Portofoliu


class PortfolioManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestionare portofoliului de acțiuni")
        self.portofoliu = Portofoliu()
        self.actiune = Actiuni("Apple", "AAPL", 0, 0, datetime.now())


        self.create_menu()
        self.create_toolbar()
        self.create_main_frame()


        # Frame pentru lista de acțiuni
        self.frame_lista_actiuni = ttk.Frame(self.main_frame)
        self.frame_lista_actiuni.pack(pady=20, fill='both', expand=True)

        self.stiri_text = tk.Text(self.main_frame, height= 20, width=80, wrap="word")
        self.stiri_text.pack(pady=10)

        self.afiseaza_stiri()

        self.actualizeaza_lista_actiuni()



    def create_menu(self):
        # Creează bara de meniu
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        # Meniu Acțiuni
        self.actiuni_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Acțiuni", menu=self.actiuni_menu)
        self.actiuni_menu.add_command(label="Adaugă acțiune", command=self.show_adauga_window)
        self.actiuni_menu.add_command(label="Vinde acțiune", command=self.show_vinde_window)
        self.actiuni_menu.add_command(label="Actualizează acțiune", command=self.show_actualizeaza_window)

        # Meniu Analize
        self.analize_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Analize", menu=self.analize_menu)
        self.analize_menu.add_command(label="Analiză dividende", command=self.show_analiza_dividende_window)
        self.analize_menu.add_command(label= "Analiză profitabilitate", command= self.show_analiza_profitabilitate_window)
        self.analize_menu.add_command(label= "Calcul risc acțiune", command= self.show_calcul_risc_window)
        self.analize_menu.add_command(label= "Semnal EMA", command= self.show_semnal_ema_window)

        self.grafice_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label= "Grafice", menu= self.grafice_menu)
        self.grafice_menu.add_command(label= "Grafic evolutie pret", command= self.show_evolutie_pret_actiuni)
        self.grafice_menu.add_command(label= "Grafic evolutie volum", command= self.show_evolutie_volum_actiuni)
        self.grafice_menu.add_command(label= "Grafi evolutie EMA", command= self.show_evolutie_ema)

    def create_toolbar(self):
        # Creează toolbar
        self.toolbar = ttk.Frame(self.root)
        self.toolbar.pack(side="top", fill="x")

        # Butoane toolbar
        ttk.Button(self.toolbar, text= "Adaugă", command= self.show_adauga_window).pack(side="left", padx=2, pady=2)
        ttk.Button(self.toolbar, text= "Vinde", command= self.show_vinde_window).pack(side="left", padx=2, pady=2)
        ttk.Button(self.toolbar, text= "Actualizează", command= self.show_actualizeaza_window).pack(side="left", padx=2,
                                                                                                  pady=2)
        ttk.Separator(self.toolbar, orient="vertical").pack(side="left", fill="y", padx=5, pady=2)
        ttk.Button(self.toolbar, text="Analiză dividende", command= self.show_analiza_dividende_window).pack(side="left",
                                                                                                            padx=2,
                                                                                                            pady=2)
        ttk.Button(self.toolbar, text= "Analiză profitabilitate", command= self.show_analiza_profitabilitate_window).pack(side='left',
                                                                                                                   padx= 2,
                                                                                                                   pady= 2)
        ttk.Button(self.toolbar, text="Calcul risc", command=self.show_calcul_risc_window).pack(side="left", padx=2,
                                                                                                pady=2)

        ttk.Button(self.toolbar, text="Semnal EMA", command=self.show_semnal_ema_window).pack(side="left", padx=2,
                                                                                              pady=2)
        ttk.Separator(self.toolbar, orient= "vertical").pack(side= "left", fill= 'y', padx = 5, pady = 2)

        ttk.Button(self.toolbar, text="Evoluție preț", command=self.show_evolutie_pret_actiuni).pack(side="left", padx=2,
                                                                                                    pady=2)
        ttk.Button(self.toolbar, text="Evoluție volum", command=self.show_evolutie_volum_actiuni).pack(side="left",
                                                                                                     padx=2,
                                                                                                     pady=2)
        ttk.Button(self.toolbar, text="Evoluție EMA", command=self.show_evolutie_ema).pack(side="left", padx=2,
                                                                                                        pady=2)




    def create_main_frame(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=True, fill="both", padx=5, pady=5)


    def show_adauga_window(self):
        window = tk.Toplevel(self.root)
        window.title("Adaugă Acțiune")

        frame = ttk.Frame(window, padding="10")
        frame.pack(fill='both', expand=True)

        # Câmpuri pentru adăugare
        ttk.Label(frame, text="Nume:").grid(row=0, column=0, sticky='w')
        entry_nume = ttk.Entry(frame)
        entry_nume.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Simbol:").grid(row=1, column=0, sticky='w')
        entry_simbol = ttk.Entry(frame)
        entry_simbol.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Cantitate:").grid(row=2, column=0, sticky='w')
        entry_cantitate = ttk.Entry(frame)
        entry_cantitate.grid(row=2, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Preț cumpărare:").grid(row=3, column=0, sticky='w')
        entry_pret = ttk.Entry(frame)
        entry_pret.grid(row=3, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Data achiziție (YYYY-MM-DD):").grid(row=4, column=0, sticky='w')
        entry_data = ttk.Entry(frame)
        entry_data.grid(row=4, column=1, padx=5, pady=2)

        def adauga():
            try:
                actiune = Actiuni(
                    entry_nume.get(),
                    entry_simbol.get().upper(),
                    entry_cantitate.get(),
                    entry_pret.get(),
                    entry_data.get()
                )
                self.portofoliu.adauga_actiune(actiune)
                messagebox.showinfo("Succes", "Acțiunea a fost adăugată cu succes!")
                self.actualizeaza_lista_actiuni()
                window.destroy()
            except Exception as e:
                messagebox.showerror("Eroare", str(e))

        ttk.Button(frame, text="Adaugă", command=adauga).grid(row=5, column=0, columnspan=2, pady=10)

    def show_vinde_window(self):
        window = tk.Toplevel(self.root)
        window.title("Vinde acțiune")

        frame = ttk.Frame(window, padding="10")
        frame.pack(fill='both', expand=True)

        ttk.Label(frame, text="Simbol:").grid(row=0, column=0, sticky='w')
        entry_simbol = ttk.Entry(frame)
        entry_simbol.grid(row=0, column=1, padx=5, pady=2)

        def vinde():
            try:
                self.portofoliu.vinde_actiune(entry_simbol.get().upper())
                messagebox.showinfo("Succes", "Acțiunea a fost vanduta cu succes!\n"
                                              "Suma a fost virata in contul dumneavoastra.")
                self.actualizeaza_lista_actiuni()
                window.destroy()
            except Exception as e:
                messagebox.showerror("Eroare", str(e))

        ttk.Button(frame, text="Vinde", command=vinde).grid(row=1, column=0, columnspan=2, pady=10)


    def show_actualizeaza_window(self):
        window = tk.Toplevel(self.root)
        window.title("Actualizează Acțiune")

        frame = ttk.Frame(window, padding="10")
        frame.pack(fill='both', expand=True)

        # Variabile pentru a stoca valorile curente
        cantitate_curenta = tk.StringVar()
        pret_curent = tk.StringVar()

        ttk.Label(frame, text="Simbol:").grid(row=0, column=0, sticky='w')
        entry_simbol = ttk.Entry(frame)
        entry_simbol.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Cantitate curentă:").grid(row=1, column=0, sticky='w')
        label_cantitate_curenta = ttk.Label(frame, textvariable=cantitate_curenta)
        label_cantitate_curenta.grid(row=1, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Adaugă cantitate:").grid(row=2, column=0, sticky='w')
        entry_cantitate = ttk.Entry(frame)
        entry_cantitate.grid(row=2, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Preț curent:").grid(row=3, column=0, sticky='w')
        label_pret_curent = ttk.Label(frame, textvariable=pret_curent)
        label_pret_curent.grid(row=3, column=1, padx=5, pady=2)

        ttk.Label(frame, text="Nou preț:").grid(row=4, column=0, sticky='w')
        entry_pret = ttk.Entry(frame)
        entry_pret.grid(row=4, column=1, padx=5, pady=2)

        def cauta_actiune():
            simbol = entry_simbol.get().upper()
            if simbol:
                try:
                    actiuni = self.portofoliu.obtine_actiuni()
                    for actiune in actiuni:
                        if actiune[2] == simbol:  # Verificăm simbolul
                            cantitate_curenta.set(str(actiune[3]))  # Setăm cantitatea curentă
                            pret_curent.set(str(actiune[4]))  # Setăm prețul curent
                            return
                    messagebox.showwarning("Atenție", f"Nu s-a găsit nicio acțiune cu simbolul {simbol}")
                except Exception as e:
                    messagebox.showerror("Eroare", str(e))

        def actualizeaza():
            try:
                simbol = entry_simbol.get().upper()
                cantitate_noua = entry_cantitate.get()
                pret_nou = entry_pret.get()

                # Calculăm noua cantitate și prețul mediu ponderat
                if cantitate_noua and pret_nou:
                    cantitate_totala = int(cantitate_curenta.get()) + int(cantitate_noua)
                    pret_total = (int(cantitate_curenta.get()) * float(pret_curent.get()) +
                                    int(cantitate_noua) * float(pret_nou)) / cantitate_totala
                else:
                    cantitate_totala = int(cantitate_curenta.get())
                    pret_total = float(pret_curent.get())

                # Actualizăm acțiunea cu cantitatea totală și noul preț mediu
                self.portofoliu.actualizeaza_actiune(
                    simbol,
                    cantitate= cantitate_totala,
                    pret_cumparare= round(pret_total, 2)
                )
                messagebox.showinfo("Succes", f"Acțiunea {simbol} a fost actualizată cu succes!\n"
                                              f"Cantitate nouă totală: {cantitate_totala}")
                self.actualizeaza_lista_actiuni()
                window.destroy()
            except Exception as e:
                messagebox.showerror("Eroare", str(e))

        # Adăugăm un buton de căutare
        ttk.Button(frame, text="Caută", command=cauta_actiune).grid(row=0, column=2, padx=5, pady=2)

        # Configurăm evenimentul pentru când se apasă Enter în câmpul simbol
        entry_simbol.bind('<Return>', lambda event: cauta_actiune())

        ttk.Button(frame, text="Actualizează", command=actualizeaza).grid(row=5, column=0, columnspan=2, pady=10)


    def actualizeaza_lista_actiuni(self):
        for widget in self.frame_lista_actiuni.winfo_children():
            widget.destroy()

        actiuni = self.portofoliu.obtine_actiuni()

        for actiune in actiuni:
            ttk.Label(
                self.frame_lista_actiuni,
                text=f"{actiune[1]} ({actiune[2]}) - {actiune[3]} acțiuni la {actiune[4]} RON"
            ).pack(pady=2)


    def show_analiza_dividende_window(self):
        window = tk.Toplevel(self.root)
        window.title("Analiză Dividende")

        frame = ttk.Frame(window, padding="10")
        frame.pack(fill='both', expand=True)

        ttk.Label(frame, text="Simbol:").grid(row=0, column=0, sticky='w')
        entry_simbol = ttk.Entry(frame)
        entry_simbol.grid(row=0, column=1, padx=5, pady=2)

        rezultat_frame = ttk.Frame(frame)
        rezultat_frame.grid(row=2, column=0, columnspan=2, pady=10)

        def analizeaza():
            for widget in rezultat_frame.winfo_children():
                widget.destroy()

            actiune = Actiuni(
                nume="Actiune exemplu",
                simbol=entry_simbol.get().upper(),
                cantitate=0,
                pret_cumparare=0,
                data_achizitie=datetime.now()
            )
            rezultat = actiune.analiza_dividendelor()
            for linie in rezultat:
                ttk.Label(rezultat_frame, text=linie).pack()

        ttk.Button(frame, text="Analizează", command=analizeaza).grid(row=1, column=0, columnspan=2, pady=10)

    def show_analiza_profitabilitate_window(self):
        window = tk.Toplevel(self.root)
        window.title("Analiză Profitabilitate")

        frame = ttk.Frame(window, padding="10")
        frame.pack(fill='both', expand=True)

        ttk.Label(frame, text="Simbol:").grid(row=0, column=0, sticky='w')
        entry_simbol = ttk.Entry(frame)
        entry_simbol.grid(row=0, column=1, padx=5, pady=2)

        rezultat_frame = ttk.Frame(frame)
        rezultat_frame.grid(row=2, column=0, columnspan=2, pady=10)

        def analizeaza():
            for widget in rezultat_frame.winfo_children():
                widget.destroy()

            actiune = Actiuni(
                nume="Actiune exemplu",
                simbol=entry_simbol.get().upper(),
                cantitate=0,
                pret_cumparare=0,
                data_achizitie=datetime.now()
            )

            rezultat = actiune.analiza_profitabilitate()

            ttk.Label(rezultat_frame, text=rezultat).pack()

        ttk.Button(frame, text="Analizează", command=analizeaza).grid(row=1, column=0, columnspan=2, pady=10)

    def show_calcul_risc_window(self):
        window = tk.Toplevel(self.root)
        window.title("Calcul Riscuri Acțiuni")

        frame = ttk.Frame(window, padding="10")
        frame.pack(fill='both', expand=True)

        ttk.Label(frame, text="Simbol:").grid(row=0, column=0, sticky='w')
        entry_simbol = ttk.Entry(frame)
        entry_simbol.grid(row=0, column=1, padx=5, pady=2)

        rezultat_frame = ttk.Frame(frame)
        rezultat_frame.grid(row=2, column=0, columnspan=2, pady=10)

        def afiseaza_risc():
            simbol = entry_simbol.get().upper()
            if simbol:
                try:
                    # Creăm obiectul Actiuni cu simbolul introdus
                    actiune = Actiuni(
                        nume="Actiune exemplu",
                        simbol=simbol,
                        cantitate=0,
                        pret_cumparare=0,
                        data_achizitie=datetime.now()
                    )
                    rezultat = actiune.calcul_risc()  # Calculăm riscul

                    # Afișăm rezultatele în fereastra GUI
                    for widget in rezultat_frame.winfo_children():
                        widget.destroy()

                    if rezultat:
                        for cheie, valoare in rezultat.items():
                            ttk.Label(rezultat_frame, text=f"{cheie}: {valoare}").pack()

                except Exception as e:
                    messagebox.showerror("Eroare", str(e))

        ttk.Button(frame, text="Calculă riscul", command=afiseaza_risc).grid(row=1, column=0, columnspan=2, pady=10)

    def show_semnal_ema_window(self):
        window = tk.Toplevel(self.root)
        window.title("Semnal EMA Acțiuni")

        frame = ttk.Frame(window, padding="10")
        frame.pack(fill='both', expand=True)

        ttk.Label(frame, text="Simbol:").grid(row=0, column=0, sticky='w')
        entry_simbol = ttk.Entry(frame)
        entry_simbol.grid(row=0, column=1, padx=5, pady=2)

        rezultat_frame = ttk.Frame(frame)
        rezultat_frame.grid(row=2, column=0, columnspan=2, pady=10)

        def afiseaza_semnal():
            simbol = entry_simbol.get().upper()
            if simbol:
                try:
                    # Creăm obiectul Actiuni cu simbolul introdus
                    actiune = Actiuni(
                        nume="Actiune exemplu",
                        simbol=simbol,
                        cantitate=0,
                        pret_cumparare=0,
                        data_achizitie=datetime.now()
                    )
                    semnal = actiune.semnal_ema()  # Obținem semnalul EMA

                    # Afișăm semnalul în fereastra GUI
                    for widget in rezultat_frame.winfo_children():
                        widget.destroy()

                    ttk.Label(rezultat_frame, text=semnal).pack()

                except Exception as e:
                    messagebox.showerror("Eroare", str(e))

        ttk.Button(frame, text="Afișează Semnal EMA", command=afiseaza_semnal).grid(row=1, column=0, columnspan=2,
                                                                                    pady=10)

    def show_evolutie_pret_actiuni(self):
        window = tk.Toplevel(self.root)
        window.title("Evoluție Preț Acțiuni")

        frame = ttk.Frame(window, padding="10")
        frame.pack(fill='both', expand=True)

        ttk.Label(frame, text="Simbol:").grid(row=0, column=0, sticky='w')
        entry_simbol = ttk.Entry(frame)
        entry_simbol.grid(row=0, column=1, padx=5, pady=2)

        def afiseaza_grafic():
            simbol = entry_simbol.get().upper()
            if simbol:
                try:
                    # Generează graficul prețului pentru simbolul acțiunii
                    actiune = Actiuni(
                        nume="Actiune exemplu",
                        simbol=simbol,
                        cantitate=0,
                        pret_cumparare=0,
                        data_achizitie=datetime.now()
                    )
                    actiune.evolutie_pret_actiuni()  # Aceasta funcție ar trebui să fie în modulul de grafic

                except Exception as e:
                    messagebox.showerror("Eroare", str(e))

        ttk.Button(frame, text="Afișează Grafic", command=afiseaza_grafic).grid(row=1, column=0, columnspan=2, pady=10)

    def show_evolutie_volum_actiuni(self):
        window = tk.Toplevel(self.root)
        window.title("Evoluție Volum Acțiuni")

        frame = ttk.Frame(window, padding="10")
        frame.pack(fill='both', expand=True)

        ttk.Label(frame, text="Simbol:").grid(row=0, column=0, sticky='w')
        entry_simbol = ttk.Entry(frame)
        entry_simbol.grid(row=0, column=1, padx=5, pady=2)

        def afiseaza_grafic():
            simbol = entry_simbol.get().upper()
            if simbol:
                try:
                    # Generează graficul prețului pentru simbolul acțiunii
                    actiune = Actiuni(
                        nume="Actiune exemplu",
                        simbol=simbol,
                        cantitate=0,
                        pret_cumparare=0,
                        data_achizitie=datetime.now()
                    )
                    actiune.evolutie_volum_actiuni()  # Aceasta funcție ar trebui să fie în modulul de grafic

                except Exception as e:
                    messagebox.showerror("Eroare", str(e))

        ttk.Button(frame, text="Afișează Grafic", command=afiseaza_grafic).grid(row=1, column=0, columnspan=2, pady=10)


    def show_evolutie_ema(self):
        window = tk.Toplevel(self.root)
        window.title("Evoluție EMA Acțiuni")

        frame = ttk.Frame(window, padding="10")
        frame.pack(fill='both', expand=True)

        ttk.Label(frame, text="Simbol:").grid(row=0, column=0, sticky='w')
        entry_simbol = ttk.Entry(frame)
        entry_simbol.grid(row=0, column=1, padx=5, pady=2)

        def afiseaza_grafic():
            simbol = entry_simbol.get().upper()
            if simbol:
                try:
                    # Generează graficul prețului pentru simbolul acțiunii
                    actiune = Actiuni(
                        nume="Actiune exemplu",
                        simbol=simbol,
                        cantitate=0,
                        pret_cumparare=0,
                        data_achizitie=datetime.now()
                    )
                    actiune.evolutie_ema_actiuni()  # Aceasta funcție ar trebui să fie în modulul de grafic

                except Exception as e:
                    messagebox.showerror("Eroare", str(e))

        ttk.Button(frame, text="Afișează Grafic", command=afiseaza_grafic).grid(row=1, column=0, columnspan=2, pady=10)

    def obtine_stiri(self):
        return self.actiune.obtine_stiri() or "Nicio știre recentă."

    def afiseaza_stiri(self):
        # Obținem știrile și curățăm zona de text
        stiri = self.obtine_stiri()
        self.stiri_text.config(state=tk.NORMAL)
        self.stiri_text.delete("1.0", tk.END)

        # Verificăm dacă `stiri` este o listă de articole sau text simplu
        if isinstance(stiri, list):
            for articol in stiri:
                titlu = articol.get("title", "Fără titlu")
                link = articol.get("link", "#")
                data_publicare = articol.get("date", "Data necunoscută")
                descriere = articol.get("summary", "Fără descriere")

                # Formatarea afișării știrilor
                self.stiri_text.insert(tk.END, f"Titlu: {titlu}\n", "titlu")
                self.stiri_text.insert(tk.END, f"Data: {data_publicare}\n", "data")
                self.stiri_text.insert(tk.END, f"Descriere: {descriere}\n", "descriere")
                self.stiri_text.insert(tk.END, f"Link: {link}\n\n", "link")

               
            # Adăugăm stiluri
            self.stiri_text.tag_configure("titlu", font=("Arial", 12, "bold"), foreground="blue")
            self.stiri_text.tag_configure("data", font=("Arial", 10, "italic"))
            self.stiri_text.tag_configure("descriere", font=("Arial", 11))
            self.stiri_text.tag_configure("link", font=("Arial", 10, "underline"), foreground="blue")
        else:
            # Dacă este text simplu
            self.stiri_text.insert(tk.END, stiri)

        self.stiri_text.config(state=tk.DISABLED)



if __name__ == "__main__":
    root = tk.Tk()
    app = PortfolioManagerGUI(root)
    root.geometry("800x600")
    root.mainloop()