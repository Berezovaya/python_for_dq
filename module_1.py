import random

if __name__ == '__main__':
    start = 0
    end = 1000
    n = 100

    # create list of 100 random numbers from 0 to 1000
    my_list = [random.randint(start, end) for _ in range(n)]

    # sort list from min to max (without using sort())
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] > my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]

    # calculate average for even and odd numbers
    even_list = [x for x in my_list if x % 2 == 0]
    odd_list = [x for x in my_list if x % 2 != 0]

    # print both average result in console
    print(sum(even_list) / len(even_list))
    print(sum(odd_list)/len(odd_list))
