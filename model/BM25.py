"""

This model is to calculate the similarity of a query and a given document

"""
import math

data = {
    'query': ['wild', 'world'],  # query (optional)
    'N': 2226,  # total number of documents in corpus
    'n': [30, 816],  # number of documents containing the term
    'f': [7, 6],   # frequency of term in the given document
    'avg_len': 72,  # average length of all the documents
    'len': 57,  # length of the given document

    # not used here but will be used if you calculate the TF
    'max_f': 15,   # maximum frequency in given document for any term
}


class BM25:
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def sim(self):
        res = 0
        for i in range(len(data['n'])):
            f = data['f'][i]
            if f == 0:
                continue
            n = data['n'][i]
            res += ((f * (1 + self.k)) / (f + self.k * ((1 - self.b) + ((self.b * data['len']) / (data['avg_len']))))) * math.log2((data['N'] - n + 0.5) / (n + 0.5))
        return res


if __name__ == '__main__':
    model = BM25(1, 0.75)
    print(model.sim())
