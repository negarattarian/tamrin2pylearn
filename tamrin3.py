print("hello to time change into second")
print("❌pay attention to am and pm")
hour=int(input("get hour:"))
minute=int(input("get minute:"))
second=int(input("get second:"))
print(hour,":",minute,":",second)
minute_s=minute*60
hour_s=hour*3600
totalsecond=hour_s+minute_s+second
print("the time i second is",":",totalsecond)