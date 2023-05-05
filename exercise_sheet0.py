from typing import List, Dict, Any, Union



###################################################
################# 1. Math tasks ###################


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    This function takes two numbers as input and returns their sum.
    Example:
        add_numbers(3, 5) -> 8
    """
    pass


def remainder(a: int, b: int) -> int:
    """
    This function takes two numbers as input and returns
    the remainder when the first number is divided by the second number.
    Handle the case when the second number is zero.
    Example:
        remainder(7, 3) -> 1
    """
    pass


def exponentiate(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """
    This function takes two numbers as input (a base and an exponent)
    and returns the result of raising the base to the power of the exponent.
    Example:
        exponentiate(2, 3) -> 8
    """
    pass


def gcd(a: int, b: int) -> int:
    """
    This function takes two numbers as input and returns their greatest common divisor.
    Example:
        gcd(14, 28) -> 14
    """
    pass


def lcm(a: int, b: int) -> int:
    """
    This function takes two numbers as input and returns their least common multiple.
    Example:
        lcm(3, 5) -> 15
    """
    pass


###################################################
################## 2. String tasks ################


def reverse_string(s: str) -> str:
    """
    This function takes a string as input and returns the reversed string.
    Example:
        reverse_string("hello") -> "olleh"
    """
    pass


def count_char(s: str, c: str) -> int:
    """
    This function takes a string and a character as input and returns the number of occurrences of the character in the string.
    Example:
        count_char("hello", "l") -> 2
    """
    pass


def is_palindrome(s: str) -> bool:
    """
    This function takes a string as input and returns True if it is a palindrome, and False otherwise.
    Example:
        is_palindrome("racecar") -> True
    """
    pass


def longest_substring_without_repeating_characters(s: str) -> str:
    """
    This function takes a string as input and returns the longest substring without repeating characters.
    Example:
        longest_substring_without_repeating_characters("abcabcbb") -> "abc"
    """
    pass


def shortest_palindrome(s: str) -> str:
    """
    This function takes a string as input and returns the shortest palindrome that can be created by adding characters to the beginning of the string.
    Example:
        shortest_palindrome("abcd") -> "dcbabcd"
    """
    pass


###################################################
################### 3. List tasks #################

def find_max_element(lst: List[int]) -> int:
    """
    This function takes a list of numbers and returns the maximum element in the list.
    Example:
        find_max_element([3, 5, 1, 8, 7]) -> 8
    """
    pass


def sum_of_elements(lst: List[int]) -> int:
    """
    This function takes a list of numbers and returns the sum of all the elements in the list.
    Example:
        sum_of_elements([3, 5, 1, 8, 7]) -> 24
    """
    pass


def remove_duplicates(lst: List[Any]) -> List[Any]:
    """
    This function takes a list and returns a new list with duplicates removed.
    Example:
        remove_duplicates([3, 5, 1, 3, 7, 5, 8]) -> [3, 5, 1, 7, 8]
    """
    pass


def find_intersection(lst1: List[Any], lst2: List[Any]) -> List[Any]:
    """
    This function takes two lists and returns a new list with the intersection of the two input lists.
    Example:
        find_intersection([3, 5, 1, 7, 8], [1, 7, 9, 5, 2]) -> [5, 1, 7]
    """
    pass


def flatten_nested_list(lst: List[Any]) -> List[Any]:
    """
    This function takes a nested list and returns a new list with all the elements flattened.
    Example:
        flatten_nested_list([1, [2, 3], [4, [5, 6]], 7]) -> [1, 2, 3, 4, 5, 6, 7]
    """
    pass


###################################################
################## 4. Dict tasks ##################


def merge_dictionaries(dict1: Dict, dict2: Dict) -> Dict:
    """
    Task 1:
    Merge two dictionaries into a single one.
    If the same key exists in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary.

    Example:
        merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        -> {'a': 1, 'b': 3, 'c': 4}
    """
    pass


def invert_dictionary(input_dict: Dict) -> Dict:
    """
    Task 2:
    Invert a dictionary by swapping its keys and values.
    Assume that the input dictionary has unique values.

    Example:
        invert_dictionary({'a': 1, 'b': 2, 'c': 3})
        -> {1: 'a', 2: 'b', 3: 'c'}
    """
    pass


def count_elements(lst: List) -> Dict:
    """
    Task 3:
    Count the occurrences of each element in a list and return the counts as a dictionary.

    Example:
        count_elements(['apple', 'banana', 'apple', 'orange'])
        -> {'apple': 2, 'banana': 1, 'orange': 1}
    """
    pass


def filter_dict(input_dict: Dict, min_value: int) -> Dict:
    """
    Task 4:
    Filter a dictionary by removing key-value pairs with values less than the specified minimum value.

    Example:
        filter_dict({'a': 1, 'b': 2, 'c': 3, 'd': 4}, 3)
        -> {'c': 3, 'd': 4}
    """
    pass


def sort_dict_by_values(input_dict: Dict) -> Dict:
    """
    Task 5:
    Sort a dictionary by its values in ascending order.
    The original dictionary should not be modified.

    Example:
        sort_dict_by_values({'a': 3, 'b': 1, 'c': 2})
        -> {'b': 1, 'c': 2, 'a': 3}
    """
    pass



