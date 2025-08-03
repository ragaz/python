# Guida Completa Yahoo Finance - Tutti i Dati Disponibili
# pip install streamlit yfinance pandas numpy

import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

def main():
    st.set_page_config(
        page_title="Guida Yahoo Finance",
        page_icon="📚",
        layout="wide"
    )
    
    st.title("📚 Guida Completa: Dati Yahoo Finance")
    st.markdown("### Tutti i dati finanziari disponibili tramite la libreria yfinance")
    st.markdown("---")
    
    # Sidebar per la navigazione
    st.sidebar.title("🧭 Navigazione")
    sections = [
        "📊 Informazioni Base",
        "💰 Ratios Finanziari", 
        "📈 Dati di Trading",
        "🏢 Informazioni Aziendali",
        "📋 Dati Storici",
        "🎯 Opzioni",
        "💼 Bilanci",
        "📊 Flussi di Cassa",
        "📈 Crescita e Dividendi",
        "🔍 Analisi Tecnica",
        "🌍 Dati ESG",
        "💡 Come Utilizzare"
    ]
    
    selected_section = st.sidebar.radio("Seleziona Sezione:", sections)
    
    # Input per testare i dati
    st.sidebar.markdown("---")
    st.sidebar.subheader("🧪 Test Dati")
    test_symbol = st.sidebar.text_input("Simbolo per test:", value="AAPL")
    
    if st.sidebar.button("🔍 Mostra Dati Esempio"):
        show_example_data(test_symbol)
        
    # Contenuto principale basato sulla sezione selezionata
    if selected_section == "📊 Informazioni Base":
        show_basic_info()
    elif selected_section == "💰 Ratios Finanziari":
        show_financial_ratios()
    elif selected_section == "📈 Dati di Trading":
        show_trading_data()
    elif selected_section == "🏢 Informazioni Aziendali":
        show_company_info()
    elif selected_section == "📋 Dati Storici":
        show_historical_data()
    elif selected_section == "🎯 Opzioni":
        show_options_data()
    elif selected_section == "💼 Bilanci":
        show_financial_statements()
    elif selected_section == "📊 Flussi di Cassa":
        show_cash_flow()
    elif selected_section == "📈 Crescita e Dividendi":
        show_growth_dividends()
    elif selected_section == "🔍 Analisi Tecnica":
        show_technical_analysis()
    elif selected_section == "🌍 Dati ESG":
        show_esg_data()
    elif selected_section == "💡 Come Utilizzare":
        show_usage_guide()

def show_basic_info():
    st.header("📊 Informazioni Base del Titolo")
    
    data_fields = [
        {
            "campo": "symbol",
            "descrizione": "Simbolo ticker del titolo",
            "esempio": "AAPL",
            "tipo": "str"
        },
        {
            "campo": "longName",
            "descrizione": "Nome completo dell'azienda",
            "esempio": "Apple Inc.",
            "tipo": "str"
        },
        {
            "campo": "shortName",
            "descrizione": "Nome abbreviato",
            "esempio": "Apple Inc.",
            "tipo": "str"
        },
        {
            "campo": "currentPrice",
            "descrizione": "Prezzo corrente dell'azione",
            "esempio": "175.43",
            "tipo": "float"
        },
        {
            "campo": "previousClose",
            "descrizione": "Prezzo di chiusura precedente",
            "esempio": "174.91",
            "tipo": "float"
        },
        {
            "campo": "open",
            "descrizione": "Prezzo di apertura giornaliero",
            "esempio": "175.20",
            "tipo": "float"
        },
        {
            "campo": "dayLow",
            "descrizione": "Prezzo minimo giornaliero",
            "esempio": "174.50",
            "tipo": "float"
        },
        {
            "campo": "dayHigh",
            "descrizione": "Prezzo massimo giornaliero",
            "esempio": "176.80",
            "tipo": "float"
        },
        {
            "campo": "regularMarketOpen",
            "descrizione": "Apertura del mercato regolare",
            "esempio": "175.20",
            "tipo": "float"
        },
        {
            "campo": "regularMarketDayHigh",
            "descrizione": "Massimo del mercato regolare",
            "esempio": "176.80",
            "tipo": "float"
        },
        {
            "campo": "regularMarketDayLow",
            "descrizione": "Minimo del mercato regolare",
            "esempio": "174.50",
            "tipo": "float"
        },
        {
            "campo": "regularMarketPreviousClose",
            "descrizione": "Chiusura precedente mercato regolare",
            "esempio": "174.91",
            "tipo": "float"
        }
    ]
    
    df = pd.DataFrame(data_fields)
    st.dataframe(df, use_container_width=True)

