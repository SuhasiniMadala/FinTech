import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sbn
ticker = ["AAPL","RELIANCE.NS"]
data=yf.download(ticker,period="1y",auto_adjust=True)
closings=data["Close"]
#print(closings.head())
returns=closings.pct_change(fill_method=None).dropna()
#print(returns.head())
sbn.set_theme(style="whitegrid")
plt.figure(figsize=(12,6))
sbn.histplot(returns["AAPL"],kde=True,label="AAPL",color="blue",alpha=0.5)
sbn.histplot(returns["RELIANCE.NS"],kde=True,label="RELIANCE",color="orange",alpha=0.5)
plt.title("Day 1: Daily Return Distribution (Risk analysis)",fontsize=16,color="green")
plt.xlabel("Daily return (%)")
plt.ylabel("Frequency")
plt.legend()
plt.show()
