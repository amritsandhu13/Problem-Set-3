#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Problem Set 3

#Question-1 Introduction: Special thanks to: https://github.com/justmarkham for sharing the dataset and materials. Occupations

#Step 1. Import the necessary libraries

import numpy as np
import pandas as pd


# In[2]:


#Step 2. Import the dataset from this address
#Step 3. Assign it to a variable called users

users = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user",sep="|")
users.head()


# In[3]:


#Step 4. Discover what is the mean age per occupation

users.groupby("occupation").age.mean()


# In[4]:


#Step 5. Discover the Male ratio per occupation and sort it from the most to the least

males_occupation = users.where(users.gender=="M").groupby(["occupation","gender"]).gender.count()

males_total = users.groupby("occupation").gender.count()

males_ratio = (males_occupation/males_total)*100

males_ratio.sort_values(ascending = False)


# In[5]:


#Step 6. For each occupation, calculate the minimum and maximum ages

users.groupby(["occupation"]).age.agg(["min","max"])


# In[6]:


#Step 7. For each combination of occupation and sex, calculate the mean age

users.groupby(["occupation","gender"]).age.mean()


# In[7]:


#Step 8. For each occupation present the percentage of women and men

Total_females = users.where(users.gender=='F').groupby(['occupation','gender']).gender.agg(['count'])

Total_males = users.where(users.gender=='M').groupby(['occupation','gender']).gender.agg(['count'])

total_genders = users.groupby('occupation').gender.agg(['count'])

Ratio_of_males = (Total_males/total_genders)*100

Ratio_of_females = (Total_females/total_genders)*100

pd.merge(Ratio_of_males,Ratio_of_females,on ='occupation')


# In[8]:


#Question 2

#Euro Teams
#Step 1. Import the necessary libraries

import numpy as np
import pandas as pd


# In[9]:


#Step 2. Import the dataset from this address
#Step 3. Assign it to a variable called euro12


euro12 = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv",sep=",")
euro12.head()


# In[10]:


#Step 4. Select only the Goal column

euro12.Goals


# In[11]:


#Step 5. How many team participated in the Euro2012?

participated_teams =euro12.groupby("Team").Team.count()
print("Participated Teams: ",len(participated_teams))


# In[12]:


#Step 6. What is the number of columns in the dataset?

print("Number of columns in the dataset: ",len(euro12.columns))


# In[13]:


#Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline


latest_dataframe = euro12[["Team","Yellow Cards","Red Cards"]]
discipline = pd.DataFrame(latest_dataframe)
discipline


# In[14]:


#Step 8. Sort the teams by Red Cards, then to Yellow Cards

discipline.sort_values(by=["Red Cards","Yellow Cards"])


# In[15]:


#Step 9. Calculate the mean Yellow Cards given per Team

discipline.groupby("Team")["Yellow Cards"].mean()


# In[16]:


#Step 10. Filter teams that scored more than 6 goals

euro12[euro12.Goals > 6]


# In[17]:


#Step 11. Select the teams that start with G

euro12[euro12.Team.str.startswith("G")]


# In[18]:


#Step 12. Select the first 7 columns

euro12.iloc[:,:7]


# In[19]:


#Step 13. Select all columns except the last 3

euro12.iloc[:,:-3]


# In[20]:


#Step 14. Present only the Shooting Accuracy from England, Italy and Russia

euro12.loc[euro12.Team.isin(['England','Italy','Russia']),['Team','Shooting Accuracy']]


# In[21]:


#Question 3
#Housing

#Step 1. Import the necessary libraries

import numpy as np
import pandas as pd
import random
import string


# In[22]:


#Step 2. Create 3 differents Series, each of length 100, as follows:
#• The first a random number from 1 to 4
#• The second a random number from 1 to 3
#• The third a random number from 10,000 to 30,000

a = pd.Series(np.random.randint(1,4,100))
b = pd.Series(np.random.randint(1,3,100))
c = pd.Series(np.random.randint(10000,30000,100))


# In[25]:


#Step 3. Create a DataFrame by joinning the Series by column

DataFrame = pd.concat ([a,b,c],axis=1)
DataFrame.head()


# In[26]:


#Step 4. Change the name of the columns to bedrs, bathrs, price_sqr_meter

DataFrame.columns = ["bedrs","bathrs","price_sqr_meter"]
DataFrame.head()


# In[28]:


#Step 5. Create a one column DataFrame with the values of the 3 Series and assign it to 'bigcolumn'

bigcolumn = pd.concat([a,b,c],axis=0)
bigcolumn



# In[31]:


#Step 6. Ops it seems it is going only until index 99. Is it true?

bigcolumn.reset_index(drop=True)
bigcolumn


# In[32]:


#Step 7. Reindex the DataFrame so it goes from 0 to 299

bigcolumn.reset_index(drop=True, inplace=True)
bigcolumn