def show_financial_ratios():
    st.header("💰 Ratios e Metriche Finanziarie")
    
    st.subheader("🔍 Ratios di Valutazione")
    valuation_ratios = [
        {
            "campo": "trailingPE",
            "descrizione": "Price-to-Earnings ratio (ultimi 12 mesi)",
            "formula": "Prezzo / Utili per Azione",
            "interpretazione": "Quanto gli investitori pagano per ogni $ di utili. P/E basso può indicare sottovalutazione."
        },
        {
            "campo": "forwardPE",
            "descrizione": "P/E prospettico basato su stime future",
            "formula": "Prezzo / Utili Stimati",
            "interpretazione": "P/E basato su previsioni analisti. Utile per valutare crescita attesa."
        },
        {
            "campo": "pegRatio",
            "descrizione": "Price/Earnings to Growth ratio",
            "formula": "P/E / Tasso Crescita Utili",
            "interpretazione": "PEG < 1 può indicare sottovalutazione rispetto alla crescita."
        },
        {
            "campo": "priceToBook",
            "descrizione": "Rapporto prezzo/valore contabile",
            "formula": "Prezzo / Patrimonio Netto per Azione",
            "interpretazione": "P/B < 1 può indicare che l'azione è sottovalutata."
        },
        {
            "campo": "priceToSalesTrailing12Months",
            "descrizione": "Rapporto prezzo/ricavi",
            "formula": "Market Cap / Ricavi Annuali",
            "interpretazione": "Valuta se l'azienda è cara rispetto ai suoi ricavi."
        },
        {
            "campo": "enterpriseValue",
            "descrizione": "Valore dell'impresa",
            "formula": "Market Cap + Debito - Liquidità",
            "interpretazione": "Costo teorico per acquisire l'intera azienda."
        },
        {
            "campo": "enterpriseToRevenue",
            "descrizione": "EV/Ricavi",
            "formula": "Enterprise Value / Ricavi",
            "interpretazione": "Rapporto enterprise value sui ricavi annuali."
        },
        {
            "campo": "enterpriseToEbitda",
            "descrizione": "EV/EBITDA",
            "formula": "Enterprise Value / EBITDA",
            "interpretazione": "Multiplo comune per valutazioni M&A."
        }
    ]
    
    df_val = pd.DataFrame(valuation_ratios)
    st.dataframe(df_val, use_container_width=True)
    
    st.subheader("💹 Ratios di Redditività")
    profitability_ratios = [
        {
            "campo": "returnOnEquity",
            "descrizione": "Return on Equity (ROE)",
            "formula": "Utile Netto / Patrimonio Netto",
            "interpretazione": "Efficienza nell'utilizzo del capitale degli azionisti. ROE > 15% è generalmente buono."
        },
        {
            "campo": "returnOnAssets",
            "descrizione": "Return on Assets (ROA)",
            "formula": "Utile Netto / Totale Attivi",
            "interpretazione": "Efficienza nell'utilizzo degli asset. ROA > 5% è positivo."
        },
        {
            "campo": "profitMargins",
            "descrizione": "Margine di profitto netto",
            "formula": "Utile Netto / Ricavi",
            "interpretazione": "Percentuale di ricavi che diventa profitto. Più alto è meglio."
        },
        {
            "campo": "operatingMargins",
            "descrizione": "Margine operativo",
            "formula": "Utile Operativo / Ricavi",
            "interpretazione": "Efficienza operativa. Margini > 15% sono buoni."
        },
        {
            "campo": "grossMargins",
            "descrizione": "Margine lordo",
            "formula": "(Ricavi - Costo Venduto) / Ricavi",
            "interpretazione": "Redditività dopo i costi diretti di produzione."
        },
        {
            "campo": "ebitdaMargins",
            "descrizione": "Margine EBITDA",
            "formula": "EBITDA / Ricavi",
            "interpretazione": "Redditività operativa prima di ammortamenti e tasse."
        }
    ]
    
    df_prof = pd.DataFrame(profitability_ratios)
    st.dataframe(df_prof, use_container_width=True)
    
    st.subheader("🏦 Ratios di Liquidità e Solidità")
    liquidity_ratios = [
        {
            "campo": "currentRatio",
            "descrizione": "Rapporto di liquidità corrente",
            "formula": "Attivi Correnti / Passivi Correnti",
            "interpretazione": "Capacità di pagare debiti a breve. Ratio > 1.5 è buono."
        },
        {
            "campo": "quickRatio",
            "descrizione": "Rapporto di liquidità immediata",
            "formula": "(Attivi Correnti - Scorte) / Passivi Correnti",
            "interpretazione": "Liquidità senza considerare le scorte. > 1 è positivo."
        },
        {
            "campo": "debtToEquity",
            "descrizione": "Rapporto debito/patrimonio",
            "formula": "Debito Totale / Patrimonio Netto",
            "interpretazione": "Livello di indebitamento. Valori bassi indicano minor rischio."
        },
        {
            "campo": "totalDebt",
            "descrizione": "Debito totale",
            "formula": "Debiti a Breve + Debiti a Lungo Termine",
            "interpretazione": "Ammontare totale dei debiti dell'azienda."
        },
        {
            "campo": "totalCash",
            "descrizione": "Liquidità totale",
            "formula": "Contanti + Equivalenti di Cassa",
            "interpretazione": "Disponibilità liquide dell'azienda."
        },
        {
            "campo": "totalCashPerShare",
            "descrizione": "Liquidità per azione",
            "formula": "Liquidità Totale / Azioni Outstanding",
            "interpretazione": "Liquidità disponibile per ogni azione."
        }
    ]
    
    df_liq = pd.DataFrame(liquidity_ratios)
    st.dataframe(df_liq, use_container_width=True)

