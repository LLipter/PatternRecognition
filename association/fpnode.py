class Fpnode:
    def __init__(self, item='root'):
        self.item = item
        self.pa = None
        self.child = {}
        self.count = 0
    
    def is_root(self):
        return self.pa is None