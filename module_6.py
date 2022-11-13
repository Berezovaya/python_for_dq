import string
import re
import csv


def word_count(str):
    counts = dict()
    words = str.lower()
    words = re.sub('[^a-zA-Z ]+', ' ', words)

    for word in words.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def letter_count(str):
    counts = dict()
    letters = re.sub('[^a-zA-Z]+', '', str)

    for letter in letters:
        low_letter = letter.lower()
        if low_letter in counts:
            counts[low_letter] += 1
        else:
            counts[low_letter] = 1
    return counts


def upper_count(str):
    counts = dict()
    letters = re.sub('[^A-Z]+', '', str)

    for letter in letters:
        low_letter = letter.lower()
        if low_letter in counts:
            counts[low_letter] += 1
        else:
            counts[low_letter] = 1
    return counts


def count_letters_total(str):
    letters = re.sub('[^a-zA-Z]+', '', str)
    return len(letters)


def write_wc(word_cnt):
    with open('wordcount.csv', 'w') as file:
        for key in word_cnt.keys():
            file.write(key)
            file.write('-')
            file.write(str(word_cnt[key]))
            file.write('\n')

def write_lc(letter_cnt, upper_cnt, total_cnt):
    with open('lettercount.csv', 'w', newline='') as csvfile:
        fieldnames = ['letter', 'count_all', 'count_uppercase', 'percentage']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for key in letter_cnt.keys():
            row = {}
            row['letter'] = key
            row['count_all'] = letter_cnt[key]
            if key not in upper_cnt.keys():
                row['count_uppercase'] = 0
            else:
                row['count_uppercase'] = upper_cnt[key]
            row['percentage'] = round(letter_cnt[key] / total_cnt, 2)

            writer.writerow(row)


def update_counts(file):
    lines = file.read()
    word_cnt = word_count(lines)
    write_wc(word_cnt)

    letter_cnt = letter_count(lines)
    upper_cnt = upper_count(lines)
    total_cnt = count_letters_total(lines)
    write_lc(letter_cnt, upper_cnt, total_cnt)


if __name__ == '__main__':
    with open('newsfeed.txt', 'r') as file:
        update_counts(file)

