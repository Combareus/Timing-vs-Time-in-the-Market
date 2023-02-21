import yfinance as yf #import yfinance library, which is essentially an API that connects my code with yahoo finance stock data
import os #import os module which helps with operating system functionality, or specifically in this code, clearing console screens 

def timingMarket(ticker, percentage, days):
  '''
  This stock simulates the timing the market strategy. 
  Args
    ticker: string
    percentage: float
    days: integer  
  
  Returns
    profits: list
  '''
  stock = yf.download(tickers = ticker, period = "20y", interval = '1d')["Close"] #download the ticker's stock data over a period of 10 years using yf library, and store the list in the variable "stock"

  profits = [] #declare the profits list, which will store all profit percentages for this investing strategy

  
  for index in range(0, len(stock)-days): #for every closing price in the stock, simulate the investing strategy
    
    daysWaited = 0 #counter for following loop        
    while daysWaited < days: #for every day that you wait            
      
      currentDay = stock[index+daysWaited+1] #the current day is assigned as the index (day) you started on in line 18, plus the amount of days you waited, plus one since daysWaited starts at 0
      previousDay = stock[index+daysWaited] #the previous day is one less than the index for currentDay 
      
      if (previousDay - currentDay)/previousDay >= percentage: #if the price dropped by (percentage) percent from the previousDay to the currentDay
        profit = (stock[index] - currentDay) / stock[index] * 100 #store the profits as a percentage
        profits.append(round(profit,2)) #append the profits into the profits list  
        break #break out of the loop and go to the next loop on ln20, since you've already finished your strategy (the stock price dropped by a certain percentage and therefore you bought it)
            
      elif daysWaited == days - 1 : #if you've waited the maximum amount of days you set out to wait
        profit = (stock[index] - currentDay) / stock[index] * 100 # store whatever profits (or losses) you may have made
        profits.append(round(profit,2)) #append the profit into profits list       
      
      daysWaited += 1 #add one to the loop counter 
  return profits
      
def dollarCostAvg(ticker, days, intervals):
  '''
  This function simulate Dollar Cost Averaging strategy
  Args:
    ticker: string
    days: int
    intervals: int
  Returns:
    profits: list
    normalProfits: list
  '''

  stock = yf.download(tickers = ticker, period = "20y", interval = '1d')["Close"] #download the ticker's stock data over a period of 20 years using yf library, and store the list in the variable "stock"
  profits = [] #declare the profits list, which will store all profit percentages for this investing strategy
  normalProfits = [] #declare the normalProfits list, which will store all profit percentages for the base case, if the user invested all their money on day 1
  
  numberOfBuys = days//intervals + 1 #numberOfBuys variable stores the number of smaller purchases the user makes over the course of the investment starting on day 1, rather than buying all at once at the start on day 1
  
  investment = round(1/numberOfBuys, 2) #investment variable stores the amount of money invested at each smaller purchase, assuming that the initial investment is $1 (does not matter because all the profits are calculated in proportions)

  for index in range(0, len(stock)-days): #for every closing price in the stock, simulate the investing strategy
    
    numberOfShares = 0 #declare numberOfShares variable, which will track the TOTAL number of shares bought at each individual buying using dollarCostAvg strategy
    
    
    for k in range(numberOfBuys): #for every integer below the number of purchases...
      currentPrice = stock[index + intervals*k] #...the share price bought at this moment is at the starting index plus the the loop counter times the interval between each purchase
      numberOfShares += investment/currentPrice  #the amount of shares bought at this smaller purhcase is added to the 'numberOfShares', assuming that the initial investment is $1. calulated by dividing the investment at this time over the stock's current price

    valueOfStock = numberOfShares * stock[index+days] #the valueOfStock using the dollarCostAvg strategy after 'days' days is the numberOfShares bought over the course of the investment strategy, times the value of the stock after 'days' days
    profit = (valueOfStock - 1) * 100 #store the profit percentage of the dollarCostAvg strategy using the fact that the initial investment was $1, and the final value of the investment is the variable 'valueOfStock'
    profit = round(profit, 2) #round the profit to two decimal places
    profits.append(profit) #append the profit into the profits list, which stores all the profits of the dollarCostAvg strategy

    
    normalProfit = (stock[index+days] - stock[index]) / stock[index] * 100 #declare the normalProfit variable, which stores the base profit percentage if all the investment money was dumped on day 1
    normalProfit = round(normalProfit, 2) #round the normalProfit to two decimal places
    normalProfits.append(normalProfit) #append the 'normalProfit' into the 'normalProfits' list


  return profits, normalProfits
    
