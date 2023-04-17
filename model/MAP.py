answer_list = [123, 84, 56, 6, 8, 9, 511, 129, 187, 25, 38, 48, 250, 113, 3]
relevant_set = {3, 5, 9, 25, 39, 44, 56, 71, 89, 123}


def map_score():
    score, count = 0, 0
    for i in range(len(answer_list)):
        if answer_list[i] in relevant_set:
            count += 1
            score += count / (i + 1)
    return score / len(relevant_set)


if __name__ == '__main__':
    print(map_score())