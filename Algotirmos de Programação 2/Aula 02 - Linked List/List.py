from Node import Node

class List:

   def __init__(self):
        self.head = None

   def append(self, data):
        if self.head:
             self.head = Node(data)
             return

     def print(self):
        if self.inicio == None:
            print("Empty List")
        current = self.inicio
        while(current):
            print(current.data, "\n")
            current = current.next