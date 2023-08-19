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
        node = Node(data)
        
        if not self.__head:
            self.__head = node
            return
        
        tail = self.__head.get_left()
        if not tail or tail == self.__head:
            self.__head.set_left(node)
            self.__head.set_right(node)
            node.set_left(self.__head)
            node.set_right(self.__head)
        else:
            node.set_right(self.__head)
            node.set_left(tail)
            self.__head.set_left(node)
            tail.set_right(node)


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
        left = self.__head
        res = 0
        done = {}

        while 1:
            right = left.get_right()
            left_height = left.get_data()
            highest_mid = 0

            while right != left:
                right_height = right.get_data()

                if right_height > left_height:
                    if right not in done.get(left, []):
                        res += 1
                        done[right] = done.get(right, []) + [left]
                    break
                elif right_height >= highest_mid:
                    if right not in done.get(left, []):
                        done[right] = done.get(right, []) + [left]
                        res += 1
                
                right = right.get_right()
                highest_mid = max(highest_mid, right_height)

            left = left.get_right()

            if left == self.__head:
                break
        return res


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