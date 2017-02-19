import string

def transform_text(word):
	"""Transform the given string/word.

	Keyword arguments:
	word -- word to transform

	Returns: str

	"""
	alphabet = string.ascii_lowercase # get all aphabet letters (ascending order)
	return word.translate(str.maketrans(alphabet, alphabet[::-1])) 

# for testing purposes
if __name__ == '__main__':
	word = 'abcd'
	print('\'{}\' is now: \'{}\''.format(word, transform_text(word)))
