from nltk.corpus import words
import json
import nltk
variable_name_1 = {'variable_a': 2, 'variable_b': 7}
print(variable_name_1)
print(variable_name_1['variable_a'])

# nltk.download()
english_dict = words.words()
print(len(english_dict))
print("find all the words in the dictionary that have swears as substrings")
print("Derek smeels")
print()
# List of words to match
matches = {'shit': [],
           'ass': [],
           'jam': [],
           'base': [],
           'tele': [],
           'damn': [],
           'wack': [],
           'dawg': [],
           'nut': []}
matches['word'] = []
word_count_thing = 0
for english_word in english_dict:
    # print(english_word)
    for word in list(matches.keys()):
        # print(english_word, word)
        index_found = english_word.find(word)
        if word == english_word or index_found > -1:
            word_count_thing = word_count_thing + 1
            # print(matches[word])
            matches[word].append(english_word)
            match_number = 0
print(word_count_thing)
print()
print(list(matches.keys()))
print(json.dumps(matches, indent=4))
for word in list(matches.keys()):
    print(word, len(matches[word]))
assert(word_count_thing == sum([len(value_list)
                                for value_list in list(matches.values())]))
with open('data.json', 'w+') as file:
    file.write(json.dumps(matches, indent=4))
