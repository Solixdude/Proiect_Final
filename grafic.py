import matplotlib.pyplot as plt

def grafic_pret(date, pret, titlu="Evoluția prețului"):
    plt.figure(figsize=(10, 5))
    plt.plot(date, pret, label="Preț")
    plt.xlabel("Dată")
    plt.ylabel("Preț")
    plt.title(titlu)
    plt.legend()
    plt.grid()
    plt.show()


def grafic_volum(date, volum, titlu="Volumul tranzacționat"):
    plt.figure(figsize=(10, 5))
    plt.bar(date, volum, color='purple', label="Volum")
    plt.xlabel("Dată")
    plt.ylabel("Volum")
    plt.title(titlu)
    plt.legend()
    plt.grid()
    plt.show()


def grafic_ema(date, pret_inchidere, ema_pe_termen_scurt, ema_pe_termen_lung, titlu="EMA pe termen scurt și lung"):
    plt.figure(figsize=(10, 5))
    plt.plot(date, pret_inchidere, label="Preț Close", color="blue")
    plt.plot(date, ema_pe_termen_scurt, label="EMA scurt", color="green")
    plt.plot(date, ema_pe_termen_lung, label="EMA lung", color="red")
    plt.xlabel("Dată")
    plt.ylabel("Preț")
    plt.title(titlu)
    plt.legend()
    plt.grid()
    plt.show()
