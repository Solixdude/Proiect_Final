import matplotlib.pyplot as plt

def grafic_pret(date, pret, titlu="Evoluția prețului"):
    plt.figure(figsize=(10, 5))
    plt.plot(date, pret, label="Preț", color="blue", marker="o")
    plt.xlabel("Dată")
    plt.ylabel("Preț")
    plt.title(titlu)
    plt.legend()
    plt.grid(visible=True, linestyle="--", alpha=0.7)
    plt.xticks(rotation=45)  # Rotim etichetele axei X
    plt.tight_layout()  # Prevenim suprapunerea elementelor
    plt.show()

def grafic_volum(date, volum, titlu="Volumul tranzacționat"):
    plt.figure(figsize=(10, 5))
    plt.bar(date, volum, color='purple', label="Volum")
    plt.xlabel("Dată")
    plt.ylabel("Volum")
    plt.title(titlu)
    plt.legend()
    plt.grid(axis='y', linestyle="--", alpha=0.7)
    plt.xticks(rotation=45)  # Rotim etichetele axei X
    plt.tight_layout()
    plt.show()

def grafic_ema(date, pret_inchidere, ema_pe_termen_scurt, ema_pe_termen_lung, titlu="EMA pe termen scurt și lung"):
    plt.figure(figsize=(10, 5))
    plt.plot(date, pret_inchidere, label="Preț Close", color="blue", linewidth=1.5)
    plt.plot(date, ema_pe_termen_scurt, label="EMA scurt", color="green", linestyle="--", linewidth=1.5)
    plt.plot(date, ema_pe_termen_lung, label="EMA lung", color="red", linestyle="-.", linewidth=1.5)
    plt.xlabel("Dată")
    plt.ylabel("Preț")
    plt.title(titlu)
    plt.legend()
    plt.grid(visible=True, linestyle="--", alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

