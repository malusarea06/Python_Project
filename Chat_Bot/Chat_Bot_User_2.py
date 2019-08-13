import json


with open("/home/aniket/Projects/Chat_Bot/assignment_1_input_2.json","r") as json_file:
	ip_data = json.load(json_file)

questions = []
vars = set()

for k in ip_data['questions']:
	keys = list(k.keys())
	if 'var' in keys:
		vars.add(k['var'])
	


user_input = dict.fromkeys(vars)


def check(var):
	if var.isdigit() == False:
		for k in ip_data['questions']:
			keys = list(k.keys())
			if 'conditions' in keys:
				print(k['text'])
				return False
	else:
		return True

matrix=[]
for i in ip_data['questions']:
	key_s = list(i.keys())
	print("\n")
	if 'instruction' in key_s and 'instruction_var' not in key_s: 
		print(i['instruction'])
	if 'instruction_var' in key_s and 'list_length' not in key_s:
		print(i['instruction']%user_input[i['instruction_var'][0]])
	if 'instruction_var' in key_s and 'list_length' in key_s:
		lenw = len(user_input['t_matrix'])
		for j in range(0,lenw):
			print(i['instruction']%(str(j),user_input['t_matrix'][j]))	
	


	if 'text' in key_s and 'var' in key_s and 'conditions' not in key_s:
		print('Sarah : ',i['text'])
		if 'options' in key_s:
			print('\tSelect one of them : ',i['options'])
	
		if 'rows' not in i['var']:
			value = input('->')
		if 'rows' in i['var']:
			value = input('->')
			l = value.split()
			k = i['var']
			matrix.append(l)
			

		


		if 'age' in i['var']:
			while(check(value) != True):
				value = input('->')
		
		key = i['var']
		user_input.update({key:value})
	
	if 'var' in key_s:
		if 'full_name' in i['var']:
			fname = user_input['first_name']
			lname = user_input['last_name']
			user_input.update({'full_name':fname+' '+lname})

		if 'matrix' in i['var']:
			k = i['var']
			user_input.update({k:matrix})		

		if 't_matrix' in i['var']:
			t_m = [[matrix[j][i] for j in range(0,3)] for i in range(0,3)]
			k = i['var']
			user_input.update({k:t_m})

