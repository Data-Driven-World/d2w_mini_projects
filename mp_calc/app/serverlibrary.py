import typing

def mergesort(array, byfunc=None):
  mergesort_recursive(array, 0, len(array)-1, byfunc)
  
# start_i = p
# end_i = r
# middle_i = q

def merge(array: list, p: int, q: int, r: int, byfunc=None) -> None:
    left_n = q-p + 1
    right_n = r-q
    leftarr = array[p:q+1]
    rightarr = array[q+1:r+1]
    left_pointer = 0
    right_pointer = 0
    destination = p     # starts of arr
    
    while left_pointer < left_n and right_pointer < right_n:
        left_value = byfunc(leftarr[left_pointer]) if byfunc else leftarr[left_pointer]
        right_value = byfunc(rightarr[right_pointer]) if byfunc else rightarr[right_pointer]
        
        if left_value < right_value:
            array[destination] = leftarr[left_pointer]
            left_pointer += 1
        else:
            array[destination] = rightarr[right_pointer]
            right_pointer += 1
        destination += 1
        
    while left_pointer < left_n:
        array[destination] = leftarr[left_pointer]
        left_pointer += 1
        destination += 1
    while right_pointer < right_n:
        array[destination] = rightarr[right_pointer]
        right_pointer += 1
        destination += 1   
        
def mergesort_recursive(array: list, p: int, r: int, byfunc) -> None:
    if r>p:
        q = (p+r)//2
        mergesort_recursive(array,p,q, byfunc)
        mergesort_recursive(array,q+1,r, byfunc)
        merge(array, p, q, r, byfunc)
        

class Stack:
  pass

class EvaluateExpression:
  pass


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]







