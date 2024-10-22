class Node:
    def __init__(self, data,nextNode = None):
        self.data = data
        self.nextNode = nextNode

class LinkedList:
    def __init__(self):
        self.head = None
    
    # append node at the end 
    def append(self, newData):
        element = Node(newData)
        if not self.head:
            self.head = element
            return
        
        current = self.head
        while current.nextNode:
            current = current.nextNode
            print('**>',newData)
        
        current.nextNode = element

        return
    
    def delete(self, value):

        # No node 
        if self.head == None:
            return

        # Node at the beginning
        if self.head.data == value:
            if not(self.head.nextNode):
                self.head = None
                return

        current = self.head
        prev = Node()
        while(current):
            if current.data == value:
                prev.nextNode = current.nextNode
                # current = None # no need to nullify the current node, we can keep that as it is. 
                return
            prev = current
            current = current.nextNode

        return
    
    













    def printLinked(self):

        current = self.head
        while current:
            print(current.data, end = " --> ")
            current= current.nextNode
        print('Completed')




ll = LinkedList()
ll.append(1)
ll.append(12)
ll.append(13)
print('DOne')
ll.printLinked()


        




         


