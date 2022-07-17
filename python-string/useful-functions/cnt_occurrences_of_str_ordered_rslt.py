import collections

# Method to get occurrences of alphabets in string
# Sort the result dictionary by key or value
# Order the dictionary in asc or desc
@staticmethod
# Arguments to this method: string, sorting key and sorting type
def cnt_occurrences_of_str_ordered_rslt(_my_string_1, _sort_key, _sort_type):
    result_set = collections.Counter(_my_string_1)
    if _sort_key == 'k':
        return collections.OrderedDict(sorted(result_set.items(), key=lambda _: _[0], reverse=_sort_type))
    elif _sort_key == 'v':
        return collections.OrderedDict(sorted(result_set.items(), key=lambda _: _[1], reverse=_sort_type))
