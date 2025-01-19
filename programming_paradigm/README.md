0. Create a Simple Bank Account Class
mandatory
Objective: Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations. Use command line arguments to interact with instances of this class.

Task Description:

You will create two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py, which interfaces with the class through command line arguments to perform banking operations.

bank_account.py:

Class Definition:

Define a class named BankAccount.
Use the __init__ method to initialize an account_balance attribute. Optionally, accept an initial balance parameter, defaulting to zero.
Encapsulation and Behaviors:

Implement deposit(amount), withdraw(amount), and display_balance() methods.
deposit should add the specified amount to account_balance.
withdraw should deduct the amount from account_balance if funds are sufficient, returning True; otherwise, return False and do not alter the balance.
display_balance should print the current balance in a user-friendly format.



1. Robust Division Calculator with Command Line Arguments
mandatory
Objective: Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.

Task Description:

Create two Python scripts: robust_division_calculator.py, which contains the division logic including error handling, and main.py, which interfaces with the user through the command line.

robust_division_calculator.py:

Define a function safe_divide(numerator, denominator) that performs division, handling potential errors:

Division by Zero: Use a try-except block to catch ZeroDivisionError.
Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block to catch ValueError for non-numeric inputs.
Return appropriate messages for errors or the result for successful division.
main.py for Command Line Interaction:

This script will import safe_divide from robust_division_calculator.py and use it to divide numbers provided as command line arguments.




2. Writing Unit Tests for a Simple Calculator Class
mandatory
Objective: Learn the basics of unit testing in Python by writing tests for a provided SimpleCalculator class that supports addition, subtraction, multiplication, and division operations.

Provided: simple_calculator.py

You’re given a SimpleCalculator class with basic arithmetic operations. Your task is to write unit tests to verify its correctness.

# simple


3. Implementing Basic OOP for a Library Management System
mandatory
Objective: Solidify understanding of basic OOP concepts in Python by implementing a system that tracks books in a library, focusing on classes, object instantiation, and method invocation.

Your Task: library_management.py

Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.
Implement a Library class with a private list _books to store instances of Book. Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.
