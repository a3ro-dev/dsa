class Node(object):
    
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous
        
        
        
class DoublyLinkedList(object):
        
        def __init__(self):
            self.head = None
            
        def insertAtStart(self, data):
            
            if self.head == None:
                newNode = Node(data)
                self.head = newNode
            else:
                newNode = Node(data)
                self.head.previous = newNode
                newNode.next = self.head
                self.head = newNode
        
        def printDLL(self):
            temp = self.head
            
            while(temp!=None):
                print(f"{temp.data}-> ", end="")
                temp = temp.next
                
            
        
