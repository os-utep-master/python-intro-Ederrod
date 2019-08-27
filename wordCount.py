import os, sys
import re

if len(sys.argv) is not 3: 
    print('''Missing argument!
            Usage: word_counter.py <input file> <output file>''')
    exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    print("Input file does not exist")

word_dict = dict()

input_read = open(input_file, "r")

for line in input_read: 
    line = re.sub('[^A-Za-z0-9]+', ' ', line)
    line = line.split(' ')

    for word in line: 
        word = word.lower()
        if word in word_dict.keys(): 
           word_dict[word] += 1
        else: 
            word_dict[word] = 1

word_dict.pop('') 

output_write = open(output_file, 'w+')

for _ in sorted(word_dict.keys()):
    output_write.write("%s %s\n" % (_, word_dict[_]))