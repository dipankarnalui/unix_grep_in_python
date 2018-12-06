string_to_search=input("Enter the String: ")
before=int(input("How many lines to print before string match ? "))
after=int(input("How many lines to print after string match ? "))
file_to_search=input("Enter the file to search: ")

def search_string(string_to_search, before, after, file_to_search):
	with open(file_to_search) as f:
		all_lines = f.readlines()
		last_line_number=len(all_lines)
		for current_lineno, current_line in enumerate(all_lines):
			if string_to_search in current_line:
				start_line_no = max(current_lineno - before, 0)				
				for i in range(start_line_no, current_lineno):print(all_lines[i])
				if last_line_number < current_lineno+after:
					end_line=last_line_number
				else:
					end_line=current_lineno+after
				for i in range(current_lineno, end_line):print(all_lines[i])
				break
search_string(string_to_search, before, after, file_to_search)

'''
$cat my_file.txt
this is line 1
this is line 2
this is line 3
this is line 4
this is line 5 my pattern is here
this is line 6
this is line 7
this is line 8
this is line 9
this is line 10

$python grep_3.py
Enter the String: my pattern
How many lines to print before string match ? 2
How many lines to print after string match ? 1000
Enter the file to search: my_file.txt
this is line 3

this is line 4

this is line 5 my pattern is here

this is line 6

this is line 7

this is line 8

this is line 9

this is line 10
'''