"""
+----------------------+
|  Binary Search Tree  |
+----------------------+
"""
class TreeNode:
    def __init__(
        self, 
        data: int, 
        left: "TreeNode" = None, 
        right: "TreeNode" = None
    ):
        self.__data = data
        self.__left = left
        self.__right = right

    def get_data(self) -> int:
        return self.__data
    
    def get_left(self) -> "TreeNode":
        return self.__left
    
    def get_right(self) -> "TreeNode":
        return self.__right
    
    def set_left(
        self, 
        node: "TreeNode"
    ):
        self.__left = node
    
    def set_right(
        self, 
        node: "TreeNode"
    ):
        self.__right = node

    def __str__(self):
        return f'DATA: {self.__data}\nLEFT: {self.__left.__data if self.__left else None}\nRIGHT: {self.__right.__data if self.__right else None}'


class BST:
    def __init__(
        self, 
        root: "TreeNode" = None
    ):
        self.__root = root

    def insert(
        self, 
        data: int
    ):
        node = TreeNode(data)
        if not self.__root:
            self.__root = node
            return
        
        prev = None
        curr = self.__root
        while curr:
            prev = curr
            curr = curr.get_left() if curr.get_data() >= data else curr.get_right()

        if prev.get_data() > data:
            prev.set_left(node)
        else:
            prev.set_right(node)

    def inorder_traversal(
        self, 
        node: "TreeNode"
    ):
        if node != None:
            self.inorder_traversal(node.get_left())
            print(node, '\n')
            self.inorder_traversal(node.get_right())

    def display(self):
        s = [self.__root]
        res = []

        while s:
            node = s.pop(0)
            if node:
                res.append(node.get_data())
                s.append(node.get_left())
                s.append(node.get_right())
            else:
                res.append(None)
        for i in range(len(res)-1, -1, -1):
            if res[i] != None:
                res = res[:i+1]
                break
        print(res)

    def height(self):
        def helper(node: "TreeNode"):
            print('x', node.get_data() if node else None)
            if not node:
                return 0
            return max(helper(node.get_left()), helper(node.get_right())) + 1
        print('root', self.__root.get_data())
        return helper(self.__root)


"""
+---------------+
|  Linked List  |
+---------------+
"""
class Node:
    def __init__(
        self, 
        data: int
    ):
        self.__data = data
        self.__pointer = None

    def get_pointer(self) -> "Node":
        return self.__pointer

    def set_pointer(
        self, 
        node: "Node"
    ):
        self.__pointer = node

    def get_data(self) -> int:
        return self.__data


class LinkedList:
    def __init__(self):
        self.__head = None

    def insert(
        self, 
        data: int
    ):
        node = Node(data)

        if not self.__head:
            self.__head = node
            return

        prev = None
        curr = self.__head
        while curr != None and curr.get_data() < data:
            prev = curr
            curr = curr.get_pointer()

        if prev != None:
            prev.set_pointer(node)
        else:
            self.__head = node

        node.set_pointer(curr)

    def display(self):
        curr = self.__head
        while curr != None:
            print(curr.get_data(), "--> ", end='')
            curr = curr.get_pointer()
        print()

    def _insert_mid_recursively(
        self, 
        arr: list,
        st: int,
        end: int,
        bst: "BST"
    ):
        if st == end:
            bst.insert(arr[st])
            return
        elif st > end:
            return
        
        mid = (st+end) // 2
        bst.insert(arr[mid])
        self._insert_mid_recursively(arr, st, mid-1, bst)
        self._insert_mid_recursively(arr, mid+1, end, bst)


    def build_bst_from_segment(
        self, 
        start: int, 
        end: int
    ) -> "BST":
        bst = BST()
        vals = []
        curr = self.__head

        for _ in range(start):
            curr = curr.get_pointer()
        for _ in range(end-start):
            vals.append(curr.get_data())
            curr = curr.get_pointer()

        self._insert_mid_recursively(vals, 0, end-start-1, bst)

        return bst
    

print("+----------+")
print("|  Test 1  |")
print("+----------+")
ll = LinkedList()
ll.insert(5)
ll.insert(7)
ll.insert(0)
ll.insert(3)
ll.insert(6)
ll.insert(9)
ll.insert(99)
ll.display() # 0 --> 3 --> 5 --> 6 --> 7 --> 9 --> 99 --> 
print()

print("+----------+")
print("|  Test 2  |")
print("+----------+")
bst = BST()
bst.insert(5)
bst.insert(7)
bst.insert(9)
bst.insert(99)
bst.insert(0)
bst.insert(3)
bst.insert(6)
bst.display() # [5, 0, 7, None, 3, 6, 9, None, None, None, None, None, 99]
print(bst.height())
print()

print("+----------+")
print("|  Test 3  |")
print("+----------+")
bst_built = ll.build_bst_from_segment(0, 7)
bst_built.display() # [6, 3, 9, 0, 5, 7, 99]
print(bst_built.height())