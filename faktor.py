import math



def faktor():

    numbers = input()

    num_articles,impact_factor = numbers.split()

    num_articles,impact_factor = int(num_articles),int(impact_factor)




    number_of_citations_required = (num_articles * (impact_factor - 1)) + 1


    print(number_of_citations_required)


if __name__ == "__main__":
    

    faktor()


