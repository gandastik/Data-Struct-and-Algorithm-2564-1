def move(n, A, C, B):
    if(n == 1):
        print(f'{n} from {A} to {C}')
    else:
        move(n-1, A, B, C)
        print(f'{n} from {A} to {C}')
        move(n-1, B, C, A)

move(4, 'A', 'C', 'B')