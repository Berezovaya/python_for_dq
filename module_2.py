import random
import string

if __name__ == '__main__':
    # create a list of random number of dicts (from 2 to 10)
    n = random.randint(2, 10)
    my_list = []

    for _ in range(n):
        tiny_dict = {}
        random_letters = random.sample(string.ascii_lowercase, random.randint(1, 5))
        for random_letter in random_letters:
            tiny_dict[random_letter] = random.randint(0, 100)
        my_list.append(tiny_dict)

    print(my_list)

    # collect all values per key
    value_collection = {}
    for idx, mini_dict in enumerate(my_list):
        for key in list(mini_dict.keys()):
            if key not in list(value_collection.keys()):
                value_collection[key] = {idx: mini_dict[key]}
            else:
                value_collection[key][idx] = mini_dict[key]
    # print(value_collection)

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

    print("result: ", result)

