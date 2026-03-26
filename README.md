# Overview of the Project

The Simple Banking System is a basic command-line Python application that simulates core banking operations. It allows users to deposit money, withdraw money, and check their account balance. The project is designed to demonstrate fundamental programming concepts like functions, loops, and conditional statements.

# Features

* Deposit money into account
* Withdraw money with balance validation
* Check current account balance
* Continuous menu-driven interface
* Input validation for invalid amounts
* Personalized user interaction using name

# Technologies / Tools Used

* Programming Language: Python
* Concepts Used:
* Functions (Deposit, Withdraw, Check)
* Conditional Statements (if-elif-else)
* Loops (while True)
* User Input (input())
* Basic Arithmetic Operations

# Steps to Install and Run the Project

* Prerequisites: Ensure you have Python 3.x installed on your system.
* Download/Clone: Download the source-code.py file to your local machine.
* Execution: Open your terminal or command prompt, navigate to the directory where the file is saved, and run the following command:
* Follow the on-screen instructions

# Instructions for Testing

1. Deposit Function
   * Input: Positive amount 
   * Expected Output: Balance increases

2. Invalid Deposit
   * Input: Negative amount 
   * Expected Output: "Invalid Deposit Amount"

3. Withdraw Function
   * Input: Valid amount less than balance
   * Expected Output: Balance decreases

4. Insufficient Balance
   * Input: Amount greater than balance
   * Expected Output: "Insufficient Balance"

5. Invalid Withdrawal
   * Input: Negative or zero
   * Expected Output: "Invalid Withdrawal Amount"

6. Check Balance
   * Select option 3
   * Expected Output: Displays current balance
   
7. Exit
   * Select option 4
   * Expected Output: Exit message with user name
