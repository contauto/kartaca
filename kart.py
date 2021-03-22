import os

var = os.listdir('.\\dosyalar')
ascii_string = ""
liste=[]

for x in var:
	f=open("dosyalar/"+x, "r")
	binary_values = f.read().split()
	liste.extend(binary_values)

for y in liste:
	an_integer = int(y, 2)
	ascii_character=chr(an_integer)
	ascii_string+=ascii_character
print(ascii_string)

dosya=open("./sonuc.txt", "w")
dosya.write(ascii_string)
