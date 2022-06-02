import random
from string import ascii_uppercase as alphabet
import colors as Color

atmospheres = [Color.red + "Corrosive",
	Color.red + "None",
	Color.bright_red + "Low",
	Color.yellow + "Marginal",
	Color.green + "Oxygen-Rich"]
temperatures = [Color.red + "Very low",
	Color.bright_red + "Low",
	Color.green + "Good",
	Color.bright_red + "High",
	Color.red + "Very high"]
waters = [Color.red + "None",
	Color.bright_red + "Trace",
	Color.yellow + "Scarce",
	Color.green + "Good",
	Color.blue + "Planet-wide ocean"]
gravity = [Color.red + "Very low",
	Color.bright_red + "Low",
	Color.green + "Good",
	Color.bright_red + "High",
	Color.red + "Very high"]
resources = [Color.red + "None",
	Color.red + "Scarce",
	Color.bright_red + "Lightly scarce",
	Color.yellow + "Good",
	Color.green + "Rich"]
anomalies = ["Alien Structures",
	"Animals",
	"Vegitation"]






class Planet:


	def __init__(self):
		self.id = random.choice(alphabet) + random.choice(alphabet) + "-" + str(random.randint(100, 999))
		self.atmosphere = random.choice(atmospheres) + Color.white
		self.gravity = random.choice(gravity) + Color.white
		self.temperature = random.choice(temperatures) + Color.white
		self.water = random.choice(waters) + Color.white
		self.resources = random.choice(resources) + Color.white
		self.get_anomalies()

	def get_anomalies(self):
		self.anomalies = []
		for n in range(random.randint(0,2)):
			self.anomalies.append(random.choice(anomalies))
		# Remove duplicates
		self.anomalies = list(set(self.anomalies))
		


		
	def __str__(self):
		info = """
Planet {0}
	Atmosphere: {1}
	Temperature: {2}
	Gravity: {3}
	Water: {4}
	Anomalies: \n\t\t\t{5}
		""".format(self.id, 
							self.atmosphere,
							self.temperature,
							self.gravity,
							self.water,
							"\n\t\t\t".join(self.anomalies))
		return info