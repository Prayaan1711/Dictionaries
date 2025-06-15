Student_data = {'id1':
    {'name':['Ansh'],
     'grade':['7'],
     'subjects':['English', 'Math', 'Science'] 
     },

     'id2':
        {'name':['Prayaan'],
     'grade':['7'],
     'subjects':['English', 'Math', 'Science'] 
     },

     'id3':
     {'name':['Ansh'],
     'grade':['7'],
     'subjects':['English', 'Math', 'Science'] 
     },

     'id4':
     {'name':['Rohan'],
     'grade':['7'],
     'subjects':['English', 'Math', 'Science'] 
     },
}

result = {}

for key,value in Student_data.items():
    if value not in result.values():
        result[key] = value

print(result)