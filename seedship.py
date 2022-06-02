import colors as Color

class Seedship:

	def __init__(self):
		self.colonists = 1000
		self.scanners = {
			"Atmosphere": 100,
			"Gravity": 100,
			"Temperature": 100,
			"Water": 100,
			"Resources": 100,
		}
		self.probes = 10
		self.systems = {
			"Landing": 100,
			"Construction": 100
		}
		self.databases = {
			"Scientific": 100,
			"Cultural": 100
		}
	def dict_str(self, d):
		info = []
		for k in d.keys():
			if d[k] > 90:
				color = Color.green
			elif d[k] > 75:
				color = Color.bright_green
			elif d[k] > 50:
				color = Color.yellow
			elif d[k] > 25:
				color = Color.bright_red
			else:
				color = Color.red
				
			value = color + str(d[k])
			info.append("\n\t" + (k+ " : ").rjust(20) + value + Color.white)
		return "".join(info)
	
	def __str__(self):
		info = """
Colonists : 	  {0}
Surface Probes :  {1}
Scanners 
	{2}
		
Systems
	{3}
		
Databases
	{4}
		""".format(self.colonists,
		self.probes,
		self.dict_str(self.scanners),
		self.dict_str(self.systems),
		self.dict_str(self.databases))
		return info