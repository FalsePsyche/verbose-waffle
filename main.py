import nltk
#nltk.download()
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
substring_list = ['shit', 'ass', 'jam', 'base', 'tele']
word_count_thing = 0
word_count_shit = 0
word_count_ass = 0
word_count_jam = 0
word_count_base = 0
word_count_tele = 0

for english_word in english_dict:
	# print(english_word)
		for word in substring_list:
			# print(english_word, word)
			index_found = english_word.find(word)
			if word == english_word or index_found > -1:
				word_count_thing = word_count_thing + 1
				print('match: ', word, english_word)
				if word == 'shit': 
					word_count_shit = word_count_shit + 1
				if word == 'ass':
					word_count_ass = word_count_ass + 1
				if word == 'jam':
					word_count_jam = word_count_jam + 1
				if word == 'base':
					word_count_base = word_count_base + 1
				if word == 'tele':
					word_count_tele = word_count_tele + 1
		# print(word, ' does not match', english_word)
print(word_count_thing)
print()
print('shit: ', word_count_shit)
print('ass: ', word_count_ass)
print('jam: ', word_count_jam)
print('base: ', word_count_base)
print('tele: ', word_count_tele)
assert(word_count_shit + word_count_ass + word_count_jam + word_count_base + word_count_tele == word_count_thing)

# todo count number of matches per word in substring_list
	
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

