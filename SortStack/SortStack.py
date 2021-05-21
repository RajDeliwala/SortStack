'''
Cracking the coding interview
Chapter 3 - Stacks and Queues
Stacks and Queues: Sort Stack
----------------------------------------
Question: Write a program to sort a stack such that the smallest items are on the top. You can use an additional temp stack, but you may not copy
the elements into any other data structure(such as an array). The stack should support the following opperations Push, Pop, Peek and isEmpty.
Example: 
input: 
output: 
Constraits or Questions you need to ask:
Does the sort need to be addressed everytime a push or pop is called? or wil it be a seperate function to sort out the current stack
Seems like a function for the sort will be seperate from the push and pop
Solution notes:


'''
class myStack:

    def __init__(self):
        self.stack = []
        self.tempStack = []

    #Push stack will just append the item in the argument to the stack
    def push(self, item):
        self.stack.append(item)

    #Pop will remove the top value in the given stack
    def pop(self):
        return print(self.stack.pop())

    #Return the value of the top value in given stack
    def peek(self):
        return self.stack[-1]

    #isEmpty will return a boolean related to the stack being empty
    def isEmpty(self):
        if self.stack == []:
            return True
        else: 
            return False

    #Sort the given stack using 1 temp variable and 1 tempStack
    def sortStack(self):
        #First check if the stack is empty
        if self.stack == []:
            return print(IndexError("The stack is currently empty, we cannot sort it"))

        #Temp variable to help with the sorting
        temp = 0

        #Loop to sort the entire stack
        while self.stack != []:
            #Make the temp value the popped value of the reg stack
            temp = self.stack.pop()
            if self.tempStack == []:
                #If temp stack is empty, just append it to temp stack
                self.tempStack.append(temp)
                #Set temp back to 0
                temp = 0
            else:
                while self.tempStack[-1] < temp:
                    self.stack.append(self.tempStack.pop())
                    #Then add the temp to the tempStack
                    self.tempStack.append(temp)
                    #Then set temp back to 0
                    temp = 0
                else:
                    self.tempStack.append(temp)
                    temp = 0
        #After the reg stack is empty and tempStack has all sorted itself out
        #Append tempStack to stack and it should append it in reverse giving you the smallest to biggest
        self.stack = self.tempStack
        #After using temp stack, set it back to empty
        self.tempStack = []
        print(self.stack)

myList = myStack()
myList.stack.append(8)
myList.stack.append(3)
myList.stack.append(7)
myList.stack.append(4)
myList.stack.append(10)
#myList.sortStack()

myList2 = myStack()
myList2.stack.append(5)
myList2.stack.append(8)
myList2.stack.append(1)
myList2.stack.append(8)
myList2.stack.append(2)

myList2.sortStack()




