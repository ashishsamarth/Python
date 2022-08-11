# Import string module
import string
# Import collections module
import collections
# Import Itertools module
import itertools


# Class definitions should use CamelCase convention based on pep-8 guidelines
class UsefulUtils:

    # Method to get the number of arguments
    # Arguments are passed as a list, separated by comma
    def get_arg_cnt(*_arg):
        # Return type is an integer
        return len(_arg)
    
    # Method to get only lower case letters (a through z)
    @staticmethod
    # Argument to this method: None
    def get_lower_case_alphabets():
        # Return type is a string
        return string.ascii_lowercase
    
    # Method to get only upper case letters (A through Z)
    @staticmethod
    # Argument to this method: None
    def get_upper_case_alphabets():
        # Return type is a string
        return string.ascii_uppercase
    
    # Method to get both lower case and upper case letters (a through Z)
    # Argument to this method: None
    @staticmethod
    def get_alphabets():
        # Return type is a string
        return string.ascii_letters
    
    # Method to get numbers 0 through 9 as string
    # Argument to this method: None
    @staticmethod
    def get_str_0_9():
        # Return type is a string
        return string.digits
    
    # Method to get numbers 0 through 7 as string
    # Argument to this method: None
    @staticmethod
    def get_str_0_7():
        # Return type is a string
        return string.octdigits
    
    # Method to get lower case a through f
    # Use of list comprehension with join
    # Argument to this method: None    
    @staticmethod
    def get_lower_case_a_to_f():
        # Return type is a string
        return ''.join(_ for _ in string.hexdigits if _.islower())
    
    # Method to get upper case A through F
    # Use of list comprehension with join
    # Argument to this method: None
    @staticmethod
    def get_upper_case_a_to_f():
        # Return type is a string
        return ''.join(_ for _ in string.hexdigits if _.isupper())
    
    # Method to get special characters
    # Argument to this method: None
    @staticmethod
    def get_special_chars():
        # Return type is a string
        # returns: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        return string.punctuation
    
    # Method to reverse the string
    # Argument to this method: string
    @staticmethod
    def reverse_string(_inp_str: str):
        # Return type is a string
        return _inp_str[::-1]
    
    # Method to check if a string is a palindrome
    # Argument to this method: string
    @staticmethod
    def is_str_a_palindrome(_inp_str: str):
        reversed_string = _inp_str[::-1]
        return True if _inp_str == reversed_string else False
    
    # Method to check if two strings are anagrams
    @staticmethod
    # Argument to this method: two strings
    def are_strs_an_anagram(_inp_str_1: str, _inp_str_2: str):
        # returns a dictionary where each alphabet of string is 'key' and their # of occurrences are values
        return True if collections.Counter(_inp_str_1) == collections.Counter(_inp_str_2) else False
    
    # Method to get occurrences of alphabets in string along with string
    # Argument to this method: string
    @staticmethod
    def cnt_elem_occurrences_in_str(_inp_str: str):
        # returns a dictionary where each alphabet of string is 'key' and their # of occurrences are values
        return dict(collections.Counter(_inp_str))
    
    # Method to get occurrences of alphabets in string
    # Sort the result dictionary by key or value
    # Order the dictionary in asc or desc based on _sort_reversal
    # Valid values for _sort_reversal are True / False
    # Valid values for _sort_key are key / value
    # Arguments to this method are: string, sorting key and sorting type
    @staticmethod
    def cnt_elem_occurrences_in_str_ordered_rslt(_inp_str:str, _sort_key='key', _sort_reversal=False):
        # collections.Counter will create a dictionary structure and get the count of each element of the string
        # element is the key and count is the value of that key
        result_set = collections.Counter(_inp_str)
        # Following if statement is triggered when user wants to sort the result by key
        if _sort_key == 'key':
            return dict(collections.OrderedDict(sorted(result_set.items(), key=lambda _: _[0], reverse=_sort_reversal)))
        # Following elif statement is triggered when user wants to sort the result by value of the key
        elif _sort_key == 'value':
            return dict(collections.OrderedDict(sorted(result_set.items(), key=lambda _: _[1], reverse=_sort_reversal)))
    
    # Method to get unique alphabets from string
    # Argument to this method: string
    @staticmethod
    def get_unique_elems_from_string(_inp_str: str):
        return collections.Counter(_inp_str).keys()
    
    # Method to create a dictionary dataset automatically
    # Argument to this method: None
    @staticmethod
    def auto_create_dict_by_counter():
        my_str = UsefulUtils.ret_upr_case_alphabets()
        return dict(collections.Counter(my_str))
    
    # Method to get top 5 alphabets based on their occurrences in string
    # Argument to this method: string
    @staticmethod
    def top_5_elem_occurrences_in_str(_inp_str: str):
        # We use the 'most_common' method for Counter
        return dict(collections.Counter(_inp_str).most_common(5))
    
    # Method to get top n alphabets based on their occurrences in string
    # Argument to this method: string
    @staticmethod
    def top_n_elem_occurrences_in_str(_inp_str: str, n):
        # We use the 'most_common' method for Counter
        return dict(collections.Counter(_inp_str).most_common(n))
    
    # Method to check if given string is empty or not
    # Argument to this method: string
    @staticmethod
    def chk_if_string_empty(_inp_str: str):
        return True if not _inp_str else False
    
    # Method to assign same values to provided keys
    # Arguments to this method: _keys as a list of elements, _value as any value
    def assign_same_val_to_all_keys(_keys, _value):
        # itertools.repeat : repeats the passed value seamlessly
        # zip : ties the keys and value together together
        my_dict = dict(zip(_keys, itertools.repeat(_value)))
        # Return type is a dictionary
        return my_dict

    # Method to join multiple string arguments into one concatenated string
    # Arguments to this method: Multiple strings as arguments (separated by comma), user provided delimiter
    # * takes care of the unpacking multiple tuples passed as arguments
    # If no delimiter is provided, <space> is used as default value
    def join_strs(*_string_iterables, _delim=' '):
        # Return type is a string
        return f'{_delim}'.join(_ for _ in _string_iterables)

    # Method to join multiple tuple arguments into one tuple
    # Arguments to this method: Multiple tuples as arguments (separated by comma)
    # * takes care of the unpacking multiple tuples passed as arguments
    def join_tuples(*_tuple_iterables):
        # itertools.chain : joins multiple tuples in to one
        joined_tuple = tuple(itertools.chain(*_tuple_iterables))
        # Return type is a tuple
        return joined_tuple

    # Method to join multiple tuples arguments into one tuple and remove duplicate elements from result tuple
    # Arguments to this method: Multiple tuples as arguments (separated by comma)
    # * takes care of the unpacking multiple tuples passed as arguments
    def merge_tuples(*_tuple_iterables):
        # itertools.chain : joins multiple tuples in to one
        # set : removes the duplicate elements from the result
        joined_tuple = tuple(set(itertools.chain(*_tuple_iterables)))
        # Return type is a tuple
        return joined_tuple

    # Method to join multiple lists into one list
    # Argument to this method: Multiple lists as arguments (separated by comma)
    # * takes care of the unpacking multiple lists passed as arguments
    def join_lists(*_lists_iterables):
        # itertools.chain : joins the multiple lists into one
        chained_list = list(itertools.chain(*_lists_iterables))
        # Return type is a list
        return chained_list
    
    # Method to join multiple lists into one list and keep only non-repeating values
    # Argument to this method: Multiple lists as arguments (separated by comma)
    # * takes care of the unpacking multiple lists passed as arguments
    def merge_lists(*_lists_iterables):
        # itertools.chain : joins the multiple lists into one
        # set removes the duplicate entries from the list
        # list converts the unique set to a list
        merged_list = list(set(list(itertools.chain(*_lists_iterables))))
        # Return type is a list
        return merged_list
    
    # Method to join multiple dictionaries to a single dictionary
    # Argument to this method: Multiple Dictionaries as arguments (separated by comma)
    # * takes care of the unpacking multiple dictionaries passed as arguments
    def join_dicts_m1(*_dicts_iterables):
        # Using list comprehension to create a new dictionary with keys and values iterated from all the dictionaries in the unpacked list of dictionaries
        chained_dict = {k:v for d in _dicts_iterables for k,v in d.items()}
        # Return type is a dictionary
        return chained_dict
    
    # Method to join multiple dictionaries to a single dictionary
    # Argument to this method: Multiple Dictionaries as arguments (separated by comma)
    # * takes care of the unpacking multiple dictionaries passed as arguments
    def join_dicts_m2(*_dicts_iterables):
        # Create an empty dictionary
        chained_dict = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the Blank dictionary with keys and Values from unpacked list of dictionaries
            chained_dict.update(_)
        # Return type is a dictionary
        return chained_dict
    
    # Method to join multiple dictionaries to a single dictionary
    # Argument to this method: Multiple Dictionaries as arguments (separated by comma)
    # * takes care of the unpacking multiple dictionaries passed as arguments
    def join_dicts_m3(*_dicts_iterables):
        # Create an empty dictionary
        merged_dict = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the Blank dictionary with keys and Values from unpacked list of dictionaries
            merged_dict |= _
        # Return type is a dictionary
        return merged_dict
    
    # Method to join multiple dictionaries to a single dictionary and sort the new dictionary based on keys or values in
    # Ascending or Descending order
    # Argument to this method: Multiple Dictionaries as arguments (separated by comma), sorting key and sorting type
    # * takes care of the unpacking multiple dictionaries passed as arguments
    # _sort_key='key', _sort_reversal=False is defaulted to sorting by key in ascending order
    # _sort_key='value' will sort the resulting dictionary by values in ascending order
    # _sort_key='value', _sort_reversal=True will sort the resulting dictionary by values in descending order
    def join_dicts_and_sort(*_dicts_iterables, _sort_key='key', _sort_reversal=False):
        # Create an empty dictionary
        merged_dict = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the Blank dictionary with keys and Values from unpacked list of dictionaries
            merged_dict |= _
        # Sort the updated dictionary based on keys in ascending order
        # usage of sorted method: sorted(iterable, key)
        # special note: key can be any user defined function as well
        # for sorting key, I am using the anonymous lambda function and item[0] refers to the dictionary keys
        if _sort_key == 'key':
            # Return type is a dictionary
            return dict(sorted(merged_dict.items(), key=lambda item:item[0], reverse=_sort_reversal))
        elif _sort_key == 'value':
            # Return type is a dictionary
            return dict(sorted(merged_dict.items(), key=lambda item:item[-1], reverse=_sort_reversal))
        
    # Method to count occurences of provided element in multiple lists
    # Arguments to this method: Multiple lists as arguments (separated by comma)
    # * takes care of the unpacking multiple lists passed as arguments
    def cnt_occurence_of_elem_in_joined_lists(*_lists_iterable, _element):
        # itertools.chain : joins the multiple lists into one
        chained_list = list(itertools.chain(*_lists_iterable))
        # chained_list.count(_element) counts the number of occurences, if will be triggered only the result is not zero
        return chained_list.count(_element) if chained_list.count(_element) else 0

    # Method to count occurences of all elements in multiple lists
    # Arguments to this method: Multiple lists as arguments (separated by comma)
    # * takes care of the unpacking multiple lists passed as arguments
    def cnt_occurence_of_all_elems_in_joined_lists(*_lists_iterable):
        # itertools.chain : joins the multiple lists into one
        chained_list = list(itertools.chain(*_lists_iterable))
        # Count the Occurence of each value in chained list and keep value as key and count as value
        occurrence_dict = dict(collections.Counter(chained_list))
        # Return type is a dictionary
        return occurrence_dict
    
    # Method to count occurences of all values in multiple dictionaries
    # Arguments to this method: Multiple dictionaries as arguments (separated by comma)
    # * takes care of the unpacking multiple dictionaries passed as arguments
    def cnt_occurence_of_all_vals_in_joined_dicts(*_dicts_iterables):
        # Create an empty dictionary
        merged_dicts = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the Blank dictionary with keys and Values from unpacked list of dictionaries
            merged_dicts |= _
        # Count the Occurence of each value in merged dictionary and keep value as key and count as value
        occurence_dict = dict(collections.Counter(merged_dicts.values()))
        # Return type is a dictionary
        return occurence_dict
    
    # Method to count occurences of all elements in multiple strings
    # Argument to this method: Multiple strings as arguments (separated by comma), sorting key and sorting type
    # * takes care of the unpacking multiple strings passed as arguments
    # _sort_key='key', _sort_reversal=False is defaulted to sorting by key in ascending order
    # _sort_key='value' will sort the resulting dictionary by values in ascending order
    # _sort_key='value', _sort_reversal=True will sort the resulting dictionary by values in descending order
    def cnt_occurrences_of_str_vals_in_joined_str_and_sort(*_iterables, _sort_key='key', _sort_reversal=False):
        # Use list comprehension to join the string without a space / delimiter
        joined_string = ''.join(_ for _ in _iterables)
        # Count the Occurence of each element in joined string and keep element as key and count as value
        occurence_dict = dict(collections.Counter(joined_string))
        # Return type is a dictionary
        if _sort_key=='key':
            return dict(sorted(occurence_dict.items(), key= lambda item:item[0], reverse=_sort_reversal))
        elif _sort_key=='value':
            return dict(sorted(occurence_dict.items(), key= lambda item:item[-1], reverse=_sort_reversal)) 