

class LinkedList:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


# 1 -> 2 -> 3
node1 = LinkedList(1)
node2 = LinkedList(2)
node3 = LinkedList(3)

# pointers
node1.nextNode = node2
node2.nextNode = node3

# unit test
if __name__ == '__main__':
    curr_node = node1

    while True:
        if curr_node.nextNode == None:
            print("None")
            break

        print("current value: ", curr_node.value)
        print("next_value: ", curr_node.nextNode.value)
        print("_____")

        curr_node = curr_node.nextNode