def show_trading_data():
    st.header("📈 Dati di Trading e Mercato")
    
    trading_data = [
        {
            "campo": "volume",
            "descrizione": "Volume di scambi giornaliero",
            "spiegazione": "Numero di azioni scambiate nel giorno. Volume alto indica interesse."
        },
        {
            "campo": "averageVolume",
            "descrizione": "Volume medio (ultimi 3 mesi)",
            "spiegazione": "Media del volume giornaliero. Utile per identificare giorni anomali."
        },
        {
            "campo": "averageVolume10days",
            "descrizione": "Volume medio (ultimi 10 giorni)",
            "spiegazione": "Volume medio più recente, utile per trend di breve periodo."
        },
        {
            "campo": "marketCap",
            "descrizione": "Capitalizzazione di mercato",
            "spiegazione": "Valore totale di tutte le azioni (Prezzo × Azioni Outstanding)."
        },
        {
            "campo": "sharesOutstanding",
            "descrizione": "Azioni in circolazione",
            "spiegazione": "Numero totale di azioni emesse e in circolazione."
        },
        {
            "campo": "floatShares",
            "descrizione": "Azioni flottanti",
            "spiegazione": "Azioni disponibili per il trading pubblico (esclude insider)."
        },
        {
            "campo": "sharesShort",
            "descrizione": "Azioni vendute allo scoperto",
            "spiegazione": "Numero di azioni attualmente in posizione short."
        },
        {
            "campo": "shortRatio",
            "descrizione": "Rapporto short",
            "spiegazione": "Giorni necessari per coprire tutte le posizioni short al volume medio."
        },
        {
            "campo": "shortPercentOfFloat",
            "descrizione": "% short sul flottante",
            "spiegazione": "Percentuale del flottante venduto allo scoperto."
        },
        {
            "campo": "beta",
            "descrizione": "Beta (volatilità relativa)",
            "spiegazione": "Volatilità rispetto al mercato. Beta > 1 = più volatile del mercato."
        },
        {
            "campo": "52WeekLow",
            "descrizione": "Minimo a 52 settimane",
            "spiegazione": "Prezzo più basso degli ultimi 12 mesi."
        },
        {
            "campo": "52WeekHigh",
            "descrizione": "Massimo a 52 settimane",
            "spiegazione": "Prezzo più alto degli ultimi 12 mesi."
        },
        {
            "campo": "fiftyTwoWeekLowChange",
            "descrizione": "Variazione dal minimo 52w",
            "spiegazione": "Differenza tra prezzo corrente e minimo annuale."
        },
        {
            "campo": "fiftyTwoWeekHighChange",
            "descrizione": "Variazione dal massimo 52w",
            "spiegazione": "Differenza tra prezzo corrente e massimo annuale."
        }
    ]
    
    df_trading = pd.DataFrame(trading_data)
    st.dataframe(df_trading, use_container_width=True)
    
    st.subheader("📊 Medie Mobili e Indicatori Tecnici")
    technical_data = [
        {
            "campo": "fiftyDayAverage",
            "descrizione": "Media mobile a 50 giorni",
            "spiegazione": "Prezzo medio degli ultimi 50 giorni. Trend di medio termine."
        },
        {
            "campo": "twoHundredDayAverage",
            "descrizione": "Media mobile a 200 giorni",
            "spiegazione": "Prezzo medio degli ultimi 200 giorni. Trend di lungo termine."
        },
        {
            "campo": "fiftyDayAverageChange",
            "descrizione": "Variazione da media 50gg",
            "spiegazione": "Differenza tra prezzo corrente e media mobile 50 giorni."
        },
        {
            "campo": "twoHundredDayAverageChange",
            "descrizione": "Variazione da media 200gg",
            "spiegazione": "Differenza tra prezzo corrente e media mobile 200 giorni."
        }
    ]
    
    df_tech = pd.DataFrame(technical_data)
    st.dataframe(df_tech, use_container_width=True)

def show_company_info():
    st.header("🏢 Informazioni Aziendali Dettagliate")
    
    company_data = [
        {
            "campo": "sector",
            "descrizione": "Settore di appartenenza",
            "esempio": "Technology, Healthcare, Financial Services",
            "utilità": "Classificazione macro-settoriale per comparazioni"
        },
        {
            "campo": "industry",
            "descrizione": "Industria specifica",
            "esempio": "Consumer Electronics, Biotechnology",
            "utilità": "Sotto-categoria più specifica del settore"
        },
        {
            "campo": "fullTimeEmployees",
            "descrizione": "Dipendenti a tempo pieno",
            "esempio": "147000",
            "utilità": "Dimensione aziendale e confronti settoriali"
        },
        {
            "campo": "longBusinessSummary",
            "descrizione": "Descrizione business completa",
            "esempio": "Descrizione dettagliata dell'attività aziendale",
            "utilità": "Comprensione del modello di business"
        },
        {
            "campo": "website",
            "descrizione": "Sito web aziendale",
            "esempio": "https://www.apple.com",
            "utilità": "Link diretto al sito ufficiale"
        },
        {
            "campo": "phone",
            "descrizione": "Numero di telefono",
            "esempio": "408 996 1010",
            "utilità": "Contatto investor relations"
        },
        {
            "campo": "address1",
            "descrizione": "Indirizzo sede principale",
            "esempio": "One Apple Park Way",
            "utilità": "Localizzazione geografica"
        },
        {
            "campo": "city",
            "descrizione": "Città sede",
            "esempio": "Cupertino",
            "utilità": "Ubicazione geografica"
        },
        {
            "campo": "state",
            "descrizione": "Stato/Provincia",
            "esempio": "CA",
            "utilità": "Giurisdizione fiscale e regolamentare"
        },
        {
            "campo": "zip",
            "descrizione": "Codice postale",
            "esempio": "95014",
            "utilità": "Indirizzo completo"
        },
        {
            "campo": "country",
            "descrizione": "Paese sede legale",
            "esempio": "United States",
            "utilità": "Giurisdizione e analisi geografica"
        }
    ]
    
    df_company = pd.DataFrame(company_data)
    st.dataframe(df_company, use_container_width=True)
    
    st.subheader("👥 Management e Governance")
    management_data = [
        {
            "campo": "companyOfficers",
            "descrizione": "Lista dirigenti aziendali",
            "contenuto": "Nome, ruolo, età, compenso totale",
            "utilità": "Analisi del management team"
        },
        {
            "campo": "governanceEpochDate",
            "descrizione": "Data aggiornamento governance",
            "contenuto": "Timestamp ultimo aggiornamento",
            "utilità": "Freschezza dei dati governance"
        },
        {
            "campo": "compensationRisk",
            "descrizione": "Rischio compensi",
            "contenuto": "Score 1-10",
            "utilità": "Valutazione politiche retributive"
        },
        {
            "campo": "auditRisk",
            "descrizione": "Rischio audit",
            "contenuto": "Score 1-10",
            "utilità": "Qualità controlli contabili"
        },
        {
            "campo": "boardRisk",
            "descrizione": "Rischio board",
            "contenuto": "Score 1-10",
            "utilità": "Efficacia consiglio amministrazione"
        },
        {
            "campo": "shareHolderRightsRisk",
            "descrizione": "Rischio diritti azionisti",
            "contenuto": "Score 1-10",
            "utilità": "Protezione interessi azionisti"
        }
    ]
    
    df_mgmt = pd.DataFrame(management_data)
    st.dataframe(df_mgmt, use_container_width=True)

