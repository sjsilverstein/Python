students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def nameList1(arr):
	for i in range(0,len(arr)):
		print arr[i]['first_name']+" "+ arr[i]['last_name']
	return True

nameList1(students)

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

def nameList2(arr):
 	for key in arr:
 		print key
 		for i in range (0, len(arr[key])):
 			print str(i+1)+" - "+ arr[key][i]['first_name']+ " " + arr[key][i]['last_name'] + " - " + str(len(arr[key][i]['first_name'])+len(arr[key][i]['last_name']))
 	return True
nameList2(users)