import math
from porter import PorterStemmer

documents = {
    'd1': 'London Bridge is falling down'.split(),
    'd2': 'Falling down falling down'.split(),
    'd3': 'London Bridge is falling down my fair lady'.split()
}
query = 'London Bridge'.split()
stemmer = PorterStemmer()
use_stemmer = True

stopwords = set()
with open('stopwords.txt', 'r') as f:
    for line in f:
        stopwords.add(line.rstrip())

book = dict()
TF_weights = dict()
IDF_weights = dict()
cnt = 0
for name, content in documents.items():
    tmp = dict()
    for word in content:
        if word not in stopwords:
            word = stemmer.stem(word) if use_stemmer else word
            if word not in book:
                book[word] = cnt
                cnt += 1
            tmp[book[word]] = 1 if book[word] not in tmp else tmp[book[word]] + 1
    max_f = max(tmp.values())
    TF_weights[name] = dict()
    for index, f in tmp.items():
        TF_weights[name][index] = f / max_f
    for key in tmp.keys():
        IDF_weights[key] = 1 if key not in IDF_weights else IDF_weights[key] + 1
N = len(documents)
for key, val in IDF_weights.items():
    IDF_weights[key] = math.log(N / val, 2)


doc_w = dict()
for key, val in TF_weights.items():
    doc_w[key] = dict()
    for index, tf_w in val.items():
        doc_w[key][index] = tf_w * IDF_weights[index]

query_w = dict()
for term in query:
    if term not in stopwords:
        term = stemmer.stem(term) if use_stemmer else term
        query_w[book[term]] = 1 if book[term] not in query_w else query_w[book[term]] + 1

max_f = max(query_w.values())
for key, val in query_w.items():
    query_w[key] = (val / max_f) * IDF_weights[key]

print(f"Book: {book}")
print(f"TF: {TF_weights}")
print(f"IDF: {IDF_weights}")
print(f"Document Weight: {doc_w}")
print(f"Query Weight: {query_w}")


def calculate_similarity(doc_weight, q_weight):
    doc_length = dict()
    for name, doc in doc_weight.items():
        doc_length[name] = math.sqrt(sum(w ** 2 for w in doc.values()))
    query_length = math.sqrt(sum(w ** 2 for w in q_weight.values()))
    res = dict()
    for name, doc in doc_weight.items():
        tmp = 0
        for term, w in q_weight.items():
            if term in doc:
                tmp += w * doc[term]
        res[name] = tmp / (query_length * doc_length[name])
    return res


res = calculate_similarity(doc_w, query_w)
print(f"Similarity: {res}")
