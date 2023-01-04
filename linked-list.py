class Node(object):
    
    """
    A node in a linked list.

    Attributes:
    - data (int): The data stored in the node.
    - next (Node): A reference to the next node in the list.
    """
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
        


    def setNext(self, next):
        self.next = next


class LinkedList(object):
    
    def __init__(self):
        self.head = None
        
        
        
    def printList(self):
        temp = self.head
        while(temp):
            print(f'{temp.data}-> ', end="")
            # print(temp.next)
            temp = temp.next
        print()  # add a newline after the last element
        
        
        
        
    def searchList(self, key):
        temp = self.head
            
        while(temp):
            if temp.data == key:
                print(f"KEY FOUND\n {key}")
                return
            temp = temp.next
            
        print("KEY NOT FOUND")
    
    
    
    
    def insertAtStart(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode






    def insertInBetween(self, previousNode, data):
        if previousNode.next is None:
            print("Previous node not found [None]\n")
        else:
            newNode = Node(data)
            newNode.next = previousNode.next
            previousNode.next = newNode            
            
            
            
            
    def insertAtEnd(self, data):
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
   