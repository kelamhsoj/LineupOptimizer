# LineupOptimizer
Python program to find the optimal lineup given a list of hitters


In an attempt to create an optimal, 9-man baseball lineup, I created the following repository. It consists of three main files, detailed below.

  players.py contains class Player which is initialized with various statistical attributes. As you can see in the file itself, these attributes are at bats, singles, doubles, triples, home runs, walks, hit by pitches, sacrifice flies, and the player’s last name. There are two main functions within this class: simPlateAppearance() and simSeason(apps). They both do as they sound - the first sims a single plate appearance of the batter and returns a string with the result, while the second sims as many plate appearances as the user inputs.
  
  The bases.py file contains a class Bases which is really only used within the game simulations. There isn’t anything too interesting within the file itself - it's just a necessary class to have in order for the simulation to work.
  
  The team.py file is the meat and potatoes of the project. This file contains all of the player initializations and simulations. The first important function is simInning(lineup) which takes a lineup and returns a tuple containing the number of runs scored and the new lineup (with the last out moved to the back and those who haven’t yet hit moved to the front). This is the main simulation function - all others use this to do the simulations - and as I explained in depth in the file itself, I decided to exclude base running and sacrifices to begin with. These are a lot more difficult to program, so for the sake of simplicity I decided to take them out of the first version of the program.
	The next functions are simGame(lineup) and simSeason(lineup), which both take a lineup and simulate either one game or 162 games and return the total number of runs scored in that time span.
	The final two functions are the most useful. getRunsperGame(lineup, N) takes a lineup and an integer. The function then simulates N games with that lineup and returns the average number of runs scored per game. This is extremely useful in comparing a small number of possible lineups, as you can have each lineup play 1000 fake games in order to see which will score the most runs. optimalLineup(batters, N) again takes two arguments, a list of players and an integer, but this time computes all possible permutations of length 8 of that list of players and for each simulates N games. In the end, the lineup with the highest number of runs scored per game is printed out.
	
	As this is just the beginning of the project, the program still runs very slowly and is not very accurate. I hope to  increase both the speed and the accuracy in the near future by eliminating lineups in rounds - i.e. running each lineup through 100 simulations and deleting the bottom 50%, running the rest through 500 simulations and deleting the bottom 50% of that, etc.
