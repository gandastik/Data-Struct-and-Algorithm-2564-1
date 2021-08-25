def hbd(age: int):
    if(age % 2 == 0):
        return f"saimai is just 20, in base {int(age / 2)}!"
    else : return f"saimai is just 21, in base {int(age / 2)}!"

year = int(input("Enter year : "))
print(hbd(year))