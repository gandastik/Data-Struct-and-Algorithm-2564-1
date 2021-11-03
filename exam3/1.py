def harmonic_sum(n):
    #code here
    if(n == 1.0):
        print("1",end='')
        return 1.0
    ret = (1.0/n) + harmonic_sum(n - 1)
    print(f' + 1/{n}',end='')
    return ret

print(" *** Harmonic sum ***")
num = int(input("Enter number of terms : ")) 
print(" = %.8f" %(harmonic_sum(num)))