filepath = "../words.txt"


def printFileByLine(path):
    with open(path, 'r') as f:
        line = f.readline()
        while line is not None:
            print(line)
            line = f.readline()


def printFileByLineWithParentheses(path):
    with open(path, 'r') as f:
        line = f.readline()
        while line is not None:
            line = "".join([f"({word}) " for word in line.strip('\n').split(" ")])
            print(line)
            line = f.readline()


def printFileByLineWithParenthesesLower(path):
    with open(path, 'r') as f:
        line = f.readline()
        while line is not None:
            line = "".join([f"({word.lower()}) " for word in line.strip('\n').split(" ")])
            print(line)
            line = f.readline()


class Statistics:
    def __init__(self, path):
        self.map = dict()
        with open(path, 'r') as f:
            for line in f:
                for word in line.strip('\n').split():
                    word = word.lower()
                    if word in self.map:
                        self.map[word] += 1
                    else:
                        self.map[word] = 1

    def show_map(self):
        print('--------------------')
        for key, val in self.map.items():
            print(f"{val}:   {key}")
        print('--------------------')

    def show_map_in_order(self):
        print('--------------------')
        for key in sorted(self.map.keys(), key=self.map.get, reverse=True):
            print(f"{key}:     {self.map[key]}")
        print('--------------------')


if __name__ == "__main__":
    s = Statistics(path=filepath)
    s.show_map()
    s.show_map_in_order()
