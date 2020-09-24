from Node import Node

class List: 

    def __init__(self):
        self.head = None
        self.end = None
        self.size = 0

    def __len__(self):
        return self.size 
    
    def AppendAtHead(self, data ):
        node = Node( data )
        if self.size == 0:
            self.head = node  
            self.end = node    
        else:
            aux = self.head
            node.next = aux
            aux.previous = node
            self.head = node
        self.size = self.size + 1

    def AppendAtEnd(self, data ):
        node = Node( data )
        if self.size == 0:
            self.head = node    
            self.end = node    
        else:
            aux = self.end
            node.previous = aux
            aux.next = node
            self.end = node
        self.size = self.size + 1

    def Print(self):
        if self.head == None:
            print("Empty List")
        aux = self.head
        while( aux ):
            print( aux.data , "\n" )
            aux = aux.next
        print( "List size: " + str(self.size ))

    def ReversePrint(self):
        if self.head == None:
            print("Empty List")
        aux = self.end
        while( aux ):
            print( aux.data , "\n" )
            aux = aux.previous
        print( "List size: " + str(self.size ))
        

    def DeleteHead( self):
        if self.tamanho == 0 :
            print( "Empty List")
        elif self.size == 1 :
            self.head = None
            self.end = None
            self.size -= 1
        else:
            self.head = self.head.next
            self.head.previous = None
            self.size -= 1

    def DeleteEnd( self):
        if self.size == 0 :
            print( "Empty List")
        elif self.size == 1 :
            self.head = None
            self.end = None
            self.size -= 1
        else:
            self.end = self.end.previous
            self.end.next = None
            self.size -= 1
           