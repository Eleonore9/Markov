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
		# if the key does not exist, add it and it's value
		if key_list not in bigram:
			bigram[key_list] = value_list
		# if the key does exist, append the new value to existing value
		else:
			value_list.extend(bigram[key_list])
			bigram[key_list] = value_list
		count += 1
	return bigram
	print bigram

def sort_bigram(the_bigram):
	for keys in sorted(the_bigram.iterkeys()):
		print keys, the_bigram[keys]

# need to define end of sentence as a period
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
def generate_sentence(bigram_dict, text):
	# get list of keys
	bigram_keys = bigram_dict.keys()
	# print a random bigram and value for each key in bigram dictionary
	random_bigram = random.choice(bigram_keys)
	value = bigram_dict[random_bigram]
	key = random_bigram[0], random_bigram[1]
	sentence = key[0].capitalize() + " " + key[1]
	counter = 0
	while counter < 1:
		word = value[random.randint(0, len(value)  - 1)]
		if word[-1] in ".?!":
			sentence += " " + word
			#print sentence
			counter +=1
			return sentence
		else:
			
			sentence += " " + word
			key = (key[1], value[random.randint(0, len(value)  - 1)])
			value = bigram_dict[key]
			#print sentence



def generate_text(bigram, sentence):
	paragraph = ""
	counter = 0
	nb_sentences = int(raw_input("enter a number of sentences: "))
	while counter < nb_sentences:
		paragraph += generate_sentence(bigram, sentence) + " "
		counter += 1
	return paragraph

def main():
	words = open_file(file)
	words = split_words(words)
	bigram_dictionary = get_bigram(words)
	sentence = generate_text(bigram_dictionary, words)
	print sentence
	#generate_sentence(bigram_dictionary, words)

main()

