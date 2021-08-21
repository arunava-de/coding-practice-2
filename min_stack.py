class MinStack:
    def __init__(self):
        self.L = []
        self.min = float('inf')
    
    def top(self):
        return self.L[-1]

    def push(self, val):
        if val<self.min:
            self.min = val 
        self.L.append(val)
    
    def get_min(self):
        return self.min

    def pop(self):
        out = self.L.pop()

        if out>self.min:
            return out

        # Need to update min 

        self.min = min(self.L)
        return out