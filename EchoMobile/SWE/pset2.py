def split_word_on_size(word, size):
	"""Creates/form sub-string from a given string/word based on given size.

	Keyword arguments:
	word -- word to split
	size -- max size/length to use when splitting

	Returns: list

	"""
	result = []

	while len(word) != 0:
		temp = word[:size]
		# add temp to result
		result.append(temp)
		# re-create word based on temp
		word = word[len(temp):]
	return result

# for testing purposes
if __name__ == '__main__':
	word = "This is a test"
	print('>: {}'.format(split_word_on_size(word)))