totalsecond=int(input("total second is:"))
hour=int(totalsecond/3600)
remain_secound=totalsecond%3600
minute=int(remain_secound/60)
secound=remain_secound%60
print(hour,":",minute,":",secound)
