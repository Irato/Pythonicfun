#Lets repractice creation of class with name Stack
class Stack:
    #every class has a constructor lets construct and return nothing xD
    def __init__(self) -> None:
        self.__stack_list = []
        print("Hi")

    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

#making a subclass of Stack
class AddingStack(Stack):

    def __init__(self) -> None:
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())


