# Given a standard english sentence passed in as a string, write a method that will return a sentence made
# up of the same words, but sorted by their first letter. However, the method of sorting has a twist to it:
# All words that begin with a lower case letter should be at the beginning of the sorted sentence, and sorted
# in ascending order. All words that begin with an upper case letter should come after that, and should be sorted
# in descending order. If a word appears multiple times in the sentence, it should be returned multiple times in
# the sorted sentence. Any punctuation must be discarded.


# def pseudo_sort(st) :
#     upper_list = []
#     lower_list = []
#     new_str = ''
#     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#     no_punc_st = ''
#     for char in st :
#         if char not in punctuations :
#             no_punc_st = no_punc_st + char
#
#     words_list = no_punc_st.split()
#     for word in words_list :
#         if word[0].isupper() :
#             upper_list.append(word)
#         else :
#             lower_list.append(word)
#
#     sorted_lower_cases = sorted(lower_list)
#     sorted_upper_cases = sorted(upper_list, reverse=True)
#
#     for each in sorted_lower_cases :
#         new_str = new_str + each + ' '
#     for each in sorted_upper_cases :
#         new_str = new_str + each + ' '
#
#     new_str = new_str.strip()
#     return new_str

#practice
def pseudo_sort(s) :
    # how join works
    # seperator = '-'
    # sequence = ('a', 'b', 'c')
    # together = seperator.join(sequence)

    print(s)
    print([i for i in s])
    s = ''.join(i for i in s if i.isalpha() or i is ' ')
    print(s)
    words_list = s.split() # split here instead of running it twice in next two lines
    print(words_list)
    a =  sorted(i for i in words_list if i[0].islower())
    b =  sorted((i for i in words_list if i[0].isupper()),reverse=True)

    # !use join instead of all this code below!
    # lower_str = ''
    # for each in a :
    #     lower_str = lower_str + each + ' '
    #
    # upper_str = ''
    # for each in b :
    #     upper_str += each + ' '
    #
    # lower_str.strip()
    # upper_str.strip()
    # return lower_str + upper_str

    return ' '.join(a + b)

# print(pseudo_sort('all THESE are Alphabetic characters'))
# print(pseudo_sort('Aword, Bword, cword, dword!'))
print(pseudo_sort({'one', 'two', 'three'}))
# print(pseudo_sort('I, habitan of the Alleghanies, treating of him as he is in himself in his own rights'))
# print(pseudo_sort("Land of the Old Thirteen! Massachusetts land! land of Vermont and Connecticut!"))
# "as habitan he him himself his in in is of of own rights the treating I Alleghanies"))

import string

print(string.punctuation)
