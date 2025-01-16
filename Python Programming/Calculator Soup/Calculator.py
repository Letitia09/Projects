# Project 2 : Calculator
# Name : Anshu Pulipati
# Major : Computer Science
# Calculator Soup website for reference : https: // www.calculatorsoup.com /

# BASIC INFORMATION
'''
    Addition: Adds two numbers.
    Subtraction: Subtracts the second number from the first.
    Multiplication: Multiplies two numbers.
    Division: Divides the first number by the second, with a check for division by zero.
'''

class Calculator:
    def __init__(self):
        self.running = True

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero!"
        return x / y

    def display_menu(self):
        print("Enter 'A' for Addition")
        print("Enter 'S' for Subtraction")
        print("Enter 'M' for Multiplication")
        print("Enter 'D' for Division\n")


    def get_choice(self):
        while True:
            try:
                choice = input('Enter Choice (A, S, M, D): ').upper()
                if choice not in ('A', 'S', 'M', 'D'):
                    raise ValueError("Invalid choice. Please enter one of 'A', 'S', 'M', or 'D'.\n")
                return choice
            except ValueError as e:
                print(e)

    def get_numbers(self):
        while True:
            try:
                num1 = float(input('Enter first number: '))
                num2 = float(input('Enter second number: '))
                return num1, num2
            except ValueError:
                print("Invalid input! Please enter numeric values.\n")

    def perform_calculation(self, choice, num1, num2):
        if choice in ('A', 'ADD', 'ADDITION'):
            return f'{num1} + {num2} = {self.add(num1, num2)}'
        elif choice in ('S', 'SUBTRACT', 'SUBTRACTION'):
            return f'{num1} - {num2} = {self.subtract(num1, num2)}'
        elif choice in ('M', 'MULTIPLY', 'MULTIPLICATION'):
            return f'{num1} * {num2} = {self.multiply(num1, num2)}'
        elif choice in ('D', 'DIVIDE', 'DIVISION'):
            return f'{num1} / {num2} = {self.divide(num1, num2)}'
        else:
            return "Invalid choice. Please input a correct choice."

    def start(self):
        while self.running:
            self.display_menu()
            choice = self.get_choice()

            num1, num2 = self.get_numbers()
            result = self.perform_calculation(choice, num1, num2)
            print(result)

            next_calculation = input("\nWant to do another calculation? (yes/no): ")
            if next_calculation.lower() in ('no', 'n', 'nope'):
                self.running = False
                print("Goodbye!")
            else:
                print("Let's go again!")


calculator = Calculator()
calculator.start()
