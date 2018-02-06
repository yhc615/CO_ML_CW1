"""
Decision-tree Class Definition
"""

class Tree:
    def __init__(self, label):
        self.op = label
        self.kids = []
        self.leaf
    def create_child(self, left, right):
        self.kids.extend([left, right])
    def label_leaf(self, label):
        if label in [0,1]:
            self.leaf = label
        else:
            raise Exception("Invalid Label for leaf node")
            