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
	while count <= len(text) -3:
		# 
		key_list = (text[count], text[count + 1])
		bigram[key_list] = text[count+2]
		count += 1
	return bigram

# need to define end of sentence as a period
# need to check for duplicate keys and create multiple values for single keys
# function to generate sentences from our dictionary
# gets list of keys, passes that list to generator
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
	# set first sentence based on bigram key and value
	first_sentence = random_bigram, bigram_dict[random_bigram]
	# search for second value of key + value as the next key to add to your sentence
	second_bigram = random_bigram[1], bigram_dict[random_bigram]
	second_sentence = bigram_dict[second_bigram]
	#third_bigram = bigram_dict[bigram_dict[random_bigram]], bigram_dict[bigram_dict[second_bigram]]
	# loop control variable
	count = 0
	while count < 1:
		print first_sentence
		print second_sentence
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
	print bigram_dictionary
	generate_text(bigram_dictionary, words)

main()

