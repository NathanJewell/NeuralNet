
udemi


def genWeight():
	return random()

def hyptan(val):
	return tanh(val)

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

	weights = [];			#nueron importance in network
	deltaWeights = [];	#difference in weight since last iteration
	value = 0;			#sum of parents
	desiredValue = 0;	#expected value based on data input
	error = 0;			#difference between output value and desired
#	biasWeight = 0;		#importance of bias
#	biasValue = 0;		#bias amount

class Layer:
	neurons = []
	activation = sigmoid()

	def __init__(self, size, iactivation):
		neurons = [Neuron() for i in range(size)]

	def feedForward(self, parent, globalBias):
		sum = 0;
		for n in self.neurons:
			for w in range(len(parent.neurons)):
				sum += parent.neurons[w].value*n.weights[w]
			n.value = activation(sum + bias)	#is bias part of activation function?
			sum = 0

	def randomizeWeights(self):
		for n in neurons:
			n.weight = genWeight()

class Topology:
	layers = []		#ordered list of number of neurons in each layer
	bias = 0
	activation = 0

	def setData(self, ilayers, ibias, iactivation):
		layers = ilayers	
		bias = ibias
		activation = iactivation

class Net:
	layers = []
	biasValue = 0;

	def __init__(self, topology):
		for size in topology.layers:					#create nuerons from topology data 
			self.layers.append(Layer(size))
		for layer in self.layers:
			layer.randomizeWeights()

	def feedForward(self, input):
		self.layers[0].setValues(input)
		for i in range(1, len(layers)-1):	#do calculations for every layer that isn't input
			self.layers[i].feedForward(layers[i-1], biasValue)

	def backPropogate(self, desired):
		print("ya")

	def getOutput(self):
		return self.layers[len(self.layers)-1]

def main():
	top = Topology();
	top.setData([3, 2, 1], 1, hyptan())

	net = Net(top)

	for i in range(iterations):
		net.feedForward(input)
		net.backPropogate(desired)

if __name__ == "__main__":
	main()
