"""
Shougan Gu   
ICS3U-04
This program - "Timing vs Time in the Market" - is a stock investment simulation that aims to simulate certain investment strategies and access their effectiveness. The first investment strategy tests the idea of waiting for a stock to dip a certain amount before buying it. The second investment strategy is to buy a stock over a period of time, with specified intervals between each smaller purchase. The third investment strategy looks at the correlation between a stock's previous performance to its future performance. My program also has a feature to see a the data of previous investment strategies run on the program, as well as a breif overview of each investment strategy through the console. In conclusion, my program revealed the general concensus that Time in the Market, does, indeed, beat Timing the Market, as the first two investment strategies almost always underperform the stock's expected returns. However, the third investment strategy revealed that a stock typically has higher returns following periods of lesser growth during a bear market, revealing that it is indeed better to double down on consistent stocks when it is in a bear market to buy shares at a "discounted" price.  
"""

  

from functions import * #import functions defined in functions.py file
from graphingFunctions import * #import graphingFunctions defined in graphingFunctions 
import yfinance as yf #import yfinance library, which is essentially an API that connects my code with yahoo finance stock data
import os #import os module which helps with operating system functionality, or specifically in this code, clearing console screens 


#investmentData dictionary stores all the user's previous simulation data, such as the stock ticker, profit list, or average profit (more specific contents commented inside the dictionary). The keys of the dictionary seperates the three different investment types used
investmentData = {
  "Timing the Market": [], #in the order [ticker, percentage, days, data, avgProfit]
  "Dollar Cost Averaging" : [], #in the order [ticker, days, intervals, profits, normalProfits, dollar_cost_avg_profit, lump_slum_avg_profit]
  "Bear vs Bull Markets" : [] #in the order [ticker, time, returnTime, previousReturnsList, futureReturnsList]
}

selection = '' #declare selection variable, which stores the user's input as to what they want to do in the program

