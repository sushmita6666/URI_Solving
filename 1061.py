dia,d1 = input().split()
d1 = int(d1)
a,b,c = map(int,input().split(':'))
dia2,d2 = input().split()
d2 = int(d2)
p,q,r = map(int,input().split(':'))
ds1 = (d1*86400)+(a*3600)+(b*60)+c
ds2 = (d2*86400)+(p*3600)+(q*60)+r
rem = ds2-ds1
day = rem//86400
rem = rem%86400
hr = rem//3600
rem = rem%3600
Min = rem//60
sec = rem%60

print(f'{day} dia(s)')
print(f"{hr} hora(s)")
print(f"{Min} minuto(s)")
print(f'{sec} segundo(s)')
