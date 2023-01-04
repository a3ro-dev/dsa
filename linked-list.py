class Node(object):
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    
    def __init__(self):
        self.head = None
        
        
        
    def printList(self):
        temp = self.head
        while(temp):
            print(f'{temp.data}-> ', end="")
            print(temp.next)
            temp = temp.next
        print()  # add a newline after the last element
    
    
    
    
    def insertAtStart(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            
            
            
            
    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head       
        while(temp.next !=None):
            temp = temp.next
        temp.next = newNode
            
if __name__ == "__main__":  # fix syntax error
    List = LinkedList()
    List.head = Node(1)
    # List.insertAtStart()
    # List.insertAtStart()
    # List.insertAtStart()
    List.insertAtEnd(5)
    List.insertAtEnd(10)
    List.insertAtEnd(15)
List.printList()  
