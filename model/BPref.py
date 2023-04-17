"""

every contribution is calculated by 1 - (n ranked higher than r) / R
sum(them) / R

"""

answer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
relevant_set = {2, 4, 9, 11}
non_relevant_set = {1, 6, 7, 8, 10}


def bpref():
    R = len(relevant_set)
    score, cnt = 0, 0
    for i in range(len(answer_list)):
        if answer_list[i] in non_relevant_set:
            cnt = min(R, cnt + 1)
        elif answer_list[i] in relevant_set:
            score += (1 - (cnt / R))
    return score / R


def bpref_10():
    R = len(relevant_set)
    score, cnt = 0, 0
    for i in range(len(answer_list)):
        if answer_list[i] in non_relevant_set:
            cnt = min(R, cnt + 1)
        elif answer_list[i] in relevant_set:
            score += (1 - (cnt / (R + 10)))
    return score / R


if __name__ == "__main__":
    print(f"bprf: {bpref()}")
    print(f"bprf-10: {bpref_10()}")