def show_historical_data():
    st.header("📋 Dati Storici Disponibili")
    
    st.subheader("🕐 Periodi Disponibili")
    periods_info = [
        {
            "periodo": "1d",
            "descrizione": "1 giorno",
            "dettaglio": "Dati intraday con intervalli di 1m, 2m, 5m, 15m, 30m, 60m, 90m"
        },
        {
            "periodo": "5d",
            "descrizione": "5 giorni",
            "dettaglio": "Dati recenti con alta granularità"
        },
        {
            "periodo": "1mo",
            "descrizione": "1 mese",
            "dettaglio": "Ultimo mese di trading"
        },
        {
            "periodo": "3mo",
            "descrizione": "3 mesi",
            "dettaglio": "Trimestre corrente"
        },
        {
            "periodo": "6mo",
            "descrizione": "6 mesi",
            "dettaglio": "Semestre corrente"
        },
        {
            "periodo": "1y",
            "descrizione": "1 anno",
            "dettaglio": "Ultimi 12 mesi"
        },
        {
            "periodo": "2y",
            "descrizione": "2 anni",
            "dettaglio": "Dati biennali"
        },
        {
            "periodo": "5y",
            "descrizione": "5 anni",
            "dettaglio": "Quinquennio"
        },
        {
            "periodo": "10y",
            "descrizione": "10 anni",
            "dettaglio": "Decennio"
        },
        {
            "periodo": "ytd",
            "descrizione": "Year-to-date",
            "dettaglio": "Dall'inizio dell'anno"
        },
        {
            "periodo": "max",
            "descrizione": "Massimo disponibile",
            "dettaglio": "Tutti i dati storici disponibili"
        }
    ]
    
    df_periods = pd.DataFrame(periods_info)
    st.dataframe(df_periods, use_container_width=True)
    
    st.subheader("📊 Dati Contenuti nei Prezzi Storici")
    historical_fields = [
        {
            "campo": "Open",
            "descrizione": "Prezzo di apertura",
            "utilità": "Primo prezzo della sessione di trading"
        },
        {
            "campo": "High",
            "descrizione": "Prezzo massimo",
            "utilità": "Prezzo più alto raggiunto nel periodo"
        },
        {
            "campo": "Low",
            "descrizione": "Prezzo minimo",
            "utilità": "Prezzo più basso raggiunto nel periodo"
        },
        {
            "campo": "Close",
            "descrizione": "Prezzo di chiusura",
            "utilità": "Ultimo prezzo della sessione"
        },
        {
            "campo": "Adj Close",
            "descrizione": "Prezzo aggiustato",
            "utilità": "Prezzo corretto per split e dividendi"
        },
        {
            "campo": "Volume",
            "descrizione": "Volume scambiato",
            "utilità": "Numero di azioni scambiate nel periodo"
        }
    ]
    
    df_hist = pd.DataFrame(historical_fields)
    st.dataframe(df_hist, use_container_width=True)
    
    st.info("""
    💡 **Nota sui Prezzi Aggiustati**: 
    I prezzi 'Adj Close' sono essenziali per analisi accurate perché tengono conto di:
    - **Stock Split**: Divisioni delle azioni
    - **Dividendi**: Pagamenti agli azionisti  
    - **Spin-off**: Separazioni aziendali
    
    Usa sempre 'Adj Close' per calcoli di rendimento e analisi tecniche.
    """)

def show_options_data():
    st.header("🎯 Dati delle Opzioni")
    
    st.subheader("📅 Date di Scadenza")
    st.write("""
    **`ticker.options`** restituisce tutte le date di scadenza disponibili come lista di stringhe.
    
    Esempio: `['2024-01-19', '2024-01-26', '2024-02-02', ...]`
    """)
    
    st.subheader("📋 Dati Call Options")
    call_fields = [
        {
            "campo": "contractSymbol",
            "descrizione": "Simbolo univoco del contratto",
            "esempio": "AAPL240119C00180000"
        },
        {
            "campo": "strike",
            "descrizione": "Prezzo di esercizio",
            "esempio": "180.0"
        },
        {
            "campo": "lastPrice",
            "descrizione": "Ultimo prezzo negoziato",
            "esempio": "5.25"
        },
        {
            "campo": "bid",
            "descrizione": "Prezzo di acquisto",
            "esempio": "5.20"
        },
        {
            "campo": "ask",
            "descrizione": "Prezzo di vendita",
            "esempio": "5.30"
        },
        {
            "campo": "change",
            "descrizione": "Variazione giornaliera",
            "esempio": "+0.15"
        },
        {
            "campo": "percentChange",
            "descrizione": "Variazione percentuale",
            "esempio": "2.95%"
        },
        {
            "campo": "volume",
            "descrizione": "Volume scambiato",
            "esempio": "1250"
        },
        {
            "campo": "openInterest",
            "descrizione": "Interesse aperto",
            "esempio": "3450"
        },
        {
            "campo": "impliedVolatility",
            "descrizione": "Volatilità implicita",
            "esempio": "0.2150"
        },
        {
            "campo": "inTheMoney",
            "descrizione": "In the money (boolean)",
            "esempio": "True/False"
        },
        {
            "campo": "contractSize",
            "descrizione": "Dimensione contratto",
            "esempio": "REGULAR"
        },
        {
            "campo": "currency",
            "descrizione": "Valuta",
            "esempio": "USD"
        },
        {
            "campo": "lastTradeDate",
            "descrizione": "Data ultimo scambio",
            "esempio": "2024-01-15"
        }
    ]
    
    df_calls = pd.DataFrame(call_fields)
    st.dataframe(df_calls, use_container_width=True)
    
    st.subheader("📉 Dati Put Options")
    st.write("I Put Options contengono gli stessi campi delle Call, ma rappresentano il diritto di **vendere** invece che acquistare.")
    
    st.subheader("🔧 Metodi per Accedere ai Dati")
    
    code_example = '''
# Esempio di utilizzo completo delle opzioni
import yfinance as yf

ticker = yf.Ticker("AAPL")

# Ottieni tutte le date di scadenza
expirations = ticker.options
print("Date disponibili:", expirations)

# Scegli una data specifica
exp_date = expirations[0]

# Ottieni la chain completa
option_chain = ticker.option_chain(exp_date)

# Accedi a calls e puts
calls = option_chain.calls
puts = option_chain.puts

# Filtra per volume minimo
high_volume_calls = calls[calls['volume'] > 100]

# Opzioni in the money
itm_calls = calls[calls['inTheMoney'] == True]

# Ordina per volatilità implicita
sorted_by_iv = calls.sort_values('impliedVolatility', ascending=False)
'''
    
    st.code(code_example, language='python')

