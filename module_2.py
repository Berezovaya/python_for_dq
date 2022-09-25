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
    result = {}

    for idx, mini_dict in enumerate(my_list):
        key = list(mini_dict.keys())[0]

        if key not in list(result.keys()):
            result[key] = mini_dict[key]
        else:
            val = result[key]
            val_i = mini_dict[key]

            if val_i>val:
                new_key = f"{key}_{idx}"
                result.pop(key)
                result[new_key] = val_i

    print("result: ",result)

