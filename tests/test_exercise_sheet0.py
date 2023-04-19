from typing import List, Dict, Any
import pytest

from exercise_sheet0 import (add_numbers,
                             remainder,
                             exponentiate,
                             gcd,
                             lcm)


from implementation import (add_numbers_correct,
                            divide_numbers_correct,
                            remainder_correct,
                            exponentiate_correct,
                            gcd_correct,
                            lcm_correct)


from exercise_sheet0 import (reverse_string,
                             count_char,
                             is_palindrome,
                             longest_substring_without_repeating_characters,
                             shortest_palindrome)


from implementation import (reverse_string_correct,
                            count_char_correct,
                            is_palindrome_correct,
                            longest_substring_without_repeating_characters_correct,
                            shortest_palindrome_correct)


from exercise_sheet0 import (find_max_element,
                            sum_of_elements,
                            remove_duplicates,
                            find_intersection,
                            flatten_nested_list)


from implementation import (find_max_element_correct,
                            sum_of_elements_correct,
                            remove_duplicates_correct,
                            find_intersection_correct,
                            flatten_nested_list_correct)


from exercise_sheet0 import (merge_dictionaries,
                             invert_dictionary,
                             count_elements,
                             filter_dict,
                             sort_dict_by_values)


from implementation import (merge_dictionaries_correct,
                            invert_dictionary_correct,
                            count_elements_correct,
                            filter_dict_correct,
                            sort_dict_by_values_correct)


#####################Tests#########################



###################Two values######################
input_two_values = [
    (3, 5),
    (-2, 7),
    (0, 0),
    (8, 2),
    (7, 3)
]


@pytest.mark.parametrize("a, b", input_two_values)
def test_add_numbers(a, b):
    add_numbers_test_data = add_numbers_correct(a, b)
    result = add_numbers(a, b)
    assert result == add_numbers_test_data, f"Expected {add_numbers_test_data}, but got {result}"



@pytest.mark.parametrize("a, b", input_two_values)
def test_remainder(a, b):
    if b != 0:
        remainder_test_data = remainder_correct(a, b)
        result = remainder(a, b)
        assert result == remainder_test_data, f"Expected {remainder_test_data}, but got {result}"


@pytest.mark.parametrize("a, b", input_two_values)
def test_exponentiate(a, b):
    exponentiate_test_data = exponentiate_correct(a, b)
    result = exponentiate(a, b)
    assert result == exponentiate_test_data, f"Expected {exponentiate_test_data}, but got {result}"


@pytest.mark.parametrize("a, b", input_two_values)
def test_gcd(a, b):
    gcd_test_data = gcd_correct(a, b)
    result = gcd(a, b)
    assert result == gcd_test_data, f"Expected {gcd_test_data}, but got {result}"


@pytest.mark.parametrize("a, b", input_two_values)
def test_lcm(a, b):
    lcm_test_data = lcm_correct(a, b)
    result = lcm(a, b)
    assert result == lcm_test_data, f"Expected {lcm_test_data}, but got {result}"


###################Strings######################


input_strings = [
    "hello",
    "world",
    "abcdef",
    "racecar",
    "python",
    "madam",
]

input_char = [
    "l",
    "r",
    "a",
    "p",
]

@pytest.mark.parametrize("s", input_strings)
def test_reverse_string(s):
    result = reverse_string(s)
    correct_result = reverse_string_correct(s)
    assert result == correct_result, f"Expected {correct_result}, but got {result}"


@pytest.mark.parametrize("s, c", [(s, c) for s in input_strings for c in input_char])
def test_count_char(s, c):
    result = count_char(s, c)
    correct_result = count_char_correct(s, c)
    assert result == correct_result, f"Expected {correct_result}, but got {result}"


@pytest.mark.parametrize("s", input_strings)
def test_is_palindrome(s):
    result = is_palindrome(s)
    correct_result = is_palindrome_correct(s)
    assert result == correct_result, f"Expected {correct_result}, but got {result}"


@pytest.mark.parametrize("s", input_strings)
def test_longest_substring_without_repeating_characters(s):
    result = longest_substring_without_repeating_characters(s)
    correct_result = longest_substring_without_repeating_characters_correct(s)
    assert result == correct_result, f"Expected {correct_result}, but got {result}"


