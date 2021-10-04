def mergesort(array, byfunc=None):
  if len(array) <= 1:
    return 

  if not byfunc:
    print("Here")
    byfunc = lambda x: x

  mid = len(array) // 2

  a = array[:mid]
  b = array[mid:]
  mergesort(a, byfunc)
  mergesort(b, byfunc)

  a_idx = 0
  b_idx = 0

  for idx in range(len(array)):    
    if a_idx < len(a) and (b_idx >= len(b) or byfunc(a[a_idx]) <= byfunc(b[b_idx])):
      array[idx] = a[a_idx]
      a_idx += 1
    else:
      array[idx] = b[b_idx]
      b_idx += 1

class Stack:
  def __init__(self, arr=None):
    self.data = arr if arr else []
    self.size = len(self.data)
    
  def __len__(self):
    return self.size

  def push(self, item):
    self.data.append(item)
    self.size += 1

  def pop(self):
    if not self.size:
      raise IndexError("Pop from empty stack.")
    self.size -= 1
    return self.data.pop()

  def peek(self):
    if not self.size:
      raise IndexError("Stack is empty.")
    return self.data[-1]

  def empty(self):
    return not self.size

class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    self.expr = None
    self.expression = string

  @property
  def expression(self):
    # Right?
    return self.expr

  @expression.setter
  def expression(self, new_expr):
    for i in new_expr:
      # Check whether each character in the potential new string is part of the valid list of characteres
      if i not in EvaluateExpression.valid_char:
        # If any character is invalid, we assign an empty string to self.expr and exit the method
        self.expr = ""
        return
    # If ALL characters are valid, we assign new_expr to self.expr
    self.expr = new_expr

  def insert_space(self):
    # Choose to append each character of self.expr to a list so that we don't have to init
    # a new string every time we append a character
    new_str = []
    for char in self.expr:
      # Check whether the character is one of the valid operators to pad with a space
      if char in EvaluateExpression.valid_char[-7:-1]:
        # If it is we append it to our list with a space character before and after
        new_str.append(" ")
        new_str.append(char)
        new_str.append(" ")
      else:
        # If it isn't, we append it as it is
        new_str.append(char)

    # Join the list to a string and let it be our new expression
    return "".join(new_str)

  def process_operator(self, operand_stack, operator_stack):
    # Check to see if there are at least 2 items to pop from operand_stack
    # If not, raise IndexError
    if len(operand_stack) < 2:
      raise IndexError("Less than 2 items in operand stack.")

    # Remove top 2 elements of operand_stack
    b = operand_stack.pop()
    a = operand_stack.pop()

    # Check to see if both the top elements of operand_stack are integers
    # If not, raise ValueError
    if not isinstance(a, int) or not isinstance(b, int):
      raise ValueError("Operands are not numeric.")

    # Check to see if operator_stack is empty
    # If it is, raise IndexError
    if operator_stack.empty():
      raise IndexError("Operator stack is empty.")

    # Remove top element of operator_stack
    operator = operator_stack.pop()

    # Check to see if top element of operator_stack is valid
    if operator not in ["+", "-", "*", "/"]:
      raise ValueError("Invalid operator.")

    # Since we are using eval() to run our math statement, we switch the division operator
    # here to the integer division one
    if operator == "/":
      operator = "//"
    
    # Push the new value onto the stack
    operand_stack.push(eval(f"{a} {operator} {b}"))

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    
    for char in tokens:
      if char.isnumeric():
        # If numeric, push to operand_stack
        operand_stack.push(int(char))
      elif char in "+-":
        # If +-, process all operators while operator_stack not empty and top not ()
        while not operator_stack.empty() and operator_stack.peek() not in "()":
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(char)
      elif char in "*/":
        # If */, process all */ operators and push new operator to stack
        while not operator_stack.empty() and operator_stack.peek() in "/*":
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(char)
      elif char == "(":
        # If (, push onto operator stack
        operator_stack.push(char)
      elif char == ")":
        # If ), process all operators until meeting a (
        while not operator_stack.empty() and operator_stack.peek() != "(":
          self.process_operator(operand_stack, operator_stack)
        operator_stack.pop()
    
    # Process the operators until operator_stack is empty
    while not operator_stack.empty():
      self.process_operator(operand_stack, operator_stack)

    return operand_stack.pop()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





