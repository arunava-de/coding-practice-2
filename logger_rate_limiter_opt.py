class Logger:

    def __init__(self):

        self.hash_items = {}
        self.curr_time = 0

    def clear_logger(self): # We clear the logger with all

        items = list(self.hash_items.keys())
        for i in items:
            if self.hash_items[i]+10<=self.curr_time:
                del self.hash_items[i]

    def should_print(self, timestamp, message):
        self.curr_time = timestamp
        self.clear_logger()

        if message in self.hash_items: # This means we can't print
            return False 
        
        self.hash_items[message] = timestamp

        return True 

logger = Logger()
logger.should_print(1, "foo")
logger.should_print(2, "bar")
logger.should_print(3, "foo")
logger.should_print(8, "bar")
logger.should_print(10, "foo")
logger.should_print(11, "foo")
logger.should_print(11, "bar")
logger.should_print(12, "bar")
logger.should_print(12, "bar")