class Node:
    def __init__(self, data: int):
        self.__data = data
        self.__left = None
        self.__right = None

    
    def get_data(self) -> int:
        return self.__data
    
    
    def get_left(self) -> "Node":
        return self.__left
    
    
    def get_right(self) -> "Node":
        return self.__right
    

    def set_left(self, node: "Node"):
        self.__left = node


    def set_right(self, node: "Node"):
        self.__right = node


class CircularLinkedList:
    def __init__(self):
        self.__head = None

    
    def insert(self, data: int):
        # +------------------+
        # |  your code here  |
        # +------------------+
        pass


    def display(self):
        if not self.__head:
            print('Empty circular linked list')
            return
        
        # left to right
        print("Left to right: ", end='')
        print(self.__head.get_data(), end='')
        curr = self.__head.get_right()

        while curr and curr != self.__head:
            print(' ->', curr.get_data(), end='')
            curr = curr.get_right()
        if curr:
            print(' ->', curr.get_data(), end='')
        print()


    def visible_mountain_pairs(self) -> int:
        # +------------------+
        # |  your code here  |
        # +------------------+
        pass


print("+----------+")
print("|  Test 1  |")
print("+----------+")
cll = CircularLinkedList()
cll.insert(1)
cll.insert(5)
cll.insert(3)
cll.insert(4)
cll.insert(2)
cll.display()
ans = cll.visible_mountain_pairs()
print('Your result:', ans, '(PASSED)' if ans == 7 else '(FAILED)')
print()
 

print("+----------+")
print("|  Test 2  |")
print("+----------+")
cll = CircularLinkedList()
cll.insert(4)
cll.insert(2)
cll.insert(2)
cll.insert(5)
cll.insert(1)
cll.display() 
ans = cll.visible_mountain_pairs()
print('Your result:', ans, '(PASSED)' if ans == 8 else '(FAILED)')
print()


print("+----------+")
print("|  Test 3  |")
print("+----------+")
cll = CircularLinkedList()
cll.insert(1)
cll.insert(5)
cll.insert(6)
cll.insert(4)
cll.insert(2)
cll.display() 
ans = cll.visible_mountain_pairs()
print('Your result:', ans, '(PASSED)' if ans == 7 else '(FAILED)')
print()


print("+----------+")
print("|  Test 4  |")
print("+----------+")
cll = CircularLinkedList()
cll.insert(1)
cll.insert(5)
cll.display() 
ans = cll.visible_mountain_pairs()
print('Your result:', ans, '(PASSED)' if ans == 1 else '(FAILED)')
print()


print("+----------+")
print("|  Test 5  |")
print("+----------+")
cll = CircularLinkedList()
cll.insert(1)
cll.insert(5)
cll.insert(1)
cll.insert(2)
cll.insert(3)
cll.insert(4)
cll.insert(4)
cll.insert(4)
cll.insert(5)
cll.display() 
ans = cll.visible_mountain_pairs()
print('Your result:', ans, '(PASSED)' if ans == 18 else '(FAILED)')
print()