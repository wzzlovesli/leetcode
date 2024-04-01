# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.


class MyQueue:

    def __init__(self):
        self.first_stack = []
        self.second_stack = []
        

    def push(self, x: int) -> None:
        self.first_stack.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        
        if self.second_stack:
            return self.second_stack.pop()
        else:
            for i in range(len(self.first_stack)):
                self.second_stack.append(self.first_stack.pop())
            
            return self.second_stack.pop()
        

    def peek(self) -> int:
        ans = self.pop()
        self.second_stack.append(ans)
        
        return ans
        
        

    def empty(self) -> bool:
        # if len(self.first_stack) ==0 and len(self.second_stack) == 0:
        #     return True
        # else:
        #     return False
        
        return not (self.first_stack or self.second_stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()