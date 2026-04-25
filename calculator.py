def show_menu():
    print("\n" + "="*30)
    print("    SMART CALCULATOR")
    print("="*30)
    print("Operations:")
    print(" + -> Addition")
    print(" - -> Subtraction")
    print(" * -> Multiplication")
    print(" / -> Division")
    print(" ^ -> Power")
    print(" % -> Modulus")
    print(" sqrt -> Square root")
    print(" q -> Quit")
    print("="*30)
    
def calculate():
    while True:
        show_menu()
        choice = input("Enter operation: ").strip()
        if choice == 'q':
            print("Exiting calculator...")
            break
        
        try:
            if choice == 'sqrt':
                num = float(input("Enter number: "))
                result = math.sqrt(num)
                print(f"Correct Result: {result}")
                continue
                  

                    
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))
            if choice == '+':
                result = num1 + num2

            elif choice == '-':
                result = num1- num2

            elif choice =='*':
                result  = num1 * num2

            elif choice == '/':
                if num2 == 0:
                    print("Cannot divide by zero")
                    continue
                result = num1 / num2

            elif choice == '^':
                result = num1 ** num2
                
            elif choice == '%':
                result = num1 % num2

            else:
                print("Invalid Operation")
                continue

            print(f"Correct Result: {result}")

        except ValueError:
            print("Please enter valid numbers")

calculate()




                

