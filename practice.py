Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 18 2019, 23:46:00) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> students = ["Abdullahi", "Raphael", "Bose", "Esther"]
>>> print students
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(students)?
>>> print(students)
['Abdullahi', 'Raphael', 'Bose', 'Esther']
>>> print(students[1])
Raphael
>>> students = ["Abdullahi",2004, "Raphael",2005, "Bose",2006, "Esther"]
>>> print(students)
['Abdullahi', 2004, 'Raphael', 2005, 'Bose', 2006, 'Esther']
>>> print(students [1])
2004
>>> students.insert (1, "Felix")
>>> print(students)
['Abdullahi', 'Felix', 2004, 'Raphael', 2005, 'Bose', 2006, 'Esther']
>>> for 2004 in students:
	print(2004)
	
SyntaxError: can't assign to literal
>>> for 2004 in (students):
	print(2004)
	
SyntaxError: can't assign to literal
>>> for "Felix" in (students):
	print(2004)
	
SyntaxError: can't assign to literal
>>> for "Felix" in (students):
	print(Felix)
	
SyntaxError: can't assign to literal
>>> for Felix in students:
	print(Felix)

	
Abdullahi
Felix
2004
Raphael
2005
Bose
2006
Esther
>>> count = 0
>>> while count < len (students):
	print(movies[count])
	count = count+1

	
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    print(movies[count])
NameError: name 'movies' is not defined
>>> while count < len (students):
	print(students[count])
	count = count+1

	
Abdullahi
Felix
2004
Raphael
2005
Bose
2006
Esther
>>> print(students)
['Abdullahi', 'Felix', 2004, 'Raphael', 2005, 'Bose', 2006, 'Esther']
>>> students = ["Abdullahi",2004, "Raphael",2005, ["Mohammed", 21, "Bashiru"] ["Bose",2006, "Esther"]]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    students = ["Abdullahi",2004, "Raphael",2005, ["Mohammed", 21, "Bashiru"] ["Bose",2006, "Esther"]]
TypeError: list indices must be integers or slices, not tuple
>>> students = ["Abdullahi",2004, "Raphael",2005, ["Mohammed", 21, "Bashiru"], ["Bose",2006, "Esther"]]
>>> print(students)
['Abdullahi', 2004, 'Raphael', 2005, ['Mohammed', 21, 'Bashiru'], ['Bose', 2006, 'Esther']]
>>> for each_item in students:
	print(each_item)

	
Abdullahi
2004
Raphael
2005
['Mohammed', 21, 'Bashiru']
['Bose', 2006, 'Esther']
>>> if 42 > 40:
	print(students)
	else:
		
SyntaxError: invalid syntax
>>> if 42 > 40:
	print(students)

	
['Abdullahi', 2004, 'Raphael', 2005, ['Mohammed', 21, 'Bashiru'], ['Bose', 2006, 'Esther']]
>>> if 42 < 40:
	print(students)

	
>>> if 42 < 40:
	print(students)
	else print(students)
	
SyntaxError: invalid syntax
>>> if 42 < 40:
	print(students)
	else print(len(students))
	
SyntaxError: invalid syntax
>>> if 42 < 40:
	print(students)
	else: print(len(students))
	
SyntaxError: invalid syntax
>>> if 42 < 40:
	print(students)
	else: print(len[students])
	
SyntaxError: invalid syntax
>>> if 42 < 40:
	print(students)
	else: print[len(students)]
	
SyntaxError: invalid syntax
>>> if 42 < 40:
	print(students)
	else: len(students)
	
SyntaxError: invalid syntax
>>> if 42 < 40:
	print(students)
	else:len(students)
	
