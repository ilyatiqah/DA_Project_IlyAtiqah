#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: Ily Atiqah
#Group Name: Line-02
#Class: PN2004L
#Date: 09/02/2021
#Version: <...>
###############################################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #show specific country dataframe
    MonthlyVisitor()
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def MonthlyVisitor():

  #load excel data (CSV format) to dataframe - 'df'
  df = pd.read_csv('MonthyVisitors.csv')
  df.columns
  #print(df.columns)

  #Picking out specific countries and years
  #Picking out years from 1998 to 2008
  years = df[['Year', 'Month', ' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ', ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ', ' Scandinavia ', ' CIS & Eastern Europe ']][240:372]
  print(years)

  #Picking out countries from Europe Region
  countries = df[[' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ', ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ', ' Scandinavia ', ' CIS & Eastern Europe ']][240:372]

  #Total number of visitors from Europe region
  TotalVisitors = countries.sum(axis=0)
  print()
  print()
  print("The total number of visitors from Europe region: ")
  print()
  print(TotalVisitors)

  #Sort value from descending (largest number on top)
  Top11 = TotalVisitors.sort_values(ascending=False)

  #Top 3 countries
  print()
  print("The top 3 countries with the most number of visitors visiting Singapore: ")
  print()
  print(Top11.head(3))

 
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
 
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  print()

  print("Period: 1998 to 2008")
  print("Region: Europe Region")
  print()

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()


#########################################################################
#ADDITION OF PIE CHART
#########################################################################

#IMPORT PIE CHART TO DISPLAY TOP 3 COUNTRIES IN EUROPE REGION
import matplotlib.pyplot as pit

top3_countries = ['United Kingdom', 'Germany', 'Scandinavia']
slices = [4868403, 1726503, 947713]
colours = ['r', 'g', 'm']

pit.pie(slices,
        labels=top3_countries,
        startangle=90,
        shadow=True,
        explode=(0.2, 0, 0),
        autopct='%1.2f%%')

pit.legend()

pit.show()

#########################################################################
#Main Branch: End of Code
#########################################################################