def show_financial_statements():
    st.header("💼 Bilanci e Statements Finanziari")
    
    st.subheader("📊 Income Statement (Conto Economico)")
    st.write("Accessibile tramite `ticker.financials` (annuale) e `ticker.quarterly_financials` (trimestrale)")
    
    income_fields = [
        {
            "campo": "Total Revenue",
            "descrizione": "Ricavi totali",
            "significato": "Vendite complessive dell'azienda"
        },
        {
            "campo": "Cost Of Revenue",
            "descrizione": "Costo dei ricavi",
            "significato": "Costi diretti per produrre beni/servizi venduti"
        },
        {
            "campo": "Gross Profit",
            "descrizione": "Utile lordo",
            "significato": "Ricavi - Costo dei ricavi"
        },
        {
            "campo": "Operating Income",
            "descrizione": "Reddito operativo",
            "significato": "Utile dalle operazioni principali"
        },
        {
            "campo": "Net Income",
            "descrizione": "Utile netto",
            "significato": "Profitto finale dopo tutte le spese"
        },
        {
            "campo": "EBITDA",
            "descrizione": "EBITDA",
            "significato": "Utili prima di interessi, tasse, deprezzamenti"
        },
        {
            "campo": "Diluted EPS",
            "descrizione": "Utile per azione diluito",
            "significato": "Utile netto / azioni totali (incluse potenziali)"
        },
        {
            "campo": "Basic EPS",
            "descrizione": "Utile per azione base",
            "significato": "Utile netto / azioni in circolazione"
        }
    ]
    
    df_income = pd.DataFrame(income_fields)
    st.dataframe(df_income, use_container_width=True)
    
    st.subheader("🏦 Balance Sheet (Stato Patrimoniale)")
    st.write("Accessibile tramite `ticker.balance_sheet` (annuale) e `ticker.quarterly_balance_sheet` (trimestrale)")
    
    balance_fields = [
        {
            "campo": "Total Assets",
            "descrizione": "Attività totali",
            "significato": "Tutti i beni posseduti dall'azienda"
        },
        {
            "campo": "Current Assets",
            "descrizione": "Attività correnti",
            "significato": "Beni convertibili in cash entro 1 anno"
        },
        {
            "campo": "Cash And Cash Equivalents",
            "descrizione": "Liquidità",
            "significato": "Denaro disponibile immediatamente"
        },
        {
            "campo": "Total Liabilities Net Minority Interest",
            "descrizione": "Passività totali",
            "significato": "Tutti i debiti dell'azienda"
        },
        {
            "campo": "Current Liabilities",
            "descrizione": "Passività correnti",
            "significato": "Debiti da pagare entro 1 anno"
        },
        {
            "campo": "Total Equity Gross Minority Interest",
            "descrizione": "Patrimonio netto",
            "significato": "Valore residuo per gli azionisti"
        },
        {
            "campo": "Retained Earnings",
            "descrizione": "Utili non distribuiti",
            "significato": "Profitti accumulati e reinvestiti"
        },
        {
            "campo": "Inventory",
            "descrizione": "Rimanenze",
            "significato": "Valore delle scorte di magazzino"
        }
    ]
    
    df_balance = pd.DataFrame(balance_fields)
    st.dataframe(df_balance, use_container_width=True)

def show_cash_flow():
    st.header("📊 Cash Flow Statement (Rendiconto Flussi di Cassa)")
    st.write("Accessibile tramite `ticker.cashflow` (annuale) e `ticker.quarterly_cashflow` (trimestrale)")
    
    cashflow_fields = [
        {
            "categoria": "💰 Flussi Operativi",
            "campo": "Operating Cash Flow",
            "descrizione": "Flusso di cassa operativo",
            "significato": "Liquidità generata dalle operazioni principali"
        },
        {
            "categoria": "💰 Flussi Operativi",
            "campo": "Net Income",
            "descrizione": "Utile netto",
            "significato": "Punto di partenza per il calcolo dei flussi"
        },
        {
            "categoria": "💰 Flussi Operativi",
            "campo": "Depreciation And Amortization",
            "descrizione": "Ammortamenti",
            "significato": "Costi non monetari da riaggiungere"
        },
        {
            "categoria": "💰 Flussi Operativi",
            "campo": "Change In Working Capital",
            "descrizione": "Variazione capitale circolante",
            "significato": "Impatto delle variazioni di crediti/debiti"
        },
        {
            "categoria": "🏗️ Flussi Investimento",
            "campo": "Investing Cash Flow",
            "descrizione": "Flusso di cassa da investimenti",
            "significato": "Liquidità usata/generata da investimenti"
        },
        {
            "categoria": "🏗️ Flussi Investimento",
            "campo": "Capital Expenditure",
            "descrizione": "Investimenti in capitale fisso",
            "significato": "Spese per impianti, macchinari, tecnologia"
        },
        {
            "categoria": "🏗️ Flussi Investimento",
            "campo": "Investments In Other Ventures",
            "descrizione": "Altri investimenti",
            "significato": "Acquisizioni, partecipazioni, joint venture"
        },
        {
            "categoria": "💳 Flussi Finanziamento",
            "campo": "Financing Cash Flow",
            "descrizione": "Flusso di cassa da finanziamento",
            "significato": "Liquidità da/per azionisti e creditori"
        },
        {
            "categoria": "💳 Flussi Finanziamento",
            "campo": "Common Stock Dividends Paid",
            "descrizione": "Dividendi pagati",
            "significato": "Distribuzioni di utili agli azionisti"
        },
        {
            "categoria": "💳 Flussi Finanziamento",
            "campo": "Repurchase Of Capital Stock",
            "descrizione": "Riacquisto azioni proprie",
            "significato": "Programmi di buyback"
        },
        {
            "categoria": "💳 Flussi Finanziamento",
            "campo": "Issuance Of Debt",
            "descrizione": "Emissione debiti",
            "significato": "Nuovi prestiti e obbligazioni"
        },
        {
            "categoria": "💳 Flussi Finanziamento",
            "campo": "Repayment Of Debt",
            "descrizione": "Rimborso debiti",
            "significato": "Pagamento di prestiti e obbligazioni"
        }
    ]
    
    df_cashflow = pd.DataFrame(cashflow_fields)
    st.dataframe(df_cashflow, use_container_width=True)
    
    st.subheader("🔍 Free Cash Flow - Calcolo")
    st.write("""
    Il **Free Cash Flow** è una metrica fondamentale che rappresenta la liquidità disponibile dopo gli investimenti necessari:
    
    **Formula**: `Free Cash Flow = Operating Cash Flow - Capital Expenditure`
    
    - **Positivo**: L'azienda genera liquidità in eccesso
    - **Negativo**: L'azienda consuma più liquidità di quella che genera
    - **Crescente**: Trend positivo nella generazione di cassa
    """)

