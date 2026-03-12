import pandas_ta as pta
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
ticker=['BTC-USD']
df=yf.download(ticker,period="6mo",interval="1d")
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)
df["SMA_20"]=pta.sma(df["Close"],length=20)
df['EMA_9']=pta.ema(df['Close'],length=9)
df['RSI']=pta.rsi(df['Close'],length=14)
# Plotting prices and moving averages
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
ax1.plot(df['Close'],color='black',alpha=0.5,label=f'{ticker[0]} Price')
ax1.plot(df['SMA_20'],color='blue',label='20 day SMA')
ax1.plot(df['EMA_9'],color='orange',label='9 day EMA')
ax1.legend()
ax2.plot(df['RSI'],color='purple',label=f'{ticker[0]} RSI')
ax2.axhline(70,color='red',linestyle='--')
ax2.axhline(30,color='green',linestyle='--')
ax2.set_xlabel('Date')
ax2.set_ylabel('RSI')
plt.tight_layout()
plt.show()
current_rsi=df['RSI'].iloc[-1]
print(f"Current RSI: {current_rsi:.2f}")
current_sma=df['SMA_20'].iloc[-1]
print(f"Current 20-day SMA: {current_sma:.2f}")
current_ema=df['EMA_9'].iloc[-1]
print(f"Current 9-day EMA: {current_ema:.2f}")
if(current_ema>current_sma and 60>current_rsi>=40):
    print("SIGNAL : STRONG BUY")
    print("REASON : Golden Cross confirmed and RSI has Room to Run")
elif(current_ema<current_sma or current_rsi>=70):
    print("SIGNAL : SELL/CAUTION")
    if(current_ema<current_sma):
         print("REASON : Death Cross Detected Trend is turning Bearish")
    if(current_rsi>=70):
         print("REASON : RSI is Overbought, Potential Reversal Risk")
else:
    print("SIGNAL : NO ACTION")
    print("REASON : Market is Chilling or the signals are conflicting")              


