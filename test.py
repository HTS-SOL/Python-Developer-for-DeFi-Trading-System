import streamlit as st
import pandas as pd
import numpy as np
import time
import asyncio

st.sidebar.title("📊 HFT Trading System (Demo)")
menu = st.sidebar.radio("Select Option", ["📈 Live Market Data", "🤖 Automated Trading", "⚠️ Risk Management", "📜 Trading Logs"])

st.sidebar.subheader("🔧 Trading Settings")
trading_pair = st.sidebar.text_input("Trading Pair", "ETH/USDT")
trade_amount = st.sidebar.number_input("Trade Amount", min_value=0.01, value=0.1)
stop_loss = st.sidebar.number_input("Stop-Loss (%)", min_value=0.1, value=2.0)

def get_demo_price():
    return round(np.random.uniform(1800, 2300), 2)  

def execute_trade(order_type, price):
    if order_type == "buy":
        st.success(f"✅ Buying {trade_amount} {trading_pair} at ${price}")
    elif order_type == "sell":
        st.warning(f"⚠️ Selling {trade_amount} {trading_pair} at ${price}")

async def trading_bot():
    st.write("🚀 Bot started monitoring the market...")
    while True:
        price = get_demo_price()
        st.write(f"🔍 Checking price... Current: ${price}")
        if price < stop_loss_price:
            st.error(f"🚨 Stop-loss triggered! Selling at ${price}")
            execute_trade("sell", price)
            break
        elif price > buy_threshold:
            st.success(f"✅ Target reached! Selling at ${price}")
            execute_trade("sell", price)
            break
        await asyncio.sleep(3)  
def risk_management():
    st.subheader("⚠️ Risk Management")
    volatility = round(np.random.uniform(0.5, 5.0), 2)  
    portfolio_value = round(np.random.uniform(5000, 10000), 2)  
    st.write(f"📉 Market Volatility: {volatility}%")
    st.write(f"💰 Portfolio Value: ${portfolio_value}")

def show_logs():
    st.subheader("📜 Trading Logs (Demo)")
    logs = [
        {"Time": time.strftime("%Y-%m-%d %H:%M:%S"), "Action": "BUY", "Price": 1950},
        {"Time": time.strftime("%Y-%m-%d %H:%M:%S"), "Action": "SELL", "Price": 2150}
    ]
    df = pd.DataFrame(logs)
    st.table(df)
if menu == "📈 Live Market Data":
    st.subheader("📈 Live Market Data (Simulated)")
    if st.button("Fetch Price"):
        price = get_demo_price()
        st.write(f"Current {trading_pair} Price: ${price}")

elif menu == "🤖 Automated Trading":
    st.subheader("🤖 Automated Trading Bot (Demo)")
    buy_threshold = st.number_input("Target Price to Sell", min_value=0.1, value=2200.0)
    stop_loss_price = st.number_input("Stop-Loss Price", min_value=0.1, value=1900.0)

    if st.button("Start Trading Bot"):
        asyncio.run(trading_bot())

    st.write("Bot will simulate market activity and execute trades.")

elif menu == "⚠️ Risk Management":
    risk_management()

elif menu == "📜 Trading Logs":
    show_logs()
