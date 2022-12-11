import os
import operator


files_dict = {}
for filename in os.listdir('sorted'):
    with open(os.path.join('sorted', filename), 'r') as f:
        text = [f.read()]
        string_count = text[0].count('\n') + 1
        text.insert(0, string_count)
        files_dict[filename] = text

with open('file.txt', 'w') as file:
    for keys, values in sorted(files_dict.items(), key=operator.itemgetter(1)):
        file.write(f'{keys} \n')
        file.write(f'{values[0]} \n')
        file.write(f'{values[1]} \n')
