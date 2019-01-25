# Make an array for the cleaned lines
cleaned_lines = []

# Open the text file and go through each line
for line in open('lyrics.txt', 'rb'):
	line = line.split('\n')[0].strip()
	# If the line doesn't have html in it or is not empty, add it to the cleaned_lines array
	# Of course, your data might be different! This was just a dataset that included urls and empty lines
	if not 'html' in line and not line == '':
		line = line + '\n'
		cleaned_lines.append(line)

# Open file and write the cleaned output
with open('input.txt', 'w') as f:
    for item in cleaned_lines:
        f.write(item)