SyntaxError: invalid syntax
>>> staff = ["Akin", "Adewale"]
>>> isinstance(names, list)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    isinstance(names, list)
NameError: name 'names' is not defined
>>> isinstance(staff, list)
True
>>> num_staff = len(staff)
>>> isinstance(num_staff, list)
False
>>> staff.append("Flora")
>>> print(staff)
['Akin', 'Adewale', 'Flora']
>>> print(num_staff)
2
>>> len(staff)
3
>>> num_staff = len(staff)
>>> print(num_staff)
3
>>> print(students)
['Abdullahi', 2004, 'Raphael', 2005, ['Mohammed', 21, 'Bashiru'], ['Bose', 2006, 'Esther']]
>>> for each_item in students:
	print(each_item, [4])

	
Abdullahi [4]
2004 [4]
Raphael [4]
2005 [4]
['Mohammed', 21, 'Bashiru'] [4]
['Bose', 2006, 'Esther'] [4]
>>> for each_item in students:
	print(each_item, 4)

	
Abdullahi 4
2004 4
Raphael 4
2005 4
['Mohammed', 21, 'Bashiru'] 4
['Bose', 2006, 'Esther'] 4
>>> isinstance(student,list)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    isinstance(student,list)
NameError: name 'student' is not defined
>>> isinstance(student, list)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    isinstance(student, list)
NameError: name 'student' is not defined
>>> isinstance(students, list)
True
>>> if 42 > 40:
	print(student, 4)

	
Traceback (most recent call last):
  File "<pyshell#70>", line 2, in <module>
    print(student, 4)
NameError: name 'student' is not defined
>>> if 42 > 40:
	print(student, [4])

	
Traceback (most recent call last):
  File "<pyshell#72>", line 2, in <module>
    print(student, [4])
NameError: name 'student' is not defined
>>> print([4], students)
[4] ['Abdullahi', 2004, 'Raphael', 2005, ['Mohammed', 21, 'Bashiru'], ['Bose', 2006, 'Esther']]
>>> print(students, [4])
['Abdullahi', 2004, 'Raphael', 2005, ['Mohammed', 21, 'Bashiru'], ['Bose', 2006, 'Esther']] [4]
>>> print([4])
[4]
>>> print(4)
4
>>> 
>>> print(nested-item)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print(nested-item)
NameError: name 'nested' is not defined
>>> print(nested_item)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    print(nested_item)
NameError: name 'nested_item' is not defined
>>> for each_item in students:
	print(each_item)

	
Abdullahi
2004
Raphael
2005
['Mohammed', 21, 'Bashiru']
['Bose', 2006, 'Esther']
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in each_item:
			print (nested_item)
	else:
		print(each_item)

		
Abdullahi
2004
Raphael
2005
Mohammed
21
Bashiru
Bose
2006
Esther
>>> print(students)
['Abdullahi', 2004, 'Raphael', 2005, ['Mohammed', 21, 'Bashiru'], ['Bose', 2006, 'Esther']]
>>> isinstance(each_item, list)
True
>>> isinstance(students, list)
True
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in each_item:
			print (nested_item)

			
Mohammed
21
Bashiru
Bose
2006
Esther
>>> print(stuents)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    print(stuents)
NameError: name 'stuents' is not defined
>>> print(students)
['Abdullahi', 2004, 'Raphael', 2005, ['Mohammed', 21, 'Bashiru'], ['Bose', 2006, 'Esther']]
>>> students = ['Abdullahi', 2004, 'Raphael', 2005, ['Mohammed', 21, 'Bashiru', ['Bose', 2006, 'Esther']]]
>>> print(students)
['Abdullahi', 2004, 'Raphael', 2005, ['Mohammed', 21, 'Bashiru', ['Bose', 2006, 'Esther']]]
>>> for each_item in students:
	print(each_item)

	
Abdullahi
2004
Raphael
2005
['Mohammed', 21, 'Bashiru', ['Bose', 2006, 'Esther']]
>>> for each_item in students:
	if isinstance(each_item, list)
	
SyntaxError: invalid syntax
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in each_item:
			print(nested_item)
	else:
		print(each_item)

		
