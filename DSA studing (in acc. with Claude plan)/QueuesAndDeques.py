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


