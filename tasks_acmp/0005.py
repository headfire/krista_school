n = int(input())
days = input().split()
days1 = list()
days2 = list()
for day in days:
    iday = int(day)
    if iday % 2 != 0:
        days1.append(iday) 
    else:
        days2.append(iday)    
print(*days1)
print(*days2)
if len(days1) > len(days2):
    print("NO")
else:
    print("YES")
        
