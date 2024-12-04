import yfinance
import pandas as pd

# baixar informações do dólar de 10 anos atrás até hj (2014 a 2024)
data = yfinance.download("USDBRL=X", start="2014-01-01", end="2024-06-30")
data = data[['Close']].reset_index()
data.columns = ['Date', 'USD_BRL']

data.to_csv("datasets/dolarData.csv", index=False)
print("[*] dataset salvo com sucesso.")