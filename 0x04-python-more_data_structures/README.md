				**0x04-python-more_data_structures**

**0-square_matrix_simple.py** - a function that computes the square value of all integers of a matrix.
				Prototype: def square_matrix_simple(matrix=[]):
				matrix is a 2 dimensional array
				Returns a new matrix:
				Same size as 'matrix'
				Each value is the square of the value of the input
				Initial matrix is not modified
				not importing any module
				using regular loops, map, etc.

**1-search_replace.py** - a function that replaces all occurrences of an element by another in a new list.
			Prototype: def search_replace(my_list, search, replace):
			my_list is the initial list
			search is the element to replace in the list
			replace is the new element
			without importing any module

**2-uniq_add.py** -  a function that adds all unique integers in a list (only once for each integer).
			Prototype: def uniq_add(my_list=[]):
			not importing any module

**3-common_elements.py** - a function that returns a set of common elements in two sets.
			Prototype: def common_elements(set_1, set_2):
			without importing any module

**4-only_diff_elements.py** - a function that returns a set of all elements present in only one set.
			Prototype: def only_diff_elements(set_1, set_2):
			without importing any module

**5-number_keys.py** - a function that returns the number of keys in a dictionary.
			Prototype: def number_keys(a_dictionary):
			without importing any module

**6-print_sorted_dictionary.py** - a function that prints a dictionary by ordered keys.
				Prototype: def print_sorted_dictionary(a_dictionary):
				assuming that all keys are strings
				Keys are sorted by alphabetic order
				Only sorting keys of the first level (not sorting keys of a dictionary inside the main dictionary)
				Dictionary values have any type
				without importing any module

**7-update_dictionary.py** - a function that replaces or adds key/value in a dictionary.
				Prototype: def update_dictionary(a_dictionary, key, value):
				key argument is always a string
				value argument is any type
				If a key exists in the dictionary, the value will be replaced
				If a key doesn’t exist in the dictionary, it will be created
				without importing any module

**8-simple_delete.py** - a function that deletes a key in a dictionary.
			Prototype: def simple_delete(a_dictionary, key=""):
			key argument is always a string
			If a key doesn’t exist, the dictionary won’t change
			without importing any module

**9-multiply_by_2.py** - a function that returns a new dictionary with all values multiplied by 2
			Prototype: def multiply_by_2(a_dictionary):
			assuming that all values are only integers
			Returns a new dictionary
			importing any module

**10-best_score.py** - a function that returns a key with the biggest integer value.
			Prototype: def best_score(a_dictionary):
			assuming that all values are only integers
			If no score is found, return None
			assuming all students have a different score
			without importing any module

**11-multiply_list_map.py** - a function that returns a list with all values multiplied by a number without using any loops.
				Prototype: def multiply_list_map(my_list=[], number=0):
				Returns a new list:
					Same length as 'my_list'
					Each value is multiplied by 'number'
				Initial list is not modified
				without importing any module
				using map
				just in 3 lines

**12-roman_to_int.py** - a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.
			assuming the number will be between 1 to 3999.
			def roman_to_int(roman_string) returns an integer
			If the roman_string is not a string or None, return 0
