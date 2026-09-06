class Stack () : 

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.items = [None] * capacity 
        self.top = -1 

    def isFull (self) : 
        return self.top == self.capacity -1  
    def isEmpty (self) : 
        return self.top == -1 
    def push (self, val): 
        if self.isFull() : 
            return "Stack is full.!"
        else :
            self.top  +=1 
            self.items[self.top] = val 
            return f"{val} is added successfully!"
    def pop (self) : 
        if self.isEmpty() : 
            return "Stack is UnderFlow"
        else : 
            val = self.items[self.top]
            self.top -=1
            return val 
    def getTop (self): 
        if self.isEmpty(): 
            return "Stack is Empty"
        return self.items[self.top]

    def getStack (self) : 
        return self.items

myStack = Stack() 

print ("-----------ISFULL Function------------", end='\n')
print(myStack.isFull())
print ("-----------ISEMPTY Function------------", end='\n')
print(myStack.isEmpty())
print ("-----------PUSH 5 Numbers------------", end='\n')
print(myStack.push(10))
print(myStack.push(20))
print(myStack.push(30))
print(myStack.push(40))
print(myStack.push(50))
print ("-----------Print the Stack ------------", end='\n')
print(myStack.getStack())
print ("-----------Add values or items more than capacity------------", end='\n')
print(myStack.push(60))
print ("-----------check if the more value added or no ------------", end='\n')
print(myStack.getStack())
print ("-----------Remove Last index  Function------------", end='\n')
print(myStack.pop(50))
print ("-----------Check last index deletion------------", end='\n')
print(myStack.getTop())
