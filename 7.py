import pandas as pd
import matplotlib.pyplot as plt

# Read CSV File using Pandas
def read_csv_pandas(file_path):
    df = pd.read_csv(file_path)
    df.set_index(df.columns[0], inplace=True)  # Set the first column (Country) as index
    df.columns = df.columns.astype(str)  # Ensure columns are strings (years)
    return df

# Calculate Statistics for a Given Year
def calc_stats_pandas(df, year):
    year = str(year)  # Convert to string for indexing
    if year not in df.columns:
        print(f"Year {year} not found in data.")
        return
    
    emissions = df[year].dropna().astype(float)  # Convert to float and drop missing values
    min_country = emissions.idxmin()  # Country with min emissions
    max_country = emissions.idxmax()  # Country with max emissions
    avg_emission = emissions.mean()   # Average emissions

    print("\nAll data from Emissions.csv has been read into a dataframe.")
    print(f"\nSelect a year to find statistics (1997 to 2010): \033[92m{year}\033[0m")
    print(f"In {year}, countries with minimum and maximum CO₂ emission levels were: [{min_country}] and [{max_country}] respectively.")
    print(f"Average CO₂ emissions in {year} were {avg_emission:.6f}")

# Plot Emissions for Two Countries
def plot_emissions_pandas(df, countries):
    df_selected = df.loc[countries].T.astype(float)  # Transpose for plotting & convert to float
    df_selected.plot(figsize=(8, 5), marker='o', linestyle='-')

    plt.xlabel("Year")
    plt.ylabel("Emissions in Capita")
    plt.title("Year vs Emissions in Capita")
    plt.legend(title="Country")
    plt.grid()
    plt.show()

# Main Execution
file_path = "D:\\PY\\Emissions.csv"  # Update with actual file path
df = read_csv_pandas(file_path)

# User Input for Yearly Statistics
user_year = input("Select a year to find statistics (1997 to 2010): ")
calc_stats_pandas(df, user_year)

# User Input for Visualization
user_countries = input("\nWrite two comma-separated countries for which you want to visualize data: ")
country_list = [c.strip() for c in user_countries.split(",")]

plot_emissions_pandas(df, country_list)
