class Calculator():

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        """Add function"""
        return self.num1 + self.num2

    def subtract(self):
        """Subtract function"""
        return self.num1 - self.num2

    def multiply(self):
        """Multiply function"""
        return self.num1 * self.num2

    def divide(self):
        """Divide function"""
        if self.num2 == 0:
            print("Cannot divide a number by zero")
        else:
            return self.num1 / self.num2
        
    def floor_divide(self):
        """function to perform floor division"""
        if self.num2 == 0:
            raise ValueError("Cannot divide a number by zero")
        else:
            return self.num1 // self.num2
        
    def modulus(self):
        """function to get the reminder of the division of the passed two numbers"""
        if self.num2 == 0:
            raise ValueError("Cannot divide a number by zero")
        else:
            return self.num1 % self.num2

if __name__ == '__main__':

    while True:
        print("""\nWhat arithmetic operation do want to perform?
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Floor division
            6. Modulus
            """)

        choice = int(input("Enter any number between 1-6(7 to quit): "))
        if choice == 7:
            break

        elif choice not in range(1, 7):
            print("\nInvalid choice. Please enter a number between 1-6")
            choice = int(input("\nEnter any number between 1-6(7 to quit): "))
            

        firstNumber = float(input("\nEnter the first number: "))
        secondNumber = float(input("Enter the second number: "))
        my_calculator = Calculator(firstNumber, secondNumber)

        match choice:
            case 1:
                # addition
                print("ADDITION")
                sum = my_calculator.add()
                print(f"The sum of {firstNumber} and {secondNumber} is: {sum}")

            case 2:
                # subtraction
                print("\nSUBTRACTION")
                difference = my_calculator.subtract()
                print(f"The difference between {firstNumber} and {secondNumber} is: {difference}")

            case 3:
                # multiplication
                print("\nMULTIPLICATION")
                product = my_calculator.multiply()
                print(f"The product of {firstNumber} and {secondNumber} is: {product}")

            case 4:
                # division
                print("\nDIVISION")
                quotient = my_calculator.divide()
                print(f"The result of dividing  {firstNumber} by {secondNumber} is: {quotient}")

            case 5:
                # floor division
                print("\nFLOOR DIVISION")
                fQuotient = my_calculator.floor_divide()
                print(f"The result of floor division of {firstNumber} by {secondNumber} is: {fQuotient}")

            case 6:
                # modulus
                print("\nMODULUS")
                remainder = my_calculator.modulus()
                print(f"The remainder of dividing {firstNumber} by {secondNumber} is: {remainder}")

            # case _:       # We dont need this case because we have already handled the default case
            #     # The underscore is used to define the default case
            #     print("\nInvalid choice. Please enter a number between 1-6")
            #     break