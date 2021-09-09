class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.search = []
        self.match_keys = []
        self.sents = dict()

        for s, t in zip(sentences, times):
            self.sents[s] = self.sents.get(s, 0) + t 

        self.match_keys = self.sents.keys()

    def input(self, c):

        if c=='#':
            new = ''.join(self.search)
            self.sents[new] = self.sents.get(new, 0) + 1
            self.match_keys = self.sents.keys()
            self.search = []
            return []
        else:
            self.search.append(c)
            l = len(self.search)
            str_match = ''.join(self.search)
            self.match_keys = [s for s in self.match_keys if s[:l]==str_match]
            res = sorted([(self.sents[s], s) for s in self.match_keys], key=lambda x: (-x[0], x[1]))[:3]
            return [r[1] for r in res]


sentences = ["abc", "abbc", "a"]
times = [3,3,3]
acs = AutocompleteSystem(sentences, times)

acs.input("b")
acs.input("c")
acs.input("#")
acs.input("b")
acs.input("c")
acs.input("#")
acs.input("a")
acs.input("b")   