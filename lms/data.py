import json

# dictionary = {
#     "name": "Thanh",
#     "rollno": 56,
#     "cgpa": 8.6,
#     "phonenumber": "9976770500"
# }
 
# with open("data.json", "w") as outfile:
#     json.dump(dictionary, outfile)


data = {
'employees' : [
    {
        'name' : 'John Doe',
        'department' : 'Marketing',
        'place' : 'Remote'
    },
    {
        'name' : 'Jane Doe',
        'department' : 'Software Engineering',
        'place' : 'Remote'
    },
    {
        'name' : 'Don Joe',
        'department' : 'Software Engineering',
        'place' : 'Office'
    }
 ]
}

encodedUnicode = json.dumps(unicodeData, ensure_ascii=False)

with open('keys.json', encoding='utf-8') as fh:
    data = json.load(fh)

with open('data.json', 'r') as openfile:
    json_object = json.load(openfile)

    json_object.update(data)


    print(json_object)

with open('data.json', 'w') as outfile:
    json.dump(json_object, outfile, ensure_ascii=False)