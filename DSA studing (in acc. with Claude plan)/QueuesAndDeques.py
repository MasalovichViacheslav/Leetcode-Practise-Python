# https://leetcode.com/problems/implement-stack-using-queues/
'''
225. Implement Stack using Queues

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the
functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is
empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque
(double-ended queue) as long as you use only a queue's standard operations.
'''
# Solution1
# from collections import deque
#
# class MyStack:
#
#     def __init__(self):
#         self._elements = deque()
#
#     def push(self, x: int) -> None:
#         self._elements.append(x)
#
#     def pop(self) -> int:
#         return self._elements.pop()
#
#
#     def top(self) -> int:
#         return self._elements[-1]
#
#     def empty(self) -> bool:
#         if len(self._elements) == 0:
#             return True
#         else:
#             return False


# # Solution2
# from collections import deque
# class MyStack:
#
#     def __init__(self):
#         self._elements = deque()
#
#     def push(self, x: int) -> None:
#         self._elements.append(x)
#
#     def pop(self) -> int:
#         temp_deque = deque()
#         for _ in range(len(self._elements) - 1):
#             temp_deque.append(self._elements.popleft())
#         element = self._elements.popleft()
#         self._elements = temp_deque
#         return element
#
#     def top(self) -> int:
#         temp_deque = deque()
#         for _ in range(len(self._elements) - 1):
#             temp_deque.append(self._elements.popleft())
#         element = self._elements.popleft()
#         temp_deque.append(element)
#         self._elements = temp_deque
#         return element
#
#     def empty(self) -> bool:
#         if self._elements:
#             return False
#         else:
#             return True

# testcases
# mystack = MyStack()
# mystack.push(4)
# mystack.push(3)
#
# print(mystack)
#
# print(mystack.empty())
#
# print(mystack.top())
#
# print(mystack.pop())
# print(mystack.pop())
#
# print(mystack.empty())


# https://leetcode.com/problems/number-of-recent-calls/
'''
933. Number of Recent Calls

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of 
requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number 
of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

 
Example 1:
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]
Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
 

Constraints:

1 <= t <= 10 ** 9
Each test case will call ping with strictly increasing values of t.
At most 10 ** 4 calls will be made to ping.
'''
# Solution1
# from collections import deque
#
# class RecentCounter:
#
#     def __init__(self):
#         self.counter = deque()
#
#     def ping(self, t: int) -> int:
#         self.counter.append(t)
#         temp_counter = deque()
#         latest_time = self.counter[-1]
#         while self.counter:
#             time = self.counter.pop()
#             if latest_time - 3000 <= time:
#                 temp_counter.appendleft(time)
#             else:
#                 break
#         self.counter = temp_counter
#         return len(self.counter)

# Solution2
# class RecentCounter:
#
#     def __init__(self):
#         self.counter = []
#
#     def ping(self, t: int) -> int:
#         temp_counter = [t]
#         while self.counter:
#             time = self.counter.pop()
#             if t - 3000 <= time:
#                 temp_counter.append(time)
#             else:
#                 break
#         self.counter = temp_counter[::-1]
#         return len(self.counter)

# Solution3
# class RecentCounter:
#
#     def __init__(self):
#         self.counter = []
#
#     def ping(self, t: int) -> int:
#         self.counter.append(t)
#         for ind in range(-2, -len(self.counter) - 1, -1):
#             if t - 3000 > self.counter[ind]:
#                 self.counter = self.counter[ind + 1:]
#                 break
#         return len(self.counter)

# Solution4
# from collections import deque
#
# class RecentCounter:
#
#     def __init__(self):
#         self.counter = deque()
#
#     def ping(self, t: int) -> int:
#         self.counter.append(t)
#         while self.counter[0] < t - 3000:
#             self.counter.popleft()
#         return len(self.counter)

# testcases
# obj = RecentCounter()
# print(obj.ping(1))
# print(obj.ping(100))
# print(obj.ping(3001))
# print(obj.ping(3002))

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# https://leetcode.com/problems/implement-queue-using-stacks/description/
'''
232. Implement Queue using Stacks

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the 
functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty 
operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque 
(double-ended queue) as long as you use only a stack's standard operations.
 

Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
'''
# # Solution1
# class MyQueue:
#
#     def __init__(self):
#         self.main_stack = []
#         self.support_stack = []
#
#     def push(self, x: int) -> None:
#         self.main_stack.append(x)
#
#     def pop(self) -> int:
#         while self.main_stack:
#             self.support_stack.append(self.main_stack.pop())
#         elem = self.support_stack.pop()
#         while self.support_stack:
#             self.main_stack.append(self.support_stack.pop())
#         return elem
#
#     def peek(self) -> int:
#         while self.main_stack:
#             self.support_stack.append(self.main_stack.pop())
#         elem = self.support_stack.pop()
#         self.main_stack.append(elem)
#         while self.support_stack:
#             self.main_stack.append(self.support_stack.pop())
#         return elem
#
#     def empty(self) -> bool:
#         if self.main_stack:
#             return False
#         else:
#             return True


# testcases
# myQueue = MyQueue()
# myQueue.push(1)
# myQueue.push(2)
# print(myQueue.peek())
# print(myQueue.pop())
# print(myQueue.empty())


# https://leetcode.com/problems/design-circular-queue/description/
'''
622. Design Circular Queue

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations 
are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first 
position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal 
queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. 
But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 

 

Example 1:

Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
 

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.

'''


class MyCircularQueue:

    def __init__(self, k: int):
        self.length = k
        self.queue = [None] * self.length
        self.front = -1
        self.rear = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.length
            self.queue[self.rear] = value
            self.size += 1
            if self.front == -1:
                self.front = (self.front + 1) % self.length
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.front = (self.front + 1) % self.length
            self.size -= 1
            return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear]

    def isEmpty(self) -> bool:
        if self.size:
            return False
        else:
            return True

    def isFull(self) -> bool:
        if self.size == self.length:
            return True
        else:
            return False

# testcases
my_circular_queue = MyCircularQueue(3)
print(my_circular_queue.Front(), 'expected:', -1)
print(my_circular_queue.Rear(), 'expected:', -1)
print(my_circular_queue.enQueue(1), 'expected:', True)
print(my_circular_queue.enQueue(2), 'expected:', True)
print(my_circular_queue.enQueue(3), 'expected:', True)
print(my_circular_queue.Front(), 'expected:', 1)
print(my_circular_queue.enQueue(4), 'expected:', False)
print(my_circular_queue.Rear(), 'expected:', 3)
print(my_circular_queue.isFull(), 'expected:', True)
print(my_circular_queue.queue)
print(my_circular_queue.deQueue(), 'expected:', True)
print(my_circular_queue.Front(), 'expected:', 2)
print(my_circular_queue.enQueue(4), 'expected:', True)
print(my_circular_queue.Rear(), 'expected:', 4)


