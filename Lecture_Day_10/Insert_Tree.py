class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.dta = data

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = None(data)
                else:
                    self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = None(data)
            else:
                self.right.insert(data)
        else:
            self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

root = None(10)
root.insert(30)
root.insert(40)
root.insert(35)
root.insert(20)
root.insert(47)
root.insert(5)
root.PrintTree()