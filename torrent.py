# from itertools import count
import os
import re
from time import sleep

filepath = 'data/test.txt'

with open(filepath, encoding='utf-8', errors='ignore') as f:
    full_list = f.read()
    print('Length of list: ', len(full_list.split('\n')))

    pattern = re.compile(r'(Deleting index entry )|( in index \$I30 of file 32A4.)')
    matches = pattern.finditer(full_list)

    pruned_list = re.sub(pattern, '', full_list)
    with open('pruned.txt', 'w', encoding='utf-8') as writer:
        writer.writelines(pruned_list)
