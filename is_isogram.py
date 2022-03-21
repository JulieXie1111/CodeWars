def is_isogram_1(string):
    """checks if a word is an isogram"""
    # Isograms are words that have no repeating letters.
    string = string.lower()
    some_list = []
    for i in string:
        if string.count(i) != 1:
            return False
        else:
            some_list.append(i)
    if ''.join(some_list) == string:
        return True  # this one takes 4.24 ms to finish


# ----------------------------------------------------------------------------------------------------------------------

def is_isogram_2(string):
    """checks if a word is an isogram"""
    # Isograms are words that have no repeating letters.
    string = string.lower()
    string = list(string)
    tmp = []
    for el in string:
        if el in tmp:
            return False
        elif el not in tmp:
            tmp.append(el)
    if tmp == string:
        return True  # this one takes 3.38 ms to finish


# ----------------------------------------------------------------------------------------------------------------------
def is_isogram_3(string):
    """checks if a word is an isogram"""
    # Isograms are words that have no repeating letters.
    return len(string) == len(set(string.lower()))
