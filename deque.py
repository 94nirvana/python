'''
Modulo Collections - Deque
Podemos dizer que o deque é uma lista de alta performace.
'''

from collections import deque

deq = deque("Geek")

print(deq)

deq.append('y')

print(deq)

deq.appendleft('k')

print(deq)

print(deq.pop())

print(deq)

print(deq.popleft())

print(deq)
