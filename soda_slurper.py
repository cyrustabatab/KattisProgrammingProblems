



def soda():
    e,f,c = map(int,input().split())


    soda_bottles =(e + f)
    total = 0
    while soda_bottles >= c:
        new_bottles = soda_bottles // c
        soda_bottles -= soda_bottles//c * c
        total += new_bottles
        soda_bottles += new_bottles
        


    print(total)



soda()














