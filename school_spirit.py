



def school():


    n = int(input())

    scores = []

    total_score = 0
    for i in range(n):
        score = int(input())
        actual_score = (1/5) * score * (4/5)**i
        total_score += actual_score
        scores.append(actual_score)

    group_score = total_score

    print(group_score)

    s = 0
    for i in range(len(scores)):
        score = scores[i]
        new_group_score = group_score - score

        for j in range(i + 1,len(scores)):
            score_2 = scores[j]
            new_group_score -= score_2
            new_group_score += score_2/(4/5)

        s += new_group_score



    print(s/n)





school()



    

