# In[35]:


#Question 4
#Wind Statistics
#The data have been modified to contain some missing values, identified by NaN.
#Using pandas should make this exercise easier, in particular for the bonus question.

#Step 1. Import the necessary libraries

import numpy as np
import pandas as pd


# In[36]:


#Step 2. Import the dataset from the attached file wind.txt

data = pd.read_csv("wind.txt",sep='\s+')
data.head()


# In[37]:


#Step 3. Assign it to a variable called data and replace the first 3 columns by a proper datetime index.

data["Date"] = pd.to_datetime(data[["Yr","Mo","Dy"]].astype(str).agg('-'.join, axis=1))
data = data.drop(columns=["Yr","Mo","Dy"])
data.head()


# In[38]:


#Step 4. Year 2061? Do we really have data from this year? Create a function to fix it and apply it.

data["Date"] = np.where(pd.DatetimeIndex(data["Date"]).year < 2021,data.Date,data.Date - pd.offsets.DateOffset(years=100))
print(data)


# In[39]:


#Step 5. Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns].

DATA = data.set_index("Date")
DATA.index.astype("datetime64[ns]")


# In[40]:


# Step 6. Compute how many values are missing for each location over the entire record.They should be ignored in all calculations below.

print(data.isnull().values.sum())


# In[41]:


#Step 7. Compute how many non-missing values there are in total

Total = DATA.count()
print("Non-missing values-",Total.sum())


# In[42]:


#Step 8. Calculate the mean windspeeds of the windspeeds over all the locations and all the times.

DATA.mean().mean()


# In[43]:


# Step 9. Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the
#days A different set of numbers for each location.

Min = DATA.min()
Max = DATA.max()
Mean = DATA.mean()
standard_deviation = DATA.std()
Statistics_values = [Min,Max,Mean,standard_deviation]
Values = ["Min","Max","Mean","Std"]
loc_stats = pd.DataFrame(Statistics_values,Values)
loc_stats


# In[44]:


#Step 11. Find the average windspeed in January for each location. Treat January 1961 and January 1962 both as January.

Jan_data = DATA[DATA.index.month == 1]
print ("Average Windspeed:")
print (Jan_data.mean())


# In[45]:


#Step 12. Downsample the record to a yearly frequency for each location

print( "Yearly frequency for each location:\n", DATA.resample('A').mean())


# In[46]:


#Step 13. Downsample the record to a monthly frequency for each location.

print ("Monthly frequency for each location:", DATA.resample('M').mean())


# In[47]:


#Step 14. Downsample the record to a weekly frequency for each location.

print ("Weekly frequency for each location:", DATA.resample('W').mean())


# In[48]:


#Step 15. Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 52 weeks.

Year1 = DATA[DATA.index.year == 1961]
StatisticsValues = DATA.resample('W').mean().apply(lambda x: x.describe())
print (StatisticsValues)


# In[49]:


#Question 5

#Step 1. Import the necessary libraries

import numpy as np 
import pandas as pd


# In[50]:


#Step 2. Import the dataset from this address.
#Step 3. Assign it to a variable called chipo.

chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv',sep="\t")


# In[51]:


#Step 4. See the first 10 entries

chipo.head(10)


# In[52]:


#Step 5. What is the number of observations in the dataset?

chipo.shape[0]


# In[53]:


#Step 6. What is the number of columns in the dataset?

chipo.shape[1]


# In[55]:


#Step 7. Print the name of all the columns.

chipo.columns


# In[56]:


#Step 8. How is the dataset indexed?

chipo.index


# In[57]:


#Step 9. Which was the most-ordered item?

most_Ordered_item = chipo.groupby('item_name').sum()
most_Ordered_item = most_Ordered_item.sort_values(by=['quantity'], ascending = False)
most_Ordered_item.head(5)


# In[58]:


#Step 10. For the most-ordered item, how many items were ordered?

most_Ordered_item.head(1)


# In[60]:


#Step 11. What was the most ordered item in the choice_description column?

most_oreder_item_bychoice = chipo.groupby('choice_description').sum()
most_oreder_item_bychoice = most_oreder_item_bychoice.sort_values(by=['quantity'], ascending = False)
most_oreder_item_bychoice.head(5)


# In[61]:


#Step 12. How many items were orderd in total?

chipo.groupby('quantity').quantity.sum().sum()


# In[62]:


#Step 13.
#• Turn the item price into a float
#• Check the item price type
#• Create a lambda function and change the type of item price
#• Check the item price type

chipo.item_price.dtype


# In[63]:


#Create a lambda function and change the type of item price

try:                                                 
    Item_pricetoFloat = lambda x: float(x[1:-1])
    chipo.item_price = chipo.item_price.apply(Item_pricetoFloat)
    
except:TypeError 


# In[64]:


#Check the item price type

