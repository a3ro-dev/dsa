import stack
import linked_list
import doubly_linked_list

stackk = stack.stack()
stackk.push(1)
stackk.pop()


ll = linked_list.LinkedList()
ll.head = linked_list.Node(5)
ll.insertAtStart(10)
ll.insertAtEnd(20)
ll.printList()





dll = doubly_linked_list.DoublyLinkedList()
dll.insertAtStart(10)
dll.insertAtEnd(20)
dll.printDLL()

