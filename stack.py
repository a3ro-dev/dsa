# Last
# In
# First
# Out
class stack(object):
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def push(self, data):
        if len(self.stack) >= self.limit:
            print('STACK IS FULL')
        else:
            self.stack.append(data)

    def pop(self):
        if len(self.stack) <= 0:
            print('STACK IS EMPTY')
        else:
            element = self.stack.pop()
            print("-> ", element)

    def size(self):
        size = len(self.stack)
        print("-> ", size)

    def IsEmpty(self):
        if len(self.stack) <= self.limit:
            print("STACK IS EMPTY")
        else:
            print("STACK IS NOT EMPTY")

    def EmptyList(self):
        print("-> ", len(self.stack))
        choice = input("Are You Sure You Want To Empty This Stack?\n")
        if choice == "Y" or "Yes" or "yes":
            self.stack.clear()
        else:
            print("PROCESS CANCELLED")



if __name__ == '__main__':
    stackk = stack()
   
    push = int(input("Data to Push\n")) 
    stackk.push(push)
    stackk.pop()
    stackk.IsEmpty()
    stackk.size()
    stackk.EmptyList()