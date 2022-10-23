#Implementation of a stack class that have push and pop methods, but in the pop return de value

class Stack:

    def __init__(self):
        self.__stack_list = []

    def push(self, val):
       self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

#adding a subclasse to count the number of pop`s on code
class acumulative_counting(Stack):

    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    def pop(self):
        self.__counter += 1
        Stack.pop(self)

    #creating a function to acess the private counter xD
    def get_counter(self):
        return self.__counter

stk = acumulative_counting()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())

