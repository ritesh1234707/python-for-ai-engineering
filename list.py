# for _ in range(7):
#      print("bark")

# students = ["Luffy", "Eren", "zoro"]

# for student in students: 
#     print(student)

# for i in range(len(students)):
#     print(i+1, students[i])

'''Use of dictonary'''

# students = {
#     "Luffy": "One piece",
#     "Zoro": "One piece",
#     "Eren": "shiganshina",
# }

# print (students["Luffy"])

# students = {
#     "Luffy": "One piece",
#     "Zoro": "One piece",
#     "Eren": "shiganshina",
# }

# for student in students: 
#     print(student, students[student], sep= ", ")

students = [
    {"name": "Luffy", "house": "One piece", "dream": "King"},
    {"name": "Eren", "house": "shiganshina", "dream": "freedon"},
    {"name": "Eren", "house": "shiganshina", "dream": "freedon"},
    {"name": "Eren", "house": "shiganshina", "dream": None},

]

for student in students: 
    print(student["name"], student["house"], student["dream"], sep= ", ")

