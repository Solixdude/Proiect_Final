Stock Portfolio Management

This project is an application for managing a stock portfolio using Python, SQLite, and Tkinter. The app provides features such as adding, updating, and selling stocks, analyzing various financial indicators, and visualizing data through graphs.
Project Structure

    actiuni.py: Defines the Actiuni class, which handles stock-related data and analyses.
    portofoliu.py: Provides the SQLite database interface for managing the stock portfolio.
    grafic.py: Includes functions for financial data visualization using matplotlib.
    gui.py: Contains the graphical user interface of the application built with Tkinter.

Key Features
actiuni.py

    obtine_pretul_curent: Returns the current stock price based on historical data.
    calculeaza_randamentul_total: Calculates the total return on investment.
    analiza_dividendelor: Provides details about a stock's dividends, including yield and payout ratio.
    calcul_risc: Analyzes the stock's risk based on volatility and beta.
    obtine_stiri: Fetches recent news about the stock.

portofoliu.py

    adauga_actiune: Adds a stock to the portfolio.
    obtine_actiuni: Retrieves all stocks in the portfolio.
    actualizeaza_actiune: Updates the quantity and price of a stock.
    vinde_actiune: Removes a stock from the portfolio.

grafic.py

    grafic_pret: Generates a graph of the stock's price evolution.
    grafic_volum: Visualizes traded volume over a specific period.
    grafic_ema: Displays short-term and long-term exponential moving averages (EMA).

gui.py

    Adding and selling stocks: Enables users to add, sell, or update stocks through the GUI.
    Financial analyses: Dedicated windows for dividend analysis, risk calculation, and profitability analysis.
    Interactive graphs: Buttons for displaying price, volume, and EMA charts.
    Theme switching: Option to switch between dark and light themes.
    News viewing: Displays the latest news about a selected stock.

Usage

    Initial setup: Ensure all dependencies (yfinance, matplotlib, sqlite3, tkinter) are installed.
    Launch application: Run the gui.py file to start the graphical interface.
    Interact: Add stocks, analyze financial indicators, or visualize charts directly within the app.
