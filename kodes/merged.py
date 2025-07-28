def merge_dict(dict1, dict2):
    merged = dict1.copy()
    for key, values in dict2.items():
        if key in merged:
            merged[key] += values
        else:
            merged[key] = values
    return merged
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merged_dict = merge_dict(dict1, dict2)
print(merged_dict)