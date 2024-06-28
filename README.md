# Web-Scraping-Python-Project
## Overview
This project involves web scraping data from a Wikipedia page to extract information about the largest companies in the United States by revenue. The extracted data is then saved into a CSV file.
With the help of extracted data, certain insights are represented using Pivot Tables and charts.

## Tech Stack
1. Python:
    - Pandas, BeautifulSoup
3. Excel:
    - Pivot Tables, Pivot Charts

## Code Walk Through
1. **Import Libraries:** The script starts by importing the necessary libraries- BeautifulSoup for parsing HTML, requests for making HTTP requests, and pandas for data manipulation.
2. **URL of the Wikipedia Page:** The URL of the Wikipedia page containing the list of the largest companies in the United States by revenue is stored in the url variable.
3. **Sending a GET Request:** An HTTP GET request is sent to the URL, and the response is stored in the page variable.
4. **Parsing the Page Content:** The content of the page is parsed using BeautifulSoup
5. **Finding the Data Table:** The script locates the table containing the desired data. It selects the second table on the page (table[1]).
6. **Extracting Table Rows:** Each row of the table is extracted and appended to the DataFrame.
7. **Saving Data to CSV:** The DataFrame is saved to a CSV file. You need to specify the path where you want to save the file.
8. **Confirmation Message:** A message is printed to confirm that the file has been generated.

## Dashboard Creation
The data obtained through the extraction was a clean data. There were no N/As. Standardization of the data was required which includes adding commas and currency symbols.

## Data Insights
The dashboard is divided into several key components:

1. **Total Employees in a Company (Top Center Chart):**
- This bar chart shows the total number of employees for each company.
- The x-axis represents the company names, and the y-axis represents the count of employees.

2. **Revenue-Based Chart (Top Right Chart):**
- This bar chart displays the revenue for each company in USD millions.
- The x-axis represents the company names, and the y-axis represents the revenue.

3. **Total Revenue Growth of Company (Bottom Center Chart):**
- This bar chart illustrates the revenue growth for each company.
- The x-axis represents the company names, and the y-axis represents the revenue growth.

4. **Industry-Based Chart (Bottom Right Chart):**
- This bar chart categorizes companies based on their industries and shows the count of companies within each industry.
- The x-axis represents the industry categories, and the y-axis represents the count of companies.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.




