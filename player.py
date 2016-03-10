import math
import random


"""The player class is used to create an instance of a player by initializing it with either past or projected statistics.
Most functions within are simply there to help in the evaluation of two main functions: simPlateAppearance and simSeason.
These are explained in more depth within the class"""
class Player:

	"""The player should be initialized with the following attributes:
		At bats, Singles, Doubles, Triples, Home Runs, Walks, Hit by Pitches, Sac Flies, and the player's last name"""
	def __init__(self, ab, sin, doub, trip, hr, bb, hbp, sf, lname):
		self.ab = ab
		self.sin = sin
		self.doub = doub
		self.trip = trip
		self.hr = hr
		self.bb = bb
		self.hbp = hbp
		self.sf = sf
		self.lname = lname

	def __str__(self):
		return self.lname

	def getPA(self):
		return (self.ab + self.bb + self.hbp + self.sf)

	def getHits(self):
		return (self.sin + self.doub + self.trip + self.hr)

	def getAVG(self):
		return self.getHits()/float(self.ab)

	def getOBP(self):
		return (self.getHits() + self.bb + self.hbp)/float(self.ab + self.bb + self.hbp + self.sf)

	def getSinglePct(self):
		return float(self.sin)/self.getPA()

	def getDoublePct(self):
		return float(self.doub)/self.getPA()

	def getTriplePct(self):
		return float(self.trip)/self.getPA()

	def getHRPct(self):
		return float(self.hr)/self.getPA()

	def getBBPct(self):
		return float(self.bb)/self.getPA()

	def getHBPPct(self):
		return float(self.hbp)/self.getPA()


	"""The function simPlateAppearance does as it sounds. Using the statistics that were input when the player was initialized, the 
	function uses a random number generator (the random module) to simulate one plate appearance by that player. The result is returned
	in string form and can then be used in a variety of ways."""
	def simPlateAppearance(self):
		rnd = random.random()
		pcts1 = [self.getSinglePct(), self.getDoublePct(), self.getTriplePct(), self.getHRPct(), self.getBBPct(), self.getHBPPct()]
		pcts = [self.getSinglePct()]
		i = 0
		while (i<5):
			pcts.append(pcts1[i+1] + pcts[i])
			i += 1
		
		if rnd < pcts[0]:
			return "Single"
		elif rnd < pcts[1]:
			return "Double"
		elif rnd < pcts[2]:
			return "Triple"
		elif rnd < pcts[3]:
			return "Home Run"
		elif rnd < pcts[4]:
			return "Walk"
		elif rnd < pcts[5]:
			return "Hit By Pitch"
		else:
			return "Out"


	"""The funtion simSeason takes in one argument: the number of plate appearances you want to run on the player. The function then
	calls the simPlateAppearance function that many times, counting how many times each outcome occurs and returning that in a list.

	This function is rather useless on its own, as it relies on the statistics that the player was intialized with. Therefore, the results
	will almost always be right around what was expected. However, it is useful in testing that the other functions in the class are 
	written correctly"""
	def simSeason(self, apps):
		sin = 0
		doub = 0
		trip = 0
		hr = 0
		bb = 0
		hbp = 0
		i = 0
		while (i<apps):
			one = self.simPlateAppearance()
			if one == "Single":
				sin += 1
			elif one == "Double":
				doub += 1
			elif one == "Triple":
				trip += 1
			elif one == "Home Run":
				hr += 1
			elif one == "Walk":
				bb += 1
			elif one == "Hit By Pitch":
				hbp += 1
			else: 
				pass
			i += 1
		return [sin, doub, trip, hr, bb, hbp]








