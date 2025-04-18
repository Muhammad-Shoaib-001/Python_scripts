# Day 2: Data Types Practice

# Integer
cpu_cores = 4
print("CPU Cores:", cpu_cores, "| Type:", type(cpu_cores))

# Float
load_avg = 1.23
print("Load Average:", load_avg, "| Type:", type(load_avg))

# String
server_name = "web01"
print("Server Name:", server_name, "| Type:", type(server_name))

# Boolean
is_server_up = True
print("Is Server Up?:", is_server_up, "| Type:", type(is_server_up))

# List
server_list = ["web01", "db01", "cache01"]
print("Server List:", server_list, "| Type:", type(server_list))

# Dictionary
server_info = {
    "name": "web01",
    "ip": "192.168.0.10",
    "status": "running"
}
print("Server Info:", server_info, "| Type:", type(server_info))

for server in server_list:
    print("Checking server:", server)