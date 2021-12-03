import turtle
class LSystem:
	#You may add additional methods and break methods up.
	#Below is the interface that I am expecting in the driver.
	def __init__(self,filename):
		'''
		creates the setup for the LSystem
		args: self, filename
		return: none
		'''
		#complete this method
		self.rules = {}
		self.file = open(filename, "r")
		self.angle = int(self.file.readline())
		self.iters = int(self.file.readline())
		self.dist = int(self.file.readline())
		self.axiom = self.file.readline()
		
		for i in self.file:
			self.split = i.split(" : ")
			thestr = self.split[1].replace("\n","")
			self.rules[self.split[0]] = thestr
		print(self.rules) 

	def createLSystem(self):
		'''
		creates the LSystem and sets the rules
		args: self
		return : none
		'''
		#complete this method
		self.results = self.axiom
		print(self.axiom)
		for k in range(int(self.iters)):
			new_string = ''
			for j in self.results:
				try:		
					new_string += self.rules[j]
				except KeyError:
					new_string += j
			self.results = new_string

		                                      
	def drawLSystem(self, snap):
		'''
		draws the LSystem by following the rules
		args: self, snap(turtle)
		return: none 
		'''
		#complete this method
		new_data = []
		for cmd in self.results:
			if(cmd == 'F'):
				snap.forward(self.dist)
			elif(cmd == '+'):
				snap.right(self.angle)
			elif(cmd == '-'):
				snap.left(self.angle)
			elif(cmd == '['):
				snap_state = vars(snap)
				new_data.append(snap_state)
			elif(cmd == ']'):
				if new_data:
					t_state = new_data.pop()
					snap.__dict__ = t_state

		


		
