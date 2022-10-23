class Stack:
    def __init__(self):
    #now a have to contruct some object
        #making the secret of universe and all the things private 0.0
        self.__stack_list = []
        self.__secret_of_universe = 42

#put the things together
    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val



#creating a instance of my object
stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())
