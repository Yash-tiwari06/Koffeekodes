'''def flattened_list(nested_list):
    flat_list = []
    for slist in nested_list:
        for item in slist:
            flat_list.append(item)
    return flat_list'''

def flatten_nested_list(nested_list):
    flat_list = []
    for slist in nested_list:
        for item in slist:
            flat_list.append(item)
    print(flat_list)
nested=[[1,2],[3,4],[5,6]]
flatten_nested_list(nested)
#nested_list = [1,[2, 3, 4], 7]
#print(flattened_nested_list(nested_list))
#print(result)