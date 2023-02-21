# Timing-vs-Time-in-the-Market
An investment simulator.
## Name
**“Timing the Market vs Time in the Market”** is a Python program that simulates three different investment strategies commonly utilized by new investors. 

## Features
My program includes three different investment strategy simulators, a “more information” feature for more information on each investment strategy, and a “past investment strategies” feature to review past investment strategies’ returns. All investment strategies can be tested on any ticker on Yahoo Finance, and all data will be based on that of a stock market's past 20 years performance. (Please note that when I write “stock”, I mean any asset that has a ticker symbol on Yahoo! Finance, including cryptocurrencies, forex currencies, minerals, etc, although the investment strategies created in this program are tailored specifically towards stocks and index funds)

The first investment strategy, **“Timing the Market”**, is simply an investment strategy where investors attempt to “buy low” to increase profits. My code features a simplified version of this strategy where users wait to buy a stock after a x% daily drop in value, and wait for a maximum of y days before deciding to buy the stock no matter what. For example, the user can wait for a daily drop of 3% in a stock before buying it, with a maximum wait period of 20 business days before buying it no matter what the performance is. The profits will be graphed in a standard histogram.

The second investment strategy, **“Dollar Cost Averaging”**, consists of an investor periodically putting money into a stock, rather than putting all their money on the first day (known as lump slum investing). The user decides to buy the stock over a period of x days, with each purchase being y day intervals from each other. For example, the user can buy a stock over a period of 252 business days (one calendar year), with intervals of 40 days. This data will be graphed in a multibar histogram, where the dollar cost averaging profits list will be directly compared to lump sum investing profits list.

The third investment strategy, **“Bull vs Bear Markets”**, is less of an investment strategy but insteads compares a stock’s previous returns to its future returns. For example, a user can compare a stock’s previous 126-day performance (first input) to its future 252-day performance, and see whether its 252-day profits are greater following a poor 126-day performance (bear market), or following a good 126-day performance (bull market). The two datalists (previous stock performance and future stock performance) will be graphed in a 2d-histogram, so that the user can clearly see a correlation between previous and future performance. 

There is also a feature to see a user’s previous investment strategy simulations that were run on the program with their important data and graph them. Finally, there is a brief information feature where users can learn a bit about each investment strategy. 

## Installations Required 
- yfinance: third-party API library that connects program to Yahoo! Finance stock data
  - To download, enter pip install yfinance into the command prompt
- Matplotlib, specifically, pyplot module: module used to graph the outcomes of investment strategies, specifically histograms (single-bar and doubled-bars) and 2d histograms
  - To download, enter pip install matplotlib into the command prompt


## Known Bugs
- All time inputs are not based on calendar days, but on business days, where the stock market is open. For reference, there are 252 stock market days in a year, and around 21 stock market days in a month. So, if the user wants to input a time period of one calendar year, they should input 252 days rather than 356 days.
- Long input statements on replit.com can be overwritten and be difficult to read. To fix this issue, please increase the width of the console or enter full-screen mode
- Please press the “full-screen” button on all graphs so that the graph is properly displayed on the output screen. Also consider enlarging the width and height of the graph console to have a clearer view of the graph.
- Not a problem on replit, but code should be online so that the yfinance API could be used to connect the program to Yahoo Finance’s stock data

## Sources
### Programming Sources
| Link        | Purpose 
| :---        | :----:   
| https://algotrading101.com/learn/yfinance-guide/      | yfinance library guides, specifically for yf.finance() function       
| https://blog.quantinsti.com/stock-market-data-analysis-python/   | yfinance library Youtube guide
|https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.hist.html| documentation for plt.hist()
|https://www.w3schools.com/python/matplotlib_histograms.asp| guide for plotting histograms
|https://matplotlib.org/3.5.0/gallery/pyplots/pyplot_text.html#sphx-glr-gallery-pyplots-pyplot-text-py| documentation for plt.text() 
|https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html| documentation for plt.show(), with block = False as an input
|https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.close.html|Documentation for plt.close()
|https://datavizpyr.com/overlapping-histograms-with-matplotlib-in-python/|Guide for plt.hist(), but with two bars
|https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.hist2d.html|Documentation for plt.2dhist()| Guide
|https://www.geeksforgeeks.org/plot-2-d-histogram-in-python-using-matplotlib/|Guide for graphing 2d histograms
### Finance/Investment Strategies Sources
| Link        | Purpose 
| :---        | :----:   
|cnbc.com/2021/03/24/this-chart-shows-why-investors-should-never-try-to-time-the-stock-market.html| How timing the market works, and why it results in lost profits
|https://www.northwesternmutual.com/life-and-money/should-you-wait-for-a-market-decline-before-investing/|How timing the market works, and why it results in lost profits (second source for another point of view)
|https://www.bankrate.com/investing/investment-strategies-for-beginners/|General Investing strategies
|https://www.investopedia.com/terms/d/dollarcostaveraging.asp#:~:text=Dollar%2Dcost%20averaging%20(DCA)%20is%20an%20investment%20strategy%20in,volatility%20on%20the%20overall%20purchase.|How dollar cost averaging works
|https://www.investopedia.com/insights/digging-deeper-bull-and-bear-markets/|Bear vs Bull Markets for investing
https://www.cnbc.com/select/bear-vs-bull-market/#:~:text=Bottom%20line,to%20any%20type%20of%20investor.|Difference between Bull and Bear economies




## Support
Contact sgu1@ocdsb.ca for user support and bugs. 