#--------------------      
'''
stock - which stocks do you want to compare against each other 
time - over what period of time do you want to measure a stock's high or low (ex: 5-day high or 30-day high)
returnTime - when do you want to measure how much you've made
'''
def bearVsBullMarket(ticker, time, returnTime):
  '''
  This stock simulates bear vs bull market investment strategy.
  Args
    ticker: string
    time: int
    returnTime: int
  Returns:
    profits: list
    normalProfits: list
  '''
  stock = yf.download(tickers = ticker, period = "20y", interval = '1d')["Close"] #download the ticker's stock data over a period of 20 years using yf library, and store the list in the variable "stock"
  previousReturnsList = [] #declare previousReturnsList, which will store all the stock's previous returns
  futureReturnsList = [] #decleare futureReturnsList, which will store all the stock's future returns. Note that the two lists' indices are linked to each other (based on the same day), but are not in one combined list to make it easier to work with
  for index in range(time, len(stock)-returnTime-1): #for every index in the stock, simulate the investment strategy. Note that it starts at index 'time' and ends at index 'len(stock)-returnTime' so that its possible to see the stock's previous and future performance (ex: if started at index 0, there'll be no information on the stock's previous prices)
    previousReturn = (stock[index] - stock[index-time]) / stock[index-time] * 100 #calculate the previous stock's return  over 'time' days ('time' being a function input) 
    previousReturn = round(previousReturn,2) #round previousReturn to two decimal places
    previousReturnsList.append(previousReturn) #append the previousReturn to the previousReturnsList
    futureReturn = (stock[index+returnTime] - stock[index]) / stock[index] * 100 #calculate the future stock's profit over 'returnTime' days, 'returnTime' being a function input
    futureReturn = round(futureReturn,2) #round it to two decimal places
    futureReturnsList.append(futureReturn) #append it to futureReturnsList
    
  return previousReturnsList, futureReturnsList #return the two profit lists

#---------------------

def userInput():
  '''
  This function's purpose is to have print a clean interface and receive the user's input on what actions they want to perform with the code.
  Args
    None
  Returns
    selection: string 
  '''
  os.system('clear') #Clear the console using os.clear() function to make output more readible
  print("What would you like to do?") #print statement asking what the user wants to do
  print("\n[1] Strategy 1: Timing the Market") #print what input '1' does
  print("[2] Strategy 2: Dollar Cost Averaging") #print what input '2' does
  print("[3] Strategy 3: Bear vs Bull Market Investing") #print what input '3' does
  print("[i] More information about each investing strategy") #print what input 'i' does
  print("[h] Review past investment strategies")
  print("[q] Quit the Simulation") #print what input 'q' does

  selection = input("\nSelection: ") #ask the user the input their choice, and store it in the selection variable

  
  while selection not in ['1','2','3','i','I','h','H','q','Q']: #while the selection is not in the list of valid inputs
    print("\nInvalid input, please try again!") #print that it's an invalid input
    selection = input("\nSelection: ") #and tell the user to input another selection

  return selection #return the user's selection/input

#---------------------

  
  
  

def stockInput():
  '''
  This function returns the ticker symbol of the stock the user wants to test on, and checks that the ticker is a valid ticker. 
  Args: 
    None
  Returns:
    ticker: String  
  '''
  ticker = input("Please insert the stock ticker you wish to test (ex: AMZN, APPL, ^GSPC, RY.TO, BTC-CAD, etc..): ") #Asks the user for ticker symbol.
  
  testData = yf.download(tickers = ticker, period = '1d', interval = '1d') #Attempts to download stock data according to the user input using the yfinance api library
  
  while len(testData) == 0: #If the ticker is invalid, then the length of the data downloaded should be 0
    print("\nThat is not a valid ticker!") #Tells user that input is invalid
    ticker = input("\nPlease insert the stock ticker you wish to test: ") #Prompts user to input ticker symbol
    testData = yf.download(tickers = ticker, period = '1d', interval = '1d') #Attempts to download stock data according to the user input using the yfinance api library
  
  return ticker #Returns ticker symbol

def is_float(test): 
  '''
  This function tests if its input can be converted to a float or not.
  Args:
    test: any datatype
  Return
    boolean: True if input can be converted to float, false if input cannot be converted to float
  
  '''
  try: 
    float(test) #try if float(test) will return an error or not
    return True #if it doesn't raise an error, "test" can be converted to a float, so return True
  except ValueError:
    return False #if it returns a ValueError, then it cannot be converted to a float, so return False
