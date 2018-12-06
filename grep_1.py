import collections
import itertools
import sys

string_to_search=input("Enter the String: ")
with open('my_file.txt') as f:
    before = collections.deque(maxlen=10)
    for line in f:
        if string_to_search in line:
            sys.stdout.writelines(before)
            sys.stdout.write(line)
            sys.stdout.writelines(itertools.islice(f, 10))
            break
        before.append(line)