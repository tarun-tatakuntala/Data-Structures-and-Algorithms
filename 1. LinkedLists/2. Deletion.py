"""
Deletion also has 3 key operations. They are:

1. Deletion at the end
2. Deletion at the start
3. Deletion at a specific position

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    #Deletion at the end. No arguments required
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next) is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:    #If there is only one item and that item is removed, then head & tail are assigned nOne
            self.head = None
            self.tail = None
        return temp
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head.next = self.head
        temp.next = None
        if self.length == 0:
            self.head = None
        return temp

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        pre = self.get(index-1)
        temp = pre.next 
        pre.next = temp.next 
        temp.next = None
        self.length -= 1
        return temp

    
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.pop()
my_linked_list.pop_first()
print(my_linked_list.remove(1))
my_linked_list.print_list()
