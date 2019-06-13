cmd=input("Enter command(only Cat)--->")
cd=cmd.split()

if cd[0]=='cat':
	if cd[1]=='-A' or cd[1]=='-E':
		f=open(cd[2],'r+')
		data=f.read().splitlines()
		f.close()
		for i in data:
			print(i+'$')
	elif cd[1]=='-n':
		f=open(cd[2],'r+')
		data=f.read().splitlines()
		f.close()
		n=1
		for i in data:
			print(n,i)
			n=n+1
	elif cd[1]=='--help':
		print('''Usage: cat [OPTION]... [FILE]...
                         Concatenate FILE(s) to standard output.

                         With no FILE, or when FILE is -, read standard input.

                         -A, --show-all           equivalent to -vET
                         -E, --show-ends          display $ at end of each line
                         -n, --number             number all output lines
                         >>,--Apend               append the data
                         --help     display this help and exit''')
	elif cd[1]=='>>':
		f=open(cd[2],'a+')
		data=[] 
		i=''
		while i !='exit':
			data.append(i+'\n')
			i=input()
		for i in data:
			f.write(i)
		f.close()				
	else:
		f=open(cd[1],'r')
		print(f.read())
		f.close()
else:
	print("bash:Command Not Found")
