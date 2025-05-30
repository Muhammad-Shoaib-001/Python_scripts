import matplotlib.pyplot as plt

def read_csv(file_path):
    with open(file_path, 'r') as file:
        header = file.readline().strip().split(",")  # Read header line
        data_dict = {}  # Dictionary to store data

        for line in file:
            values = line.strip().split(",")
            key = values[0]  # Country name as key
            data_dict[key] = {header[i]: values[i] for i in range(1, len(header))}

    return header, data_dict  # Return both header and data


def calc_stats(year, header, data_dict):
    if year not in header:
        print(f"Year {year} not found in data.")
        return

    emission = {}  # Dictionary to store emissions for the given year

    for country, values in data_dict.items():
        try:
            emission[country] = float(values[year])
        except ValueError:
            continue  # Skip if data is missing or invalid

    if not emission:  # If no valid emissions found
        print(f"No data available for year {year}.")
        return
    
    # Calculate statistics
    min_country = min(emission, key=emission.get)  # Country with min emissions
    max_country = max(emission, key=emission.get)  # Country with max emissions
    avg_emission = sum(emission.values()) / len(emission)  # Average emissions

    print("\nAll data from Emissions.csv has been read into a dictionary.")
    print(f"\nIn {year}, countries with minimum and maximum CO₂ emission levels were: [{min_country}] and [{max_country}] respectively.")
    print(f"Average CO₂ emissions in {year} were {avg_emission:.6f}")


def plot_emissions(country, header, data_dict):
    if country not in data_dict:
        print(f"Country {country} not found in data.")
        return

    years = header[1:]  # Exclude the "Country" column
    emissions = []

    for year in years:
        try:
            emissions.append(float(data_dict[country][year]))
        except ValueError:
            emissions.append(None)  # Handle missing data

    plt.figure(figsize=(7, 5))
    plt.plot(years, emissions, marker='o', linestyle='-')
    plt.xlabel("Year")
    plt.ylabel(f"Emissions in {country}")
    plt.title("Year vs Emissions in Capita")
    plt.grid()
    plt.show()


# Example usage:
file_path = "D:\\PY\\Emissions.csv"  # Replace with actual file path
header, csv_data = read_csv(file_path)

# Taking user input for the year
user_year = input("Select a year to find statistics (1997 to 2010): ")
calc_stats(user_year, header, csv_data)

# Taking user input for the country
user_country = input("\nSelect the country to visualize: ")
plot_emissions(user_country, header, csv_data)
