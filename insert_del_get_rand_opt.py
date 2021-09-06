import random 

class RandomizedSet:

    def __init__(self):
        self.ls = []
        self.map = dict()
        self.size

    def insert(self, val):

        if val in self.map:
            return False

        self.ls.append(val)
        self.size += 1
        self.map[val] = self.size

        return True

    def remove(self, val):

        if val not in self.map:
            return False

        idx = self.map[val]

        self.map[self.ls[-1]] = idx
        self.ls[-1], self.ls[idx] = self.ls[idx], self.ls[-1]

        self.ls.pop()
        self.size -= 1

        return True

    def getRandom(self):
        return random.choice(self.ls)