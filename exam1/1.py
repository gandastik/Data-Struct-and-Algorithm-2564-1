print(" *** Wind classification ***")
n = float(input("Enter wind speed (km/h) : "))
if(n >= 209):
    print("Wind classification is ",end='')
    print("Super Typhoon.")
elif(n >=  102):
    print("Wind classification is ",end='')
    print("Typhoon.")
elif(n >= 56):
    print("Wind classification is ",end='')
    print("Tropical Storm.")
elif(n >= 52):
    print("Wind classification is ",end='')
    print("Depression.")
elif(n >= 0):
    print("Wind classification is ",end='')
    print("Breeze.")
else:
    print("!!!Wrong value can't classify.")
    