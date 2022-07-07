num=str(input("Digite um numero: "))
def isphonenumber(number):
	if len(number) !=12:
		return False
	if number[:3].isdecimal() and number[3]=="-" and number[4:7].isdecimal() and number[7]=="-" and number[8:13].isdecimal():
		return True
for i in range(len(num)):
	chunk=num[i:i+12]
	print(chunk)
	if isphonenumber(chunk):
		print("Number: ", chunk)
#	else:
			#print("nenhum numero found")
		