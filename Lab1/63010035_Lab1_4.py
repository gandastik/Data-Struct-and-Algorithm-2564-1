def odd_list(al): 
    ret = []
    for i in al:
        if(i % 2 != 0):
            ret.append(i)
    return ret

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)