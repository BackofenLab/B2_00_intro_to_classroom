<img src="./figures/banner.png" alt="UniFreiburg Banner"/>

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

---
## Bioinformatics 2
###### SS 2023
##### Exercise sheet 0: Introduction to GitHub classroom
---
    
# Programming Tasks

These programming tasks are designed to help you practice and improve your skills in various areas, such as working with strings, lists, dictionaries, and mathematical operations. By working on these tasks, you will become more familiar with the fundamental concepts of programming and will be better prepared for more advanced topics.

## 1. Math Tasks

These tasks focus on basic mathematical operations, such as addition, division, exponentiation, and finding the greatest common divisor (GCD) and least common multiple (LCM) of two numbers. These tasks are important because they help you develop a strong foundation in mathematical concepts, which is crucial for problem-solving in programming.

### Task List

1. **Add Numbers**: Write a function that takes two numbers as input and returns their sum. This task helps you practice addition and working with numbers.
2. **Remainder**: Write a function that takes two numbers as input and returns the remainder when the first number is divided by the second number. This task helps you practice division and handling edge cases, such as when the second number is zero.
3. **Exponentiate**: Write a function that takes two numbers as input (a base and an exponent) and returns the result of raising the base to the power of the exponent. This task helps you practice exponentiation and working with numbers.
4. **GCD**: Write a function that takes two numbers as input and returns their greatest common divisor. This task helps you practice finding the GCD, an essential concept in number theory.
5. **LCM**: Write a function that takes two numbers as input and returns their least common multiple. This task helps you practice finding the LCM, another important concept in number theory.

## 2. String Tasks

These tasks focus on string manipulation, such as reversing a string, counting the occurrences of a character in a string, and finding palindromes. These tasks are important because they help you practice working with strings, a fundamental data type in programming.

### Task List

1. **Reverse String**: Write a function that takes a string as input and returns the reversed string. This task helps you practice string manipulation and working with strings.
2. **Count Char**: Write a function that takes a string and a character as input and returns the number of occurrences of the character in the string. This task helps you practice string manipulation and counting occurrences of a specific character.
3. **Is Palindrome**: Write a function that takes a string as input and returns True if it is a palindrome, and False otherwise. This task helps you practice string manipulation and working with palindromes.
4. **Longest Substring Without Repeating Characters**: Write a function that takes a string as input and returns the longest substring without repeating characters. This task helps you practice string manipulation and finding unique substrings.
5. **Shortest Palindrome**: Write a function that takes a string as input and returns the shortest palindrome that can be created by adding characters to the beginning of the string. This task helps you practice string manipulation and working with palindromes.

## 3. List Tasks

These tasks focus on list manipulation, such as finding the maximum element in a list, summing the elements of a list, and removing duplicates from a list. These tasks are important because they help you practice working with lists, a fundamental data structure in programming.

### Task List

1. **Find Max Element**: Write a function that takes a list of numbers and returns the maximum element in the list. This task helps you practice list manipulation and finding the maximum value.
2. **Sum of Elements**: Write a function that takes a list of numbers and returns the sum of all the elements in the list. This task helps you practice list manipulation and summing elements.
3. **Remove Duplicates**: Write a function that takes a list and returns a new list with duplicates removed. This task helps you practice list manipulation and removing duplicates.
4. **Find Intersection**: Write a function that takes two lists and returns a new list with the intersection of the two input lists. This task helps you practice list manipulation and finding the intersection of two lists.
5. **Flatten Nested List**: Write a function that takes a nested list and returns a new list with all the elements flattened. This task helps you practice list manipulation and working with nested data structures.

## 4. Dict Tasks

These tasks focus on dictionary manipulation, such as merging dictionaries, inverting dictionaries, counting the occurrences of elements in a list, filtering dictionaries by a minimum value, and sorting dictionaries by values. These tasks are important because they help you practice working with dictionaries, a fundamental data structure in programming.

### Task List

1. **Merge Dictionaries**: Write a function that merges two dictionaries into a single one. If the same key exists in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary. This task helps you practice dictionary manipulation and merging dictionaries.
2. **Invert Dictionary**: Write a function that inverts a dictionary by swapping its keys and values. Assume that the input dictionary has unique values. This task helps you practice dictionary manipulation and inverting dictionaries.
3. **Count Elements**: Write a function that counts the occurrences of each element in a list and returns the counts as a dictionary. This task helps you practice dictionary manipulation and counting occurrences of elements in a list.
4. **Filter Dict**: Write a function that filters a dictionary by removing key-value pairs with values less than the specified minimum value. This task helps you practice dictionary manipulation and filtering dictionaries based on values.
5. **Sort Dict by Values**: Write a function that sorts a dictionary by its values in ascending order. The original dictionary should not be modified. This task helps you practice dictionary manipulation and sorting dictionaries by values.

## Testing Your Code Locally

To test your code locally, you can run the provided tests found in the file `tests/test_exercise_sheet0.py` using pytest. To do this, follow these steps:

1. Make sure you have Python installed on your computer. You can download it from the [official Python website](https://www.python.org/downloads/).
2. Install pytest by running the following command: `pip install pytest`
3. Open a terminal or command prompt and navigate to the folder containing the `tests` folder.
4. Run the following command to execute the tests: `pytest tests/test_exercise_sheet0.py`

## Pushing Your Changes

```
git add exercise_sheet0.py
git commit -m "Completed exercise sheet 0 tasks"
git push origin master
```
