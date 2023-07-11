class Node:
    def __init__(self, data: str):
        self.__data = data
        self.__pointer: "Node" = None

    def get_data(self) -> str:
        return self.__data
    
    def set_data(self, data: str):
        self.__data = data

    def get_pointer(self) -> "Node":
        return self.__pointer
    
    def set_pointer(self, node: "Node"):
        self.__pointer = node

class LinkedList:
    def __init__(self):
        self.__head: "Node" = None

    def get_head(self) -> "Node":
        return self.__head
    
    def set_head(self, node: "Node"):
        self.__head = node

    def is_empty(self) -> bool:
        return self.__head == None

    def insert(self, data: str):
        # your code here
        pass

    def reverse(self):
        # your code here
        pass

    def reverse_without_stack(self):
        # your code here
        pass

    def display(self):
        if self.is_empty():
            print('Empty linked list')
            return
        
        print_str = ''
        curr = self.get_head()
        
        while curr:
            print_str += f'{curr.get_data()} -> '
            curr = curr.get_pointer()
        print(print_str[:-4])


def test_basic():
    print('+--------------+')
    print('|  Test basic  |')
    print('+--------------+')
    ll = LinkedList()
    ll.insert(5)
    ll.insert(3)
    ll.insert(2)
    ll.display()

    ll.reverse()
    ll.display()

    ll.reverse_without_stack()
    ll.display()
    print()

def test_edge_case():
    print('+-------------------+')
    print('|  Test edge cases  |')
    print('+-------------------+')
    ll = LinkedList()
    ll.display()

    ll.reverse()
    ll.display()
    print()

test_basic()
test_edge_case()