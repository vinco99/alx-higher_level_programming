				**0x03-python-data_structures**

**0-print_list_integer.py** - a function that prints all integers of a list.
				Prototype: def print_list_integer(my_list=[]):
				Format: one integer per line.
				no imported module
				assuming that the list only contains integers
				no integers casted  into strings
				using str.format() to print integers

**1-element_at.py** - a function that retrieves an element from a list like in C.
			Prototype: def element_at(my_list, idx):
			If idx is negative, the function returns None
			If idx is out of range (> of number of element in my_list), the function returns None
			no imported module
			without using try/except

**2-replace_in_list.py** - a function that replaces an element of a list at a specific position (like in C).
			Prototype: def replace_in_list(my_list, idx, element):
			If idx is negative, the function will not modify anything, and returns the original list
			If idx is out of range (> of number of element in my_list), the function will not modify anything, and returns the original list
			without importing any module
			without using try/except

**3-print_reversed_list_integer.py** - a function that prints all integers of a list, in reverse order.
					Prototype: def print_reversed_list_integer(my_list=[]):
					Format: one integer per line. See example
					without importing any module
					assuming that the list only contains integers
					without casting integers into strings
					using str.format() to print integers

**4-new_in_list.py** - a function that replaces an element in a list at a specific position without modifying the original list (like in C).
			Prototype: def new_in_list(my_list, idx, element):
			If idx is negative, the function will return a copy of the original list
			If idx is out of range (> of number of element in my_list), the function will return a copy of the original list
			without importing any module
			without using try/except

**5-no_c.py** - a function that removes all characters c and C from a string.
		Prototype: def no_c(my_string):
		The function will return the new string
		without importing any module
		without using str.replace()

**6-print_matrix_integer.py** - a function that prints a matrix of integers.
				Prototype: def print_matrix_integer(matrix=[[]]):
				without importing any module
				assuming that the list only contains integers
				without casting integers into strings
				using str.format() to print integers

**7-add_tuple.py** - a function that adds 2 tuples.
			Prototype: def add_tuple(tuple_a=(), tuple_b=()):
			Returns a tuple with 2 integers:
				The first element is the addition of the first element of each argument
				The second element is the addition of the second element of each argument
			without importing any module
			assuming that the two tuples will only contain integers
			If a tuple is smaller than 2, using value 0 for each missing integer
			If a tuple is bigger than 2, using only the first 2 integers

**8-multiple_returns.py** - a function that returns a tuple with the length of a string and its first character.
				Prototype: def multiple_returns(sentence):
				If the sentence is empty, the first character is equal to None
				not importing any module

**9-max_integer.py** - a function that finds the biggest integer of a list.
			Prototype: def max_integer(my_list=[]):
			If the list is empty, returns None
			assuming that the list only contains integers
			without importing any module

**10-divisible_by_2.py** - a function that finds all multiples of 2 in a list.
				Prototype: def divisible_by_2(my_list=[]):
				Return a new list with True or False,
				depending on whether the integer at the same position in the original list is a multiple of 2
				The new list have the same size as the original list
				without importing any module

**11-delete_at.py** - a function that deletes the item at a specific position in a list.
			Prototype: def delete_at(my_list=[], idx=0):
			If idx is negative or out of range, nothing change (returns the same list)
			not using pop()
			without importing any module
