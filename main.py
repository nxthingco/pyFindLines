with open('1.txt','r') as file:
	content_1 = file.read()
	file.close()
with open('2.txt','r') as file:
	content_2 = file.read()
	file.close()
with open('result.txt','w') as out:
	for x in content_1.split(' '):
		for y in content_2.split(' '):
			if x == y: out.write(x)
			elif x in y: out.write(y)