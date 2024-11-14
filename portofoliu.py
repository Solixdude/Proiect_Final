import sqlite3
from actiuni import Actiuni  # Importă clasa Actiuni

class Portofoliu:
    def __init__(self, db_name="portofoliu.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.creeaza_tabel()

    def creeaza_tabel(self):
        """Creează tabela pentru portofoliu dacă nu există deja."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS actiuni (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nume TEXT,
                simbol TEXT,
                cantitate INTEGER,
                pret_cumparare REAL,
                data_achizitie TEXT
            )
        ''')
        self.conn.commit()

    def adauga_actiune(self, actiune: Actiuni):
        """Adaugă o acțiune în portofoliu."""
        self.cursor.execute('''
            INSERT INTO actiuni (nume, simbol, cantitate, pret_cumparare, data_achizitie)
            VALUES (?, ?, ?, ?, ?)
        ''', (actiune.nume, actiune.simbol, actiune.cantitate, actiune.pret_cumparare, actiune.data_achizitie))
        self.conn.commit()


    def obtine_actiuni(self):
        """Obține toate acțiunile din portofoliu."""
        self.cursor.execute("SELECT * FROM actiuni")
        actiuni = self.cursor.fetchall()
        return actiuni


    def actualizeaza_actiune(self, simbol, cantitate, pret_cumparare):
        """Actualizează o acțiune din portofoliu."""
        self.cursor.execute('''
            UPDATE actiuni
            SET cantitate = ?, pret_cumparare = ?
            WHERE simbol = ?
        ''', (cantitate, pret_cumparare, simbol))
        self.conn.commit()


    def vinde_actiune(self, simbol):
        """Șterge o acțiune din portofoliu."""
        self.cursor.execute('DELETE FROM actiuni WHERE simbol = ?', (simbol,))
        self.conn.commit()

        self.conn.execute("SELECT id from actiuni ORDER BY id ASC")
        rows = self.cursor.fetchall()

        new_id = 1
        for row in rows:
            self.cursor.execute("UPDATE actiuni SET id = ? WHERE id = ?", (new_id, row[0]))
            new_id += 1
        self.conn.commit()


    def inchide_conexiune(self):
        """Închide conexiunea la baza de date."""
        self.conn.close()