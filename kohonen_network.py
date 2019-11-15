from PIL import Image
from numpy import array
from neuron import Neuron
import random  
import sys

_LEARN_ = 0
_TEST_ = 1
_RELEARN_ = 2

_NUMBER_OF_WEIGHTS_ = 10000

MODE = _TEST_

DEBUG = 1

number_of_images = 0
number_of_neurons = 0
age_of_learning = 5

max =- 1000000
MIN = -9999999

list_of_neurons = []
list_of_images = []

winner_images_id =[]
winner_neurons_id = []


def print_usage():
	print("USAGE: python neraul_network.py [MODE] [NUMBER_OF_IMAGES]")
	print("\t[MODE] {LEARN | TEST | RELEARN}")
	print("\tNUMBER_OF_IMAGES number of image to learn or classification")
	sys.exit(1)

def check_parameters():
	if len(sys.argv) != 3:
		print_usage()
		
	if (sys.argv[1] == "LEARN"):
		MODE = _LEARN_
	elif (sys.argv[1] == "TEST"):
		MODE = _TEST_
	elif (sys.argv[1] == "RELEARN"):
		MODE = _RELEARN_
	else:
		print("Wrong parameter !")
		print_usage()

	liczbaObrazow = sys.argv[2]
	if (liczbaObrazow.isdigit() == False):
		print("Input number, as a number of image, not a string !")
		sys.exit(1)
	if (int(liczbaObrazow) > 50):
		print("In test just 50 images")
		sys.exit(1)
	liczbaNeuronow = int(liczbaObrazow) + int(int(liczbaObrazow) / 5)
	
	return MODE, int(liczbaObrazow), liczbaNeuronow

def create_neurons(numOfNeurons, ageOfLearning):
	Neurons = []
	for i in range(numOfNeurons):
		neuron = Neuron(10000, ageOfLearning, MODE, i)
		Neurons.append(neuron)
	return Neurons

def read_images(numOfImages):
	images = []
	for i in range(numOfImages):
		img = Image.open(str(i + 1)+".png")
		arr = array(img)
		x = arr.reshape(len(arr)*len(arr),1)		
		images.append(x)
	return images

def getWinners(matrix, winImageId, winNeuronId):
	Obr=0
	Neu=0
	max =- 10000
	for o in range(len(list_of_images)):
		if o not in winImageId:
			for n in range(len(list_of_neurons)):
				if n not in winNeuronId:
					elem = matrix[o][n]
					#print("elem[",o,"][",n,"]=",elem)	
					if elem > max:
						max = elem 
						Obr = o
						Neu = n
			#print("\n")
		#matrix[Obr][Neu] = 
	print("winner to elem[obr=",Obr,"][neuron=",Neu,"]=",max)	
	return Obr, Neu		

(MODE, number_of_images, number_of_neurons ) = check_parameters()

list_of_neurons = create_neurons(number_of_neurons, age_of_learning)
list_of_images = read_images(number_of_images)

if (DEBUG == 1):
	print(MODE, number_of_images, number_of_neurons )

if (DEBUG == 1):
	print("number of loaded images = "+str(len(list_of_images)))
	print("Number of created neurons = "+str(len(list_of_neurons)))
	print("Simple info about neurons: ")
	print("(y, num of weights, value of 5th wieght)")

	for neuron in list_of_neurons:
		neuron.print_info()

#time to show all images to all neurons and get the winners 
matrix = [] 


if MODE == _LEARN_:
	for image in list_of_images:
		neurons_stimulations = []
		#show image to all neurons and save their stimulation 
		for neuron in list_of_neurons:
			neuron.obliczWyjscie(image)
			neurons_stimulations.append(neuron.getWyjscie())
		matrix.append(neurons_stimulations)

	#time to get winners :) 
	#from matrix we will get next biggest stimulation 
	#winners takes all

	for i in range(number_of_images):
		image_id, neuron_id = getWinners(matrix, winner_images_id, winner_neurons_id)
		for j in range(number_of_images):
			matrix[j][neuron_id] = MIN
		winner_images_id.append(image_id)
		winner_neurons_id.append(neuron_id)
		
	#print and save id images with their winners - neurons id
	winners_matrix_file = open("winners_matrix.txt","w")	
	
	print("(image id, neuron id)")
	for i in range(len(winner_images_id)):
		print(winner_images_id[i], winner_neurons_id[i])
		winners_matrix_file.write(str(winner_images_id[i])+", "+str(winner_neurons_id[i])+"\n")
	winners_matrix_file.close()

if MODE != _LEARN_:
	#getting winners_matrix
	print("getting winners matrix from file")
	winners_matrix_file = open("winners_matrix.txt", "r")
	
	line =" "
	while line != "":
		line = winners_matrix_file.readline()
		if line =="": break
		line = line.replace('\n', '')
		line = line.split(", ")
		winner_images_id.append(int(line[0]))
		winner_neurons_id.append(int(line[1]))
	winners_matrix_file.close()
	for i in range(len(winner_images_id)):
		print(winner_images_id[i], winner_neurons_id[i])
	







