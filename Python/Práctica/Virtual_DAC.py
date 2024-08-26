
value = 350

def V_DAC(value):
	if (value>=0 and value<=1023):
		return f"{(round(5*value/1023, 2))}V" #Formula: 5V/1023*VALUE

print(V_DAC(value))

