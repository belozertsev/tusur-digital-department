from pprint import pprint

lst = [
	{
		"surname": "Belozertsev",
		"name": "Eduard",
		"patronymic": "Eduardovich",
		"year": 2001,
		"course": 4,
		"group": "729-1",
		"marks": [5, 5, 5, 5, 4]
	},
	{
		"surname": "Ivanov",
		"name": "Ivan",
		"patronymic": "Ivanovich",
		"year": 1998,
		"course": 6,
		"group": "727-2",
		"marks": [3, 4, 5, 4, 4]
	},
	{
		"surname": "Petrov",
		"name": "Petr",
		"patronymic": "Petrovich",
		"year": 2001,
		"course": 3,
		"group": "740-1",
		"marks": [3, 4, 4, 3, 5]
	},
	{
		"surname": "Sergeev",
		"name": "Sergey",
		"patronymic": "Sergeevich",
		"year": 2001,
		"course": 3,
		"group": "760-1",
		"marks": [4, 5, 5, 3, 5]
	},
	{
		"surname": "Romanov",
		"name": "Roman",
		"patronymic": "Romanovich",
		"year": 2001,
		"course": 3,
		"group": "710",
		"marks": [4, 4, 4, 4, 4]
	},
]

def getStudentsByCourse(students, course):
    
    
	suitableStudents = [student for student in students if student["course"] == course]
	return sorted(suitableStudents, key = lambda st: st["surname"] + st["name"] + st["patronymic"])

def getAvg(students):
    groups = {}
    for st in students:
        current_group = st["group"]
        
        if current_group not in groups:
            groups[current_group] = [st["marks"]]
        else:
            groups[current_group].append(st["marks"])

    for key in groups.keys():
        students_count = len(groups[key])
        avg_scores = [ sum(scores)/students_count for scores in zip(*groups[key]) ]
        groups[key] = avg_scores

    return groups

def getYoungest(students):
    return min(students, key=lambda obj: obj["year"])

def getOldest(students):
    return max(students, key=lambda obj: obj["year"])
    
def getMostSuccessfulOverall(students):
    best_students = {}
    
    for st in students:
        current_group = st["group"]
        if current_group not in best_students:
            best_students[current_group] = [st]
        else:
            best_students[current_group].append(st)

    for key in best_students.keys():
        scores = [sum(obj["marks"]) for obj in best_students[key]]
        max_index = scores.index(max(scores))
        best_st = best_students[key][max_index]
        best_students[key] = best_st

    return best_students

print(" -- getStudentsByCourse --")
pprint(getStudentsByCourse(lst, 3))

print("\n -- getAvg --")
pprint(getAvg(lst))

print("\n -- getYoungest --")
pprint(getYoungest(lst))

print("\n -- getOldest --")
pprint(getOldest(lst))

print("\n -- getMostSuccessfulOverall --")
pprint(getMostSuccessfulOverall(lst))