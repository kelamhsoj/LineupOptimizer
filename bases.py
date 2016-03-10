import player


"""The Bases class is used within the game simulation. It is simply a list of length three (corresponding to first, second,
	and third base). If a base is empty, the list will have the string 'empty' at that index. If there is a player on the base,
	the list will have the player object instead.

	The various functions are simply written to help make evaluating a game easier. On their own, they're nothing special."""
class Bases:

	def __init__(self):
		self.first = "empty"
		self.second = "empty"
		self.third = "empty"

	def areLoaded(self):
		return self.first != "empty" and self.second != "empty" and self.third != "empty"

	def areEmpty(self):
		return self.first == "empty" and self.second == "empty" and self.third == "empty"

	def firstAndSecond(self):
		return self.first != "empty" and self.second != "empty" and self.third == "empty"

	def firstAndThird(self):
		return self.first != "empty" and self.second == "empty" and self.third != "empty"

	def secondAndThird(self):
		return self.first == "empty" and self.second != "empty" and self.third != "empty"

	def firstOnly(self):
		return self.first != "empty" and self.second == "empty" and self.third == "empty"

	def secondOnly(self):
		return self.first == "empty" and self.second != "empty" and self.third == "empty"

	def thirdOnly(self):
		return self.first == "empty" and self.second != "empty" and self.third != "empty"

	def menOn(self):
		men = 0
		if self.first != "empty":
			men += 1
		if self.second != "empty":
			men += 1
		if self.third != "empty":
			men += 1
		return men
		