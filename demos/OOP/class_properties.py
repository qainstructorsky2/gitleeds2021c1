class Presenter():
	def __init__(self, name):
		# Constructor
		self.name = name

	@property #getter - accessor
	def name(self):
		print('Retrieving name...')
		return self.__name


	@name.setter  # setter - mutator
	def name(self, value):
		# cool validation here
		print('Validating name...')
		self.__name = value


presenter = Presenter('Pete')
presenter.name = 'Peter'
print(presenter.name)