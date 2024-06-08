students = {
    "classA" : [
        {"name": "三苫", "height": 170}, 
        {"name": "伊東", "height": 165}, 
        {"name": "久保", "height": 168}, 
    ],
    "classB" : [
        {"name": "遠藤", "height": 175}, 
        {"name": "南野", "height": 163}, 
        {"name": "田中", "height": 162}, 
    ]
}

for class_name, students_list in students.items():
    # print(class_name, students_list)
    for student in students_list:
        print(f"名前: {student["name"]}, 身長: {student["height"]}")