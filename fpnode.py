class Fpnode:
    def __init__(self, item='root'):
        self.item = id
        self.pa = None
        self.child = {}
        self.count = 0
    
    def is_root(self):
        return self.pa is None