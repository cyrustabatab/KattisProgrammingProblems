


def icpc_awards():


    n = int(input())


    unis = set()

    winners = 0
    while winners < 12:
        university,team = input().split()

        if university not in unis:
            winners += 1
            print(university,team)
            unis.add(university)





icpc_awards()