def show_growth_dividends():
    st.header("📈 Crescita e Dividendi")
    
    st.subheader("📊 Metriche di Crescita")
    growth_fields = [
        {
            "campo": "revenueGrowth",
            "descrizione": "Crescita ricavi",
            "calcolo": "(Ricavi Anno Corrente - Ricavi Anno Precedente) / Ricavi Anno Precedente",
            "interpretazione": "Tasso di crescita delle vendite year-over-year"
        },
        {
            "campo": "earningsGrowth",
            "descrizione": "Crescita utili",
            "calcolo": "(Utili Anno Corrente - Utili Anno Precedente) / Utili Anno Precedente",
            "interpretazione": "Tasso di crescita degli utili year-over-year"
        },
        {
            "campo": "earningsQuarterlyGrowth",
            "descrizione": "Crescita utili trimestrale",
            "calcolo": "Crescita utili ultimo trimestre vs stesso trimestre anno precedente",
            "interpretazione": "Crescita più recente degli utili"
        },
        {
            "campo": "revenueQuarterlyGrowth",
            "descrizione": "Crescita ricavi trimestrale",
            "calcolo": "Crescita ricavi ultimo trimestre vs stesso trimestre anno precedente",
            "interpretazione": "Crescita più recente dei ricavi"
        }
    ]
    
    df_growth = pd.DataFrame(growth_fields)
    st.dataframe(df_growth, use_container_width=True)
    
    st.subheader("💰 Informazioni sui Dividendi")
    dividend_fields = [
        {
            "campo": "dividendRate",
            "descrizione": "Tasso dividendo annuale",
            "esempio": "0.92",
            "significato": "Dividendo annuale per azione in dollari"
        },
        {
            "campo": "dividendYield",
            "descrizione": "Rendimento dividendo",
            "esempio": "0.0052 (0.52%)",
            "significato": "Dividendo annuale / Prezzo corrente"
        },
        {
            "campo": "exDividendDate",
            "descrizione": "Data ex-dividendo",
            "esempio": "2024-02-09",
            "significato": "Ultima data per ricevere il prossimo dividendo"
        },
        {
            "campo": "payoutRatio",
            "descrizione": "Payout ratio",
            "esempio": "0.15 (15%)",
            "significato": "Percentuale di utili distribuita come dividendi"
        },
        {
            "campo": "fiveYearAvgDividendYield",
            "descrizione": "Rendimento medio 5 anni",
            "esempio": "0.0048",
            "significato": "Dividend yield medio degli ultimi 5 anni"
        },
        {
            "campo": "trailingAnnualDividendRate",
            "descrizione": "Dividendo trailing annuale",
            "esempio": "0.92",
            "significato": "Dividendi pagati negli ultimi 12 mesi"
        },
        {
            "campo": "trailingAnnualDividendYield",
            "descrizione": "Yield trailing annuale",
            "esempio": "0.0052",
            "significato": "Yield basato sui dividendi ultimi 12 mesi"
        }
    ]
    
    df_dividends = pd.DataFrame(dividend_fields)
    st.dataframe(df_dividends, use_container_width=True)
    
    st.subheader("📅 Dati Storici Dividendi")
    st.write("""
    I dati storici dei dividendi sono accessibili tramite:
    
    ```python
    # Dividendi storici
    dividends = ticker.dividends
    
    # Stock splits storici
    splits = ticker.splits
    ```
    
    **Contenuto**:
    - **Date**: Date di pagamento dividendi
    - **Amounts**: Importi per azione
    - **Split Ratios**: Rapporti di frazionamento (es. 2:1, 3:2)
    """)

