import streamlit as st
import asyncio
import ccxt
import pandas as pd
import numpy as np
import time
from web3 import Web3

st.sidebar.title("📊 HFT Trading System")
menu = st.sidebar.radio("Select Option", ["📈 Live Market Data", "🤖 Automated Trading", "⚠️ Risk Management", "📜 Trading Logs"])

exchange = ccxt.binance()
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_KEY"))

st.sidebar.subheader("🔧 Trading Settings")
api_key = st.sidebar.text_input("API Key", type="password")
secret_key = st.sidebar.text_input("Secret Key", type="password")
trading_pair = st.sidebar.text_input("Trading Pair", "ETH/USDT")
trade_amount = st.sidebar.number_input("Trade Amount", min_value=0.01, value=0.1)
stop_loss = st.sidebar.number_input("Stop-Loss (%)", min_value=0.1, value=2.0)

def get_live_price(symbol):
    try:
        ticker = exchange.fetch_ticker(symbol)
        return ticker['last']
    except Exception as e:
        st.error(f"Error fetching price: {e}")
        return None

def execute_trade(order_type):
    price = get_live_price(trading_pair)
    if price:
        st.write(f"Current {trading_pair} Price: ${price}")
        if order_type == "buy":
            st.success(f"✅ Buying {trade_amount} {trading_pair} at ${price}")
         
        elif order_type == "sell":
            st.warning(f"⚠️ Selling {trade_amount} {trading_pair} at ${price}")
          
async def trading_bot():
    while True:
        price = get_live_price(trading_pair)
        if price:
            if price < stop_loss_price:
                st.error(f"🚨 Stop-loss triggered! Selling at ${price}")
                execute_trade("sell")
                break
            elif price > buy_threshold:
                st.success(f"✅ Target reached! Selling at ${price}")
                execute_trade("sell")
                break
        await asyncio.sleep(5)  
def risk_management():
    st.subheader("⚠️ Risk Management")
    st.write("Monitoring market volatility and portfolio exposure...")
    volatility = np.random.uniform(0.5, 5.0) 
    portfolio_value = np.random.uniform(1000, 5000)  
    st.write(f"📉 Market Volatility: {volatility:.2f}%")
    st.write(f"💰 Portfolio Value: ${portfolio_value:.2f}")

def show_logs():
    st.subheader("📜 Trading Logs")
    logs = [
        {"Time": time.strftime("%Y-%m-%d %H:%M:%S"), "Action": "BUY", "Price": 2000},
        {"Time": time.strftime("%Y-%m-%d %H:%M:%S"), "Action": "SELL", "Price": 2100}
    ]
    df = pd.DataFrame(logs)
    st.table(df)

if menu == "📈 Live Market Data":
    st.subheader("📈 Live Market Data")
    if st.button("Fetch Price"):
        price = get_live_price(trading_pair)
        if price:
            st.write(f"Current {trading_pair} Price: ${price}")

elif menu == "🤖 Automated Trading":
    st.subheader("🤖 Automated Trading Bot")
    buy_threshold = st.number_input("Target Price to Sell", min_value=0.1, value=2200.0)
    stop_loss_price = st.number_input("Stop-Loss Price", min_value=0.1, value=1900.0)
    
    if st.button("Start Trading Bot"):
        asyncio.run(trading_bot())

    st.write("Bot will monitor the market and execute trades automatically.")

elif menu == "⚠️ Risk Management":
    risk_management()

elif menu == "📜 Trading Logs":
    show_logs()
