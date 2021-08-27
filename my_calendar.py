class MyCalendarTwo:

    def __init__(self):
        self.single = []
        self.double = []

    def book(self, start: int, end: int):

        for e in self.double:
            if not (start>=e[1] or end<=e[0]):
                return False 

        for e in self.single:
            if not (start>=e[1] or end<=e[0]):
                self.double.append([max(start, e[0]),min(end, e[1])]) # Add the intersection

        self.single.append([start, end]) 
        return True 

        

