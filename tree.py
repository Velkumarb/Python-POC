#Trees Data Structure pgm in Python

#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:

#Tree Traversal in Python Pgm

#TreeNode class is used to represent the tree
#tree is the recursive data structure


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []  # in this list each children is the instance of the treenode class
        self.parent = None  # this parent property is stored in these parent of the treenode

#To Insert the Child using add_child method fucntion

    def add_child(self, child):
        child.parent = self  # Here child is the instance of the tree node class, It have an parent property i.e (self)
        self.children.append(child)

    def print_tree(self):
        print(self.data)
        for child in self.children:
            child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")
    

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("DELL"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("Vivo"))
    cellphone.add_child(TreeNode("Redmi"))
    cellphone.add_child(TreeNode("Oppo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Samsung"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    root.print_tree()


if __name__ == '__main__':
    build_product_tree()


