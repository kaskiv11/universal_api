def add(a, b):
    return a + b


def is_found_item_of_list(items, item):
    return item in items


def merge_two_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result


def check_positive_number(number):
    if number < 0:
        raise ValueError("The number cannot be negative.")
    return number




