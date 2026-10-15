#Constructing
class Constructor:
	def __init__(key, value):
		key.value = key
		
	def construct(key):
		var = (f"#{key.value}")
		return(var)
		
script = Constructor(None)
print(script.construct())
