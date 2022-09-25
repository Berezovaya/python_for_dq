import re
import string

wrong_txt = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

def fix_capitalization(mystr):
    mystr = mystr.lower() + ""
    newstr = []
    for s in mystr.split('.'):
        tmp = re.sub('^(\s*\w+)', lambda x:x.group(1).title(), s)
        newstr.append(tmp)
    return '. '.join(newstr).replace(' i ', ' I ').replace(' iz ', ' is ')

proper_txt = fix_capitalization(wrong_txt)

space_count = 0
for i in proper_txt:
    if i in string.whitespace:
        space_count += 1

print(proper_txt)
print(space_count)