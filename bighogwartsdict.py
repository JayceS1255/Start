students = [
    {'name': "Hermione", 'house': 'Gryffindor', 'patronus': 'Otter'},
    {'name': "Harry", 'house': 'Gryffindor', 'patronus': 'Stag'},
    {'name': "Ron", 'house': 'Gryffindor', 'patronus': 'Jack Russel Terrier'},
    {'name': 'Draco', 'house': 'Gryffindor', 'patronus': None}
]#this is a list with dict inside of it, has 3 keys

for student in students:
    print(student["name"])