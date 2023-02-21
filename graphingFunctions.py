import matplotlib.pyplot as plt #from the matplotlib library, import the pyplot module, which includes functions to graph datasets in a variety of mediums, and import it with the key "plt"


def oneDimensionHistogram(data):
  '''
  This function aims to graph a one-dimension histogram given a data list
  Args:
    data: list
  Returns:
    None
  '''
  plt.hist(x=data, bins=50, color='blue', alpha=0.7, rwidth=0.85) #plot the histogram using the built-in hist() function in the pyplot module. Inputs include x = data (data to be used when graphing, retrieved as a function input), bins = 50(the number of individuals binsBars graphed), alpha=0.7 refers to the bar's transparency, rwidth = 0.85 refers to its bar width
  
  
  plt.grid(axis='both', alpha=0.75) #add a horizontal and a vertical grid using grid() function, with a transparency of aplha = 0.75
  plt.xlabel('Profit Percentage') #add x-axis title
  plt.ylabel('Frequency') #add y-axis title
  plt.title('Timing the Market Profits') #add title
  
  
  ax = plt.gca() #get current axis instance information on the graphed figure
  x_min, x_max = ax.get_xlim() #receive the axis' max and min x-values using get_xlim() function
  y_min, y_max = ax.get_ylim() #receive the axis' max and min y-values using get_ylim() function
  x_cord = x_max / 4 #declare x_cord variable, which is the x-cord of where the text will be plotted on the graph. calculate its location based on the maximum and minimum values of the x-axis
  y_cord = y_max * 5 / 6  #declare y_cord variable, which is the y-cord of where the text will be plotted on the graph. calculate its location based on the maximum and minimum values of the y-axis
  avg_profit = round(sum(data) / len(data),2) #calculate the average profit of the investment strategy by summing all the profits by the length of the profits, and round it to 2 decimal places
  
  if avg_profit > 0: #if the average profit was above 0
    plt.text(x_cord, y_cord, "Average Profit: " + str(avg_profit) + "%", color = 'green') #plot the average profit text on the histogram at the (x_cord,y_cord) location calculated earlier, and using the color green to represent profit
  else: #otherwise
    plt.text(x_cord, y_cord, "Average Loss: " + str(avg_profit) + "%", color = 'red') #plot the average lost text on the histogram at the same location as described bove using the color red to symbolise lost
  
  
  plt.show(block = False) #plot the graph using show() function, set block=False, meaning that the code does not stop running after graphing it
  a = input("Press anything to continue: ") #ask the user for any input to continue, so that when the user is done with the graph they can enter anything to continue the program     
  plt.close() #close the graph

def multiBarHistogram(profits, normalProfits):
  '''
  This function aims to graph a two-bar histogram given two datalists
  Args:
    profits: list
    normalProfits: list
  Returns:
    None
  '''
  dollar_cost_avg_profit = round(sum(profits) / len(profits),2) #find the average profit of the first datalist by summing up all the profits and dividing it by its total length, round it to 2 decimal places. store it to 'dollar_cost_avg_profit' variable
  lump_slum_avg_profit = round(sum(normalProfits)/len(normalProfits),2) #find the average profit of the second datalist by summing up all the profits and dividing it by its total length, round it to 2 decimal places. store it to 'lump_slum_avg_profit'

  
  n, bins, patches = plt.hist(x = [profits, normalProfits], bins='auto', color=['red', 'blue'], alpha=0.35, rwidth=0.85, label = ['Dollar Cost Avg Profits', 'Lump Slum Profits']) #use hist() function to graph the two investment lists. instead of a single list as the data input for the histogram, its a 2D list containing both investment lists, as shown in x = [profits, normalProfits], where profits and normalProfits are both lists as well. Set the colors of the bars be red and blue, and the labels be 'Dollar Cost Avg Profits' and 'Lump Slum Profits', respectively


  plt.legend(loc = 'upper left') #put the legend of the graph at the top left of the graph, using legend() Function
  plt.grid(axis='both', alpha=0.75) #put a grid on both axis, with a transparency of alpha = 0.75
  plt.xlabel('Profit Percentage') #label x-axis
  plt.ylabel('Frequency') #label y-axis
  plt.title('Dollar Cost Avg v.s. Lump Slum') #add title
  
  axes = plt.gca() #get current axis instance information on the graphed figure
  x_min, x_max = axes.get_xlim() #receive the axis' max and min x-values using get_xlim() function
  y_min, y_max = axes.get_ylim() #receive the axis' max and min y-values using get_ylim() function
  x_cord = x_max - (x_max - x_min) * 2 /5 #declare x_cord variable, which is the x-cord of where the text will be plotted on the graph. calculate its location based on the maximum and minimum values of the x-axis
  y_cord = y_max * 4 / 5  #declare y_cord variable, which is the y-cord of where the text will be plotted on the graph. calculate its location based on the maximum and minimum values of the y-axis  

  
  plt.text(x_cord, y_cord, "Average Dollar Cost Averaging Profit:" + str(dollar_cost_avg_profit) + "%", fontsize = 8) #plot the average dollar cost avg profit using text(), at the cords (x_cord, y_cord) calculated earlier, with fond size 8, since there's more text
  plt.text(x_cord, y_cord - 10, "Average Lump Slum (default) Profit:" + str(lump_slum_avg_profit) + "%", fontsize = 8) #plot the average lump slum profit using text(), at the cords (x_cord, y_cord-10) calculated earlier, so that it's located 10 frequencies below the text plotted earlier, with fond size 8, since there's more text
  
  
  
  plt.show(block = False) #plot the graph using show() function, set block=False, meaning that the code does not stop running after graphing it
  a = input("Press anything to continue: ") #ask the user for any input to continue, so that when the user is done with the graph they can enter anything to continue the program     
  plt.close() #close the graph

def twoDimensionHistogram(previousReturnsList, futureReturnsList):
  '''
  This function graphs a 2d histogram from two datalists
  Args:
    previousReturnsList: list
    futureReturnsList: list
  Returns:
    None
  '''
  plt.hist2d(previousReturnsList, futureReturnsList, bins=50) #plot the graph in a 2d histogram using hist2d() function, with the inputs being the two lists previousReutnrsList and futureReturnsList from the function's input. Also set bins=50 so that the histogram is seperated into 50 sections in both x and y axis (a greater number of bins makes trend correlation easier to visualise, when there is a lot of data)
  plt.colorbar() #add a color bar to the right of the 2d histogram
  plt.xlabel('Previous Return') #label x-axis
  plt.ylabel('Future Return') #label y-axis
  plt.title('Bull vs Bear Markets') #add title
  plt.show(block = False) #show the graph using show() function, set block=False, meaning that the code does not stop running after graphing it
  a = input("Press anything to continue: ") #ask the user for any input to continue, so that when the user is done with the graph they can enter anything to continue the program     
  plt.close() #close the graph
