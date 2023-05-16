"""

This model is to calculate the similarity of a query and a given document

"""
import math


class BM25:
    def __init__(self, k, b, N, n, f, avg, len):
        self.k = k
        self.b = b
        self.N = N
        self.n = n
        self.f = f
        self.avg = avg
        self.len = len

    def sim(self):
        res = 0
        for i in range(len(self.n)):
            f = self.f[i]
            if f == 0:
                continue
            n = self.n[i]
            res += ((f * (1 + self.k)) / (f + self.k * ((1 - self.b) + ((self.b * self.len) / self.avg)))) * math.log2((self.N - n + 0.5) / (n + 0.5))
        return res


if __name__ == '__main__':
    model = BM25(1, 0.75, 500000, [40000, 300], [15, 25], 10, 9)
    print(model.sim())
