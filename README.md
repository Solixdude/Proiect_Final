# Gestionare Portofoliu de Acțiuni

Acest proiect este o aplicație pentru gestionarea portofoliului de acțiuni, utilizând Python, SQLite și Tkinter. Aplicația oferă funcționalități precum adăugarea, actualizarea și vânzarea acțiunilor, analiza diverselor indicatori financiari, și vizualizarea graficelor.

## Structura Proiectului

- **`actiuni.py`**: Definește clasa `Actiuni`, care gestionează datele și analizele legate de acțiuni.
- **`portofoliu.py`**: Oferă interfața cu baza de date SQLite pentru gestionarea portofoliului de acțiuni.
- **`grafic.py`**: Include funcții pentru vizualizarea grafică a datelor financiare folosind matplotlib.
- **`gui.py`**: Conține interfața grafică a aplicației folosind Tkinter.

## Funcționalități Cheie

### actiuni.py
- **`obtine_pretul_curent`**: Returnează prețul curent al acțiunii pe baza datelor istorice.
- **`calculeaza_randamentul_total`**: Calculează randamentul total al investiției.
- **`analiza_dividendelor`**: Oferă detalii despre dividendele unei acțiuni, inclusiv randamentul și raportul de plată.
- **`calcul_risc`**: Analizează riscul acțiunii pe baza volatilității și beta.
- **`obtine_stiri`**: Returnează știri recente despre acțiune.

### portofoliu.py
- **`adauga_actiune`**: Adaugă o acțiune în portofoliu.
- **`obtine_actiuni`**: Returnează toate acțiunile din portofoliu.
- **`actualizeaza_actiune`**: Actualizează cantitatea și prețul unei acțiuni.
- **`vinde_actiune`**: Elimină o acțiune din portofoliu.

### grafic.py
- **`grafic_pret`**: Generează graficul evoluției prețului unei acțiuni.
- **`grafic_volum`**: Vizualizează volumul tranzacționat pe o perioadă.
- **`grafic_ema`**: Afișează media mobilă exponențială (EMA) pe termen scurt și lung.

### gui.py
- **Adăugare și vânzare acțiuni**: Permite utilizatorului să adauge, vândă sau actualizeze acțiuni prin GUI.
- **Analize financiare**: Ferestre dedicate pentru analiza dividendelor, calculul riscurilor și analiza profitabilității.
- **Grafică interactivă**: Butoane pentru afișarea graficelor de preț, volum și EMA.
- **Schimbare temă**: Opțiune pentru schimbarea între temele dark și light.
- **Vizualizare știri**: Afișează cele mai recente știri despre o acțiune selectată.

## Utilizare
1. **Setare inițială**: Asigurați-vă că toate dependențele (`yfinance`, `matplotlib`, `sqlite3`, `tkinter`) sunt instalate.
2. **Lansare aplicație**: Rulați fișierul `gui.py` pentru a porni interfața grafică.
3. **Interacțiune**: Adăugați acțiuni, analizați indicatori financiari sau vizualizați graficele direct din aplicație.

