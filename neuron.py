import random

class Neuron:
	
	def __init__(self, iloscWejsc, liczbaEpok, tryb, id):
		self.wspUczenia = 0.1 # od 0.1 do 0.7 
		self.spadekWspUczenia = (self.wspUczenia / liczbaEpok) / 2
		self.y = 0
		self.wagi = []
		self.id = id
		if tryb == 0:
			for i in range(iloscWejsc):
				self.wagi.append(random.uniform(-0.9, 0.9))
		else:
			inputFile = open("wagi/wagiNeuronu"+str(id)+".txt", "r")
			line =" "
			while line != "":
				line = inputFile.readline()
				if line =="": break
				#print(line)
				line2=line.replace("\n","")
				line = line2.replace(",",".")
				line2=line.replace("[","")
				line = line2.replace("]","")
				w = float(line)
				self.wagi.append(w)
			inputFile.close()
			
	def obliczWyjscie(self, x):
		self.y = 0
		for i in range(len(self.wagi)):
			self.y = self.y + x[i]*self.wagi[i]
	
	def getWyjscie(self):
		return float(self.y)
		
	def modyfikujWage(self, x):
		for i in range(len(self.wagi)):
			wp = self.wagi[i] + (self.wspUczenia*(x[i] - self.wagi[i]))#tadeusiewicz s 38
			self.wagi[i] = wp
		
		self.wspUczenia = self.wspUczenia - self.spadekWspUczenia 
		#print(self.wspUczenia)
	
	def zapiszWagi(self):
		out = open("wagi/wagiNeuronu"+str(self.id)+".txt","w")
		for i in range(len(self.wagi)):
			#print((self.wagi[i]))
			out.write(str(self.wagi[i])+"\n")
		out.close()
		
	def wczytajWagi(self):
		inputFile = open("wagi/wagiNeuronu"+str(self.id)+".txt", "r")
		while line != "":
			line = inputFile.readline()
			if line =="": break
			#print(line)
			line2=line.replace("\n","")
			line = line2.replace(",",".")
			line2=line.replace("[","")
			line = line2.replace("]","")
			w = float(line)
			self.wagi.append(w)
		
	def print_info(self):
		print(self.y, len(self.wagi), self.wagi[5])
		
	
