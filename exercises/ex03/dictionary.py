"""Dictionary_exercise"""

__author__ = "730677063"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """dictionary that gets inverted"""
    inverted_dict: dict[str, str] = {}

    for key in dictionary:
        i_d_key = dictionary[key]
        if i_d_key in inverted_dict:
            raise KeyError("i need to put smtg here")
        inverted_dict[i_d_key] = key

    return inverted_dict


def count(freqcount: list[str]) -> dict[str, int]:
    """dictionary where val is associated with the frequency val appeared in list"""
    dict_ionary: dict[str, int] = {}
    number: int = 0
    for item in freqcount:
        if item in dict_ionary:
            number = dict_ionary[item] + 1
        else:
            number = 1
        dict_ionary[item] = number

    return dict_ionary

    # we are converting a dictionarys value to a new dictionarys key value


def favorite_color(name_n_color: dict[str, str]) -> str:
    """dictionary of name n colors and will return favorite color"""
    first_dict: dict[str, int] = {}
    for k, colors in name_n_color.items():
        if colors in first_dict.keys():
            first_dict[colors] += 1
        else:
            first_dict[colors] = 1

    # making the count for the new dictionary
    max = 0
    max_color = ""
    for color, count in first_dict.items():
        if count > max:
            max = count
            max_color = color

    return max_color


def bin_len(list: list[str]) -> dict[int, set[str]]:
    """will bin list of strings into dictionary"""
    product: dict[int, set[str]] = {}
    keey: int = 0
    while keey < len(list):
        if len(list[keey]) in product:
            product[len(list[keey])].add(list[keey])
        else:
            product[len(list[keey])] = set([list[keey]])
        keey += 1

    return product
