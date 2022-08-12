# Import string module
import string
# Import collections module
import collections
# Import Itertools module
import itertools


# Class definitions should use CamelCase convention based on pep-8 guidelines
class UsefulUtils:

    # Method to add elements at same index from multiple lists and create a new list
    # Argument to this method: Multiple lists as arguments (separated by comma)
    # * takes care of the unpacking multiple lists passed as arguments
    def add_same_idx_elems_in_lists(*_lists_iterable):
        # create an empty list to hold result of index wise additions
        final_result = []
        # Get the count of lists passed as arguments
        list_arg_cnt = UsefulUtils.get_arg_cnt(*_lists_iterable)
        # Identify the number of elements in biggest list
        biggest_list = [max(len(_) for _ in _lists_iterable)][0]
        # Depending on which variable is bigger, create a new dynamic condition for final addition
        # Creation of dynamic condition is needed since we will use it with zip(*_lists_iterable)
        if biggest_list < list_arg_cnt:
            dyn_condition = str(','.join('var'+str(_) for _ in range(1, list_arg_cnt+1)))
        else:
            dyn_condition = str(','.join('var'+str(_) for _ in range(1, biggest_list+1)))
        # Iterate over the lists from arguments and append the list which are shorter than the biggest list
        # If the iterated list is smaller than biggest list, append the list with 0 (int) to resize the list
        for _iter in _lists_iterable:
            if len(_iter) < dyn_condition.count(',') + 1:
                list_len_manager = (dyn_condition.count(',') + 1) - (len(_iter))
                for _extend in range(list_len_manager):
                    _iter.append(0)
        # Iterate over elements starting at 0th index of all lists and add them
        # Once Addition is done for the 0th index, append the sum to final_result
        # This approach is more of a columnar addition
        for dyn_condition in zip(*_lists_iterable):
            # Define an Initial result variable and assign it with 0
            # This gets reset for every index position (vertically)
            init_res = 0
            # Iterate over new vertical list (0th, 1st, 2nd etc index positions) and add them
            for _ in dyn_condition:
                init_res += _
            # Append the sum of each columnar index position to final result
            final_result.append(init_res)
        # Return type is a list
        return final_result

    # Method to check if two strings are anagrams
    # Argument to this method: two strings
    def are_strs_an_anagram(_inp_str_1, _inp_str_2):
        # Return type is boolean
        return True if collections.Counter(_inp_str_1) == collections.Counter(_inp_str_2) else False

    # Method to assign same values to provided keys and create a dictionary
    # Arguments to this method: _keys as a list of elements, _value as any value
    def assign_same_val_to_all_keys(_keys, _value):
        # itertools.repeat : repeats the passed value seamlessly
        # zip : ties the keys and value together together
        my_dict = dict(zip(_keys, itertools.repeat(_value)))
        # Return type is a dictionary
        return my_dict

    # Method to create a dictionary dataset automatically
    # Argument to this method: None
    # Keys are - Upper case Alpbabets
    # Values are - Their count of occurrence
    def auto_create_dict_by_counter():
        my_str = UsefulUtils.get_upper_case_alphabets()
        # Return type is a dictionary
        return dict(collections.Counter(my_str))

    # Method to check if given string is empty or not
    # Argument to this method: string
    def chk_if_str_empty(_inp_str):
        return True if not _inp_str else False

    # Method to concatenate elements of multiple lists
    # Arguments to this method: Multiple lists as arguments (separated by comma), case of the result
    # * takes care of the unpacking multiple lists passed as arguments
    # Valid values for case are: 'capitalize', 'lower', 'original', 'swapcase', 'title', 'upper'
    # Default value of case is : original
    def concatenate_elems_of_lists(*_inp_list, case='original'):
        # Following is a dictionary with case values as keys and corresponding list comprehensions as their evaluated values
        # itertools.chain(*_inp_list) will join all the lists in to one list
        # Each element of the list will be evaluated and only elements having alphabet will be passed over
        # Each passed over element is then joined using space as delimiter and then strin function based on user selection are applied
        conditional = {'capitalize' : ' '.join(_ for _ in itertools.chain(*_inp_list) if str(_).isalpha()).capitalize(),
                       'lower'      : ' '.join(_ for _ in itertools.chain(*_inp_list) if str(_).isalpha()).lower(),
                       'original'   : ' '.join(_ for _ in itertools.chain(*_inp_list) if str(_).isalpha()),
                       'swapcase'   : ' '.join(_ for _ in itertools.chain(*_inp_list) if str(_).isalpha()).swapcase(),
                       'title'      : ' '.join(_ for _ in itertools.chain(*_inp_list) if str(_).isalpha()).title(),
                       'upper'      : ' '.join(_ for _ in itertools.chain(*_inp_list) if str(_).isalpha()).upper()}
        # Return type is a string
        return conditional.get(case)

    # Method to get occurrences of alphabets in string along with string
    # Argument to this method: string
    def cnt_elem_occurrences_in_str(_inp_str):
        # Return type is a dictionary where each alphabet of string is 'key' and their # of occurrences are values
        return dict(collections.Counter(_inp_str))

    # Method to get occurrences of alphabets in string
    # Sort the result dictionary by key or value
    # Order the dictionary in asc or desc based on _sort_reversal
    # Valid values for _sort_reversal are True / False
    # Valid values for _sort_key are key / value
    # Arguments to this method are: string, sorting key and sorting type
    def cnt_elem_occurrences_in_str_ordered_rslt(_inp_str, _sort_key='key', _sort_reversal=False):
        # collections.Counter will create a dictionary structure and get the count of each element of the string
        # element is the key and count is the value of that key
        result_set = collections.Counter(_inp_str)
        # Following if statement is triggered when user wants to sort the result by key
        # key can be any function, I have used the anonymous lambda function
        if _sort_key == 'key':
            return dict(collections.OrderedDict(sorted(result_set.items(), key=lambda _: _[0], reverse=_sort_reversal)))
        # Following elif statement is triggered when user wants to sort the result by value of the key
        # key can be any function, I have used the anonymous lambda function
        elif _sort_key == 'value':
            return dict(collections.OrderedDict(sorted(result_set.items(), key=lambda _: _[1], reverse=_sort_reversal)))

    # Method to count occurrences of provided element in multiple lists
    # Arguments to this method: Multiple lists as arguments (separated by comma), element to be counted
    # * takes care of the unpacking multiple lists passed as arguments
    def cnt_occurrence_of_elem_in_chained_lists(*_lists_iterable, _element):
        # itertools.chain : joins the multiple lists into one
        chained_list = list(itertools.chain(*_lists_iterable))
        # chained_list.count(_element) counts the number of occurrences, if will be triggered only the result is not zero
        return chained_list.count(_element) if chained_list.count(_element) else 0

    # Method to count occurrences of all elements in multiple lists
    # Arguments to this method: Multiple lists as arguments (separated by comma)
    # * takes care of the unpacking multiple lists passed as arguments
    def cnt_occurrence_of_all_elems_in_chained_lists(*_lists_iterable):
        # itertools.chain : joins the multiple lists into one
        chained_list = list(itertools.chain(*_lists_iterable))
        # Count the Occurrence of each value in chained list and keep value as key and occurrence count as value
        # Return type is a dictionary
        return dict(collections.Counter(chained_list))
        
    # Method to count occurrences of all values in multiple dictionaries
    # Arguments to this method: Multiple dictionaries as arguments (separated by comma)
    # * takes care of the unpacking multiple dictionaries passed as arguments
    def cnt_occurrence_of_all_vals_in_joined_dicts(*_dicts_iterables):
        # Create an empty dictionary
        merged_dicts = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the empty dictionary with keys and Values from unpacked list of dictionaries
            merged_dicts |= _
        # Count the Occurrence of each value in merged dictionary and keep value as key and occurrence count as value
        # Return type is a dictionary
        return dict(collections.Counter(merged_dicts.values()))

    # Method to count occurrences of specific value in multiple dictionaries
    # Arguments to this method: Multiple dictionaries as arguments (separated by comma), _value to count occurence for
    # * takes care of the unpacking multiple dictionaries passed as arguments
    def cnt_occurrence_of_val_in_joined_dicts(*_dicts_iterables, _value):
        # Create an empty dictionary
        merged_dicts = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the empty dictionary with keys and Values from unpacked list of dictionaries
            merged_dicts |= _
        # Count the Occurrence of each value in merged dictionary and keep value as key and occurrence count as value
        occurrence_dict = dict(collections.Counter(merged_dicts.values()))
        # Return type is an integer
        try:
            # If the searched value exists in the dictionary, return its count of occurence
            return occurrence_dict[_value]
            # If the searched value does not exist in dictionary, return integer 0
        except KeyError:
            return 0

    # Method to count occurrences of all elements in multiple strings
    # Argument to this method: Multiple strings as arguments (separated by comma), sorting key and sorting type
    # * takes care of the unpacking multiple strings passed as arguments
    # _sort_key='key', _sort_reversal=False is defaulted to sorting by key in ascending order
    # _sort_key='value' will sort the resulting dictionary by values in ascending order
    # _sort_key='value', _sort_reversal=True will sort the resulting dictionary by values in descending order
    def cnt_and_sort_occurrences_of_str_vals_in_concatenated_str(*_iterables, _sort_key='key', _sort_reversal=False):
        # Use list comprehension to join the string without a space / delimiter
        joined_string = ''.join(_ for _ in _iterables)
        # Count the Occurrence of each element in joined string and keep element as key and occurrence count as value
        occurrence_dict = dict(collections.Counter(joined_string))
        # Return type is a dictionary
        if _sort_key == 'key':
            return dict(sorted(occurrence_dict.items(), key = lambda item:item[0], reverse=_sort_reversal))
        elif _sort_key == 'value':
            return dict(sorted(occurrence_dict.items(), key = lambda item:item[-1], reverse=_sort_reversal))
    
    # Method to get the number of arguments
    # Arguments are passed as a list, separated by comma
    def get_arg_cnt(*_arg):
        # Return type is an integer
        return len(_arg)
    
    # Method to get only lower case letters (a through z)
    # Argument to this method: None
    def get_lower_case_alphabets():
        # Return type is a string
        return string.ascii_lowercase
    
    # Method to get only upper case letters (A through Z)
    # Argument to this method: None
    def get_upper_case_alphabets():
        # Return type is a string
        return string.ascii_uppercase
    
    # Method to get both lower case and upper case letters (a through Z)
    # Argument to this method: None
    def get_alphabets():
        # Return type is a string
        return string.ascii_letters
    
    # Method to get numbers 0 through 9 as string
    # Argument to this method: None
    def get_str_0_9():
        # Return type is a string
        return string.digits
    
    # Method to get numbers 0 through 7 as string
    # Argument to this method: None
    def get_str_0_7():
        # Return type is a string
        return string.octdigits
    
    # Method to get lower case a through f
    # Use of list comprehension with join
    # Argument to this method: None    
    def get_lower_case_a_to_f():
        # Return type is a string
        return ''.join(_ for _ in string.hexdigits if _.islower())
    
    # Method to get upper case A through F
    # Use of list comprehension with join
    # Argument to this method: None
    def get_upper_case_a_to_f():
        # Return type is a string
        return ''.join(_ for _ in string.hexdigits if _.isupper())
    
    # Method to get special characters
    # Argument to this method: None
    def get_special_chars():
        # Return type is a string
        # returns: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        return string.punctuation

    # Method to get unique alphabets from input string
    # Argument to this method: string
    def get_unique_elems_from_str(_inp_str):
        return collections.Counter(_inp_str).keys()

    # Method to return first value by max count of occurrence
    # Arguments to this method: Multiple dictionaries as arguments (separated by comma)
    # * takes care of the unpacking multiple dictionaries passed as arguments
    def get_first_val_by_max_occurence_in_joined_dicts(*_dicts_iterables):
        # Create an empty dictionary
        merged_dicts = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the empty dictionary with keys and Values from unpacked list of dictionaries
            merged_dicts |= _
        # Count the Occurrence of each value in merged dictionary and keep value as key and occurrence count as value
        occurrence_dict = dict(collections.Counter(merged_dicts.values()))
        # Following will pick the first value from the dictionary with max count of occurence
        # If their are others, they will be ignored
        max_first_value = max(occurrence_dict, key=occurrence_dict.get)
        # Return type dependent on key
        return max_first_value

    # Method to return last value by max count of occurrence
    # Arguments to this method: Multiple dictionaries as arguments (separated by comma)
    # * takes care of the unpacking multiple dictionaries passed as arguments
    def get_last_val_by_max_occurence_in_joined_dicts(*_dicts_iterables):
        # Create an empty dictionary
        merged_dicts = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the empty dictionary with keys and Values from unpacked list of dictionaries
            merged_dicts |= _
        # Count the Occurrence of each value in merged dictionary and keep value as key and occurrence count as value
        occurrence_dict = dict(collections.Counter(merged_dicts.values()))
        # Following will pick the last value from the dictionary with max count of occurrence
        # If their are others, they will be ignored
        max_last_value = max(reversed(occurrence_dict), key=occurrence_dict.get)
        # Return type dependent on key
        return max_last_value

    # Method to return Values by min count of occurrence
    # Arguments to this method: Multiple dictionaries as arguments (separated by comma)
    # * takes care of the unpacking multiple dictionaries passed as arguments
    def get_vals_by_min_occurence_in_joined_dicts(*_dicts_iterables):
        # Create an empty dictionary
        merged_dicts = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the empty dictionary with keys and Values from unpacked list of dictionaries
            merged_dicts |= _
        # Count the Occurrence of each value in merged dictionary and keep value as key and occurrence count as value            
        occurrence_dict = dict(collections.Counter(merged_dicts.values()))
        # List comprehension to get the list of values with min occurrence in dictionaries
        # Using list comprehension, since their may be mutliple values having same occurence count as min count
        min_value = [k for k, v in occurrence_dict.items() if v == min(occurrence_dict.values())]
        # Return type is a List
        return min_value

    # Method to return Values by max count of occurrence
    # Arguments to this method: Multiple dictionaries as arguments (separated by comma)
    # * takes care of the unpacking multiple dictionaries passed as arguments
    def get_vals_by_max_occurence_in_joined_dicts(*_dicts_iterables):
        # Create an empty dictionary
        merged_dicts = {}
        # Iterate over all the dictionaries in the unpacked list of dictionaries
        for _ in _dicts_iterables:
            # Update the empty dictionary with keys and Values from unpacked list of dictionaries
            merged_dicts |= _
        # Count the Occurrence of each value in merged dictionary and keep value as key and occurrence count as value
        occurrence_dict = dict(collections.Counter(merged_dicts.values()))
        # List comprehension to get the list of values with max occurrence in dictionaries
        # Using list comprehension, since their may be mutliple values having same occurrence count as max count
        max_value = [k for k, v in occurrence_dict.items() if v == max(occurrence_dict.values())]
        # Return type is a List
        return max_value

    # Method to check if a string is a palindrome
    # Argument to this method: string
    def is_str_a_palindrome(_inp_str):
        reversed_string = _inp_str[::-1]
        return True if _inp_str == reversed_string else False

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

    # Method to join multiple lists into one list
    # Argument to this method: Multiple lists as arguments (separated by comma)
    # * takes care of the unpacking multiple lists passed as arguments
    def join_lists(*_lists_iterables):
        # itertools.chain : joins the multiple lists into one
        chained_list = list(itertools.chain(*_lists_iterables))
        # Return type is a list
        return chained_list

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

    # Method to join multiple tuples arguments into one tuple and remove duplicate elements from result tuple
    # Arguments to this method: Multiple tuples as arguments (separated by comma)
    # * takes care of the unpacking multiple tuples passed as arguments
    def merge_tuples(*_tuple_iterables):
        # itertools.chain : joins multiple tuples in to one
        # set : removes the duplicate elements from the result
        joined_tuple = tuple(set(itertools.chain(*_tuple_iterables)))
        # Return type is a tuple
        return joined_tuple

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

    # Method to reverse the string
    # Argument to this method: string
    def reverse_string(_inp_str):
        # Return type is a string
        return _inp_str[::-1]

    # Method to join multiple lists into one list and sum all the digits
    # Argument to this method: Multiple lists as arguments (separated by comma)
    # * takes care of the unpacking multiple lists passed as arguments
    def sum_elems_of_lists(*_inp_list):
        # itertools.chain(*_inp_list) : Joins all the lists into one list
        # Following List comprehension, filters only digits from the input list
        # Return type is an integer
        return sum(_ for _ in itertools.chain(*_inp_list) if str(_).isdigit())

    # Method to get top 5 alphabets based on their occurrences in string
    # Argument to this method: string
    def top_5_elem_occurrences_in_str(_inp_str):
        # We use the 'most_common' method for Counter
        return dict(collections.Counter(_inp_str).most_common(5))
    
    # Method to get top n alphabets based on their occurrences in string
    # Argument to this method: string, and n = Integer
    def top_n_elem_occurrences_in_str(_inp_str, n):
        # We use the 'most_common' method for Counter
        return dict(collections.Counter(_inp_str).most_common(n))