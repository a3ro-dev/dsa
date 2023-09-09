import stack
import linked_list
import doubly_linked_list
import queue_ds as queue


print('DataStructure: Stack')
stackk = stack.stack()
stackk.push(1)
stackk.push(5)
stackk.pop()
stackk.pop()




print('Datastructure: Linked-List')
ll = linked_list.LinkedList()
ll.head = linked_list.Node(5)
ll.insertAtStart(11)
ll.insertAtEnd(20)
ll.printList()




print('DataStructure: Doubly-Linked-List')
dll = doubly_linked_list.DoublyLinkedList()
dll.insertAtStart(10)
dll.insertAtEnd(20)
dll.printDLL()




print('DataStructure: Queue')
myQueue = queue.Queue()
myQueue.enqueue(19)
myQueue.enqueue(7**2)
print(myQueue)
print(f'Size {myQueue.getSize()}')
myQueue.dequeue()

