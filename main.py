import nltk
# nltk.download()
from nltk.corpus import words
english_dict = words.words()
print(len(english_dict))
print("find all the words in the dictionary that have swears as substrings")

# shit
# ass
# jam
# base
# tele

print()
# todo put words in list
test_list = ['a', 'b', 'c', 'jammy', 'baseball', 'tel', 'tele']
word_list = ['shit', 'ass', 'jam', 'base', 'tele']

for english_word in english_dict:
  # print(english_word)
  for word in word_list:
    # print(english_word, word)
    index_found = english_word.find(word)
    if word == english_word or index_found > -1:
      print('match: ', word, english_word)
    # else:
      # print(word, ' does not match', english_word)

# todo count number of matches per word in word_list
# todo walk through setup of git repo, then github

# print(word_list)
# for word in word_list:
#   print(word)

# print()

# for index in range(0, len(word_list)):
#   print(index)
#   print(word_list[index])

# print(word_list[4])

# start_index = 0
# current_index = start_index
# max_index = 10
# while (current_index <= max_index):
#   print("hello: ", current_index)
#   current_index = current_index + 1

