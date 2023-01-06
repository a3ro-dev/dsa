class Node(object):
    
    # Represents a single node in a doubly-linked list.
    
    # Attributes:
    # - data (int): The data stored in the node.
    # - next (Node): A reference to the next node in the list.
    # - previous (Node): A reference to the previous node in the list.
        
    def __init__(self, data, next=None, previous=None):
        
        # Initializes a new Node with the given data.
        
        # Args:
        # - data (int): The data to store in the node.
        # - next (Node): A reference to the next node in the list.
        # - previous (Node): A reference to the previous node in the list.
        
        self.data = data
        self.next = next
        self.previous = previous
        
class DoublyLinkedList(object):
    
    # Represents a doubly-linked list.
    
    # Attributes:
    # - head (Node): A reference to the first node in the list.
        
    def __init__(self):
            
        # Initializes a new empty doubly-linked list.
            
        self.head = None
            
    def insertAtStart(self, data):
        
        # Inserts a new node with the given data at the beginning of the list.
        
        # Args:
        # - data (int): The data to store in the new node.
            
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
        
    def printDLL(self):
        
        # Prints the contents of the list from head to tail.
        
        temp = self.head
            
        while(temp!=None):
            print(f"{temp.data}-> ", end="")
            temp = temp.next
        print("NULL")
            
    def insertAtEnd(self, data):
        
        # Inserts a new node with the given data at the end of the list.
        
        # Args:
        # - data (int): The data to store in the new node.
        
        newNode = Node(data)
            
        temp = self.head
        while(temp.next != None):
            temp = temp.next
                
            temp.next = newNode
            newNode.previous = temp
            
    def searchDLList(self, key):
        
        # Searches for a node with the given key in the list.
        # Prints a message indicating whether the key was found or not.

        # Args:
        # - key (int): The data to search for in the list.    
        
        temp = self.head
            
        while(temp):
            if temp.data == key:
                print(f"KEY FOUND\n {key}")
                return
            temp = temp.next
            
        print("KEY NOT FOUND")
                
if __name__ == "__main__":
    
    dll = DoublyLinkedList()
    dll.insertAtStart(1)
    dll.insertAtStart(45)
    dll.insertAtEnd(9)

    dll.printDLL()
    dll.searchDLList(45)
 
            
        
