import pandas as pd

# Load the data
data = pd.read_csv('BigMartSalesData.csv')
import matplotlib.pyplot as plt

# Convert date to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Extract month and year from the date
data['YearMonth'] = data['Date'].dt.to_period('M')

# Group by YearMonth and sum sales
monthly_sales = data.groupby('YearMonth')['Sales'].sum()

# Plot total sales per month
plt.figure(figsize=(10, 6))
monthly_sales.plot()
plt.title('Total Sales Per Month for Year 2011')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

# Plot total sales per month as bar chart
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='bar')
plt.title('Total Sales Per Month for Year 2011 (Bar Chart)')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

# Group by Country and sum sales
country_sales = data.groupby('Country')['Sales'].sum()

# Plot pie chart
plt.figure(figsize=(8, 8))
country_sales.plot(kind='pie', autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Sales Distribution by Country for Year 2011')
plt.ylabel('')
plt.show()

# Plot scatter plot for invoice amounts
plt.figure(figsize=(10, 6))
plt.scatter(data['InvoiceAmount'], data['Sales'], c='blue', alpha=0.5)
plt.title('Scatter Plot of Invoice Amounts')
plt.xlabel('Invoice Amount')
plt.ylabel('Sales')
plt.show()

plt.figure(figsize=(10, 6))
bar_plot = monthly_sales.plot(kind='bar')
plt.title('Total Sales Per Month for Year 2011 (Bar Chart)')
plt.xlabel('Month')
plt.ylabel('Total Sales')

# Adding values on top of the bars
for p in bar_plot.patches:
    bar_plot.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))

plt.show()

plt.figure(figsize=(8, 8))
country_sales.plot(kind='pie', autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Sales Distribution by Country for Year 2011')
plt.ylabel('')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(data['InvoiceAmount'], data['Sales'], c='green', alpha=0.5)
plt.title('Scatter Plot of Invoice Amounts')
plt.xlabel('Invoice Amount')
plt.ylabel('Sales')
plt.show()

