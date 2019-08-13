import json

with open("/home/aniket/Projects/Chat_Bot/assignment_1_input_1.json","r") as json_file:
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


for i in ip_data['questions']:
	keys = list(i.keys())

	if 'instruction' in keys:
		print(i['instruction'])

	if 'text' in keys and 'var' in keys and 'conditions' not in keys:
		print('Sarah : ',i['text'])
		if 'options' in keys:
			print('\tSelect one of them : ',i['options'])

		
		value = input('->')
		
		if 'age' in i['var']:
			while(check(value) != True):
				value = input('->')
		

		key = i['var']
		user_input.update({key:value})
	

