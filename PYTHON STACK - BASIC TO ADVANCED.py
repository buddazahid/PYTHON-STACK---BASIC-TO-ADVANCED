# ========================================================
#           PYTHON STACK - BASIC TO ADVANCED
# ========================================================

# Stack follows:
# LIFO = Last In First Out

# Example:
#
# Push 10
# Push 20
# Push 30
#
# Stack = [10, 20, 30]
#
# Pop
#
# Stack = [10, 20]
#
# Last element entered is removed first.

# ========================================================
#               BASIC STACK USING LIST
# ========================================================

stack = []

print("Initial Stack")
print(stack)

# Push Operation

stack.append(10)
stack.append(20)
stack.append(30)

print("\nAfter Push")
print(stack)

# Pop Operation

stack.pop()

print("\nAfter Pop")
print(stack)

# Top Element

print("\nTop Element")
print(stack[-1])

# ========================================================
#               CHECK STACK EMPTY
# ========================================================

if len(stack) == 0:

    print("Stack is Empty")

else:

    print("Stack is Not Empty")

# ========================================================
#               STACK SIZE
# ========================================================

print("\nStack Size")
print(len(stack))

# ========================================================
#               DISPLAY STACK
# ========================================================

print("\nDisplay Stack")

for item in stack:

    print(item)

# ========================================================
#           ADVANCED STACK USING CLASS
# ========================================================

class Stack:

    def __init__(self):

        self.items = []

    # Push Method
    def push(self, item):

        self.items.append(item)

    # Pop Method
    def pop(self):

        if not self.is_empty():

            return self.items.pop()

        return "Stack Underflow"

    # Peek Method
    def peek(self):

        if not self.is_empty():

            return self.items[-1]

        return "Stack Empty"

    # Check Empty
    def is_empty(self):

        return len(self.items) == 0

    # Size
    def size(self):

        return len(self.items)

    # Display
    def display(self):

        print(self.items)


# ========================================================
#           STACK OBJECT CREATION
# ========================================================

s = Stack()

s.push(100)
s.push(200)
s.push(300)

print("\nCustom Stack")

s.display()

print("\nPeek Element")
print(s.peek())

print("\nPop Element")
print(s.pop())

print("\nAfter Pop")
s.display()

print("\nStack Size")
print(s.size())

# ========================================================
#           STACK USING COLLECTIONS.DEQUE
# ========================================================

from collections import deque

stack2 = deque()

stack2.append("Python")
stack2.append("Java")
stack2.append("PHP")

print("\nDeque Stack")
print(stack2)

stack2.pop()

print("\nAfter Pop")
print(stack2)

# ========================================================
#           REAL WORLD EXAMPLE
#               BROWSER HISTORY
# ========================================================

browser_history = []

browser_history.append("Google")
browser_history.append("YouTube")
browser_history.append("GitHub")

print("\nBrowser History")
print(browser_history)

print("\nBack Button Pressed")

browser_history.pop()

print(browser_history)

# ========================================================
#           REAL WORLD EXAMPLE
#               UNDO OPERATION
# ========================================================

actions = []

actions.append("Type A")
actions.append("Type B")
actions.append("Type C")

print("\nActions")
print(actions)

print("\nUndo Last Action")

actions.pop()

print(actions)

# ========================================================
#           DECIMAL TO BINARY USING STACK
# ========================================================

number = 10

binary_stack = []

while number > 0:

    binary_stack.append(number % 2)

    number //= 2

print("\nBinary Number")

while binary_stack:

    print(binary_stack.pop(), end="")

print()

# ========================================================
#               PROGRAM END
# ========================================================

# Important Stack Operations:
#
# 1. push()   -> Insert element
# 2. pop()    -> Remove top element
# 3. peek()   -> View top element
# 4. size()   -> Count elements
# 5. is_empty() -> Check empty
#
# Applications:
#
# - Undo/Redo
# - Browser History
# - Function Calls
# - Expression Evaluation
# - Backtracking Algorithms
#
# ========================================================