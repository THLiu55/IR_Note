import json
import os

# backlinks = {
#     1: [4],
#     2: [1, 3],
#     3: [2],
#     4: [1, 2, 3]
# }

class PageRank:
    def __init__(self, bs, damping):
        self.backlinks = bs
        self.damping = damping
        self.weight = dict()
        for _, values in self.backlinks.items():
            for val in values:
                if val not in self.weight:
                    self.weight[val] = 1
                else:
                    self.weight[val] += 1
        for key, val in self.weight.items():
            self.weight[key] = 1 / val
        self.rank = [1 for _ in range(len(backlinks))]

    def next_step(self):
        newRank = [0 for _ in range(len(backlinks))]
        for i in range(len(self.rank)):
            newRank[i] = 1 - self.damping
            if i in self.backlinks:
                froms = self.backlinks[i]
            else:
                froms = []
            for start in froms:
                newRank[i] += self.damping * (self.rank[start] * self.weight[start])
        self.rank = newRank


if __name__ == "__main__":
    with open('/Users/liutianhao/PycharmProjects/IR_Note/exercise/pagerank.json', 'r') as f:
        backlinks = json.load(f)
        print(backlinks)
        model = PageRank(backlinks, 0.85)
        for i in range(10):
            model.next_step()
            print(model.rank)
