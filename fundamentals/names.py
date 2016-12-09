#NAMES

# PartI
students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for i in range(len(students)):
		print students[i].get('first_name'),students[i].get('last_name')

# PartII
users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
 
# print users.keys() //'Students', 'Instructors'
i = 1
for i in range(len(users['Students'])):
	a = users['Students']
	get_first = a[i].get('first_name')
	get_last = a[i].get('last_name')
	print str(i) + ' - ' + get_first+' ' + get_last+ ' - ' + str(len(get_first) + len(get_last))
