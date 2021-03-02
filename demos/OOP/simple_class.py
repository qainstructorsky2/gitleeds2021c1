class Presenter():




	def __init__(self, name): # Constructor
		self.name = name  #instance variable

	def say_hello(self):
		# method
		print('Hello, ' + self.name)

presenter = Presenter('Pete')
#presenter.name = 'Peter'
presenter.say_hello()