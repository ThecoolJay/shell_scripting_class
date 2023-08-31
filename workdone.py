#Auth: "<Cooljay>"

print ("==========CAL SIMPLE INTREST=========")
principal =int(input("Enter Principal: "))
rate = int(input("Enter Rate: "))
time = int(input("Enter Time: "))
si = principal * rate * time // 100
print (f"Answer: {si}")


print ("==========CAL AREA OF CIRCLE=========")
radius = int(input("Enter Radius: "))
ac = (radius ** 2) * 3.14
print (f'Answer: {ac}')


print ("==========CAL AREA OF TRIANGLE=========")
base = int(input("Enter Base: "))
height = int(input("Enter Height: "))
a = 0.5 * base *height
print (f"Answer: {a}")