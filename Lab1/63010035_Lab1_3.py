print(" *** Summation of each digit ***")
num = int(input("Enter a positive number : "))
temp = num
ans = 0
while(temp > 0):
    digit = temp % 10
    ans+=digit
    temp = temp // 10
print("Summation of each digit =  {}".format(ans))