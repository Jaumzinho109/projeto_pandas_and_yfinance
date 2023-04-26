import yfinance as yf
import pandas as pd


tickers = ['BBDC4.SA', 'BBAS3.SA', 'ITUB4.SA']

start_date = '2018-01-01'

end_date = '2023-04-01'


df = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
jls_extract_var = 'Adj Close'
df_mensal = df = yf.download(tickers, start=start_date, end=end_date).resample("Y").last()

retorno_mensal = df_mensal.pct_change()

df = pd.DataFrame(df)
print(df_mensal)