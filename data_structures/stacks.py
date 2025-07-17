class Stack:
    def __init__(self):
        self.stack = []

    def add_item(self, value):
        self.stack.append(value)

    def go_back(self):
        if not self.stack:
            print('End of stack: nothing to go back from.')
            return

        last = self.stack.pop()
        print('Last value removed:', last)

        if not self.stack:
            print('End of stack: no current value remaining.')
        else:
            print('Current top value:', self.stack[-1])
        return


if __name__ == '__main__':
    stack = Stack()
    stack.add_item(10)
    stack.add_item(100)
    stack.add_item(1000)
    stack.add_item(10000)

    for _ in range(5):
        stack.go_back()
        print('---')
