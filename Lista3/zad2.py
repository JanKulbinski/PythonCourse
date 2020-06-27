def flatten(list_of_elements):
    for element in list_of_elements:
        if isinstance(element, list):
            yield from flatten(element) # yield from g <=> for v in g: yield v
        else:
            yield element

if __name__== "__main__":
    l = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6 ], 7, [[9, [123, [[123]]]], 10]]
    print(list(flatten(l)))
