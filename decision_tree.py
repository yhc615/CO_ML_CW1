"""
Decision-tree Class Definition
"""

class Tree:
    def __init__(self,label ,i='b'): #i = { 'b':branch , 'l':leaf}, default branch
        self.kids = []
        if i == 'b':
            self.node_label = label
        else:
            if label in [0,1]:
                self.leaf_label = label
            else:
                raise Exception("Invalid Label for leaf node")
            
    def create_child(self, left, right):
        self.kids = [left, right]
        
            