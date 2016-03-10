import player
import bases
import itertools

# Below I have initialized the projected Marlins batters based on their Steamer projections.
# Pitcher is initialized with Jose Fernandez's 2013 stats, because why not. It doesn't really matter within the current projections.
deeGordon = player.Player(584, 132, 23, 8, 3, 35, 4, 4, "Gordon")
christianYelich = player.Player(525, 105, 31, 3, 12, 62, 3, 4, "Yelich")
giancarloStanton = player.Player(481, 67, 27, 2, 28, 83, 4, 4, "Stanton")
justinBour = player.Player(476, 79, 24, 1, 18, 48, 3, 4, "Bour")
martinPrado = player.Player(485, 95, 26, 2, 9, 37, 4, 4, "Prado")
marcellOzuna = player.Player(498, 85, 29, 2, 18, 36, 3, 4, "Ozuna")
jtRealmuto = player.Player(398, 71, 19, 4, 8, 25, 3, 3, "Realmuto")
adeinyHechavarria = player.Player(461, 91, 19, 6, 4, 29, 2, 4, "Hechavarria")
jeffMathis = player.Player(118, 16, 5, 1, 2, 10, 1, 1, "Mathis")
chrisJohnson = player.Player(224, 41, 12, 0, 4, 11, 1, 2, "Johnson")
derekDietrich = player.Player(246, 38, 12, 2, 8, 19, 9, 2, "Dietrich")
coleGillespie = player.Player(61, 12, 3, 0, 1, 5, 0, 1, "Gillespie")
ichiroSuzuki = player.Player(220, 45, 7, 2, 1, 14, 1, 2, "Suzuki")
pitcher = player.Player(50, 8, 1, 1, 1, 0, 0, 1, "Pitcher")


travisDarnaud = player.Player(380, 60, 21, 2, 16, 35, 3, 3, "d'Arnaud")
lucasDuda = player.Player(466, 65, 23, 0, 23, 71, 9, 4, "Duda")
neilWalker = player.Player(499, 83, 25, 2, 18, 49, 9, 4, "Walker")
asdrubalCabrera = player.Player(448, 70, 23, 3, 13, 39, 5, 4, "Cabrera")
davidWright = player.Player(384, 70, 21, 1, 11, 42, 3, 3, "Wright")
michaelConforto = player.Player(476, 78, 25, 2, 18, 43, 4, 4, "Conforto")
yoenisCespedes = player.Player(550, 85, 28, 3, 26, 38, 4, 4, "Cespedes")
curtisGranderson = player.Player(551, 77, 26, 2, 23, 77, 6, 4, "Granderson")

# I then created two lists: one with every player and one with just the projected starting lineup.
# These are simply here so that the user does not have to retype them each time they are needed.
everyone = [deeGordon, christianYelich, giancarloStanton, justinBour, martinPrado, marcellOzuna, jtRealmuto, adeinyHechavarria, jeffMathis, chrisJohnson,
derekDietrich, coleGillespie, ichiroSuzuki]
marlins = [deeGordon, christianYelich, giancarloStanton, justinBour, martinPrado, marcellOzuna, jtRealmuto, adeinyHechavarria]
mets = [travisDarnaud, lucasDuda, neilWalker, asdrubalCabrera, davidWright, michaelConforto, yoenisCespedes, curtisGranderson]
"""The function simInning is the backbone of the projections system. It takes one argument - the lineup - as a list of players.
	The function then operates as expected. It sims each player's plate apperance, editing the base variable, runs variable, and outs
	variable as needed. At the end, the lineup is adjusted so that whoever made the last out in the inning will be last in the order
	the next time around, and this is returned along with the number of runs scored in a tuple.

	The one thing to note about simInning is that neither baserunning nor sacrifices were factored into the simulation. What this means
	is that a runner on third with 0 or 1 outs will never score when the batter makes an out, even though it could have been a fly ball
	which the runner would then have tagged up on. Similarly, a single with a runner on second will never result in that runner scoring,
	even though this happens somewhat often in real life. Also, there are no stolen bases in this simulation.

	Because of this choice, the projected runs per inning are lower than they should be, and over the course of a season, this can 
	translate to a team projecting to 100 fewer runs than expected. 

	While these could later be added, I was going for simplicity to begin with, and so the decision was made to omit these features
	(at least to start with)."""
def simInning(lineup):
	outs = 0
	runs = 0
	batter = 0
	base = bases.Bases()
	while outs < 3:
		pa = lineup[batter].simPlateAppearance()
		if pa == "Out":
			outs += 1
		elif pa == "Walk" or pa == "Hit By Pitch" or pa == "Single":
			if base.areLoaded():
				runs += 1
				base.third = base.second
				base.second = base.first
				base.first = lineup[batter]
			elif base.areEmpty() or base.secondOnly() or base.thirdOnly() or base.secondAndThird():
				base.first = lineup[batter]
			elif base.firstAndSecond():
				base.third = base.second
				base.second = base.first
				base.first = lineup[batter]
			elif base.firstAndThird() or base.firstOnly():
				base.second = base.first
				base.first = lineup[batter]
		elif pa == "Double":
			if base.areLoaded():
				runs += 2
				base.third = base.first
				base.second = lineup[batter]
				base.first = "empty"
			elif base.areEmpty():
				base.second = lineup[batter]
			elif base.secondOnly() or base.thirdOnly():
				runs += 1
				base = bases.Bases()
				base.second = lineup[batter]
			elif base.secondAndThird():
				runs += 2
				base = bases.Bases()
				base.second = lineup[batter]
			elif base.firstOnly():
				base.third = base.first
				base.second = lineup[batter]
				base.first = "empty"
			elif base.firstAndThird() or base.firstAndSecond():
				runs += 1
				base.third = base.first
				base.second = lineup[batter]
				base.first = "empty"
		elif pa == "Triple":
			runs += base.menOn()
			base = bases.Bases()
			base.third = lineup[batter]
		elif pa == "Home Run":
			runs += base.menOn() + 1
			base = bases.Bases()

		if batter == 8:
			batter = 0
		else:
			batter += 1

	lineup = lineup[batter:] + lineup[:batter]
	return (runs, lineup)


