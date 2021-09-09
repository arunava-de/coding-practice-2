class TrieNode:
    def __init__(self):
        self.children = [None]*27
        self.isEndOfWord = False
        self.timesOccur = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def char_to_idx(self, c):
        if c==' ':
            return 26
        return ord(c) - ord('a')

    def _get_node(self):
        return TrieNode()

    def insert(self, key, t):

        length = len(key)
        curr = self.root

        for i in range(length):
            idx = self.char_to_idx(key[i])

            if not curr.children[idx]:
                curr.children[idx] = self._get_node()

            curr = curr.children[idx]
        
        curr.isEndOfWord = True
        curr.timesOccur = t 

class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.search_engine = Trie()
        self.pfx = ""
        self.start = self.search_engine.root
        self.valid = -1

        for i in range(len(sentences)):
            self.search_engine.insert(sentences[i], times[i])

    def DFS(self, u, results, curr_pfx):
            
        if u==None:
            return

        if u.isEndOfWord:
            results.append((curr_pfx, u.timesOccur))

        for i in range(27):
            if u.children[i]:
                if i==26:
                    char = ' '
                else:
                    char = chr(i+ord('a'))
                self.DFS(u.children[i], results, curr_pfx + char)

    def get_results(self, c):
        
        if c=='#': #Make corresponding updates
            if self.start.isEndOfWord:
                self.start.timesOccur += 1
            else:
                self.search_engine.insert(self.pfx, 1)
            self.start = self.search_engine.root
            self.pfx = ""
            self.valid = -1
            return []

        self.pfx += c
        curr = self.start
        idx = self.search_engine.char_to_idx(c)

        if self.valid==0:
            return []

        if not curr.children[idx]: # We ensure that till # comes, we keep on giving []
            self.valid = 0 
            return []
        else:
            self.valid = 1
        self.start = curr.children[idx]

        # if curr.isEndOfWord:
        #     return [self.pfx]

        results = []

        self.DFS(self.start, results, self.pfx)
        results.sort(key=lambda x: (-x[1],x[0]))

        return results[:3]

sentences = ["abc", "abbc", "a"]
times = [3,3,3]
acs = AutocompleteSystem(sentences, times)

# acs.get_results("b")
# acs.get_results("c")
# acs.get_results("#")
# acs.get_results("b")
# acs.get_results("c")
# acs.get_results("#")
# acs.get_results("a")
# acs.get_results("b")
# acs.get_results("c")
# acs.get_results("#")
# acs.get_results("a")
# acs.get_results("b")
# acs.get_results("c")
# acs.get_results("#")

# acs.pfx += "a"
# curr = acs.start 
# idx = acs.search_engine.char_to_idx("a")
# start = curr.children[idx]
# results = []

# def DFS(u, results, curr_pfx):
        
#     if u==None:
#         return

#     if u.isEndOfWord:
#         results.append((curr_pfx, u.timesOccur))

#     for i in range(27):
#         if u.children[i]:
#             if i==26:
#                 char = ' '
#             else:
#                 char = chr(i+ord('a'))
#             DFS(u.children[i], results, curr_pfx + char)

# DFS(start, results, acs.pfx)