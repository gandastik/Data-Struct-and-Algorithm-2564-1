print(" *** Divisible number ***")
num = int(input("Enter a positive number : "))
factors = []
for i in range(1,num+1):
    if(num % i == 0):
        factors.append(i)
if(len(factors) == 0):
    print("0 is OUT of range !!!")
else:
    print("Output ==> ", end='')
    for i in factors:
        print(i, end=' ')
    print(f"\nTotal ==> {len(factors)}")
