




def sum_kind():


    lines = int(input())


    for _ in range(lines):

        i,n = map(int,input().split())

        first_n_sum = (n * (n + 1)) // 2
        first_n_even_sum = n * ((2 * n + 2)//2)
        first_n_odd_sum = n * ((2 * n//2))


        print(f"{i} {first_n_sum} {first_n_odd_sum} {first_n_even_sum}")




sum_kind()


















