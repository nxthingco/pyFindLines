with open('1.txt','r') as file:
	content_1 = file.read()
	file.close()
with open('2.txt','r') as file:
	content_2 = file.read()
	file.close()
with open('result.txt','w') as out:
	for x in content_1.split(' '):
		print(x)
		for y in content_2.split(' '):
			print(y)
			if x == y:
				out.write(x)