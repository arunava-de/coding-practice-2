import random 

class RandomizedSet:

    def __init__(self):
        self.randset = set()
        self.ls = []

    def insert(self, val):

        if val in self.randset:
            return False 

        self.randset.add(val)
        self.ls.append(val)

        return True 

    def remove(self, val):

        if val not in self.randset:
            return False 

        self.randset.remove(val)
        return True 

    def getRandom(self):

        # return random.choice(list(self.randset))
        r = random.choice(self.ls)

        while r not in self.randset:
            r = random.choice(self.ls)

        return r 
