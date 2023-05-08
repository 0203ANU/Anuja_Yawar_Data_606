import streamlit as st
from datetime import datetime,timedelta
from statsmodels.tsa.arima.model import ARIMA
import yfinance as yf
import pandas as pd
from stocknews import StockNews
from prophet import Prophet
from plotly import graph_objs as go

import requests


def get_symbol(symbol):
    company = yf.Ticker(symbol)
    company_name = company.info['longName']
    return company_name


preselected_date = datetime.now() - timedelta(days=365)
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://media.istockphoto.com/id/1473527034/photo/abstract-financial-graph-with-up-trend-line-chart-in-stock-market-on-grey-colour-background.jpg?s=612x612&w=is&k=20&c=ulip0J3O8qOBt8ZJq0PVtqIxp3j4tgUh_d4EXYSs3BU=");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
#add_bg_from_url()
st.title('Stock Forecast App')
selected_stock = st.sidebar.text_input('Select Stock for prediction',"AMZN")
start_date=st.sidebar.date_input("Start Date",preselected_date)
end_date=st.sidebar.date_input("End Date")




def load_data(ticker, start_date, end_date):
    data = yf.download(ticker, start_date, end_date)
    data.reset_index(inplace=True)
    return data


data_load_state = st.text('Loading data...')
data = load_data(selected_stock,start_date,end_date)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())


# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


plot_raw_data()
df_month=data
data_new=data
data_prophet=data
data_prophet=data_prophet.drop(['Open', 'High','Low','Adj Close',"Volume"], axis=1)
data_prophet = data_prophet.rename({'Date': 'ds', 'Close': 'y'}, axis='columns')
data_new.set_index('Date', inplace=True)
diff_stock = data_new.diff().dropna()
diff_train_len = int(len(diff_stock)*0.8)
diff_train = diff_stock[:diff_train_len]
diff_test = diff_stock[diff_train_len:]
forecast_arima=None
forecast_prophet=None

# Make predictions for the next 10 days
def arima_pred():
    try:
        model = ARIMA(data_new['Close'], order=(1 , 0 , 1))
        results = model.fit()
        forecast = results.forecast(steps=90)
        forecast_index = pd.date_range(data_new.index[-1], periods=90)
        forecast.index=forecast_index
        fig1 = go.Figure()
        fig1.add_trace(go.Line(x=data_new.index, y=data_new['Close'], name="stock_close"))
        fig1.add_trace(go.Line(x=forecast.index, y=forecast, name="Predicted"))
        forecast_arima=forecast
        fig1.layout.update(title_text='Forcasting of stock based on Arima Model', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig1)
    except Exception as e:
        st.subheader("Please select appropriate values")

def phrophet_pred():
    try:
        m = Prophet(daily_seasonality=True)
        m.fit(data_prophet)
        future = m.make_future_dataframe(periods=90)
        last_10days_data=future.tail(90)
        forecast = m.predict(future)
        last_10days_data_forecast=forecast.tail(90)
        fig2 = go.Figure()
        fig2.add_trace(go.Line(x=future.ds, y=forecast['trend'], name="stock_close"))
        fig2.add_trace(go.Line(x=last_10days_data.ds, y=last_10days_data_forecast['trend'], name="trend"))
        fig2.add_trace(go.Line(x=last_10days_data.ds, y=last_10days_data_forecast['trend_lower'], name="trend_lower"))
        fig2.add_trace(go.Line(x=last_10days_data.ds, y=last_10days_data_forecast['trend_upper'], name="trend_upper"))
        fig2.layout.update(title_text='Forcasting of stock based on Prophet  Model', xaxis_rangeslider_visible=True)
        st.plotly_chart(fig2)
        last_10days_data_forecast["Date"]=last_10days_data
        forecast_prophet=last_10days_data_forecast
    except Exception as e:
        st.subheader("Please select appropriate values")




prediction,news,technical_indicators=st.tabs(["Predictions","News","Technical Indicators"])
with prediction:
    st.header("Predictions")
    arima_pred()
    phrophet_pred()


with news:
    st.header(get_symbol(selected_stock)+" News")
    stock_n = StockNews([selected_stock] , save_news=False)
    dt_news=stock_n.read_rss()
    for i in range(10):
        st.subheader(dt_news['title'][i])
        st.write(dt_news['published'][i])
        #st.write(dt_news['title'][i])
        st.write(dt_news['summary'][i])

with technical_indicators:
    st.header("Candle stick chart")
    try:
        fig4 = go.Figure()
        fig4.add_trace(go.Candlestick(x = data_new.index, open = data_new['Open'], high = data_new['High'], low =data_new['Low'], close = data_new['Close']) )
        st.plotly_chart(fig4)
    except Exception as e:
        st.write("Loading...")











