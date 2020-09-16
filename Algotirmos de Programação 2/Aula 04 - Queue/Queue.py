from Node import Node

class Queue:

    def __init__(self):
        "constructor to initiate this object"
        
        # store the first in the queue
        self.head = None
        # store the last in the queue
        self.tail = None
        # store the size of the queue
        self.size = 0
    
    def append(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = self.tail = Node(data)
        self.size += 1
        '''
        current = self.head
        while (current.next != null):
            current = current.next
        current.next = Node(data)
        '''

    def print(self):
        text = ""
        # if the first is empty
        if self.head is None:
            text = "Empty Queue!"
        else:
            current = self.head
            #while not null
            while(current):
                text = text + str(current.data)
                current = current.next
        print(text)

    def invertedPrint(self):
        text = ""
        # if the first is empty
        if self.head is None:
            text = "Empty Queue!"
        else:
            current = self.tail
            #while not null
            while(current):
                text = text + str(current.data)
                current = current.previous
        print(text)
        

    def dequeue(self):
        if self.head is None:
            print("Empty Queue!")
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            self.head = self.head.next
            self.size -=1


