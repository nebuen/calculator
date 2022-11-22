from art import logo



#Calculation
def add(n1,n2):
  return n1 + n2

def sub(n1,n2):
  return n1 - n2

def div(n1,n2):
  return n1 / n2

def mul(n1,n2):
  return n1 * n2

operations = {
  "+": add,
  "-": sub,
  "/": div,
  "*": mul
}
def calculator():
  print(logo)
  num1 = float(input("What is the first number?: "))
  for key in operations:
    print(key)
  
  should_continue = True
  while should_continue:
    operations_symbol = input("Pick an operations: ")
    num2 = float(input("What is the next number?: "))
    calculation_function = operations[operations_symbol]
    answer = calculation_function(num1,num2)
    
    print(f"{num1} {operations_symbol} {num2} = {answer}")
    
    calculation_continuation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
    
    if calculation_continuation == 'y':
      num1 = answer
    else:
      should_continue = False
    
calculator()