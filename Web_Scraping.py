# Importing necessary libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL of the Wikipedia page containing the list of largest companies in the United States by revenue
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

# Sending a GET request to the URL
page = requests.get(url)

# Parsing the page content with BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# Finding the table containing the data
table = soup.find_all('table')[1]

# Extracting table headers
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]

# Creating a DataFrame with the extracted headers
df = pd.DataFrame(columns=world_table_titles)

# Extracting table rows
column_data = table.find_all('tr')

# Iterating over each row and extracting data
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data

# Saving the DataFrame to a CSV file
df.to_csv("path to save", index=False)

# Printing confirmation message
print("File Generated!")
