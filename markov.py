from sys import argv
file = argv[1]

bigram = {}

# open file for reading and assign file contents to variable filetext, return filetext
def open_file(filename):
	text = open(filename)
	filetext = text.read()
	text.close()
	print filetext
	return filetext

# split string filetext into a list, return the list
def split_words(text):
	text = text.split()
	print text
	return text

# create bigram dictionary from words in list
def get_bigram(text):
	count = 0
	while count <= len(text) -3:
		#print "at the top count is %d" % count
		bigram[text[count]+ " " +text[count+1]] = text[count+2]
		#print bigram
		count += 1
		#print "at the bottom count is %d" % count
	print bigram
	return bigram
	# count = 0
	# while count < len(text):
	# 	text = text.replace(" ", "*")
	# 	print text
	# 	count += 2
	# return text


def main():
	words = open_file(file)
	words = split_words(words)
	words_edited = get_bigram(words)

main()

