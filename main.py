import nltk
#nltk.download()
from nltk.corpus import words
english_dict = words.words()
print(len(english_dict))
print("find all the words in the dictionary that have swears as substrings")
print()
# List of words to match
substring_list = ['shit', 'ass', 'jam', 'base', 'tele', 'damn', 'work', 'wack']
word_count_thing = 0
substring_count_list = [0] * len(substring_list)
for english_word in english_dict:
	# print(english_word)
		for word in substring_list:
			# print(english_word, word)
			index_found = english_word.find(word)
			if word == english_word or index_found > -1:
				word_count_thing = word_count_thing + 1
				print('match: ', word, english_word)
				match_number = 0
				for match in substring_list:
					if word == match:
						substring_count_list[match_number] +=1 
					match_number +=1
print(word_count_thing)
print()
print(substring_count_list)
print(substring_list)
assert(sum(substring_count_list)==word_count_thing)