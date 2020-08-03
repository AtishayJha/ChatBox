class Database:
	def read():
		file = open("Database.txt", "r")
		filelines = file.readlines()
		chatlst = []
		semilst = []
		split = None
		for i in range (int(len(filelines)/2)):	
			semilst.append(filelines[2*i][0:len(filelines[2*i])-1])
			split = filelines[(2*i)+1].split()
			semilst.append(int(split[0]))
			semilst.append(int(split[1]))
			chatlst.append(semilst)
			semilst = []
		return chatlst
		file.close()
	def write(chatlst):
		writelst = []
		file = open("Database.txt", 'w')
		for i in chatlst:
			writelst.append(i[0]+"\n")
			writelst.append(str(i[1])+" "+str(i[2])+"\n")
		file.writelines(writelst)
		file.close()
