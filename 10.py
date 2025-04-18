load = float(input('Enter current server load'))
if load < 1.0:
      print("✅ Server is healthy.")
elif load < 2.0:
        print("⚠️  Server load is moderate.")
else:
        print("❌ Server load is high. Investigate immediately!")

port = int(input("Enter port number: "))
if port == 22:
    print("🛡️  SSH port detected.")
elif port == 80 or port == 443:
    print("🌐 Web port detected.")
else:
    print("🔎 Unknown port. May need inspection.")

servers = {
    "web01": True,
    "db01": False,
    "cache01": True
}
for server, status in servers.items():
    if status:
        print(f"{server} is ✅ up")
else:
        print(f"{server} is ❌ down")