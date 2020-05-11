#!/usr/bin/env python3

import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os


# get historic data for March 2019
historic_march_data = yf.download("^RUI", start="2019-03-01", end="2019-03-31")
print('Historic March data: {}'.format(historic_march_data))

if not os.path.exists('charts'):
    os.makedirs('charts')

# build chart for historic data for March 2019
historic_march_data['Close'].plot()
plt.savefig(os.path.join('charts','historic_march_2019.png'))

# train the system using archive data
# use Multiple Regression with 3 dependent values
reg = LinearRegression()
X = historic_march_data[['Open', 'High', 'Low']]
y = historic_march_data['Close']
reg.fit(X, y)

# get historic data for April 2019
historic_april_data = yf.download("^RUI", start="2019-04-01", end="2019-04-30")
print('Historic April data: {}'.format(historic_april_data))

# build chart for historic data for April 2019
historic_april_data['Close'].plot()
plt.savefig(os.path.join('charts','historic_april_2019.png'))

# predict and compare
predicted_close_prices = []
for index, row in historic_april_data.iterrows():
    predicted_price = reg.predict([[row['Open'], row['High'], row['Low']]])
    predicted_close_prices.append(predicted_price)
    print('Predicted April Price: {}'.format(predicted_price))
    print('Real April Price: '.format(row[['Close']]))

# build chart for predicted data for April 2019
plt.plot(range(len(predicted_close_prices)), predicted_close_prices)
plt.savefig(os.path.join('charts','predicted_april_2019.png'))
