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
substring_list = ['shit', 'ass', 'jam', 'base', 'tele', 'damn']
word_count_thing = 0
word_count_shit = 0
word_count_ass = 0
word_count_jam = 0
word_count_base = 0
word_count_tele = 0
word_count_damn = 0

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
					print(match_number)
					if word == match:
						substring_count_list[match_number] +=1 
						print(substring_count_list)
					match_number +=1
					#print('incremented match_number: ', match_number)
						

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
				if word == 'damn':
					word_count_damn = word_count_damn + 1
		# print(word, ' does not match', english_word)
print(word_count_thing)
print()
print('shit: ', word_count_shit)
print('ass: ', word_count_ass)
print('jam: ', word_count_jam)
print('base: ', word_count_base)
print('tele: ', word_count_tele)
print('damn: ', word_count_damn)
assert(word_count_shit + word_count_ass + word_count_jam + word_count_base + word_count_tele + word_count_damn == word_count_thing)

#TODO add item to substring list

print(type(substring_count_list))
print(substring_count_list)
assert(sum(substring_count_list)==word_count_thing)
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

