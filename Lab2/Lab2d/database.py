
name1 = raw_input('Write a name?')
age1 = raw_input('Write an age?')
age1 = int(age1)

name2 = raw_input('Write a different name?')
age2= raw_input('Write an age?')
age2 = int(age2)

name3 = raw_input('Write another name?')
age3 = raw_input('Write an age?')
age3 = int(age3)


Dictionary_names = {str(name1)+':'+ str(age1)+ ", " + str(name2) +':'+   str(age2)+ ", " + str(name3)+':'+  str(age3)}

print Dictionary_names
