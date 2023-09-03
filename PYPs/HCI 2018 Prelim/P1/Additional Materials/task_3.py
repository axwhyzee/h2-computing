class Node():
    def __init__(self):
        self.name = ""
        self.pointer = -1


    def setname(self, n):
        self.name = n


    def setpointer(self, p):
        self.pointer = p


    def getname(self):
        return self.name


    def getpointer(self):
        return self.pointer



class LinkedList():
    def __init__(self):
        self.node = [None] + [Node() for i in range(10)]
        for i in range(1, len(self.node)):
            self.node[i].setpointer(i + 1)
        self.node[-1].setpointer(0)
        
        self.start = 0
        self.nextfree = 1


    def insert(self, n, p):
        if self.isfull():
            print("Full")
        else:
            prev = 0
            curr = self.start
            pos = 1
            while pos != p:
                prev = curr
                curr = self.node[curr].getpointer()
                pos += 1

            temp = self.node[self.nextfree].getpointer()
            if pos == 1:
                self.start = self.nextfree
            else:
                self.node[prev].setpointer(self.nextfree)
                
            self.node[self.nextfree].setpointer(curr)
            self.node[self.nextfree].setname(n)
            self.nextfree = temp
        

    def delete(self, p):
        if self.isempty():
            print("Empty")
            return
        
        curr = self.start
        prev = 0
        pos = 1
        while pos != p:    
            prev = curr
            curr = self.node[curr].getpointer()
            pos += 1

        if pos == 1:
            self.start = self.node[self.start].getpointer()

        # detach from used list
        else:
            self.node[prev].setpointer(self.node[curr].getpointer())

        # add to unused list
        self.node[curr].setpointer(self.nextfree)
        self.node[curr].setname("")
        self.nextfree = curr


    def length(self):
        def helper(lst, i):
            if i == 0:
                return 0
            else:
                return helper(lst, lst[i].getpointer()) + 1

        return helper(self.node, self.start)


    def isempty(self):
        if self.start == 0:
            return True
        return False


    def isfull(self):
        if self.nextfree == 0:
            return True
        return False


    def display(self):
        print("START:", self.start)
        print("NEXT FREE:", self.nextfree)
        i = 1
        for node in self.node[1:]:
            print(i, "NAME:", node.getname(), "POINTER:", node.getpointer())
            i += 1


class Queue(LinkedList):
    def __init__(self):
        super().__init__()
        self.front = 0
        self.rear = 0
    
    def enqueue(self, i):
        if self.isfull():
            print("Full")
            return
        elif self.isempty():
            self.front = 1
    
        self.rear += 1
        self.insert(i, self.rear)


    def dequeue(self):
        self.delete(1)
        self.front = self.start


    def display(self):
        curr = self.start
        print_str = self.node[curr].getname()
        print_str += "<- Front"
        
        while curr != self.rear:
            print(print_str)
            curr = self.node[curr].getpointer()
            print_str = self.node[curr].getname()

        print_str += "<- Rear"
        print(print_str)
        
            
##ll = LinkedList()
##ll.insert('Ali', 1)
##
##ll.insert('Jack', 1)
##ll.display()
##ll.insert('Ben',2)
##ll.display()
##ll.delete(1)
##ll.display()
##ll.insert('Jane', 2)
##ll.insert('Ken', 3)
##ll.display()
##ll.delete(2)
##ll.display()

##q = Queue()
##q.enqueue("John")
##q.enqueue("May")
##q.enqueue("Steven")
##q.enqueue("Celine")
##q.enqueue("Tom")
##q.enqueue("Ryan")
##q.display()
##print("===")
##q.dequeue()
##q.display()
##print("===")
##q.dequeue()
##q.display()