chipo.item_price.dtype


# In[65]:


#Step 14. How much was the revenue for the period in the dataset?

dataset_revenue = (chipo['quantity'] * chipo['item_price'])
dataset_revenue.sum()


# In[66]:


#Step 15. How many orders were made in the period?

chipo.order_id.value_counts().count()


# In[67]:


#Step 16. What is the average revenue amount per order?

chipo.groupby('order_id').agg({'item_price':'mean'}).mean()


# In[68]:


#Step 17. How many different items are sold?

chipo.item_name.value_counts().count()


# In[69]:


#Question 6
#Create a line plot showing the number of marriages and divorces per capita in the U.S. between 1867 and 2014. Label both lines and show the legend.
#Don't forget to label your axes!

import matplotlib.pyplot as plt
import pandas as pd


# In[70]:


US_Data = pd.read_csv('us-marriages-divorces-1867-2014.csv')
US_Data.head()


# In[71]:


Total_Years = US_Data.Year.values
Marriages_US = US_Data.Marriages_per_1000.values
Divorces_US = US_Data.Divorces_per_1000.values

plt.plot(Total_Years,Marriages_US,color="Black")
plt.plot(Total_Years,Divorces_US,color="Red")
plt.xlabel("Years")
plt.ylabel("Total Mariages & divoces per capita in the US")
plt.title("Number of marriages and divorces per capita in the US. between 1867 and 2014 \n")
plt.show()


# In[72]:


#Question 7
#Create a vertical bar chart comparing the number of marriages and divorces per
#capita in the U.S. between 1900, 1950, and 2000.
#Don't forget to label your axes!


Year1900 = US_Data.Year>=1900
Year2000 = US_Data.Year<=2000
Both_Year_data = US_Data[Year1900 & Year2000]
## plt.bar(Data_1900_2000['Marriages_per_1000'],Data_1900_2000['Divorces_per_1000'])
plt.bar(Both_Year_data['Year'],Both_Year_data['Marriages_per_1000'],color="Black")
plt.bar(Both_Year_data['Year'],Both_Year_data['Divorces_per_1000'],color="Red")
plt.title("Number of marriages and divorces per capita in the U.S between 1900, 1950, and 2000 \n")
plt.xlabel(" Years(1900 & 2000)")
plt.ylabel("Number of Marriages & Divorces per capita in U.S")
plt.show()


# In[73]:


#Question 8
#Create a horizontal bar chart that compares the deadliest actors in Hollywood. Sort
#the actors by their kill count and label each bar with the corresponding actor's name.
#Don't forget to label your axes!

deadliest_actors = pd.read_csv('actor_kill_counts.csv')
deadliest_actors.head()
Sort_deadliest_actors = deadliest_actors.sort_values(by='Count',ascending=True)
Actors_by_name = Sort_deadliest_actors.Actor
plt.barh(Sort_deadliest_actors['Actor'],Sort_deadliest_actors['Count'],color="Black")
plt.xlabel("Number of Kills by actors")
plt.ylabel("Hollywood actors")
plt.title("Deadliest actors in Hollywood \n ")
plt.show()


# In[74]:


#Question 9
#Create a pie chart showing the fraction of all Roman Emperors that were assassinated.
#Make sure that the pie chart is an even circle, labels the categories, and shows the
#percentage breakdown of the categories.


Roman_Emperors_data = pd.read_csv('roman-emperor-reigns.csv')
Roman_Emperors_data.head()
Data = Roman_Emperors_dat.where(Roman_Emperors_data.Cause_of_Death=="Assassinated").Cause_of_Death.count()
Roman = Roman_Emperors_data.Cause_of_Death.count()-Data
label=["Death Causes","Roman's Assassinated"]
plt.pie([Romans,Data],labels=label,autopct='%.2f%%')
plt.title("Roman Emperors Data \n")
plt.show()


# In[75]:


#Question 10
#Create a scatter plot showing the relationship between the total revenue earned by
#arcades and the number of Computer Science PhDs awarded in the U.S. between 2000 and 2009.
#Don't forget to label your axes!
#Color each dot according to its year.

data = pd.read_csv('arcade-revenue-vs-cs-doctorates.csv')
Both_years = data.Year
arcade = data['Total Arcade Revenue (billions)']
Computer_Science_PhDs = data['Computer Science Doctorates Awarded (US)']
Plot_colors = ["Maroon","Black","Blue","Orange","Green","Red","Yellow","Pink","Brown","Gray"]
plt.scatter(arcade,Computer_Science_PhDs,color=Plot_colors)
plt.xlabel("total revenue")
plt.ylabel("Award winner computer science PhDs")
plt.title("Relationship between the total revenue earned by arcades and the number of Computer Science PhDs awarded in the U.S. between 2000 and 2009 \n")
plt.show()


# In[ ]:




