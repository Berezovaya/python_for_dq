import re
import string

wrong_txt = """homEwork:
tHis iz your homeWork, copy these Text to variable.
You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


def get_last_word(mystr):
    mystr = mystr.lower()
    newstr = []
    for s in mystr.split('.'):
        if len(s)>1:
            newstr.append(s.split()[-1])
    return mystr + ' '.join(newstr) + '.'


def fix_capitalization(mystr):
    mystr = mystr.lower() + ""
    newstr = []
    for s in mystr.split('.'):
        tmp = re.sub('^(\s*\w+)', lambda x: x.group(1).title(), s)
        newstr.append(tmp)
    return '. '.join(newstr).replace(' i ', ' I ').replace(' iz ', ' is ')


def space_counter(txt):
    space_count = 0
    for i in txt:
        if i in string.whitespace:
            space_count += 1
    return space_count


if __name__ == '__main__':
    wrong_txt = get_last_word(wrong_txt)
    proper_txt = fix_capitalization(wrong_txt)
    space_count = space_counter(wrong_txt)

    print(proper_txt)
    print(space_count)
