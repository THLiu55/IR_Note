import math

from porter import PorterStemmer
import numpy

documents = {
    'd1': ['Shipment', 'of', 'gold', 'damaged', 'in', 'a', 'fire'],
    'd2': ['Delivery', 'of', 'silver', 'arrived', 'in', 'a', 'silver', 'truck'],
    'd3': ['Shipment', 'of', 'gold', 'arrived', 'in', 'a', 'large', 'truck']
}
processed_docs = []
query = ['gold', 'silver', 'truck']
processed_query = set()
book = dict()
stemmer = PorterStemmer()


stopwords = set()
with open('stopwords.txt', 'r') as f:
    for line in f:
        stopwords.add(line.rstrip())


def preprocess():
    cnt = 0
    for key, vals in documents.items():
        tmp = set()
        for val in vals:
            if val not in stopwords:
                val = stemmer.stem(val)
                if val not in book:
                    book[val] = cnt
                    cnt += 1
                tmp.add(book[val])
        processed_docs.append(tmp)
    for term in query:
        processed_query.add(book[term])


def get_binary_weight():
    doc_w = numpy.zeros(shape=[len(documents), len(book)])
    for vec, doc in zip(doc_w, processed_docs):
        length = 0
        for index in doc:
            vec[index] = 1
            length += vec[index] ** 2
        vec *= 1 / math.sqrt(length)
    query_w = numpy.zeros(shape=[len(book)])
    length = 0
    for index in processed_query:
        query_w[index] = 1
        length += query_w[index] ** 2
    query_w *= 1 / math.sqrt(length)
    return doc_w, query_w


def sim(doc_w, query_w):
    print(numpy.matmul(doc_w, query_w.T))


if __name__ == '__main__':
    preprocess()
    d, q = get_binary_weight()
    sim(d, q)
