






def batting_average():


    at_bats = int(input())

    bats = input().split()

    

    total = 0
    number_of_official_at_bats = 0
    for bat in bats:
        bat = int(bat)
        if bat == -1:
            continue

        total += bat
        number_of_official_at_bats += 1



    slugging_percentage = total / number_of_official_at_bats


    print(slugging_percentage)



batting_average()

















