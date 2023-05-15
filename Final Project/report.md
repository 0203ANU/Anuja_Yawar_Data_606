## Amazon Stock Prediction - Time Series

![Stock](stock_photo.jpg)

Link to youtube video - https://www.youtube.com/watch?v=2i5jqzMqr5c

Link to PPT - https://1drv.ms/p/s!Atx5QosFxCRboU28bL8xwhldAgsl

### Abstract 

In this project, we have developed an application for stock market prediction that utilizes machine learning models such as ARIMA, LSTM, and Prophet. These models enable accurate forecasting of stock price movements. 
To ensure the project's reliability and incorporate the latest market information, we have utilized data from the Yahoo Finance API and StockNews API. Ultimately, we have created a web application using Streamlit that allows users to forecast the stock price of any given stock.<br><br>

### Introduction 

We aim to create a robust machine learning model capable of effectively forecasting future stock price movements using historical data and relevant variables. The model will be designed to handle the intricate and unpredictable nature of the stock market, providing dependable predictions for various stocks and indices. 
The objective is to assist investors and financial institutions in making well-informed decisions, minimizing risks, and optimizing returns in the stock market.
<br><br>

### Data 

In this project, we have utilized the [YahooFinance API](https://finance.yahoo.com/) to retrieve data for our dataset. 
The dataset itself is dependent on user input, including the start date, end date, and ticker symbol, 
which are provided through the application's front-end. However, for the purpose of exploratory data analysis (EDA), we have specifically selected the AMZN (Amazon) stock data from May 15, 1997, to February 3, 2023.
The dataset includes the following fields:
- Date :-  Date <br>
- Open :- Price at which stocks start trading<br>
- High :- The Highest price of the stock on following day<br>
- Low :- The Lowest price of the stock on following day<br>
- Close :- Closing price of the stock<br>
- Volume :- Total number of the shares traded on that particular day<br>

<br><br>

### Data Preprocessing

**Data Retrieval**
<br>
Use the Yahoo Finance API to fetch the desired stock market data based on user input, such as the start date, end date, and ticker symbol.

**Data Cleaning**
<br>
We Checked for missing values, outliers, or any inconsistencies in the retrieved data. But it turns out that the data was clean and there was no missing potential value.

**Feature Selection**
<br>
Identify the relevant features for our analysis and model. Consider factors such as stock price, trading volume, open, high, and low.

### Algorithm 
**ARIMA**
<br>
ARIMA stands for Autoregressive Integrated Moving Average. 
It is a time series forecasting model that combines autoregression (AR), differencing (I), and moving average (MA) components to make predictions about future values in a time series.
To implement ARIMA, you need to specify three parameters: p, d, and q. These represent the order of the AR, I, and MA components, respectively. The p parameter specifies the number of lags to include in the AR component, while the q parameter specifies the number of error terms to include in the MA component. The d parameter specifies the number of times the time series needs to be differenced to achieve stationarity
<br>
**LSTM**
<br>
LSTM (Long Short-Term Memory) is a type of recurrent neural network (RNN) architecture that is widely used in sequence prediction tasks, such as time series forecasting. It addresses the limitations of traditional RNNs by introducing a memory cell and three gating mechanisms: the input gate, forget gate, and output gate.
<br>
**Phrophet**
<br>
We have also implemented another model called Prophet but it is directly implemented in Streamlit. 
Prophet is open source software released by Facebook’s Core Data Science team.
Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well.

<br><br>

### Conclusion
- One key lesson is that stock market prediction is an extremely difficult task. While historical trends and patterns can be useful indicators, the stock 
market is influenced by a multitude of unpredictable factors, such as economic conditions, geopolitical events, and natural disasters, among others. 
This complexity makes it challenging to accurately predict stock market trends over the long-term, and even short-term predictions can be subject to 
significant uncertainty.

- Another important insight is that data analysis and machine learning techniques can be valuable tools for making informed investment decisions. 
By analyzing historical stock data and identifying patterns, investors can gain insights into market trends and make more informed decisions about
when to buy or sell stocks. However, it is important to recognize that no model is perfect, and even the most advanced machine learning algorithms 
have limitations and potential sources of error. Investors should always use caution and conduct thorough research before making investment decisions.