def show_technical_analysis():
    st.header("🔍 Dati per Analisi Tecnica")
    
    st.subheader("📈 Indicatori di Momentum")
    momentum_indicators = [
        {
            "indicatore": "RSI (Relative Strength Index)",
            "calcolo": "Non diretto - calcolabile dai prezzi storici",
            "interpretazione": "RSI > 70 = ipercomprato, RSI < 30 = ipervenduto",
            "periodo": "Tipicamente 14 giorni"
        },
        {
            "indicatore": "MACD",
            "calcolo": "EMA(12) - EMA(26)",
            "interpretazione": "Crossover segnalano cambi di trend",
            "periodo": "12, 26, 9 giorni standard"
        },
        {
            "indicatore": "Stochastic Oscillator",
            "calcolo": "(Close - Low) / (High - Low) * 100",
            "interpretazione": "> 80 ipercomprato, < 20 ipervenduto",
            "periodo": "14 giorni tipicamente"
        }
    ]
    
    df_momentum = pd.DataFrame(momentum_indicators)
    st.dataframe(df_momentum, use_container_width=True)
    
    st.subheader("📊 Medie Mobili Disponibili")
    ma_data = [
        {
            "campo": "fiftyDayAverage",
            "descrizione": "Media mobile 50 giorni",
            "utilizzo": "Trend di medio termine, supporto/resistenza"
        },
        {
            "campo": "twoHundredDayAverage",
            "descrizione": "Media mobile 200 giorni",
            "utilizzo": "Trend di lungo termine, bull/bear market"
        }
    ]
    
    df_ma = pd.DataFrame(ma_data)
    st.dataframe(df_ma, use_container_width=True)
    
    st.subheader("📐 Bande di Bollinger e Volatilità")
    volatility_data = [
        {
            "metrica": "Bollinger Bands",
            "calcolo": "Media Mobile ± (2 × Deviazione Standard)",
            "interpretazione": "Prezzi vicini alle bande indicano possibili inversioni",
            "dati_necessari": "Close prices per calcolo"
        },
        {
            "metrica": "Average True Range (ATR)",
            "calcolo": "Media dei True Range su N periodi",
            "interpretazione": "Misura la volatilità del titolo",
            "dati_necessari": "High, Low, Close prices"
        },
        {
            "metrica": "Volatilità Storica",
            "calcolo": "Deviazione standard dei rendimenti",
            "interpretazione": "Volatilità passata del titolo",
            "dati_necessari": "Close prices storici"
        }
    ]
    
    df_vol = pd.DataFrame(volatility_data)
    st.dataframe(df_vol, use_container_width=True)
    
    st.subheader("🎯 Livelli di Supporto e Resistenza")
    support_resistance = [
        {
            "livello": "52 Week High",
            "campo_yahoo": "52WeekHigh",
            "utilizzo": "Resistenza psicologica forte"
        },
        {
            "livello": "52 Week Low",
            "campo_yahoo": "52WeekLow",
            "utilizzo": "Supporto psicologico forte"
        },
        {
            "livello": "Media Mobile 200",
            "campo_yahoo": "twoHundredDayAverage",
            "utilizzo": "Supporto/resistenza dinamica long-term"
        },
        {
            "livello": "Media Mobile 50",
            "campo_yahoo": "fiftyDayAverage",
            "utilizzo": "Supporto/resistenza dinamica medium-term"
        }
    ]
    
    df_sr = pd.DataFrame(support_resistance)
    st.dataframe(df_sr, use_container_width=True)

def show_esg_data():
    st.header("🌍 Dati ESG (Environmental, Social, Governance)")
    
    st.subheader("🌱 Environmental (Ambientali)")
    env_fields = [
        {
            "campo": "environmentScore",
            "descrizione": "Punteggio ambientale",
            "range": "1-100",
            "significato": "Performance su temi ambientali"
        },
        {
            "campo": "socialScore",
            "descrizione": "Punteggio sociale",
            "range": "1-100",
            "significato": "Performance su responsabilità sociale"
        },
        {
            "campo": "governanceScore",
            "descrizione": "Punteggio governance",
            "range": "1-100",
            "significato": "Qualità della governance aziendale"
        },
        {
            "campo": "totalEsg",
            "descrizione": "Punteggio ESG totale",
            "range": "1-100",
            "significato": "Score complessivo ESG"
        },
        {
            "campo": "esgPerformance",
            "descrizione": "Performance ESG",
            "valori": "UNDER_PERF, AVG_PERF, OUT_PERF",
            "significato": "Performance relativa nel settore"
        }
    ]
    
    df_esg = pd.DataFrame(env_fields)
    st.dataframe(df_esg, use_container_width=True)
    
    st.subheader("🏆 Classificazioni ESG")
    st.write("""
    I punteggi ESG sono forniti da provider specializzati e indicano:
    
    **Environmental (E)**:
    - Emissioni di carbonio
    - Efficienza energetica  
    - Gestione rifiuti
    - Impatto sulla biodiversità
    
    **Social (S)**:
    - Relazioni con dipendenti
    - Sicurezza prodotti
    - Coinvolgimento comunità
    - Diversità e inclusione
    
    **Governance (G)**:
    - Struttura del board
    - Compensi executive
    - Diritti degli azionisti
    - Etica aziendale
    """)
    
    st.info("""
    ⚠️ **Nota**: I dati ESG potrebbero non essere disponibili per tutti i titoli.
    La disponibilità dipende dalla copertura del provider di dati ESG.
    """)

