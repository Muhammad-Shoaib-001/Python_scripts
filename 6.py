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
    year = str(year)  # Ensure year is a string for dictionary lookup
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
    print(f"\nSelect a year to find statistics (1997 to 2010): \033[92m{year}\033[0m")  # Green text
    print(f"In {year}, countries with minimum and maximum CO₂ emission levels were: [{min_country}] and [{max_country}] respectively.")
    print(f"Average CO₂ emissions in {year} were {avg_emission:.6f}")


def plot_emissions(countries, header, data_dict):
    years = [int(year) for year in header[1:]]  # Convert years to int for correct x-axis
    plt.figure(figsize=(8, 5))

    for country in countries:
        if country not in data_dict:
            print(f"Country {country} not found in data.")
            continue

        emissions = []
        for year in header[1:]:
            try:
                emissions.append(float(data_dict[country][year]))
            except ValueError:
                emissions.append(None)  # Handle missing data
        
        plt.plot(years, emissions, marker='o', linestyle='-', label=country)

    plt.xlabel("Year")
    plt.ylabel("Emissions in Capita")
    plt.title("Year vs Emissions in Capita")
    plt.legend()
    plt.grid()
    plt.show()


# Example usage:
file_path = "D:\\PY\\Emissions.csv"  # Replace with actual file path
header, csv_data = read_csv(file_path)

# Taking user input for the year
user_year = input("Select a year to find statistics (1997 to 2010): ")
calc_stats(user_year, header, csv_data)

# Taking user input for visualization

user_countries = input("\nWrite two comma-separated countries for which you want to visualize data: ")

country_list = [c.strip() for c in user_countries.split(",")]

plot_emissions(country_list, header, csv_data)
