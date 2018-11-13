
'''
Queue
A queue follows FIFO (first-in, first-out). FIFO is the case where the
first element added is the first element that can be retrieved. Consider
a list with values [2, 5, 3, 6]. Create a class called MyQueue that will have
two methods: queueadd and queueretrieve to add and pop elements
from the list in FIFO order respectively. After each function call,
print the contents of the list. Add 7 to the queue and then follow the
FIFO rules to pop elements until the list is empty.

Your call to the class will be as follows
a = [2, 5, 3, 6]
q = MyQueue(a)
q.queueadd(7)
q.queueretrieve()

The output on the screen should similar to
1 2 3 7
2 3 7
3 7
7
'''

class MyQueue:

    mylist = []
    def __init__(self, list):
        self.mylist = list

    def queueadd(self, item):
        self.mylist.append(item)
        print(self.mylist)

    def queueretrieve(self):
        self.mylist.pop(0)
        print(self.mylist)

a = [2,5,3,6]
q = MyQueue(a)
q.queueadd(7)
q.queueretrieve()
while q.mylist:
    q.queueretrieve()