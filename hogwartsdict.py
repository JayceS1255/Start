students = {
            'Hermione':'Gryffindor',
            'Harry':'Gryffindor', 
            'Ron':'Gryffindor',
            'Draco':'Slytherin'
           }

for student in students: #shows only the keys!
    print(student)

for student in students: 
    print(student, students[student], sep=", ")