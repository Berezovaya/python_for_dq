import random

if __name__ == '__main__':
    start = 0
    end = 1000
    n = 100
    my_list = [random.randint(start, end) for _ in range(n)]

    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] > my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]

    even_list = [x for x in my_list if x % 2 == 0]
    print(sum(even_list)/len(even_list))

    odd_list = [x for x in my_list if x % 2 != 0]
    print(sum(odd_list)/len(odd_list))