class Read:
    
    def __init__(self):
        self.buf = [None, None, None, None]
        self.pos = 0
        self.length = 0
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i<n:
            if self.length==0 or self.pos==self.length: # Empty or used up
                num_read = read4(self.buf)
                if num_read==0: #End of line
                    break 
                    
                self.pos = 0 
                self.length = num_read
                
            buf[i] = self.buf[self.pos]
            self.pos += 1
            i += 1
            
        return i