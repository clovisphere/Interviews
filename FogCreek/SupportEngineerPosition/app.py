#Sort the characters in a string 
#by the number of times the character appear in a given text (descending).
string = 'abcdefghijklmnopqrstuvwxyz_'
# retrieve file content
text = ''
with open('text.txt', 'r') as f:
	for line in f:
		text += line

a_list = {}

for c in string:
	temp = 0
	for letter in text:
		if letter == c:
			temp += 1
	a_list[c] = temp
	
# sorted dict values
values = sorted(a_list.values())
word = '' # will hold the sorted string
for i in values:
	for key, value in a_list.items():
		if i == value:
			word += key	
print('\n>Given string: {} | After sorting: {}\n\n'.format(string, word))
#We then need to drop all characters that appear after (and including) the '_'
#in the sorted string.
print('>Answer: {}\n'.format(word.split('_')[0]))
	

