class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

# Second largest element in a binary search tree

# notes:    largest element will be bottom right of binary tree.
#           Next largest would be the parent of the bottom right element

currentElement = Bin

while BinaryTreeNode.Right != null :