Abdullahi
2004
Raphael
2005
Mohammed
21
Bashiru
['Bose', 2006, 'Esther']
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if instance(nested_item, list):
				for deeper_item in nested_item:
					print(deeper_item)
			else:
				print(nested_item)
	else:
		print(each_item)
	else:
		print(each_item)
		
SyntaxError: invalid syntax
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if instance(nested_item, list):
				for deeper_item in nested_item:
					print(deeper_item)
			else:
				print(nested_item)
	else:
		print(each_item)

		
Abdullahi
2004
Raphael
2005
Traceback (most recent call last):
  File "<pyshell#111>", line 4, in <module>
    if instance(nested_item, list):
NameError: name 'instance' is not defined
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if isinstance(nested_item, list):
				for deeper_item in nested_item:
					print(deeper_item)
			else:
				print(nested_item)
	else:
		print(each_item)

		
Abdullahi
2004
Raphael
2005
Mohammed
21
Bashiru
Bose
2006
Esther
>>> for each_item in students:
	if isinstance(each_item, list):
		print(each_item)

		
['Mohammed', 21, 'Bashiru', ['Bose', 2006, 'Esther']]
>>> for each_item in students:
	if isinstance(each_item, list):
		print(each_item)
	else:
		print(student)

		
Traceback (most recent call last):
  File "<pyshell#122>", line 5, in <module>
    print(student)
NameError: name 'student' is not defined
>>> for each_item in students:
	if isinstance(each_item, list):
		print(each_item)
	else:
		print(each_item)

		
Abdullahi
2004
Raphael
2005
['Mohammed', 21, 'Bashiru', ['Bose', 2006, 'Esther']]
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if isinstance(nested_item, list):
				for deeper_item in nested_item:
					if isinstance(deeper_item, list)
					
SyntaxError: invalid syntax
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if isinstance(nested_item, list):
				for deeper_item in nested_item:
					if isinstance(deeper_item, list):
			else:
				
SyntaxError: expected an indented block
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if isinstance(nested_item, list):
				for deeper_item in nested_item:
					if isinstance(deeper_item, list):
				else:
					
SyntaxError: expected an indented block
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if isinstance(nested_item, list):
				for deeper_item in nested_item:
					print(deeper_item)
			else:
				print(nested_item)
	else:
		print(each_item)

		
Abdullahi
2004
Raphael
2005
Mohammed
21
Bashiru
Bose
2006
Esther
>>> for each_item in students:
	if isinstance(each_item, list)
	
SyntaxError: invalid syntax
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in students
		
SyntaxError: invalid syntax
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in students:
			if isinstance(nested_item, list)
			
SyntaxError: invalid syntax
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if isinstance(nested_item, list):
				for deeper_item in nested_item
				
SyntaxError: invalid syntax
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if isinstance(nested_item, list):
				for deeper_item in nested_item:
					print(deeper_item)
			else:
				print(each_item)

		
['Mohammed', 21, 'Bashiru', ['Bose', 2006, 'Esther']]
['Mohammed', 21, 'Bashiru', ['Bose', 2006, 'Esther']]
['Mohammed', 21, 'Bashiru', ['Bose', 2006, 'Esther']]
Bose
2006
Esther
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if isinstance(nested_item, list):
				for deeper_item in nested_item:
					print(deeper_item)
			else:
				print(each_item)

				
['Mohammed', 21, 'Bashiru', ['Bose', 2006, 'Esther']]
['Mohammed', 21, 'Bashiru', ['Bose', 2006, 'Esther']]
['Mohammed', 21, 'Bashiru', ['Bose', 2006, 'Esther']]
Bose
2006
Esther
>>> for each_item in students:
	if isinstance(each_item, list):
		for nested_item in each_item:
			if isinstance(nested_item, list):
				for deeper_item in nested_item:
					print(deeper_item)
			else:
				print(nested_item)
	else:
		print(each_item)

		
Abdullahi
2004
Raphael
2005
Mohammed
21
Bashiru
Bose
2006
Esther
>>> print(students)

                
