import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("Emissions.csv")

# Convert the data into a dictionary format
data_dict = df.set_index('Country').to_dict()

print("All data from Emissions.csv has been read into a dictionary.\n")

# Get user input for the year
year = int(input("Select a year to find statistics (1997 to 2010): "))
column_name = str(year)

if column_name in df.columns:
    min_country = df.loc[df[column_name].idxmin(), 'Country']
    max_country = df.loc[df[column_name].idxmax(), 'Country']
    avg_emissions = df[column_name].mean()

    print(f"\nIn {year}, countries with minimum and maximum CO2 emission levels were: [{min_country}] and [{max_country}] respectively.")
    print(f"Average CO2 emissions in {year} were {avg_emissions:.6f}\n")
else:
    print(f"Year {year} not found in the dataset.")

# Get user input for the country
country = input("\nSelect the country to visualize: ")

if country in df["Country"].values:
    plt.figure(figsize=(7, 5))
    plt.plot(df.columns[1:], df[df["Country"] == country].values[0][1:], marker='o', linestyle='-')
    plt.xlabel("Year")
    plt.ylabel(f"Emissions in {country}")
    plt.title("Year vs Emissions in Capita")
    plt.grid()
    plt.show()
else:
    print(f"Country {country} not found in the dataset.")