def show_usage_guide():
    st.header("💡 Come Utilizzare i Dati Yahoo Finance")
    
    st.subheader("🚀 Setup Base")
    setup_code = '''
import yfinance as yf
import pandas as pd

# Crea oggetto ticker
ticker = yf.Ticker("AAPL")

# Ottieni informazioni base
info = ticker.info
print(f"Nome: {info['longName']}")
print(f"Prezzo: ${info['currentPrice']}")
print(f"P/E: {info.get('trailingPE', 'N/A')}")
'''
    st.code(setup_code, language='python')
    
    st.subheader("📊 Accesso ai Dati Storici")
    historical_code = '''
# Dati storici con diversi periodi
hist_1y = ticker.history(period="1y")
hist_5y = ticker.history(period="5y")
hist_ytd = ticker.history(period="ytd")

# Dati storici con intervalli specifici
hist_1min = ticker.history(period="1d", interval="1m")
hist_1hour = ticker.history(period="5d", interval="1h")

# Dati tra date specifiche
from datetime import datetime, timedelta
start_date = datetime.now() - timedelta(days=365)
end_date = datetime.now()
hist_custom = ticker.history(start=start_date, end=end_date)
'''
    st.code(historical_code, language='python')
    
    st.subheader("💼 Financial Statements")
    statements_code = '''
# Bilanci
balance_sheet = ticker.balance_sheet  # Annuale
quarterly_balance = ticker.quarterly_balance_sheet  # Trimestrale

# Conto economico
income_stmt = ticker.financials  # Annuale
quarterly_income = ticker.quarterly_financials  # Trimestrale

# Flussi di cassa
cash_flow = ticker.cashflow  # Annuale
quarterly_cf = ticker.quarterly_cashflow  # Trimestrale

# Accesso a specifiche voci
try:
    total_revenue = income_stmt.loc['Total Revenue'].iloc[0]
    print(f"Ricavi ultimo anno: ${total_revenue:,.0f}")
except KeyError:
    print("Dato non disponibile")
'''
    st.code(statements_code, language='python')
    
    st.subheader("🎯 Gestione Opzioni")
    options_code = '''
# Date di scadenza disponibili
exp_dates = ticker.options
print("Scadenze disponibili:", exp_dates)

# Chain di opzioni per una data specifica
if exp_dates:
    exp_date = exp_dates[0]  # Prima scadenza
    option_chain = ticker.option_chain(exp_date)
    
    calls = option_chain.calls
    puts = option_chain.puts
    
    # Filtra opzioni liquide
    liquid_calls = calls[calls['volume'] > 50]
    
    # Opzioni vicine al prezzo corrente
    current_price = ticker.info['currentPrice']
    near_money = calls[
        (calls['strike'] >= current_price * 0.95) & 
        (calls['strike'] <= current_price * 1.05)
    ]
'''
    st.code(options_code, language='python')
    
    st.subheader("🔍 Gestione Errori e Dati Mancanti")
    error_handling_code = '''
def safe_get_info(ticker_symbol, field):
    """Funzione per accesso sicuro ai dati"""
    try:
        ticker = yf.Ticker(ticker_symbol)
        info = ticker.info
        return info.get(field, None)
    except Exception as e:
        print(f"Errore per {ticker_symbol}: {e}")
        return None

# Esempio di uso
pe_ratio = safe_get_info("AAPL", "trailingPE")
if pe_ratio:
    print(f"P/E Ratio: {pe_ratio:.2f}")
else:
    print("P/E Ratio non disponibile")

# Verifica disponibilità dati
def check_data_availability(symbol):
    ticker = yf.Ticker(symbol)
    info = ticker.info
    
    checks = {
        'Basic Info': info.get('longName') is not None,
        'Financial Ratios': info.get('trailingPE') is not None,
        'Options': len(ticker.options) > 0,
        'Dividends': len(ticker.dividends) > 0,
        'ESG': info.get('totalEsg') is not None
    }
    
    return checks

# Test disponibilità
availability = check_data_availability("AAPL")
for category, available in availability.items():
    status = "✅" if available else "❌"
    print(f"{status} {category}")
'''
    st.code(error_handling_code, language='python')
    
    st.subheader("📈 Calcoli Comuni")
    calculations_code = '''
import numpy as np

def calculate_returns(prices):
    """Calcola rendimenti percentuali"""
    return prices.pct_change().dropna()

def calculate_volatility(prices, window=30):
    """Calcola volatilità mobile"""
    returns = calculate_returns(prices)
    return returns.rolling(window=window).std() * np.sqrt(252)  # Annualizzata

def calculate_rsi(prices, window=14):
    """Calcola RSI"""
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def calculate_moving_averages(prices):
    """Calcola medie mobili multiple"""
    return {
        'MA_20': prices.rolling(window=20).mean(),
        'MA_50': prices.rolling(window=50).mean(),
        'MA_200': prices.rolling(window=200).mean()
    }

# Esempio di utilizzo
ticker = yf.Ticker("AAPL")
hist = ticker.history(period="1y")

# Calcoli
returns = calculate_returns(hist['Close'])
volatility = calculate_volatility(hist['Close'])
rsi = calculate_rsi(hist['Close'])
mas = calculate_moving_averages(hist['Close'])

print(f"Rendimento medio giornaliero: {returns.mean():.4f}")
print(f"Volatilità corrente: {volatility.iloc[-1]:.4f}")
print(f"RSI corrente: {rsi.iloc[-1]:.2f}")
'''
    st.code(calculations_code, language='python')
    
    st.subheader("⚠️ Limitazioni e Considerazioni")
    st.warning("""
    **Limitazioni Yahoo Finance**:
    
    1. **Rate Limiting**: Evita troppe richieste simultanee
    2. **Dati Real-time**: Ritardo di 15-20 minuti per dati gratuiti
    3. **Disponibilità**: Non tutti i campi sono disponibili per tutti i titoli
    4. **Accuratezza**: Verifica sempre dati critici con fonti ufficiali
    5. **Delisting**: Titoli rimossi dalla quotazione hanno dati limitati
    
    **Best Practices**:
    - Implementa sempre gestione errori
    - Cache i dati per evitare richieste ripetute  
    - Valida i dati prima dell'uso
    - Usa timeout nelle richieste
    - Considera API alternative per uso professionale
    """)

def show_example_data(symbol):
    """Mostra dati di esempio per il simbolo inserito"""
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        
        if not info or info.get('longName') == 'N/A':
            st.error(f"❌ Simbolo '{symbol}' non trovato")
            return
            
        st.success(f"✅ Dati trovati per {symbol}")
        
        # Informazioni base
        st.subheader("📊 Informazioni Base")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write(f"**Nome**: {info.get('longName', 'N/A')}")
            st.write(f"**Settore**: {info.get('sector', 'N/A')}")
            st.write(f"**Prezzo**: ${info.get('currentPrice', 0):.2f}")
        
        with col2:
            st.write(f"**P/E**: {info.get('trailingPE', 'N/A')}")
            st.write(f"**Market Cap**: {info.get('marketCap', 'N/A')}")
            st.write(f"**Beta**: {info.get('beta', 'N/A')}")
        
        # Dati disponibili
        st.subheader("🔍 Disponibilità Dati")
        checks = {
            'Dati Storici': len(ticker.history(period="5d")) > 0,
            'Opzioni': len(ticker.options) > 0,
            'Dividendi': len(ticker.dividends) > 0,
            'Bilanci': hasattr(ticker, 'balance_sheet') and not ticker.balance_sheet.empty,
            'Flussi Cassa': hasattr(ticker, 'cashflow') and not ticker.cashflow.empty,
            'Dati ESG': info.get('totalEsg') is not None
        }
        
        for category, available in checks.items():
            status = "✅" if available else "❌"
            st.write(f"{status} {category}")
            
    except Exception as e:
        st.error(f"❌ Errore nel recupero dati: {e}")

if __name__ == "__main__":
    main()
