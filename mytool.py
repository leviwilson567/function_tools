from langchain_core.tools import tool

@tool #Decorator placed on top of the function
def add_numbers(first: float, second: float) -> float:
  'Add 2 numbers and return the total.'
  return first + second

@tool
def sub_numbers(first: float, second: float) -> float:
  'Subtract 2 numbers and return the difference.'
  return first + second

@tool
def mul_numbers(first: float, second: float) -> float:
  'Multiply 2 numbers and return the product.'
  return first * second

@tool
def div_numbers(first: float, second: float) -> float:
  'Divides 2 numbers and return the quotient.'
  return first / second

print(add_numbers.name)
print(add_numbers.description)
print(add_numbers.args)

