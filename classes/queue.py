#Lets practice more classes and subclasses, now create a class of queue
#with two methods put() and get() put insert a element ang get return
#the first element inserted on the queue like fast food style "in good days" xD
class MyException(Exception):
    pass
    
class Queue:

    def __init__(self):
        self.__queue_list = []

    def put(self, val):
        self.__queue_list.append(val)

    def get(self):
        transfer = self.__queue_list[0]
        del self.__queue_list[0]
        return transfer

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except Exception:
    print("Queue error :( ")
