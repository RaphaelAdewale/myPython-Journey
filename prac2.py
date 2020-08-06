students = ["Abdullahui", "Esther", "Sylvester", "Daniel", ["Timilehin", ["Bayo", "Farouk"]]]
def print_lol(students):
	for each_item in students:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			print(each_item)

print_lol(students)


			