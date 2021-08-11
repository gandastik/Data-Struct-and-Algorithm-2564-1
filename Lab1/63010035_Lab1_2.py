height, weight = [float(x) for x in input("Enter your High and Weight : ").split()]
bmi = float(weight) / (height**2)

if bmi >= 30:
    print("Fat")
elif bmi >= 25:
    print("Getting Fat")
elif bmi >= 23:
    print("More than Normal Weight")
elif bmi >= 18.50:
    print("Normal Weight")
elif bmi >= 0:
    print("Less Weight")