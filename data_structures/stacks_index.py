

class Stack:
    def __init__(self):
        self.stack  = []
        self.curr_index = -1

    def add_item(self, value):

        if self.curr_index < (len(self.stack) - 1):
            self.stack = self.stack[:self.curr_index + 1]

        self.stack.append(value)
        self.curr_index += 1

        print(f'added value {value} st pos : {self.curr_index}')

    
    def go_back(self):

        if self.curr_index <= 0:
            print('begining of stack')
            return

        val = self.stack[self.curr_index - 1]
        self.curr_index -= 1

        return val
    
    def go_front(self):

        if self.curr_index  >= (len(self.stack) - 1):
            print('end of stack')
            return

        val =  self.stack[self.curr_index + 1]
        self.curr_index += 1

        return val

if __name__ == '__main__':
    stack = Stack()
    stack.add_item(10)
    stack.add_item(100)
    stack.add_item(1000)
    stack.add_item(10000)
    stack.add_item(100000)

    print('current index', stack.curr_index)
    print('previous value', stack.go_back())
    print('\n\n')

    print('current index', stack.curr_index)
    print('previous value', stack.go_back())
    print('\n\n')

    print('current index', stack.curr_index)
    print('previous value', stack.go_back())
    print('\n\n')

    print('current index', stack.curr_index)
    print('previous value', stack.go_back())
    print('\n\n')

    print('current index', stack.curr_index)
    print('next value', stack.go_front())
    print('\n\n')

    print('current index', stack.curr_index)
    print('next value', stack.go_front())
    print('\n\n')

    stack.add_item(1234)
    print('current index', stack.curr_index)
    print('next value', stack.go_front())
    print('\n\n')

    print('current index', stack.curr_index)
    print('prev value', stack.go_back())
    print('\n\n')

    stack.add_item(1234)
    print('current index', stack.curr_index)
    print('next value', stack.go_front())
    print('\n\n')

    print('current index', stack.curr_index)
    print('prev value', stack.go_back())
    print('\n\n')

    stack.add_item(1234)
    print('current index', stack.curr_index)
    print('next value', stack.go_front())
    print('\n\n')

    print('stack\n', stack.stack)

