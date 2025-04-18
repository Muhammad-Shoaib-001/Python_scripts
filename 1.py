def read_csv(file_path):
  data_dict = {}
  with open(file_path,'r') as file:
   header = file.readline().strip().split(",")

   for line in file:
     values = line.strip().split(",")
     key = values[0]
     data_dict[key] = values[1:]

     return data_dict

file_path = "D:\PY\Emissions.csv"
csv_data = read_csv(file_path)

for key,value in csv_data.items():
    print(f"{key}: {value}")
   
    