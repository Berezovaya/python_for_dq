import random
import string


# create a list of random number of dicts (from 2 to 10)
def generate_dicts():
    n = random.randint(2, 10)
    my_list = []

    for _ in range(n):
        tiny_dict = {}
        random_letters = random.sample(string.ascii_lowercase, random.randint(1, 5))
        for random_letter in random_letters:
            tiny_dict[random_letter] = random.randint(0, 100)
        my_list.append(tiny_dict)
    return my_list


def collect_values(list_of_dicts):
    # collect all values per key
    value_collection = {}
    for idx, mini_dict in enumerate(list_of_dicts):
        for key in list(mini_dict.keys()):
            if key not in list(value_collection.keys()):
                value_collection[key] = {idx: mini_dict[key]}
            else:
                value_collection[key][idx] = mini_dict[key]
    return value_collection
# print(value_collection)

def pick_max_values(value_collection):
    # if more than one key pick the biggest and update key name
    result = {}
    for key in value_collection.keys():
        index_values_dict = value_collection[key]
        if len(index_values_dict) == 1:
            result[key] = list(index_values_dict.values())[0]
        else:
            new_key = max(index_values_dict, key=index_values_dict.get)
            max_value = index_values_dict[new_key]
            new_key = f'{key}_{new_key+1}'
            result[new_key] = max_value
    return result


if __name__ == '__main__':
    my_list = generate_dicts()
    print(my_list)
    value_collection = collect_values(my_list)
    result = pick_max_values(value_collection)
    print("result: ", result)

