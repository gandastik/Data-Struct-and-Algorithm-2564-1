codeWord=str(input("Put your code word here : "))
divisor=str(input("Put your divisor here : "))
# divisor='11001'

def toList(x):
	l = []
	for i in range (0,len(x)):
		l.append(int(x[i]))
	return (l)
def toString(x):
	str1 =""
	for i in range (0,len(x)):
		str1+=str(x[i])
	return (str1)

def divide(val1,val2):
    a = toList(val1)
    b = toList(val2)
    working = toString(val1) +"\n"

    res=""
    addspace=""

    while len(b) <= len(a) and a:
        if a[0] == 1:
            del a[0]
            for j in range(len(b)-1):
                    a[j] ^= b[j+1]
            if (len(a)>0):
                working +=addspace+toString(b)+"\n"
                working +=addspace+"-" * (len(b))+"\n"
                addspace+=" "
                working +=addspace+toString(a)+"\n"
                res+= "1"

        else:
            del a[0]
            working +=addspace+"0" * (len(b))+"\n"
            working +=addspace+"-" * (len(b))+"\n"
            addspace+=" "
            working +=addspace+toString(a)+"\n"
            res+="0"


    print("Result is\t",res)
    print("Remainder is\t",toString(a))

    print("Working is\t\n\n",res.rjust(len(val1)),"\n",)
    print("-" * (len(val1)),"\n",working)

    return toString(a)

res = divide(codeWord, divisor)
print(res)