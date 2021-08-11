print("*** Converting hh.mm.ss to seconds ***")
h, m, s = [int(x) for x in input("Enter hh mm ss : ").split()]
if h < 0:
    print("hh({}) is invalid!".format(h))
elif m<0 or m>59:
    print("mm({}) is invalid!".format(m))
elif s<0 or s>59:
    print("ss({}) is invalid!".format(s))
else:
    print("{:02d}:{:02d}:{:02d} = {:,} seconds".format(h, m, s, (h*3600 + m*60 + s)))