z = input("Welcome to the investing simulation! Press anything to get started: ") #Print welcome statement and ask user for any input to start running the code
while selection != 'q': #keep the program running until the selection is equal to q, which means the user wants to end the program
  selection = userInput() #receive the user selection using the userInput() function
  
  if selection == '1': #if the selection was option '1'
    os.system('clear') #Clear the console using os.clear() function to make output more readible
    ticker = stockInput() #receive the user's input on which stock ticker they want to test the investment strategy on using stockInput() function, and store it in the variable 'ticker'
    
    percentage = input("\nWhat daily percentage drop will you be happy to buy at? ")   #receive the user's input on what daily percentage drop they are looking for before buying the stock
    while is_float(percentage) == False:
      print("\nThat is not a valid input. Please input an integer or a float") #print that percentage is an invalid input
      percentage = input("What daily percentage drop will you be happy to buy at: ")  #receive the user's input on what daily percentage drop they are looking for before buying the stock
    percentage = float(percentage) / 100 #convert percentage into a float and divide it by 100 to turn the percentage into a decmial
    
    days = input("What is the maximum number of days you can wait for?: ")#receive user input on the maximum number of days they are willing to wait for the percentage drop before buying the stock anyways
    while days.isdigit() == False or int(days) < 1: #while not all values in the 'days' string are digits and it cannot be convert to an integer, or while it can be converted to an integer but is negative
      print("\nThat is not a valid input. Please input a positive integer") #print that percentage is an invalid input
      days = input("\nWhat is the maximum number of days you can wait for?: ")#receive user input on the maximum number of days they are willing to wait for the percentage drop before buying the stock anyways
    days = int(days) #convert days into an integer
    
    data = timingMarket(ticker, percentage, days) #use timingMarket() function to find the profits from the investing strategy
    avgProfit = sum(data) / len(data) #find the average profit of the investment strategy by taking the sum of all historical returns and dividing it by the total number of historical data
    avgProfit = round(avgProfit , 2) #round the profit to two decimal places 
    oneDimensionHistogram(data) #graph the profits data using oneDimensionHistogram() function
    investmentData["Timing the Market"].append([ticker, percentage, days, data, avgProfit])  #append important data on this investment strategy (such as stock ticker and average profit) into the investmentData dictionary, specifically into the list assosicated with the key "Timing the Market"
    
     
  elif selection == '2':
    os.system('clear') #Clear the console using os.clear() function to make output more readible
    ticker = stockInput() #receive the user's input on which stock ticker they want to test the investment strategy on using stockInput() function, and store it in the variable 'ticker'

    days = input("\nOver what period of time do you want to buy your stock? ")#receive user input on the period of time they want to buy their stocks 
    while days.isdigit() == False or int(days) < 1: #while not all values in the 'days' string are digits and it cannot be convert to an integer, or while it can be converted to an integer but is negative
      print("\nThat is not a valid input. Please input aa positive integer") #print that the 'days' is an invalid input
      days = input("\nOver what period of time do you want to buy your stock? ")#receive user input on the period of time they want to buy their stocks is
    days = int(days) #convert days into an integer

    intervals = input("\nWhat is the period in days between each purchase? ")#receive user input on the interval in between each smaller stock purchase 
    while intervals.isdigit() == False or int(intervals) < 1 or int(intervals) >= days: #while not all values in the 'intervals' string are digits and it cannot be convert to an integer, or while it can be converted to an integer but is negative, or while it is actually larger than the period of time they want to buy their stocks
      print("\nThat is not a valid input. Please input a positive integer smaller than the period of time you want to buy your stock (previous input, which was " + str(days) + ")") #print that 'intervals' is an invalid input
      intervals = input("\nWhat is the period in days between each purchase? ") #receive user input on the period of time they want to buy their stocks 
    intervals = int(intervals) #convert intervals into an integer

    
    profits, normalProfits = dollarCostAvg(ticker, days, intervals) #use dollarCostAvg() function to find the profits of this investment strategy compared to the normal profits    
    dollar_cost_avg_profit = round(sum(profits) / len(profits),2) #find the average profit of the investment strategy by taking the sum of all historical returns and dividing it by the total number of historical data
    lump_slum_avg_profit = round(sum(normalProfits)/len(normalProfits),2) #find the average profit of the base case (lump slum investing) by taking the sum of all historical returns and dividing it by the total number of historical data
    multiBarHistogram(profits, normalProfits) #use the multiBarHistogram() function to compare the two profits by graphing them side to side in a 2-bar histogram
    investmentData["Dollar Cost Averaging"].append([ticker, days, intervals, profits, normalProfits, dollar_cost_avg_profit, lump_slum_avg_profit]) #append important data on this investment strategy (such as stock ticker and average profit) into the investmentData dictionary, specifically into the list assosicated with the key "Dollar Cost Averaging"
    

  elif selection == '3':
    os.system('clear') #Clear the console using os.clear() function to make output more readible
    ticker = stockInput() #receive the user's input on which stock ticker they want to test the investment strategy on using stockInput() function, and store it in the variable 'ticker'
    
    time = input("\nOver what period of time do you want to measure a stock's previous return (ex: 5-day history, 30-day history)? ") #receive user input on what period of time they want to measure a stock's previous performance    
    while time.isdigit() == False or int(time) < 1: #while not all values in the 'time' string are digits and it cannot be convert to an integer, or while it can be converted to an integer but is negative
      print("\nThat is not a valid input. Please input a positive integer") #print that 'time' is an invalid input
      time = input("\nOver what period of time do you want to measure a stock's previous return (ex: 5-day history, 30-day history)? ") #receive user input on what period of time they want to measure a stock's previous performance
    time = int(time) #convert time into an integer

    
    returnTime = input("\nOver what period of time do you want to measure a stock's future return (ex: 5-day return, 30-day return)? ") #recieve user input on what period of time they want to measure the stock's future return   
    while returnTime.isdigit() == False or int(returnTime) < 1: #while not all values in the 'returnTime' string are digits and it cannot be convert to an integer, or while it can be converted to an integer but is negative
      print("\nThat is not a valid input. Please input a positive integer") #print that 'returnTime' is an invalid input
      returnTime = input("\nOver what period of time do you want to measure a stock's future return (ex: 5-day return, 30-day return)? ") #receive user input on what period of time they want to measure a stock's previous performance
    returnTime = int(returnTime) #convert returnTime into an integer

    

    previousReturnsList, futureReturnsList = bearVsBullMarket(ticker, time, returnTime) #use the bearVsBullMarket() function to compare historical stock returns to its future stock returns, and see if a stock yields more future profits during its bear market (during low returns, when it has lost value in the last period of time), or during its bull market (during high returns, when it has gained value in the last period of time)

    twoDimensionHistogram(previousReturnsList, futureReturnsList) #use the twoDimensionHistogram() to compare previousReturnsList with futureReturnsList 

    investmentData["Bear vs Bull Markets"].append([ticker, time, returnTime, previousReturnsList, futureReturnsList]) #append important data on this investment strategy (such as stock ticker and average profit) into the investmentData dictionary, specifically into the list assosicated with the key "Timing the Market"

  
  elif selection == 'i' or selection == 'I':
    os.system('clear') #Clear the console using os.clear() function to make output more readible
    print("Timing the Market: This strategy involves investors trying to buy the 'dip', or when the stock market is down suddenly in a day. They hope that by waiting for the stock to dip, they can buy the stock at a lower price and increase profits")
    print("\nEspecially for consistent growth stocks, this investment strategy normally does not work, due to the nature of a stock's growth, there is a higher likelihood of the stock price rising before buying the stock at a dip, thus losing money")
    print("\n\nDollar Cost Averaging: When investors want to minimize risk in the market, many resort to dollar cost averaging. This is the process of putting equal amounts of money into a stock over a period of time, rather than dumping all of the money at once (which is known as lump slum investing)")
    print("\nThis investment strategy does indeed generally reduce a stock's risk, since the investor is consistently buying shares at an updated price. However, it also reduces profits as most of the time, the investor will end up buying the stock at a higher price at later intervals")
    print("\n\nBull vs Bear Markets: Less so of an investment strategy, this simulation compares a stock's previous returns to its future returns. For example how does a stock's monthly returns compare following a -5% dip vs a +5% gain in the previous month. This can help investors learn if it has historically been better to buy a stock during/following a bear market, or during/following a bull market. ")
    print("\nThe 2d histogram generally has a correlation of hotspots from the top-left corner to the bottom-right corner, showing that a stock typically performs better following a decline in prices. For example, left bars normally have high hot spots, meaning that low historical returns often lead to higher future returns. On the contrary, right bars normally have lower hot spots, meaning that higher historical returns often lead to lower future returns.")
    a = input("\nPress anything to continue")

  elif selection == 'h' or selection == 'H':
    #give user option to seelct which ever historical data they want to see (or go back), then use the graphing functions
    os.system('clear') #Clear the console using os.clear() function to make output more readible
    print("Past investment strategies tested ")
    if len(investmentData["Timing the Market"]) + len(investmentData["Dollar Cost Averaging"]) + len(investmentData["Bear vs Bull Markets"]) == 0: #if the length of the diciontary's lists are all 0 (the dictionary is empty)
      print("You have not tested any investment strategies! ") #print that the user hasn't tested any investment strategies and end the function
    else:
      counter = 0 #counter for number of datasets printed
      index = 0
      if len(investmentData["Timing the Market"]) > 0: #if investmentData["Timing the Market"] list is not empty, then print its content
        print("\nTiming the Market") #print investment strategy name
        print("{:<7}{:<20} {:<20} {:<20} {:<20} ".format(' ', 'Ticker','Percentage Drop','Max Days', 'Avg Profit')) #print headings with f string formatting
        print("-"*80) #print line to seperate heading from content
        for list in investmentData["Timing the Market"]: #for each individual investment datalist under the investment strategy list investmentData["Timing the Market"]
          print("{:<7} {:<20} {:<20} {:<20} {:<20}".format("[" + str(counter) + "]", list[0], list[1] * 100, list[2], str(list[4]) + "%")) #print out its content using f string formatting
          counter += 1 #add one to the counter for the number of datasets printed

      if len(investmentData["Dollar Cost Averaging"]) > 0: #if investmentData["Dollar Cost Averaging"] list is not empty, then print its content
        print("\n\nDollar Cost Averaging") #print investment strategy name
        print("{:<7}{:<20} {:<20} {:<20} {:<20} ".format(' ', 'Ticker','Period of Time','Interval', 'Dollar Cost Avg / Lump Slum Profits')) #print headings with f string formatting
        print("-"*80) #print line to seperate heading from content
        for list in investmentData["Dollar Cost Averaging"]: #for each individual investment datalist under the investment strategy list investmentData["Dollar Cost Averaging"]
          print("{:<7} {:<20} {:<20} {:<20}{:<20} ".format("[" + str(counter) + "]", list[0], list[1], list[2], str(list[5]) + "%/" + str(list[6]) + "%")) #print out its content using f string formatting
          counter += 1 #add one to the counter for the number of datasets printed
      
      if len(investmentData["Bear vs Bull Markets"]) > 0: #if investmentData["Bear vs Bull Markets"] list is not empty, then print out its content
        print("\n\nBear vs Bull Markets") #print investment strategy name
        print("{:<7}{:<20} {:<25} {:<25} ".format(' ', 'Ticker','Historical Return Time','Future Return Time')) #print headings with f string formatting
        print("-"*80) #print line to seperate heading from content
        for list in investmentData["Bear vs Bull Markets"]: #for each individual investment datalist under the investment strategy list investmentData["Bear vs Bull Markets"]
          print("{:<7}{:<20} {:<25} {:<25}".format("[" + str(counter) + "]", list[0], list[1], list[2])) #print out its content using f string formatting
          counter += 1 #add one to the counter for the number of datasets printed

      a = input("Press anything to continue, or an input number (left number on the chart) to see an investment strategy's graph again") #receive user input on whether or not they want to see an investment's graph again, or continue on with the simulation
      while a.isdigit() and int(a) < counter: #while the input is an integer that is less than the counter, it means that the user wants to graph the investment strategy's graph
        a = int(a) #set the input to an integer value
        
        if a >= ( len(investmentData["Timing the Market"]) + len(investmentData["Dollar Cost Averaging"]) ): #if the input is larger than the sum of the lengths of the first two lists printed ("Timing the Market" and "Dollar Cost Averaging"), this means that the user selected an investment strategy from the last list ("Bear vs Bull Markets")
          index = a - len(investmentData["Timing the Market"]) - len(investmentData["Dollar Cost Averaging"]) #the index of the last list is the user input minus the length of the previous two lists
          previousReturnsList = investmentData["Bear vs Bull Markets"][index][3] #the previousReturnsList is stored in the third index of the investmentData["Bear vs Bull Markets"][index] list
          futureReturnsList = investmentData["Bear vs Bull Markets"][index][4] #and the futureReturnsList is stored in the fourth index of the investmentData["Bear vs Bull Markets"][index] list
          twoDimensionHistogram(previousReturnsList, futureReturnsList) #use the twoDimensionHistogram() to graph the two lists previousReturnsList and futureReturnsList 

        elif a >= len(investmentData["Timing the Market"]): #elif the input is larger than the length of the first list investmentData["Timing the Market"] (but obviously smaller than the sum of the first two lists, since it passed the first if statement), then the user selected an investment strateged from the second list investmentData["Timing the Market"]
          index = a - len(investmentData["Timing the Market"]) #The index of the second list the user inputted is its user input minus the length of the first list investmentData["Timing the Market"] 
          profits = investmentData["Dollar Cost Averaging"][index][3] #profits list is stored in the third index of investmentData["Dollar Cost Averaging"][index] list
          normalProfits = investmentData["Dollar Cost Averaging"][index][4] #normalProfits list is stored in the fourth index of investmentData["Dollar Cost Averaging"][index] list
          multiBarHistogram(profits, normalProfits) #use the multiBarHistogram() function to compare the two profits by graphing them side to side in a 2-bar histogram

        else: #otherwise, if the two if statmenets failed to pass, it means that the user inputted a selection from the first list
          index = a #the index of the first list is then simply the user's input 
          profits = investmentData["Timing the Market"][index][3] #the profits list is stored in the list investmentData["Timing the Market"][index]'s third index
          oneDimensionHistogram(profits) #graph the profits data using oneDimensionHistogram() function
        
        a = input("Press anything to continue, or an input number (left number on the chart) to see an investment's strategy graph again") #receive user input on whether or not they want to see an investment's graph again, or continue on with the simulation  
          
          
          
        

print("Thank you for using the simulation") #print closing statement
