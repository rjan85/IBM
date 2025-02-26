#!/usr/bin/env python
# coding: utf-8

# In[57]:


get_ipython().system('pip install yfinance')
get_ipython().system('pip install bs4')
get_ipython().system('pip install matplotlib')


# In[22]:


import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)


# ## Question 1: Use yfinance to Extract Stock Data
# Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is Tesla and its ticker symbol is TSLA.

# In[23]:


import yfinance as yf

# Create a Ticker object for Tesla using its stock symbol 'TSLA'
tesla = yf.Ticker("TSLA")

# Retrieve the complete historical market data for Tesla
# 'period="max"' fetches data from the earliest available date to the most recent
tesla_data = tesla.history(period="max")

# Reset the DataFrame index to convert the date index into a column
tesla_data.reset_index(inplace=True)

# Display the first five rows of the DataFrame to preview the data
tesla_data.head()


# ## Question 2: Use Webscraping to Extract Tesla Revenue Data
# Use the requests library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm Save the text of the response as a variable named html_data.

# In[32]:


import requests

# URL of the webpage to download
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

# Send GET request to the URL
response = requests.get(url)

# Save the text of the response as html_data
html_data = response.text


# In[43]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

# URL of the webpage containing Tesla's revenue data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"

# Sending an HTTP request to the URL
response = requests.get(url)
html_data = response.text

# Parsing the content of the page with BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')

# Finding all table elements on the page
tables = soup.find_all('table')

# Extracting the data from the table into a DataFrame
df = pd.read_html(str(revenue_table))[0]
    
# Displaying the first 15 rows of the DataFrame
df.head(15)





# ## Question 3: Use yfinance to Extract Stock Data
# Using the Ticker function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is GameStop and its ticker symbol is GME.

# In[46]:


gamestop = yf.Ticker("GME")


# In[47]:


gamestop_data = gamestop.history(period = "max")


# In[48]:


gamestop_data.reset_index(inplace=True)
gamestop_data.head()


# ## Question 4: Use Webscraping to Extract GME Revenue Data
# Use the requests library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html. Save the text of the response as a variable named html_data_2.

# In[56]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

# Get the webpage content
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

# Send an HTTP request to the URL
response = requests.get(url)
html_data_2 = response.text

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
    
# Find all tables on the page
tables = soup.find_all('table')
        
# Extract the data from the table into a DataFrame
revenue_df = pd.read_html(str(revenue_table))[0]
        
# Display the first few rows of the DataFrame
revenue_df.head(15)
    


# ## Question 5: Plot Tesla Stock Graph
# Use the make_graph function to graph the Tesla Stock Data, also provide a title for the graph. Note the graph will only show data upto June 2021.

# In[58]:


import pandas as pd
import matplotlib.pyplot as plt

# Define the make_graph function
def make_graph(data, x_column, y_column, title):
    plt.figure(figsize=(10, 5))
    plt.plot(data[x_column], data[y_column], marker='o')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Fetch Tesla revenue data (from previous steps)
print("Fetching Tesla revenue data...")
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
tables = pd.read_html(url)
tesla_revenue = tables[0]
tesla_revenue.columns = ['Date', 'Revenue']
tesla_revenue['Revenue'] = tesla_revenue['Revenue'].str.replace('$', '').str.replace(',', '')
tesla_revenue['Revenue'] = pd.to_numeric(tesla_revenue['Revenue'], errors='coerce')

# Remove rows with NaN revenue for cleaner graph
tesla_revenue = tesla_revenue.dropna(subset=['Revenue'])

# Graph the data
make_graph(tesla_revenue, 'Date', 'Revenue', 'Tesla Quarterly Revenue Over Time')


# ## Question 6: Plot GameStop Stock Graph
# Use the make_graph function to graph the GameStop Stock Data, also provide a title for the graph. The structure to call the make_graph function is make_graph(gme_data, gme_revenue, 'GameStop'). Note the graph will only show data upto June 2021

# In[59]:


import pandas as pd
import matplotlib.pyplot as plt

# Define the make_graph function
def make_graph(data, x_column, y_column, title):
    plt.figure(figsize=(10, 5))
    plt.plot(data[x_column], data[y_column], marker='o')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Fetch Gamestop revenue data (from previous steps)
print("Fetching Gamestop revenue data...")
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
tables = pd.read_html(url)
gamestop_revenue = tables[0]
gamestop_revenue.columns = ['Date', 'Revenue']
gamestop_revenue['Revenue'] = gamestop_revenue['Revenue'].str.replace('$', '').str.replace(',', '')
gamestop_revenue['Revenue'] = pd.to_numeric(gamestop_revenue['Revenue'], errors='coerce')

# Remove rows with NaN revenue for cleaner graph
gamestop_revenue = gamestop_revenue.dropna(subset=['Revenue'])

# Graph the data
make_graph(gamestop_revenue, 'Date', 'Revenue', 'Gamestop Quarterly Revenue Over Time')


# In[ ]:




