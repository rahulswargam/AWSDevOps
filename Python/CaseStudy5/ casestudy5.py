import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
hurricanes_data = pd.read_csv('hurricanes.csv')  # Adjust the filename/path as necessary

# Plot a Bar Graph
plt.figure(figsize=(10, 6))
plt.bar(hurricanes_data['Year'], hurricanes_data['Number of Hurricanes'], color='blue')
plt.xlabel('Year')
plt.ylabel('Number of Hurricanes')
plt.title('Number of Hurricanes in the US Along the Atlantic Coast')
plt.show()


# Plot Histogram of City Temperatures

# Load the dataset
temperatures_data = pd.read_csv('city_temperatures.csv')  # Adjust the filename/path as necessary

# Plot Histograms
plt.figure(figsize=(12, 6))

# San Francisco
plt.subplot(1, 2, 1)
plt.hist(temperatures_data[temperatures_data['City'] == 'San Francisco']['Temperature'], bins=20, color='green', alpha=0.7)
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.title('San Francisco Temperatures (2014-2015)')

# Moscow
plt.subplot(1, 2, 2)
plt.hist(temperatures_data[temperatures_data['City'] == 'Moscow']['Temperature'], bins=20, color='red', alpha=0.7)
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.title('Moscow Temperatures (2014-2015)')

plt.tight_layout()
plt.show()


# Plot a Pie-Chart of Number of Models Released by Manufacturers
# Load the dataset
manufacturers_data = pd.read_csv('manufacturers.csv')  # Adjust the filename/path as necessary

# Group by manufacturer and count the number of models
manufacturer_counts = manufacturers_data['Manufacturer'].value_counts()

# Plot a Pie-Chart
plt.figure(figsize=(8, 8))
plt.pie(manufacturer_counts, labels=manufacturer_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Number of Models Released by Each Manufacturer')
plt.show()

# Find the manufacturer with the largest releases
largest_manufacturer = manufacturer_counts.idxmax()
print(f'The manufacturer with the largest releases is {largest_manufacturer}')


# Create CSV File, Read in Pandas, Describe, Filter, and Plot

# Create the CSV file (already provided in the case study)

# Read in Pandas DataFrame
data = pd.read_csv('sales_data.csv')  # Adjust the filename/path as necessary

# Describe the Data
print(data['unit price'].describe())

# Filter the Data
filtered_data = data[['name', 'net_price', 'date']]
grouped_data = filtered_data.groupby('name').sum().reset_index()

# Plot the Graph
plt.figure(figsize=(12, 6))
plt.bar(grouped_data['name'], grouped_data['net_price'], color='purple')
plt.xlabel('Customer Name')
plt.ylabel('Total Sales')
plt.title('Total Sales by Each Customer')
plt.xticks(rotation=90)
plt.show()