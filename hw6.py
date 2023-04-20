def display_multiplication_table() :
    for i in range(1, 10) :
        for j in range(2, 6):
            print(f'{j} X {i} = {j * i:2d}', end='\t')
    print('\n')
    for i in range(1, 10) :
        for j in range(6, 10):
            print(f'{j} X {i} = {j * i:2d}', end='\t')

display_multiplication_table()