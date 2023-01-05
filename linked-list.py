class Node(object):
    
    
    # A node in a linked list.

    # Attributes:
    # - data (int): The data stored in the node.
    # - next (Node): A reference to the next node in the list.
    
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
        


    def setNext(self, next):
        
    
    # Sets the reference to the next node in the list.

    # Args:
    # - next (Node): The next node in the list.
       
        
        self.next = next


class LinkedList(object):
    
    # A linked list data structure.

    # Attributes:
    # - head (Node): The head node of the list.

    
    def __init__(self):
        self.head = None
        
        
        
    def printList(self):
        
    # Prints the data of all the nodes in the list
    
        temp = self.head
        while(temp):
            print(f'{temp.data}-> ', end="")
            # print(temp.next)
            temp = temp.next
        print()  # add a newline after the last element
        
        
        
        
    def searchList(self, key):
        
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
    
    
    
    
    def insertAtStart(self, data):
        
    # Inserts a new node with the given data at the beginning of the list.

    # Args:
    # - data (int): The data to be stored in the new node.    
        
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode






    def insertInBetween(self, previousNode, data):
        
    # Inserts a new node with the given data after the specified previous node.

    # Args:
    # - previous_node (Node): The node after which the new node should be inserted.
    # - data (int): The data to be stored in the new node.    
        
        if previousNode.next is None:
            print("Previous node not found [None]\n")
        else:
            newNode = Node(data)
            newNode.next = previousNode.next
            previousNode.next = newNode            
            
            
            
            
    def insertAtEnd(self, data):
        
    # Inserts a new node with the given data at the end of the list.

    # Args:
    # - data (int): The data to be stored in the new node.    
        
        newNode = Node(data)
        temp = self.head       
        while(temp.next !=None):
            temp = temp.next
        temp.next = newNode
            
if __name__ == "__main__":  # fix syntax error
    
    try:
        List = LinkedList()
        a = int(input("Enter List Head:\n"))
        List.head = Node(a)
        b = int(input("Enter Node 2's Vale:\n"))
        Node2 = Node(b)
        c = int(input("Enter Node 3's Vale\n"))
        Node3 = Node(c)
    
        List.head.setNext(Node2)
        Node2.setNext(Node3)
    
        d = int(input("Please enter the 1st value that you would like to insert at the end.\n"))
        List.insertAtEnd(d)
        f = int(input("Please enter the 2nd value that you would like to insert at the end.\n"))
        List.insertAtEnd(f)
        g = int(input("Please enter the 3rd value that you would like to insert at the end.\n"))
        List.insertAtEnd(g)
        h = int(input("Please enter the 4th value that you would like to insert at the end.\n"))
        List.insertAtEnd(h)
    
        i = int(input(f"Please enter the value that you would like to insert in between Node2 {Node2}\n"))
        List.insertInBetween(Node2, i)
    
        j = int(input(f"Please enter the value that you would like to insert at the beginning.\n"))
        List.insertAtStart(j)
        List.printList()  

        l = int(input(f"Please enter the value that you would like to search for\n"))
        List.searchList(l)
        
    except Exception as e:
        print(e)
    
    finally:
        print("Linked-List DataStructure Finished!")
   
   
   
