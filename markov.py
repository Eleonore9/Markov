from sys import argv
import random

file = argv[1]

# open file for reading and assign file contents to variable filetext, return filetext
def open_file(filename):
	text = open(filename)
	filetext = text.read()
	text.close()
	#print filetext
	return filetext

# split string filetext into a list, return the list
def split_words(text):
	text = text.split()
	# print text
	return text

# create bigram dictionary from words in list
def get_bigram(text):
	bigram = {}
	count = 0
	while count <= len(text) -3:
		# 
		key_list = (text[count], text[count + 1])
		bigram[key_list] = text[count+2]
		#bigram[[text[count]+ " " + text[count+1]]] = text[count+2]
		#print bigram
		count += 1
		#print "at the bottom count is %d" % count
	#print bigram
	return bigram
	# count = 0
	# while count < len(text):
	# 	text = text.replace(" ", "*")
	# 	print text
	# 	count += 2
	# return text

# need to define end of sentence as a period
# need to check for duplicate keys and create multiple values for single keys


# function to generate sentences from our dictionary
# gets list of keys, passes that list to generator
def generate_text(bigram_dict):
	bigram_keys = bigram_dict.keys()
	#print bigram_keys
	# print a random bigram and value for each key in bigram dictionary1
		#print random_bigram
	random_bigram = random.choice(bigram_keys)
	# search for second value of key + value as the next key to add to your sentence
	second_bigram = random_bigram[1] , bigram_dict[random_bigram]


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
	for keys in bigram_dict.items():	
		start_sentence = random_bigram
		next_word = bigram_dict[random_bigram]
		print start_sentence, next_word
		print second_bigram
		#if bigram_dict[second] != None:
		if second_bigram in bigram_dict:
			print bigram_dict[second_bigram]
		else:
			print "not found"
		
		second_bigram = second_bigram[1], bigram_dict[second_bigram]

def main():
	words = open_file(file)
	words = split_words(words)
	bigram_dictionary = get_bigram(words)
	generate_text(bigram_dictionary)

main()

