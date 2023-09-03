from typing import List


class Tree:
    def __init__(self):
        self.thisTree: List["Node"] = []
        self.root: int = -1


    def add(self, newItem: str):
        curr = self.root
        prev = -1
        new_idx = len(self.thisTree)
        
        while curr != -1:
            node = self.thisTree[curr]
            prev = curr
            curr = node.getLeftPtr() if node.getData() > newItem else node.getRightPtr()

        if prev == -1:
            self.root = 0
        elif self.thisTree[prev].getData() > newItem:
            self.thisTree[prev].setLeftPtr(new_idx)
        else:
            self.thisTree[prev].setRightPtr(new_idx)

        node = Node()
        node.setData(newItem)
        self.thisTree.append(node)


    def print(self):
        s = [self.root]
        res = []
        while s:
            front = s.pop(0)
            if front == -1:
                res.append(None)
            else:
                node = self.thisTree[front]
                res.append(node.getData())    
                s.append(node.getLeftPtr())
                s.append(node.getRightPtr())
        
        while res[-1] == None:
            res.pop()
        
        print(res)

    
    def postOrderTraversal(self):
        tree = self.thisTree

        def helper(idx: int):
            if idx != -1:            
                # left, display, right
                helper(tree[idx].getLeftPtr())
                print(tree[idx].getData())
                helper(tree[idx].getRightPtr())

        helper(self.root)


class Node:
    def __init__(self):
        self.data: str = ''
        self.leftPtr: int = -1
        self.rightPtr: int = -1
    

    def setData(self, data: str):
        self.data = data


    def setLeftPtr(self, x: int):
        self.leftPtr = x

    
    def setRightPtr(self, y: int):
        self.rightPtr = y


    def getData(self) -> str:
        return self.data
    

    def getLeftPtr(self) -> int:
        return self.leftPtr
    

    def getRightPtr(self) -> int:
        return self.rightPtr
    


################
#   test 3.2   #
################

t = Tree()
t.add('Tiger')
t.add('Lemur')
t.add('Bat')
t.add('Yak')
t.add('Ostrich')
t.add('Raccoon')
t.add('Macaw')
t.add('Zebra')
t.print()


################
#   test 3.3   #
################

t.postOrderTraversal()