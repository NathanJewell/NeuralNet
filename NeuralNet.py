



def genWeight():
	return random()

class Neuron:
	'Building block for layers'

	def __init__(self, iw, idw, iv, idv, ie, ibw, ibv):
		self.weight = iw
		self.deltaWeight = idw
		self.value = iv
		self.desiredValue = idv
		self.error = ie
		self.biasWeight = ibw
		self.biasValue = ibv

	weight = 0;			#nueron importance in network
	deltaWeight = 0;	#difference in weight since last iteration
	value = 0;			#sum of parents
	desiredValue = 0;	#expected value based on data input
	error = 0;			#difference between output value and desired
#	biasWeight = 0;		#importance of bias
#	biasValue = 0;		#bias amount

class Layer:
	neurons = []

	def __init__(self, size, bias = True):
		neurons = [Neuron() for i in range(size)]
		if bias:
			nuerons.append(Nueron())

	def feedForward(self, parent):
		print("fed")

	def randomizeWeights(self):
		for n in neurons:
			n.weight = genWeight()

class Topology:
	layers = []		#ordered list of number of neurons in each layer
	bias = True

	def setData(self, ilayers, ibias):
		layers = ilayers	
		bias = ibias		

class Net:
	layers = []

	def __init__(self, topology):
		for size in topology.layers:					#create nuerons from topology data 
			self.layers.append(Layer(size, topology.bias))
		for layer in self.layers:
			layer.randomizeWeights()

	def feedForward(self, input):
		self.layers[0].setValues(input)
		for i in range(1, len(layers)-1):	#do calculations for every layer that isn't input
			self.layers[i].feedForward(layers[i-1])

	def backPropogate(self, desired):
		print("ya")

	def getOutput(self):
		return self.layers[len(self.layers)-1]

def main():
	top = Topology();
	top.setData([3, 2, 1], True)

	net = Net(top)

	for i in range(10):
		print(i)

if __name__ == "__main__":
	main()
