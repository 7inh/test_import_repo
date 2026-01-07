#!/usr/bin/env python3
"""
Sample Python Application for Testing Repository Import
"""

import sys
from datetime import datetime


def greet(name):
    """
    Greet a user by name.
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: A greeting message
    """
    return f"Hello, {name}! Welcome to the test import repository."


def get_current_time():
    """
    Get the current time formatted as a string.
    
    Returns:
        str: Current time in ISO format
    """
    return datetime.now().isoformat()


def calculate_sum(numbers):
    """
    Calculate the sum of a list of numbers.
    
    Args:
        numbers (list): A list of numbers to sum
        
    Returns:
        int or float: The sum of all numbers (type matches input types)
    """
    return sum(numbers)


def main():
    """Main function to demonstrate the sample application."""
    print("=" * 50)
    print("Sample Python Application")
    print("=" * 50)
    print()
    
    # Demonstrate greeting
    name = "Developer"
    print(greet(name))
    print()
    
    # Demonstrate time function
    current_time = get_current_time()
    print(f"Current time: {current_time}")
    print()
    
    # Demonstrate calculation
    numbers = [1, 2, 3, 4, 5]
    total = calculate_sum(numbers)
    print(f"Sum of {numbers} = {total}")
    print()
    
    print("=" * 50)
    print("Application completed successfully!")
    print("=" * 50)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