@pytest.mark.parametrize("s", input_strings)
def test_shortest_palindrome(s):
    result = shortest_palindrome(s)
    correct_result = shortest_palindrome_correct(s)
    assert result == correct_result, f"Expected {correct_result}, but got {result}"


###################Lists######################

@pytest.mark.parametrize("lst", [
    ([3, 5, 2, 8, 1]),
    ([1, 1, 1, 1]),
    ([])
])
def test_find_max_element(lst):
    expected = find_max_element_correct(lst)
    result = find_max_element(lst)
    assert result == expected, f"Expected {expected}, but got {result}"


@pytest.mark.parametrize("lst", [
    ([1, 2, 3, 4, 5]),
    ([5, 5, 5, 5, 5]),
    ([])
])
def test_sum_of_elements(lst):
    expected = sum_of_elements_correct(lst)
    result = sum_of_elements(lst)
    assert result == expected, f"Expected {expected}, but got {result}"


@pytest.mark.parametrize("lst", [
    ([1, 2, 2, 3, 4, 4, 5]),
    (["apple", "banana", "apple", "orange"]),
    ([])
])
def test_remove_duplicates(lst):
    expected = remove_duplicates_correct(lst)
    result = remove_duplicates(lst)
    assert result == expected, f"Expected {expected}, but got {result}"


@pytest.mark.parametrize("lst1, lst2", [
    ([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]),
    (["apple", "banana", "orange"], ["banana", "grape", "apple"]),
    ([], [1, 2, 3]),
])
def test_find_intersection(lst1, lst2):
    expected = find_intersection_correct(lst1, lst2)
    result = find_intersection(lst1, lst2)
    assert result == expected, f"Expected {expected}, but got {result}"


@pytest.mark.parametrize("lst", [
    ([1, [2, [3, 4], 5], 6]),
    (["apple", ["banana", ["orange", "grape"]], "pear"]),
    ([]),
])
def test_flatten_nested_list(lst):
    expected = flatten_nested_list_correct(lst)
    result = flatten_nested_list(lst)
    assert result == expected, f"Expected {expected}, but got {result}"


###################Dictionaries######################
input_two_dicts = [({"a": 1, "b": 2}, {"c": 3, "d": 4}),
                   ({"apple": 3, "banana": 2}, {"apple": 1, "kiwi": 5})]


@pytest.mark.parametrize("dict1, dict2", input_two_dicts)
def test_merge_dictionaries(dict1, dict2):
    expected = merge_dictionaries_correct(dict1, dict2)
    result = merge_dictionaries(dict1, dict2)
    assert result == expected, f"Expected {expected}, but got {result}"


input_dicts = [{"a": 1, "b": 2}, {"apple": 3, "banana": 2}]


@pytest.mark.parametrize("input_dict", input_dicts)
def test_invert_dictionary(input_dict):
    expected = invert_dictionary_correct(input_dict)
    result = invert_dictionary(input_dict)
    assert result == expected, f"Expected {expected}, but got {result}"


input_lists = [["apple", "banana", "apple", "kiwi", "banana", "apple"],
               [1, 2, 3, 2, 1, 2, 1, 1, 1]]


@pytest.mark.parametrize("lst", input_lists)
def test_count_elements(lst):
    expected = count_elements_correct(lst)
    result = count_elements(lst)
    assert result == expected, f"Expected {expected}, but got {result}"


input_dicts_min_values = [({"a": 1, "b": 2, "c": 3}, 2),
                          ({"apple": 3, "banana": 2, "kiwi": 5}, 3)]


@pytest.mark.parametrize("input_dict, min_value", input_dicts_min_values)
def test_filter_dict(input_dict, min_value):
    expected = filter_dict_correct(input_dict, min_value)
    result = filter_dict(input_dict, min_value)
    assert result == expected, f"Expected {expected}, but got {result}"


input_dicts_to_sort = [{"a": 1, "b": 2, "c": 3}, {"apple": 3, "banana": 2, "kiwi": 5}]


@pytest.mark.parametrize("input_dict", input_dicts_to_sort)
def test_sort_dict_by_values(input_dict):
    expected = sort_dict_by_values_correct(input_dict)
    result = sort_dict_by_values(input_dict)
    assert result == expected, f"Expected {expected}, but got {result}"
