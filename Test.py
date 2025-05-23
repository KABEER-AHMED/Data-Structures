# Creating the node class
class Node:
    def __init__(self,data):
        self._data = data
        self._next = None
    def get_data(self):
        return self._data
    def set_data(self,data):
        self._data = data
    
    data = property(get_data,set_data)
    
    def get_next(self):
        return self._next
    def set_next(self,node_next):
        self._next = node_next
    
    next = property(get_next,set_next)
    
class LinkedList:
    def __init__(self):
        self.head = None
    def add_node(self,item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
    def print(self):
        llstr =''
        iterator = self.head
        if iterator == None:
            print("Linked list is empty")
            return None
        while iterator!=None:
            llstr += str(iterator.data) + "-->"
            iterator = iterator.next
        print(llstr)
    
    
    def search(self,value):
        itr = self.head
        index = 0
        while itr:
            if itr.data == value:
                return index
            itr = itr.next
            index+=1
    
    def remove(self,item):
        count = 0
        index = self.search(item)
        if index is None:
            print("The item was not found")
            return
        if index == 0:  
            self.head = self.head.next
            return
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1

ll = LinkedList()
ll.add_node(45)
ll.add_node(50)
ll.add_node(55)
ll.print()
ll.add_node(66)
ll.print()
ll.remove(50)
ll.print()