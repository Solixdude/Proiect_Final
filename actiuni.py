import yfinance as yf
from functools import wraps
from datetime import datetime, timedelta


def gestionarea_erorilor(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            print(f"Eroare în {func.__name__} pentru {self.simbol}: {e}")
            return None
    return wrapper



class Actiuni:
    def __init__(self, nume, simbol, cantitate, pret_cumparare, data_achizitie):
        self.nume = nume
        self.simbol = simbol.upper().strip()
        self.cantitate = cantitate
        self.pret_cumparare = pret_cumparare
        self.data_achizitie = data_achizitie
        self.data = yf.Ticker(simbol)
        self.cache_istoric = None
        self.cache_expirare = datetime.min
        self.cache_perioada = ""
        self.pret_curent = self.obtine_pretul_curent()
        self.volum = self.obtine_volum_tranzactionat()


    def obtine_istoric_cache(self, perioada='1mo', perioada_cache=timedelta(days=1)):
        """Obține istoricul din cache sau îl reînnoiește dacă este expirat sau perioada diferă."""

        # Verificăm dacă datele sunt în cache și cache-ul este încă valabil
        if (self.cache_istoric is None
                or datetime.now() > self.cache_expirare
                or self.cache_perioada != perioada):
            try:
                # Reîmprospătăm cache-ul și actualizăm perioada expirării
                self.cache_istoric = self.data.history(period=perioada)
                self.cache_expirare = datetime.now() + perioada_cache
                self.cache_perioada = perioada  # Salvăm perioada actuală în cache pentru verificări viitoare
            except Exception as e:
                print(f"Eroare la obținerea istoricului pentru {self.simbol}: {e}")
                return None

        return self.cache_istoric



    @gestionarea_erorilor
    def obtine_pretul_curent(self):
        pret_curent = self.obtine_istoric_cache('1d')['Close'].iloc[0]
        return pret_curent


    @gestionarea_erorilor
    def calculeaza_randamentul_total(self):
        pret_curent = self.obtine_pretul_curent()
        if pret_curent:
            return ((pret_curent - self.pret_cumparare) / self.pret_cumparare) * 100
        return None


    @gestionarea_erorilor
    def calculeaza_randamentul_anual(self):
        from datetime import datetime
        pret_curent = self.obtine_pretul_curent()
        if pret_curent:
            zile_detinere = (datetime.now() - self.data_achizitie).days
            randament_total = self.calculeaza_randamentul_total() / 100
            return ((1 + randament_total) ** (365 / zile_detinere) - 1) * 100
        return None


    @gestionarea_erorilor
    def obtine_volum_tranzactionat(self):
        volum = self.obtine_istoric_cache('1d')['Volume'].iloc[0]
        return volum


    @gestionarea_erorilor
    def obtine_pretul_minim_maxim(self):
        istoricul = self.obtine_istoric_cache("1mo")
        pret_minim = istoricul['Low'].min()
        pret_maxim = istoricul['High'].max()
        return pret_minim, pret_maxim


    @gestionarea_erorilor
    def obtine_dividende(self):
        dividende = self.data.dividends
        return dividende if not dividende.empty else "Niciun dividend înregistrat"


    @gestionarea_erorilor
    def calculeaza_volatilitatea(self, perioada):
        istoricul = self.obtine_istoric_cache(perioada)
        volatilitate = istoricul['Close'].pct_change().std() * (252 ** 0.5)
        return volatilitate * 100


    @gestionarea_erorilor
    def obtine_beta(self):
        beta = self.data.info.get('beta')
        return beta


    @gestionarea_erorilor
    def calcul_risc(self):
        volatilitate = self.calculeaza_volatilitatea('1y')
        beta = self.obtine_beta()

        # Verificăm dacă avem toate datele necesare
        if volatilitate is None or beta is None:
            print(f"Nu s-au putut calcula volatilitatea sau beta pentru {self.simbol}.")
            return None

        # Calculăm riscul total pe baza volatilitații și beta
        risc_total = volatilitate * beta
        risc_interpretat = ""

        # Interpretem volatilitatea și beta
        if volatilitate > 20:  # Volatilitate mare (> 20%) poate fi riscantă
            risc_interpretat += "Volatilitatea este ridicată, ceea ce poate face investiția mai riscantă. "
        else:
            risc_interpretat += "Volatilitatea este moderată, ceea ce sugerează o investiție mai stabilă. "

        if beta > 1:  # Riscuri mai mari pentru beta > 1
            risc_interpretat += "Beta este mai mare decât 1, ceea ce înseamnă că acțiunea este mai volatilă decât piața, crescând riscul. "
        elif beta < 1:
            risc_interpretat += "Beta este mai mic decât 1, ceea ce sugerează că acțiunea este mai puțin volatilă decât piața, reducând riscul. "
        else:
            risc_interpretat += "Beta este 1, ceea ce înseamnă că acțiunea se mișcă similar cu piața. "

        # Evaluarea riscului total
        if risc_total > 30:
            risc_interpretat += "Riscul total este mare, recomandând o prudență suplimentară înainte de a investi."
        elif risc_total > 15:
            risc_interpretat += "Riscul total este moderat, dar există o anumită volatilitate.\n Trebuie să iei în considerare profilul tău de risc."
        else:
            risc_interpretat += "Riscul total este scăzut, ceea ce face ca investiția să fie mai sigură."

        # Creăm dicționarul cu valori rotunjite pentru afișare
        rezultat = {
            "Volatilitatea actiunii": round(float(volatilitate), 2),
            "Beta": round(float(beta), 2),
            "Riscul actiunii": round(float(risc_total), 2),
            "Recomandare": risc_interpretat
        }

        # Afișăm rezultatele într-un format concret
        print("Rezultatele analizei riscului pentru acțiune:")
        for cheie, valoare in rezultat.items():
            print(f"{cheie}: {valoare}")

        return rezultat


    @gestionarea_erorilor
    def obtine_stiri(self):
        stiri = self.data.news
        return stiri if stiri else "Nicio știre recentă."


    @gestionarea_erorilor
    def obtine_ema(self, perioada = 20):
        istoricul = self.data.history(period= '1y')
        ema = istoricul['Close'].ewm(span=perioada, adjust=False).mean()
        return ema.iloc[-1]


    @gestionarea_erorilor
    def semnal_ema(self):
        ema_pe_termen_scurt = self.obtine_ema(20)
        ema_pe_termen_lung = self.obtine_ema(50)

        if ema_pe_termen_scurt > ema_pe_termen_lung:
            return "Semnal de Cumpărare: EMA pe termen scurt a depășit EMA pe termen lung."
        elif ema_pe_termen_scurt < ema_pe_termen_lung:
            return "Semnal de Vânzare: EMA pe termen scurt este sub EMA pe termen lung."
        else:
            return "Nu există un semnal clar de cumpărare sau vânzare în acest moment."


    @gestionarea_erorilor
    def obtine_raport_pe(self):
        pe_ratio = self.data.info.get('trailingPE')
        return pe_ratio


    @gestionarea_erorilor
    def obtine_eps(self):
        eps = self.data.info.get('trailingEps')
        return eps


    def analiza_profitabilitate(self):
        eps = self.obtine_eps()
        pe_ratio = self.obtine_raport_pe()

        if eps is None or pe_ratio is None:
            return "Nu există date suficiente pentru a analiza profitabilitatea."

        if eps > 2 and pe_ratio < 20:
            return (f"Acțiunea are un EPS ridicat {round(eps), 2} și un P/E Ratio scăzut {round(eps), 2}, "
                    "ceea ce sugerează o oportunitate bună de investiție datorită profitabilității ridicate.")
        elif eps < 1:
            return (f"Acțiunea are un EPS scăzut {round(eps), 2}, ceea ce poate indica o profitabilitate redusă "
                    "și necesită o analiză suplimentară.")
        else:
            return  (f"Acțiunea are un EPS de {round(eps), 2} și un P/E Ratio de {round(eps), 2}. Aceasta poate fi o "
                    "opțiune stabilă, dar fără avantaje remarcabile de profitabilitate.")


    @gestionarea_erorilor
    def obtine_randamentul_dividendelor(self):
        randamentul_dividendelor = self.data.info.get('dividendYield')
        return randamentul_dividendelor * 100 if randamentul_dividendelor else None

    @gestionarea_erorilor
    def analiza_dividendelor(self):
        randamentul_dividendelor = self.obtine_randamentul_dividendelor()
        dividende = self.obtine_dividende()
        raport_plata = self.data.info.get('payoutRatio')


        if randamentul_dividendelor is None:
            return "Acțiunea nu are un randament al dividendelor disponibil sau nu plătește dividende."

        analiza = []

        # Analiza randamentul dividendelor
        if randamentul_dividendelor > 3:
            analiza.append(f"Acțiunea are un randament al dividendelor ridicat {randamentul_dividendelor:.2f}%, "
                           f"ceea ce este atractiv pentru investitorii axați pe venituri.")
        elif randamentul_dividendelor < 1:
            analiza.append(f"Randamentul dividendelor este scăzut {randamentul_dividendelor:.2f}%, "
                           f"ceea ce poate indica o opțiune mai puțin atractivă pentru investitorii care caută venituri pasive.")
        else:
            analiza.append(f"Randamentul dividendelor este moderat {randamentul_dividendelor:.2f}%, "
                           f"oferind un echilibru între creștere și venit pasiv.")


        # Analiza istoricului dividendelor
        if isinstance(dividende, str) or dividende.empty:
            analiza.append("Compania nu a plătit dividende recente.")
        else:
            analiza.append(f"Compania are un istoric consistent al dividendelor, cu ultimele divide înregistrate.")


        #Analiza raportului de plata a dividendelor.
        if raport_plata:
            if raport_plata > 0.5:
                analiza.append(f"Payout Ratio-ul este ridicat {raport_plata:.2%}, "
                               f"ceea ce poate sugera o presiune pe profitabilitatea companiei.")
            elif 0.3 <= raport_plata <= 0.5:
                analiza.append(f"Payout Ratio-ul este balansat {raport_plata:.2%}, "
                               f"indicând o distribuție echilibrată a câștigurilor către acționari.")
            else:
                analiza.append(
                    f"Payout Ratio-ul este scăzut {raport_plata:.2%}, "
                    f"sugerând că o mare parte a câștigurilor este reinvestită în companie.")

        return analiza


    def evolutie_pret_actiuni(self):
        istoric = self.obtine_istoric_cache('1y')
        date = istoric.index
        pret = istoric["Close"]
        from grafic import grafic_pret
        grafic_pret(date, pret, titlu=f"Evolutia pretului actiunii cu simbolul {self.simbol}")


    def evolutie_volum_actiuni(self):
        istoric = self.obtine_istoric_cache('1y')
        date = istoric.index
        volum_tranzactionat = istoric["Volume"]
        from grafic import grafic_volum
        grafic_volum(date, volum_tranzactionat, titlu= f"Volumul tranzactionat pentru {self.simbol}")


    def evolutie_ema_actiuni(self):
        istoricul = self.data.history(period='1y')
        dates = istoricul.index
        close_prices = istoricul['Close']
        ema_short = close_prices.ewm(span=20, adjust=False).mean()
        ema_long = close_prices.ewm(span=50, adjust=False).mean()

        from grafic import grafic_ema
        grafic_ema(dates, close_prices, ema_short, ema_long, titlu= f"Evoluția EMA pentru {self.simbol}")





