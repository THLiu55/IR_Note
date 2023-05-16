# rank based fusion

# interleaving - rank-based fusion:
# use roundrobin to add item from top of the set into result without replication

def interleaving(data1, data2, size):
    res = []
    for i in range(size):
        p1, p2 = 0, 0
        # pick value in turn
        if i % 2 == 0:
            tmp = data1[p1]
            # skip the value already in result set
            while tmp in res and p1 != len(data1) - 1:
                p1 += 1
                tmp = data1[p1]
            if tmp not in res:
                res.append(tmp)
        else:
            tmp = data2[p2]
            while tmp in res and p2 != len(data2) - 1:
                p2 += 1
                tmp = data2[p2]
            if tmp not in res:
                res.append(tmp)
    return res


# Borda fuse
# first list all the docs without replication, then score each answer set from different IR algorithm, add the score to creat a new rank

# empty score - (1+2+3+..+n) / n   -- n is the documents that are not chosen
def empty_score(n):
    return sum(i for i in range(n + 1)) / n


def borda(data1, data2):
    docs = set(data1) | set(data2)
    size = len(docs)
    score1, score2 = dict(), dict()
    emptyScore1, emptyScore2 = empty_score(len(docs) - len(data1)), empty_score(len(docs) - len(data2))
    # calculate the score for each voter
    for i in range(len(data1)):
        score1[data1[i]] = size - i
    for val in docs - set(data1):
        score1[val] = emptyScore1
    for i in range(len(data2)):
        score2[data2[i]] = size - i
    for val in docs - set(data2):
        score2[val] = emptyScore2
    # calculate final score
    final_score = dict()
    # rank
    for val in docs:
        final_score[val] = score2[val] + score1[val]
    rank = list(final_score.items())
    rank = [x[0] for x in sorted(rank, key=lambda x: x[1], reverse=True)]
    return rank


# Reciprocal Rank Fusion
# s = sum(1/(k+r(d))), r(d) is the rank of the answer set, k is 60 by experiment

def RRF(dataset):  # dataset: [result_list1, result_list2, ...]
    final_score = dict()
    for data in dataset:
        for i in range(len(data)):
            final_score[data[i]] = 1 / (60 + i) if data[i] not in final_score else final_score[data[i]] + 1 / (60 + i)
    # rank
    rank = list(final_score.items())
    rank = [x[0] for x in sorted(rank, key=lambda x: x[1], reverse=True)]
    return rank


# Score-based Fusion
# CombSum: normalize the score range from different IR algorithm and then add them together and generate a rank base on that

def normalize(data):
    max_val = max(d[1] for d in list(data.items()))
    min_val = min(d[1] for d in list(data.items()))
    for key, val in data.items():
        data[key] = (val - min_val) / (max_val - min_val)
    return data


def CombSum(dataset):
    sum_score = dict()
    for i in range(len(dataset)):
        dataset[i] = normalize(dataset[i])
        for key, val in dataset[i]:
            sum_score[key] = val if key not in sum_score else sum_score[key] + val
    rank = list(sum_score.items())
    rank = [x[0] for x in sorted(rank, key=lambda x: x[1], reverse=True)]
    return rank


# CombMNZ: based on CombSUM, at the end multiply the score by number of result sets it occurred
def CombMNZ(dataset):
    sum_score = dict()
    num_result_set = dict()
    for i in range(len(dataset)):
        dataset[i] = normalize(dataset[i])
        for key, val in dataset[i]:
            (sum_score[key], num_result_set[key]) = (val, 1) if key not in sum_score else (sum_score[key] + val, num_result_set[key] + 1)
    for key, val in sum_score:
        sum_score[key] *= num_result_set[key]
    rank = list(sum_score.items())
    rank = [x[0] for x in sorted(rank, key=lambda x: x[1], reverse=True)]
    return rank


if __name__ == "__main__":
    print(borda([19, 5, 12, 4, 14, 15, 1, 9, 10, 11], [5, 14, 20, 7, 1, 11, 18, 3]))

# score based fusion
