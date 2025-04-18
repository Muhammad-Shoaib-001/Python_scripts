servers = ["web01", "db01", "cache01"]

for server in servers:
  print(f" checking servers :  {server}")

print("\n🔢 Port scan simulation")
for port in range(80, 85):  # 80 to 84
    print(f"🧪 Scanning port: {port}")

print("\n⏳ While loop demo")
attempt = 1
while attempt <= 3:
    print(f"⚙️  Restart attempt {attempt}")
    attempt += 1

status = {"web01": True, "db01": False, "api01": True}
up_count = 0
for server, is_up in status.items():
   if is_up:
    up_count += 1
print(f"\n✅ Total servers UP: {up_count}/{len(status)}")


server_cpu_load = {
    "web01": 45,
    "db01": 83,
    "api01": 78,
    "cache01": 91,
    "worker01": 59
}
for server, load in server_cpu_load.items():
   if load >= 80 :
       print(f"❌ ALERT! {server} has high CPU load: {load}%")