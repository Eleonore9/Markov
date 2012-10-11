from sys import argv
import random

file = argv[1]

# open file for reading and assign file contents to variable filetext, return filetext
def open_file(filename):
	text = open(filename)
	filetext = text.read()
	text.close()
	return filetext

# split string filetext into a list, return the list
def split_words(text):
	text = text.split()
	return text

# create bigram dictionary from words in list, return bigram dictionary
def get_bigram(text):
	bigram = {}
	count = 0
	# loop through the text and make key pairs, assign values
	while count <= len(text) - 3:
		key_list = (text[count], text[count + 1])
		value_list = [text[count + 2]]
		#print value_list
		# if the key does not exist, add it and it's value
		if key_list not in bigram:
			#print "1"
			bigram[key_list] = value_list
			#print bigram[key_list]
		# if the key does exist, append the new value to existing value
		else:
			#print "2"
			#print key_list
			#print bigram[key_list]
			value_list.append(bigram[key_list])
			bigram[key_list] = value_list
			#print key_list
			#print bigram[key_list]
		count += 1
	return bigram
	print bigram

def sort_bigram(the_bigram):
	for keys in sorted(the_bigram.iterkeys()):
		print keys, the_bigram[keys]

# need to define end of sentence as a period
# function to generate sentences from our dictionary
''' 
for random value, get the key. To get the next key, take the 2nd element of the key
and the value of that key. Use that key pair to lookup the next value. Rough idea:

		random => value
		(a, b) =>  (c)
		new_key => new_value
		(b, c)	=> (d)
		another_new_key => another_new_value
		(c, d) = (e)

A while loop may be more suitable for this operation. Also needed: how do we stop the loop?
'''	
def generate_text(bigram_dict, text):
	# get list of keys
	bigram_keys = bigram_dict.keys()
	# print a random bigram and value for each key in bigram dictionary
	random_bigram = random.choice(bigram_keys)
	value = bigram_dict[random_bigram]
	key = random_bigram[0], random_bigram[1]
	first_sentence = key[0] + " " + key[1] + " " + value[0]
	# set first sentence based on bigram key and value
	#first_sentence = random_bigram[0], random_bigram[1], bigram_dict[random_bigram]
	# search for second value of key + value as the next key to add to your sentence
	second_bigram = key[1] + " " + value[0]
	second_sentence = bigram_dict[key[1], value[0]]
	#third_bigram = second_bigram[1], bigram_dict[second_bigram]
	#fourth_bigram = third_bigram[1], bigram_dict[third_bigram]

	#second_sentence = bigram_dict[second_bigram]
	#third_bigram = bigram_dict[bigram_dict[random_bigram]], bigram_dict[bigram_dict[second_bigram]]
	# loop control variable
	count = 0
	while count < 1:
		print first_sentence
		#print second_bigram
		print second_sentence[0]
		#print third_bigram
		#print fourth_bigram
		#print second_sentence
		#new_text += random_bigram[0] + " " + random_bigram[1] + " " + bigram_dict[random_bigram[0]] + " " + bigram_dict[random_bigram[1]] + " " + bigram_dict[second_bigram]
		#print new_text
		count += 1

	# for keys in bigram_dict.items():	
	# 	start_sentence = random_bigram
	# 	next_word = bigram_dict[random_bigram]
	# 	print start_sentence, next_word
	# 	print second_bigram
	# 	#if bigram_dict[second] != None:
	# 	if second_bigram in bigram_dict:
	# 		print bigram_dict[second_bigram]
	# 	else:
	# 		print "not found"
		
		#second_bigram = second_bigram[1], bigram_dict[second_bigram]

def main():
	words = open_file(file)
	words = split_words(words)
	bigram_dictionary = get_bigram(words)
	#print bigram_dictionary["of", "her"]
	#sort_bigram(bigram_dictionary)
	generate_text(bigram_dictionary, words)

main()

