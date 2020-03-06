
def convert(value):
	if value<10:
		return value
	elif value>=10 and value<=35:
		return chr(value+55)
	else:
		return chr(value+61)
