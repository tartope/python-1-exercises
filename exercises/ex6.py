def slice_it(strings):
    result = ""
    for char in strings:
        result = result + char[:2]
    return result