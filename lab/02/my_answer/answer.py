class Solution:
    def __init__(self, file_path):
        self.map = dict()
        self.book = dict()
        with open(file_path, 'r') as f:
            for line in f:
                tokens = line.split()
                self.map[tokens[0]] = [int(x) for x in tokens[1:]]

    def simple_query(self, query):
        if query == "":
            return []
        terms = query.split()
        if len(terms) == 1:
            if query in self.book:
                return self.book[query]
            return self.map[terms[0]]
        elif len(terms) == 3:
            first = [index for index in self.map[terms[0]]] if terms[0] not in self.book else self.book[terms[0]]
            second = [index for index in self.map[terms[2]]] if terms[2] not in self.book else self.book[terms[2]]
            if terms[1] == 'AND':
                res = mergeAND(first, second)
            elif terms[1] == "OR":
                res = mergeOR(first, second)
            else:
                res = mergeNOT(first, second)
            return res
        else:
            print("Invalid input")
            return None

    def query(self, query):
        terms = query.split()
        if len(terms) <= 3:
            return self.simple_query(query)
        else:
            ptr = 2
            cur_range = self.simple_query(terms[0])
            while ptr < len(terms):
                if terms[ptr - 1] == 'AND':
                    cur_range = mergeAND(cur_range, self.simple_query(terms[ptr]))
                elif terms[ptr - 1] == 'OR':
                    cur_range = mergeOR(cur_range, self.simple_query(terms[ptr]))
                else:
                    cur_range = mergeNOT(cur_range, self.simple_query(terms[ptr]))
                ptr += 2
            return cur_range

    def complex_query(self, query):
        stack = []
        query = f'( {query} )'
        terms = query.split()
        for term in terms:
            if term != ')':
                stack.append(term)
            else:
                tmp = stack.pop()
                q, key = "", ""
                while tmp != "(":
                    q = tmp.join([" ", q])
                    key = tmp.join(["_", key])
                    tmp = stack.pop()
                self.book[key] = self.query(q.strip())
                stack.append(key)
        return self.book[stack[0]]


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
                res.append(l2[ptr2])
                ptr2 += 1
        else:
            res += l1[ptr1:] if ptr2 == len(l2) else l2[ptr2:]
            return res
    return res


def mergeOR_verify(list1, list2):
    li = list(set(list1) | set(list2))
    li.sort()
    return li


def mergeNOT(list1, list2):
    ptr1, ptr2 = 0, 0
    res = []
    while ptr1 < len(list1) or ptr2 < len(list2):
        if ptr1 < len(list1) and ptr2 < len(list2):
            if list1[ptr1] == list2[ptr2]:
                ptr1, ptr2 = ptr1 + 1, ptr2 + 1
            elif list1[ptr1] < list2[ptr2]:
                res.append(list1[ptr1])
                ptr1 += 1
            else:
                ptr2 += 1
        elif ptr1 < len(list1):
            res += list1[ptr1:]
            return res
        else:
            return res
    return res


def mergeNOT_verify(list1, list2):
    li = list(set(list1) - set(list2))
    li.sort()
    return li


def compare(list1, list2):
    for i, j in zip(list1, list2):
        if i != j:
            return False
    return True


if __name__ == '__main__':
    s = Solution('../index.txt')
    print(s.complex_query('( ( ( consists AND experimental AND gases ) ) )'))