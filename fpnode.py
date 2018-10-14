class Fpnode:
    def __init__(self, id):
        self.id = id
        self.pa = None
        self.child = {}
    
    def setPa(self,pa):
        self.pa = pa
    
    def is_root(self):
        return self.pa is None