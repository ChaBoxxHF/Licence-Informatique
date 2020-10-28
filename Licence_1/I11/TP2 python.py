a = float(input())
b = float(input())
if a==0 and b==0:
    print("INF")
elif a==0:
    print("0")
elif b==0:
    print("1")
elif a<0 or b<0:
    print(0)
else:
    print("2")