"""The simGame function takes a starting lineup and simply sims nine innings. Again, this doesn't account for games in which
the team only bats in eight innings, but it gives us a starting point. I also took care to make sure the lineup was correctly 
updating from inning-to-inning (i.e. the same three players weren't starting each inning)."""
def simGame(lineup):
	runs = 0
	x = 0
	while x < 9:
		sim = simInning(lineup)
		runs += sim[0]
		lineup = sim[1]
		x += 1
	return runs

"""The simSeason function simply sims 162 games and returns the number of runs scored."""
def simSeason(lineup):
	runs = 0
	x = 0
	while x < 162:
		lineup1 = lineup
		runs += simGame(lineup1)
		x += 1
	return runs

"""The getRunsperGame function takes a lineup and an integer N, sims N games with that lineup, and then divides the 
total number of runs scored by the number of games played, thus returning the average runs scored per game by that
lineup. This is a helper for the optimalLineup function, but can also be used on it's own in comparing two or three
lineups."""
def getRunsperGame(lineup, N):
	runs = 0
	x = 0
	while x < N:
		lineup1 = lineup
		runs += simGame(lineup1)
		x += 1
	return runs/float(N)


"""The optimalLineup function puts all of the previous functions together to find the optimal lineup given a list of batters.

The function takes two arguments: batters and N. Batters is the list of players to be considered in the lineup optimization and
N is the number of games each lineup will play to determine the average number of runs per game that the lineup scores.

NOTE: The larger the N value is, the longer the function will take to run. In testing, I tried to use an N of 200 or less. For 
reference, when I used an N of 100 it took about 2.5 seconds to calculate the output of 100 lineups. Obviously, a larger N will
result in more accurate results, but in the interest of keeping the computation time to a minimum, it is much better to use a 
smaller value.

ALSO NOTE: The longer your batters list is, the longer the function will take to run. The minimum length for this is 8, and I 
would reccomend not going any longer than 10. When the length is 8, there are P(8, 8) or 40,320 individual lineups that need
to be tested. When the length is 9, this number is nine times greater -> P(9, 8) = 362,880 distinct lineups. At length 10, this
number jumps to 3,628,800 lineups that need to be tested.

In order to make the simulation run faster, I have the pitcher batting ninth in all simulations. I think it's safe to say that
you probably don't want the pitcher anywhere other than 9th (sometimes 8th, but that throws another wrinkle into the function), 
so I restricted him to batting 9th, thus cutting the computation time to 11% of what it was."""
def optimalLineup(batters, N):
	best = 0
	optlineup = []
	lineups = itertools.permutations(batters, 8)
	num = 1
	for x in lineups:
		x = x + (pitcher,)
		runs = getRunsperGame(x, N)
		if runs > best:
			optlineup = x
			best = runs
			for i in optlineup:
				print i
			print best
			print "-----------------------"
		num += 1

	for i in optlineup:
		print i
	return best
#Want to test all 50 times, take top 50% and test 100 times, take top 20% of that and test 500 times, then take top 5% of that and test 1000 times, then top 5 100000 times each


def optimalLineup2(batters):
	top500 = SortedList()
	lineups = itertools.permutations(batters, 8)
	num = 1
	for x in lineups:
		x = x + (pitcher,)
		runs = getRunsperGame(x, 100)
		if len(top500)<500:
			top500.append([runs, x])
		elif runs > top500[0][0]:
			top500.append([runs, x])
			top500 = top500[1:]
			for i in x:
				print i
			print runs
		if num%500 == 0:
			print str(num/40320.)
		num += 1

	print "DONE WITH ROUND 1"
	
	top50 = SortedList()
	for x in top500:
		runs = getRunsperGame(x[1], 500)
		if len(top50)<50:
			top50.append([runs, x[0]])
		elif runs > top50[0][0]:
			top50.append([runs, x[0]])
			top50 = top50[1:]
			for i in x:
				print i
			print runs

	optlineup = []
	best = 0 
	for x in top50:
		runs = getRunsperGame(x[1], 1000)
		if runs > best:
			optlineup = x[1]
			best = runs
			for i in optlineup:
				print i
			print best
			print "-----------------------"
	for i in optlineup:
		print i
	return best



class SortedList:

	def __init__(self):
		self.list = []

	def __len__(self):
		return len(self.list)

	def __getitem__(self, i):
		return self.list[i]

	def __str__(self):
		string = ""
		for i in self.list:
			string += str(i[0]) + str(i[1]) + "\n"
		return string

	def append(self, elt):
		index = elt[0]
		i = 0
		for x in self.list:
			if index >= x[0]:
				i += 1
		self.list = self.list[:i] + [elt] + self.list[i:]

