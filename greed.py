
import pytest

from random import randint 

class Dice(object):
	def __init__(self):
		self._values = []
		self.points = 0
		self._rolling = True
	
	def roll(self):
		if not self._values:
			self._values = [randint(1,6) for unused_i in range(5)]
		else:
			num_of_dice = len(self._values)
			self._values = [randint(1,6) for unused_i in range(num_of_dice)]
		
		
	def calc_points(self):
		points = 0
		#gets trip points
		trips = self.find_triples()
		if trips == 1:
			points += 1000
			for i in range(0,3):
				self._values.remove(trips)
		if trips != 0 and trips != 1:
			points += (trips * 100)
			for i in range(0,3):
				self._values.remove(trips)
		#gets reg points
		while 1 in self._values:
			points += 100
			self._values.remove(1)
		while 5 in self._values:
			points += 50
			self._values.remove(5)
		
		#allows continuous rolling or deletes object if no points gotten
		if points == 0:
			self._rolling = False
		else:
			self.points += points
			
		
		
	def find_triples(self):
		value = [i for i in self._values if self._values.count(i) >= 3]
		if value:
			return value[0]
		else:
			return 0
			

def user_turn():
	dice = Dice()
	while True:
		dice.roll()
		print "You rolled: %r" % dice._values

		dice.calc_points()
		if dice._rolling == False:
			print "Y0U R0LLED N0 P0INTS. YOU GET 0 POINTS THIS TURN!"
			return 0
			del dice
			break
		elif len(dice._values) == 0:
			print "WOW YOUR OUT OF DICE AND GOT A TON OF POINTS! LUCKY DOG!"
			return dice.points
			del dice
			break
		else:
			print "YOU ROLLED '%d' POINTS.  YOU HAVE '%d' DICE LEFT." % (dice.points, 
																		 len(dice._values)
																		)
			if get_user_descision(dice):
				return dice.points
				del dice
				break


def get_user_descision(dice_obj):
	while True:
		print "Your total points this turn: %d" % dice_obj.points
		answ = str(raw_input("Do you want to 'bank' or 'roll': ")).lower()
		if answ == 'bank':
			return True
			break
		elif answ == 'roll':
			return False
			break
		else:
			print 'That is not a choice.'
			
			
def how_many_players():
	try:
		num = input('How many players? (1-4): ')
	except:
		print "Not a valid entry"
		return how_many_players()
	else:
		if num in range(1,5):
			print "You chose %d players" % num
			return num
		else:
			print "Not a valid entry"
			return how_many_players()
	
	
def make_players():
	player_points = {}
	num = how_many_players()
	for i in range(1,num+1):
		player_points[i] = 0
	return player_points
		

def game_play(players_from_created):
	player_points = players_from_created
	highest_score = 0
	whose_turn = 0
	while highest_score < 400:
		print "*" * 25
		if whose_turn < len(player_points):
			whose_turn += 1
		else:
			whose_turn = 1
		print "PLAYER %d's turn. You have '%d' points." % (whose_turn, player_points[whose_turn])
		points_gotten = user_turn()
		print "You got %d points that turn!" % points_gotten
		player_points[whose_turn] += points_gotten
		highest_score = max([j for i,j in player_points.iteritems()])
		
	print "GAME OVER! PLAYER '%d' WINS!" % whose_turn
		

def main():
	players = make_players()
	game_play(players)
	

if __name__ == "__main__":
	main()


					
				
			
			
			


# Testing goes below here.  To test type py.test greed.py into terminal.

def test_rolling_no_points_deletes_obj():
	dice = Dice()
	dice._values = [2,3,4,3,2]
	assert dice.calc_points() == None


def test_rolling():
	dice = Dice()
 	dice.roll()
 	assert len(dice._values) == 5
 	dice._values = [1,3,10]
 	dice.roll()
 	assert len(dice._values) == 3 
 	assert len(dice._values) != [1,3,10]
 		
 		
def check_triples_works():
	dice = Dice()
 	dice._values = [1,2,4,3,1]
 	assert dice.find_triples() == 0
 	dice._values = [1,1,1,4,3]
 	assert dice.find_triples() == 1
 	dice._values = [1,3,5,3,3]
 	assert dice.find_triples() == 3
 	
 
def test_scoring():
 	dice = Dice()
 	dice._values = [2,2,3,3,4]
 	dice.calc_points()
 	
 	dice.points = 0
 	dice._values = [2,2,3,1,4]
 	dice.calc_points()
 	assert dice.points == 100
 	assert len(dice._values) == 4
 	
 	dice.points = 0
 	dice._values = [2,5,3,5,4]
 	dice.calc_points()
 	assert dice.points == 100
 	assert len(dice._values) == 3
 	
 	dice.points = 0
 	dice._values = [3,2,3,2,3]
 	dice.calc_points()
 	assert dice.points == 300
 	assert len(dice._values) == 2
 	
 	dice.points = 0
 	dice._values = [1,1,1,3,4]
 	dice.calc_points()
 	assert dice.points == 1000
 	assert len(dice._values) == 2
 	
 	dice.points = 0
 	dice._values = [4,4,2,5,4]
 	dice.calc_points()
 	assert dice.points == 450
 	assert len(dice._values) == 1
 	
 	
 	dice.points = 0
 	dice._values = [1,1,2,1,1]
 	dice.calc_points()
 	assert dice.points == 1100
 	assert len(dice._values) == 1
 	
 	dice.points = 0
 	dice._values = [5,5,5,5,5]
 	dice.calc_points()
 	assert dice.points == 600
 	assert len(dice._values) == 0
 
