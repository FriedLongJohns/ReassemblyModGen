import helpers as hps

print("\n\t\t[helpers]")
print("\n\t-boundName-")
print("in bound 1 : expecting 1")
print(hps.boundName(99, bounds=[(0,100,"1"),(100,1000,"2"),(1000,10000,"3")]))
print("outside bounds : expecting False")
print(hps.boundName(-5, bounds=[(0,100,"1"),(100,1000,"2")]))
print("in bound 2, negative : expecting 2")
print(hps.boundName(-5, bounds=[(0,100,"1"),(-5,1000,"2")]))

print("\n\t-boundNum-")
print("bound 1 : expecting 0-100")
print(hps.boundNum("1", bounds=[(0,100,"1"),(100,1000,"2"),(1000,10000,"3")]))
print("not a bound : expecting False")
print(hps.boundNum("five", bounds=[(0,100,"1"),(100,1000,"2")]))

print("\n\t-randColor-")
print("0-255 0-255 0-0 : expecting 000000 - ffff00")
[print(hps.randColor(min=(0,0,0),max=(255,255,0))) for i in range(5)]

print("\n\t-randfloat-")
print("0 10 : expecting 0-10")
[print(hps.randfloat(0,10)) for i in range(5)]
print("0.0 1.0 : expecting 0.0-1.0")
[print(hps.randfloat(0.0,1.0)) for i in range(5)]
