from porter import PorterStemmer as Stemmer


class Solution:
    def __init__(self, stopwords_path):
        self.stemmer = Stemmer()
        self.docs = None
        self.stopwords = set()
        self.dictionary = dict()
        with open(stopwords_path, 'r') as f:
            for line in f:
                self.stopwords.add(line.rstrip())

    def load_docs(self, doc_path):
        f = open(doc_path, 'r')
        self.docs = f.read().split('   /\n')
        f.close()

    def create_dict(self):
        for doc in self.docs:
            terms = doc.split()
            if terms[0] != '/':
                doc_dict = dict()
                for term in terms[1:]:
                    if term not in self.stopwords:
                        term = self.stemmer.stem(term)
                        doc_dict[term] = 1 if term not in doc_dict else doc_dict[term] + 1
                self.dictionary[terms[0]] = doc_dict

    def test(self):
        for doc_id in self.dictionary:
            sorted_keys = sorted(self.dictionary[doc_id], key=self.dictionary[doc_id].get, reverse=True)
            if self.dictionary[doc_id][sorted_keys[0]] > 1:
                print('{}:'.format(doc_id), end='')
                i = 0
                while self.dictionary[doc_id][sorted_keys[i]] > 1:
                    print(' {} ({})'.format(sorted_keys[i], self.dictionary[doc_id][sorted_keys[i]]), end='')
                    i += 1
                print()


if __name__ == '__main__':
    s = Solution('stopwords.txt')
    s.load_docs('npl-doc-text.txt')
    s.create_dict()
    s.test()
