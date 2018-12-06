import re
string_to_search=input("Enter the string: ")
regex='((?:.*\n){5})' + string_to_search
with open("my_file.txt") as f:
	lines=f.readlines()
	for line in lines:
		found_line=re.findall(regex,line)
		print(found_line)