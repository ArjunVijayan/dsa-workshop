# fifo

class Ques:
    def __init__(self):
        self.que = []
        self.curr_index = -1

    def insert_element(self, value):

        self.que.append(value)
        self.curr_index += 1

    def retrieve_element(self):

        elem =  self.que[0]
        self.que.pop(0)

        return elem
    


if __name__=='__main__':
    que = Ques()
    que.insert_element(10)
    que.insert_element(12)
    que.insert_element(14)
    que.insert_element(16)

    print('que element \n', que.que)

    out = que.retrieve_element()
    print('first out: ', out)

    out = que.retrieve_element()
    print('second out: ', out)

    print('que element \n', que.que)
