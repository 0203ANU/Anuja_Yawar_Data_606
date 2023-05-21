## Amazon Stock Prediction - Time Series

![Stock](stock_photo.jpg)

Link to youtube video - https://www.youtube.com/watch?v=2i5jqzMqr5c

Link to PPT - https://1drv.ms/p/s!Atx5QosFxCRboU28bL8xwhldAgsl

### Abstract 

In this project, we have developed an application for stock market prediction that utilizes machine learning models such as ARIMA, LSTM, and Prophet. These models enable accurate forecasting of stock price movements. To ensure the project's reliability and incorporate the latest market information, we have utilized data from the Yahoo Finance API and StockNews API. Ultimately, we have created a web application using Streamlit that allows users to forecast the stock price of any given stock.<br><br>

### Introduction 

We aim to create a robust machine learning model capable of effectively forecasting future stock price movements using historical data and relevant variables. The model will be designed to handle the intricate and unpredictable nature of the stock market, providing dependable predictions for various stocks and indices. The objective is to assist investors and financial institutions in making well-informed decisions, minimizing risks, and optimizing returns in the stock market.
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
<br>
### Data Preprocessing Data Cleaning <br> 
**Data Retrieval**
<br>
Use the Yahoo Finance API to fetch the desired stock market data based on user input, such as the start date, end date, and ticker symbol.
Data Loading: The stock data was loaded into a pandas DataFrame using the read_csv function.

Before conducting the analysis on the Amazon stock data, several data preprocessing steps were performed to ensure the data is in the appropriate format for analysis. The following steps were taken:
Column Data Types: The data types of the columns were carefully reviewed and adjusted as needed. The following changes were made:

Date Column: The 'Date' column, initially stored as a string, was converted to the datetime data type using the to_datetime function in pandas. This allows for easier manipulation and plotting of the temporal data.

Other Columns: If there were other columns with incorrect data types, similar steps would be taken to convert them to the appropriate data types. For example, numerical columns like 'Volume' or 'Price' would be converted to float or integer data types if necessary.

Indexing: To facilitate time-based analysis, the 'Date' column was set as the DataFrame index using the set_index function. This enables easy access and slicing of data based on specific dates.

Handling Missing Values: If there were any missing values in the dataset, they were addressed appropriately. In this case, there was no missing values ensuring that only complete and valid data was used for the analysis.
<br>
For our project, we are predicting the price of column "Close". To gain insights into the distribution of the 'Close' prices in the Amazon stock data, a histogram was created to visualize the frequency distribution of the data points.

(Final Project/report/Distribution Plot.png)


Histogram Analysis: <br>
The histogram revealed a left-skewed distribution of the 'Close' prices. A left-skewed distribution, also known as a negatively skewed or left-tailed distribution, indicates that the tail of the distribution extends towards the lower values.<br>
The left-skewed histogram suggests that lower 'Close' prices occur more frequently than higher prices. This skewness can be attributed to various factors, such as market dynamics, investor sentiment, or specific events impacting the stock price.
The left-skewed distribution implies that there might be some outliers on the higher end of the 'Close' prices, resulting in a longer left tail.
<br>
Implications
The left-skewed distribution of the 'Close' prices in the Amazon stock data highlights the importance of considering the lower range of prices in the analysis. It suggests that the majority of 'Close' prices tend to be concentrated towards the lower end, with fewer occurrences of higher prices.<br>
Understanding the distribution and skewness of the 'Close' prices can assist in making informed investment decisions and assessing the risk associated with trading Amazon stock. It provides a basis for identifying potential trends, anomalies, or patterns in the stock's price movements.

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







