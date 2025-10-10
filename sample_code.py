"""
Sample Python code with intentional knowledge gaps for testing SkillLens GitHub Action.
This code contains various issues that reviewers can comment on to trigger learning recommendations.
"""

import pickle
import os
from typing import List


class UserManager:
    def __init__(self):
        self.users = []
        self.passwords = {}  # Storing passwords in plain text

    def add_user(self, username, password, email):
        # No input validation
        self.users.append(username)
        self.passwords[username] = password  # Plain text password storage

        # SQL injection vulnerability example
        query = f"INSERT INTO users VALUES ('{username}', '{password}', '{email}')"
        print(query)

    def authenticate(self, username, password):
        try:
            if self.passwords[username] == password:
                return True
        except:  # Bare except clause
            pass
        return False

    def find_user(self, username):
        # Inefficient linear search
        for user in self.users:
            if user == username:
                return user
        return None

    def calculate_factorial(self, n):
        # Inefficient recursive implementation without memoization
        if n == 0:
            return 1
        else:
            return n * self.calculate_factorial(n - 1)

    def process_data(self, data):
        # No type hints for parameters
        result = []
        for i in range(len(data)):  # Not pythonic
            if data[i] > 0:
                result.append(data[i] * 2)
        return result

    def save_to_file(self, filename):
        # Using pickle for data serialization (security risk)
        with open(filename, 'wb') as f:
            pickle.dump(self.users, f)

    def load_from_file(self, filename):
        # Unsafe pickle loading
        with open(filename, 'rb') as f:
            self.users = pickle.load(f)  # Arbitrary code execution risk


class DataProcessor:
    def __init__(self):
        self.data = []

    def bubble_sort(self, arr):
        # Inefficient sorting algorithm
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    temp = arr[j]  # Not using Python swap idiom
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        return arr

    def find_duplicates(self, list1, list2):
        # Inefficient O(n*m) algorithm
        duplicates = []
        for item1 in list1:
            for item2 in list2:
                if item1 == item2 and item1 not in duplicates:
                    duplicates.append(item1)
        return duplicates

    def read_large_file(self, filepath):
        # Loading entire file into memory
        with open(filepath, 'r') as f:
            content = f.read()  # Memory inefficient for large files
            lines = content.split('\n')
        return lines

    def concat_strings(self, strings):
        # String concatenation in loop (inefficient)
        result = ""
        for s in strings:
            result = result + s + ", "
        return result


def global_function(x, y):
    # Function doing too many things
    # Calculate sum
    sum_result = x + y

    # Calculate product
    product = x * y

    # Check if prime (inefficient implementation)
    is_x_prime = True
    for i in range(2, x):
        if x % i == 0:
            is_x_prime = False
            break

    # File operation mixed with logic
    with open('output.txt', 'w') as f:
        f.write(f"Sum: {sum_result}, Product: {product}")

    return sum_result, product, is_x_prime


# Global variables (poor practice)
GLOBAL_COUNTER = 0
GLOBAL_CONFIG = {}


def increment_counter():
    # Modifying global state
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 1
    return GLOBAL_COUNTER


class APIClient:
    def __init__(self, api_key):
        self.api_key = api_key  # API key stored in code

    def make_request(self, endpoint):
        # No error handling for network requests
        import urllib.request
        response = urllib.request.urlopen(f"http://api.example.com/{endpoint}?key={self.api_key}")
        return response.read()

    def parse_json(self, json_string):
        # No error handling for JSON parsing
        import json
        return json.loads(json_string)


if __name__ == "__main__":
    # Example usage with issues
    manager = UserManager()
    manager.add_user("admin", "password123", "admin@example.com")  # Weak password

    processor = DataProcessor()
    data = [5, 2, 8, 1, 9]
    sorted_data = processor.bubble_sort(data)

    # Using eval (dangerous)
    user_input = "print('Hello')"
    eval(user_input)  # Security vulnerability
