def add_numbers(a: float, b: float) -> float:
  result = a + b
  print("[TOOL EXECUTED] add_numbers")
  return result

def sub_numbers(a: float, b: float) -> float:
  result = a - b
  print("[TOOL EXECUTED] sub_numbers")
  return result

def mul_numbers(a: float, b: float) -> float:
  result = a * b
  print("[TOOL EXECUTED] mul_numbers")
  return result

def div_numbers(a: float, b: float) -> float:
  result = a / b
  print("[TOOL EXECUTED] div_numbers")
  return result

if __name__ == "__main__":
  print("Addition: ", add_numbers(50, 5))
  print("Subtraction: ", sub_numbers(50, 5))
  print("Multiply: ", mul_numbers(50, 5))
  print("Division: ", div_numbers(50, 5))