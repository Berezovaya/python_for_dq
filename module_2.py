import random
import string

if __name__ == '__main__':
    n = random.randint(2, 10)
    my_list = []
    for _ in range(n):
        random_letter = random.choice(string.ascii_letters).lower()
        random_int = random.randint(0, 100)
        my_list.append({random_letter: random_int})

    print(my_list)

    value_collection = {}
    result = {}
    for idx, mini_dict in enumerate(my_list):
        key = list(mini_dict.keys())[0]
        if key not in value_collection:
            value_collection[key] = [mini_dict[key]]
        else:
            value_collection[key].append(mini_dict[key])

    for key in value_collection.keys():
        if len(value_collection[key]) == 1:
            result[key] = value_collection[key][0]
        else:
            max_value = max(value_collection[key])
            new_key = my_list.index({key:max_value})
            new_key = f'{key}_{new_key+1}'
            result[new_key] = max_value

    print("result: ", result)

