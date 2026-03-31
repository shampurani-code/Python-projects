def calculator():
    print("--//SIMPLE CALCULATOR//--")
    try:
        num1 = float(input("Enter the first number: "))
        op = input("Enter the operators (+,-,*,/) ")
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input, retry!")
    if op == '+':
        print(f"Result : {num1 + num2}")
    elif op == '-':
        print(f"Result : {num1 - num2}")
    elif op == '*':
        print(f"Result : {num1 * num2}")
    elif op == '/':
        if num2 != 0:
            print(f"Result : {num1 / num2}")
        else:
            print("Invalid")
    else:
        print("Invalid inputs, Retry!")
def main():
    while True:
        calculator()
        again = input("Want to calculate again?(y/n) ").strip().lower()
        if again != 'y':
            break
main()


input('Press any key to exit...')