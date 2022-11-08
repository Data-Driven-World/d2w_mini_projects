

def merge(array, p, q, r, byfunc):
    n1 = q-p+1 #length of left array
    n2 = r-q #length of right array
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]
    i = 0 #left pointer
    j = 0 #right pointer
    k = p #array pointer
    
    while i < n1 and j < n2:
        if byfunc(left_array[i]) <= byfunc(right_array[j]):
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1
    while i < n1:
        array[k] = left_array[i]
        i+=1
        k+=1
    while j < n2:
        array[k] = right_array[j]
        j+=1
        k+=1
    pass

def mergesort_recursive(array, p, r,byfunc):
    if p < r:
        q = (p+r)//2
        mergesort_recursive(array,p,q,byfunc)
        mergesort_recursive(array,q+1,r,byfunc)
        merge(array,p,q,r,byfunc)
    pass

def mergesort(array,byfunc = None):
    mergesort_recursive(array,0,len(array)-1,byfunc)
    pass

class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)

    def pop(self):    
        if len(self.__items) >= 1:
            return self.__items.pop()  

    def peek(self):
        if len(self.__items) >= 1:
            return self.__items[-1]     

    @property
    def is_empty(self):
        return len(self.__items) == 0

    @property
    def items(self):
        return self.__items
        
    @property
    def size(self):
        return len(self.__items)


class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    self.expr=string
    pass

  @property
  def expression(self):
    return self.expr

  @expression.setter
  def expression(self, new_expr):
    valid_set = set("0123456789+-*/() ")
    if (any(x not in valid_set for x in new_expr)):
      self.expr = ""
    else:
      self.expr = new_expr
    
  def insert_space(self):
    final_exp = ""
    math_exp = self.expression
    operators_ls = "+-*/()"
    for char in math_exp:
      if char in operators_ls:
        final_exp+=(" "+char+" ")
      else:
        final_exp+=(char)
    return final_exp

  def process_operator(self, operand_stack, operator_stack):
    val2 = int(operand_stack.pop())
    val1 = int(operand_stack.pop())
    operator = operator_stack.pop()
    if  operator == "+":
      operand_stack.push(val1 + val2)
    elif operator == "-":
      operand_stack.push(val1 - val2)
    elif operator == "*":
      operand_stack.push(val1 * val2)
    elif operator == "/":
      operand_stack.push(val1 // val2)

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
  #phase1
    for char in tokens:
      if char in '1234567890':
        operand_stack.push(char)
      elif char in '+-':
        while (not(operator_stack.is_empty)) and (operator_stack.peek() not in "()"):
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(char)
      elif char in "*/":
        while (not (operator_stack.is_empty)) and (operator_stack.peek() in "*/"):
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(char)
      elif char == "(":
        operator_stack.push(char)
      elif char == ")":
        while operator_stack.peek() !="(":
          self.process_operator(operand_stack, operator_stack)
        operator_stack.pop()

  #phase2
    while (not(operator_stack.is_empty)):
      self.process_operator(operand_stack, operator_stack)
    return operand_stack.pop()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





