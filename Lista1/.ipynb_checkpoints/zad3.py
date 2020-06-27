from collections import OrderedDict

# The fromkeys() method returns a dictionary with the specified keys and the specified value.
# keys	Required. An iterable specifying the keys of the new dictionary
# value	Optional. The value for all keys. Default value is None

def remove_duplicats(list_with_duplicats) :
    return list(OrderedDict.fromkeys(list_with_duplicats))

remove_duplicats([1,1,2,2,2,3,3,5,5,5,4,4,4,0])