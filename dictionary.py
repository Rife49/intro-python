# Dictionary store data in Key: Value pairs
# written with curly brackets {}

student = {
    "name": "Leo",
    "age": 23,
    "major": "Computer Science"
}
print(student)

# Accessing Items
print(student["name"]) # access by key
print(student.get("major"))

# Adding new items
student["graduation_year"] = 2026
print(student)

# Changing values
student["age"] = 20
print(student)

# Removing items
student.pop("major") # removes key value "key"
print(student)

# Check to see if key exists
if "name" in student:
    print("key, 'name' exists in the dictionary")
    
    # Nested dictionary
    studentss = {
        "student1": {"name": "loe", "age": 22},
        "student2": {"name": "josh", "age": 24}
        }
    print(studentss)
    print(studentss["student2"]["age"])

print("____________________") 


report_card = {
    "name": "Rife",
    "subject": "Full Stack" ,
    "grade": (90, 85, 88)
}
print("Student", report_card["name"])
print("Student", report_card["subject"])

Average = sum(report_card["grade"])/ len(report_card["grade"])

# Average = int(input("calculate results"))

if  Average >= 90:
    print("Excellent")
elif  Average >= 70 and 89:
    print("Good Job!")
else:
    print("Needs Improvement!")
    
report_card.pop("subject")
print(report_card)





print("---------------------")
# Homework
work = {
    "name": "Rife",
    "job": "Full Stack",
    "skill": "Fast Talker",
}
print(work)

work ["title"] = "Grunt"
print(work)

work.pop("title") 
print(work)

