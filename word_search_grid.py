class TrieNode:
    
    def __init__(self):

        self.children = [None]*26
        self.isEndOfWord = False 

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def _charToInd(self, ch):
        return ord(ch)-ord('a')

    def _getNode(self): # Get a new node which is not root
        return TrieNode()

    def insert(self, key):
        curr = self.root
        length = len(key)

        for i in range(length):
            idx = self._charToInd(key[i])

            if not curr.children[idx]:
                curr.children[idx] = self._getNode()
            
            curr = curr.children[idx]
        
        curr.isEndOfWord = True 

    def search(self, key):

        curr = self.root
        length = len(key)
        prev = None

        for i in range(length):
            idx = self._charToInd(key[i])

            prev = curr

            if not curr.children[idx]:
                return False 
            curr = curr.children[idx]

        out = curr.isEndOfWord
        curr.isEndOfWord = False # Ensures no duplicates come up

        if curr.children == [None]*26: # We're at leaf node
            prev.children[idx] = None # Prune this leaf
            return out
        else:
            return out

    def startsWith(self, pfx):

        curr = self.root 
        length = len(pfx)

        for i in range(length):
            idx = self._charToInd(pfx[i])

            if not curr.children[idx]:
                return False 
            
            curr = curr.children[idx]
        
        return True

def word_search(board, words):

    t = Trie()

    m = len(board)
    n = len(board[0])

    for word in words:
        t.insert(word)

    results = []

    def recur(i, j, cand, t):

        l = board[i][j]
        if t.search(cand):
            if cand not in results:
                results.append(cand)
        
        board[i][j] = "*"


        x_diff = [0, 0, 1, -1]
        y_diff = [1, -1, 0, 0]

        for k in range(4):
            x = i+x_diff[k]
            y = j+y_diff[k]

            if x>=0 and x<m and y>=0 and y<n and board[x][y]!='*':
                curr = cand + board[x][y]
                if t.startsWith(curr):
                    recur(x, y, curr, t)
        
        board[i][j] = l

    for i in range(m):
        for j in range(n):
            if t.startsWith(board[i][j]):
                recur(i, j, board[i][j], t)
                
    
    return results 


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
word_search(board, words)

board = [["a","b"],["c","d"]]
words = ["abcb"]
word_search(board, words)

board = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
word_search(board, words)