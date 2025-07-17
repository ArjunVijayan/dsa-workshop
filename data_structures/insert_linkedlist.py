
class LinkedNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        node = LinkedNode(value)
        if self.head is None:
            self.head = node
            return
        
        curr_node = self.head
        while True:
            if curr_node.nextNode is None:
                curr_node.nextNode = node
                return
            
            curr_node = curr_node.nextNode

    def printLinkedList(self):
        curr_node = self.head
        while True:
            if curr_node.nextNode is None:
                print("None")
                break

            print(curr_node.value, "-> ", sep="")
            curr_node = curr_node.nextNode

        print("_______")

    

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(5)
    ll.printLinkedList()

    ll.insert(10)
    ll.printLinkedList()

    ll.insert(10)
    ll.printLinkedList()
    



