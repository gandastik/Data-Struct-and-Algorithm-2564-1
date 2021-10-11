from itertools import permutations
import time
'''
Permutations of 8 queens, 1 queen per row. 
Can we do better than the previous? Of course! 
If we only take care of the permutations of the numbers 1 to 8, 
and map the first place to row 1, the second place to row 2, 
and so on, we do not worry anymore about being in the same 
row or being in the same column. The total arrangements in this 
case is 8! = 40,320, 416 times better than the previous!
https://python.plainenglish.io/coding-the-8-queens-problem-in-python-d168f8df844b
'''
n = 12


def print_table():
    for row in range(n):
        print(table[row])


def put_queen(x, y):
    if table[y][x] == 0:
        for m in range(n):
            table[y][m] = 1
            table[m][x] = 1
            table[y][x] = 2
            if y+m <= (n-1) and x+m <= (n-1):
                table[y+m][x+m] = 1
            if y-m >= 0 and x+m <= (n-1):
                table[y-m][x+m] = 1
            if y+m <= (n-1) and x-m >= 0:
                table[y+m][x-m] = 1
            if y-m >= 0 and x-m >= 0:
                table[y-m][x-m] = 1
        return True
    else:
        return False


start = time.time()

table = [[0]*n for _ in range(n)]
listinput = [x for x in range(n)]
# print(listinput)
perms = permutations(listinput)


num_comb = 0
for perm in perms:
    for index in range(0, n, 1):
        if put_queen(perm[index], index) == True:
            if index == n-1:
                # print_table()
                num_comb += 1
                print(f"solution{num_comb}")
                print(" ")
        else:
            break

    table = [[0] * n for _ in range(n)]


end = time.time()
print("nqueen (iterative)")
print(f"N : {n}")
print('number of solutions = ', num_comb)
print(end-start, "sec")