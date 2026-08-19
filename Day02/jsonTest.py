import json

student={
    "Name": "Mayur",
    "Age": 21,
    "Courses": ["Python", "Java", "C++"]
}

jsonData= json.dumps(student)
print(jsonData)


# dumps = it converts python object into json string
# loads = it converts json string into python object

jsonString= ' { "Name": "Mayur", "Age": 21} '

pythonObject= json.loads(jsonString)
print(pythonObject)