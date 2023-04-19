from typing import List, Dict, Any, Union


##################################################
############### 1. Math tasks#####################


def add_numbers_correct(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


def remainder_correct(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a % b


def exponentiate_correct(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    return base ** exponent


def gcd_correct(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def lcm_correct(a: int, b: int) -> int:
    return abs(a * b) // gcd_correct(a, b)


##################################################
############### 2. String tasks ##################


def reverse_string_correct(s: str) -> str:
    return s[::-1]


def count_char_correct(s: str, c: str) -> int:
    return s.count(c)


def is_palindrome_correct(s: str) -> bool:
    return s == s[::-1]


def longest_substring_without_repeating_characters_correct(s: str) -> str:
    longest_substring = ""
    current_substring = ""

    for c in s:
        if c not in current_substring:
            current_substring += c
        else:
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            current_substring = current_substring[current_substring.index(c) + 1:] + c

    return longest_substring if len(longest_substring) > len(current_substring) else current_substring


def shortest_palindrome_correct(s: str) -> str:
    if is_palindrome_correct(s):
        return s

    for i in range(len(s) - 1, 0, -1):
        substring = s[:i]
        if is_palindrome_correct(substring):
            return s[i:][::-1] + s

    return s[::-1][1:] + s


##################################################
################ 3. List tasks ###################

def find_max_element_correct(lst: List[int]) -> int:
    return max(lst)


def sum_of_elements_correct(lst: List[int]) -> int:
    return sum(lst)


def remove_duplicates_correct(lst: List[Any]) -> List[Any]:
    return list(dict.fromkeys(lst))


def find_intersection_correct(lst1: List[Any], lst2: List[Any]) -> List[Any]:
    return [value for value in lst1 if value in lst2]


def flatten_nested_list_correct(lst: List[Any]) -> List[Any]:
    result = []
    for el in lst:
        if isinstance(el, list):
            result.extend(flatten_nested_list_correct(el))
        else:
            result.append(el)
    return result


###################################################
################ 4. Dictionary tasks ##############

def merge_dictionaries_correct(dict1: Dict, dict2: Dict) -> Dict:
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict


def invert_dictionary_correct(input_dict: Dict) -> Dict:
    inverted_dict = {v: k for k, v in input_dict.items()}
    return inverted_dict


def count_elements_correct(lst: List) -> Dict:
    element_count = {}
    for item in lst:
        if item in element_count:
            element_count[item] += 1
        else:
            element_count[item] = 1
    return element_count


def filter_dict_correct(input_dict: Dict, min_value: int) -> Dict:
    filtered_dict = {k: v for k, v in input_dict.items() if v >= min_value}
    return filtered_dict


def sort_dict_by_values_correct(input_dict: Dict) -> Dict:
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1]))
    return sorted_dict
