"""

Precision: (rel & ret) / ret
the proportion of retrieved documents that are relevant

Recall: (rel & ret) / rel
the proportion of relevant documents that are retrieved
"""

answer_list = [123, 84, 56, 6, 8, 9, 511, 129, 187, 25, 38, 48, 250, 113, 3]
relevant_set = {3, 5, 9, 25, 39, 44, 56, 71, 89, 123}


def precision():
    # get the number of (rel & ret)
    rel_ret = 0
    for doc in answer_list:
        rel_ret = rel_ret + 1 if doc in relevant_set else rel_ret
    return rel_ret / len(answer_list)


def recall():
    # get the number of (rel & ret)
    rel_ret = 0
    for doc in answer_list:
        rel_ret = rel_ret + 1 if doc in relevant_set else rel_ret
    return rel_ret / len(relevant_set)


def precision_at(index):
    # get the number of (rel & ret)
    rel_ret = 0
    for i in range(index):
        rel_ret = rel_ret + 1 if answer_list[i] in relevant_set else rel_ret
    return rel_ret / index


def precisionR():
    # get the number of (rel & ret)
    rel_ret = 0
    for i in range(len(relevant_set)):
        rel_ret = rel_ret + 1 if answer_list[i] in relevant_set else rel_ret
    return rel_ret / len(relevant_set)


if __name__ == "__main__":
    print(f"precision: {precision()}")
    print(f"recall: {recall()}")
    i = 3
    print(f"precision@{i}:  {precision_at(i)}")
    print(f"R-precision: {precisionR()}")

