from numpy import random


class Solution:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            self.map = dict()
            line = f.readline()
            while line is not None:
                split_line = line.split(" ")
                self.map[split_line[0]] = split_line[1:]


def mergeAND(l1, l2):
    res = []
    ptr1, ptr2 = 0, 0
    while ptr1 < len(l1) and ptr2 < len(l2):
        if l1[ptr1] == l2[ptr2]:
            res.append(l1[ptr1])
            ptr1, ptr2 = ptr1 + 1, ptr2 + 1
        elif l1[ptr1] < l2[ptr2]:
            ptr1 += 1
        else:
            ptr2 += 1
    return res


def mergeAND_verify(l1, l2):
    li = list(set(l1) & set(l2))
    li.sort()
    return li

def mergeOR(l1, l2):
    res = []
    ptr1, ptr2 = 0, 0
    while ptr1 < len(l1) or ptr2 < len(l2):
        if ptr1 < len(l1) and ptr2 < len(l2):
            if l1[ptr1] == l2[ptr2]:
                res.append(l1[ptr1])
                ptr2 += 1
                ptr1 += 1
            elif l1[ptr1] < l2[ptr2]:
                res.append(l1[ptr1])
                ptr1 += 1
            else:
                res.append(l1[ptr2])
                ptr2 += 1
        else:
            res += l1[ptr1:] if ptr2 == len(l2) else l2[ptr2:]
            return res
    return res


def mergeOR_verify(list1, list2):
    li = list(set(list1) | set(list2))
    li.sort()
    return li

def compare(list1, list2):
    for i, j in zip(list1, list2):
        if i != j:
            return False
    return True


if __name__ == '__main__':
    l1 = list(set(random.randint(0, 10000000, size=10)))
    l2 = list(set(random.randint(0, 10000000, size=10)))
    l1.sort()
    l2.sort()
    print(mergeOR_verify(l1, l2))
    print(mergeOR(l1, l2))
    print(compare(mergeAND_verify(l1, l2), mergeAND(l1, l2)))