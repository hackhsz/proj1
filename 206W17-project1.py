import random
import unittest
import pdb

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison 

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = []
		for c in self.cards:
			card_strs.append(c.__str__())
		if card.__str__() not in card_strs:
			self.cards.append(card)

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


# Class Hand: Represents a hand of cards for a game, with basic functionality
# Functionality available: Number of cards attribute
# Methods: Can place a card out of the hand, add a card to the hand that is not a duplicate, find all suits available, find all ranks available, look for a specific card in the hand and return it if there
class Hand(object): 
	def __init__(self,deck_to_use,num_cards=5): # Constructor
		self.deck = deck_to_use # Needs a deck
		self.cards_in_hand = [] 
		for i in range(num_cards):
			#pdb.set_trace()
			#cards_be_pop = self.deck.pop_card(i)
			#print(cards_be_pop)
			#print(self.cards_in_hand)
			self.cards_in_hand.append(self.deck.pop_card(i))
		
	def place_card(self,i=0):
		return self.cards_in_hand.pop(i) # Basically the same as pop_card from the deck, but referencing the HAND's cards

	def get_suits_available(self): # Returns list of all the suits that are in the hand
		suits = []
		for c in self.cards_in_hand:
			if c.suit not in suits:
				suits.append(c.suit)
		return suits

	def get_ranks_available(self): # Returns list of all the ranks that are in the hand
		ranks = []
		for c in self.cards_in_hand:
			if c.rank not in ranks:
				ranks.append(c.rank)
		return ranks

	def specific_card(self,suit,rank):
		card_strs = []
		ind = 0
		for c in self.cards_in_hand:
			if c.suit == suit and c.rank == rank:
				return self.place_card(ind) # If find the card in the hand, get rid of that card from the hand and return it from this method
			ind = ind + 1
		return None # if there is none such card in the hand, return None value
		
	def add_card(self,card): # add card to hand (if there is no identical one, assuming working with 1 deck here)
		card_strs = []
		for c in self.cards_in_hand:
			card_strs.append(c.__str__())
		if card.__str__() not in card_strs:
			self.cards_in_hand.append(card)

	def __str__(self):
		total = []
		for card in self.cards_in_hand:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

#### Functions for games ####

# Function that plays an altered version of the game of War when invoked.
def play_war_game(testing=False):
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:
			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

## Below this line, indented beneath it, goes function invocations, any code you want to run when you run this file.
if __name__ == "__main__":

	print("Test code here!\n")
#	d = Deck()
#	onde = d(1)
#	pdb.set_trace()
	#print(onde)
	## The following is code to try out functionality of the class Hand. Uncomment the following lines to try it out. Note that each line depends on the former lines!

	# deck_to_play = Deck() # Create a deck
	# deck_to_play.shuffle() # Shuffle the deck!
	# single_hand = Hand(deck_to_play,num_cards=5) # Deal one hand of 5 cards
	# print(single_hand) # Print the hand to view it
	print("\n\n\n") # Print new lines, just for clarity


########### TESTS SHOULD GO BELOW THIS LINE ###########

# INCLUDE YOUR TESTS FROM HW2 HERE.

# HW2 

class test_card_rank(unittest.TestCase):
	# test that if you created a card with rank 12, its rank will be Queen
	def test_rank(self):
		x = Card(rank=12)
		#x.rank_levels  = 12
		self.assertEqual(x.rank , "Queen")
	## Test that if you create a card with rank 1, its rank will be "Ace"
	
	def test_rank_Ace(self):
		y = Card(rank=1)
		#y.rank_levels = 1
		self.assertEqual(y.rank,"Ace")
	



## Test that if you create a card instance with rank 3, its rank will be 3


class test_card_simple_rank(unittest.TestCase):
	
	def test_rank_3(self):
		x = Card(rank=3)
		#x.rank_levels = 3
		self.assertEqual(x.rank,3)
	

## Test that if you create a card instance with suit 1, it will be suit "Clubs"

	def test_suit_one(self):
		y = Card(suit=1)
		#y.suit_names = "Clubs"
		self.assertEqual(y.suit,"Clubs")
## Test that if you create a card instance with suit 2, it will be suit "Hearts"
	def test_suit_2(self):
		z = Card(suit=2)
		self.assertEqual(z.suit,"Hearts")
## Test that if you create a card instance, it will have access to a variable suit_names that contains the list ["Diamonds","Clubs","Hearts","Spades"]

class test_access_instance(unittest.TestCase):
	
#	pdb.set_trace
	def test_access(self):
		x = Card()
#		x.suit_names
		#print(x.suit_names)
		self.assertEqual((x.suit_names),["Diamonds","Clubs","Hearts","Spades"])
## Test that if you invoke the __str__ method of a card instance that is created with suit=2, rank=7, it returns the string "7 of Hearts"

	def test_str(self):
		y = Card(2,7)
		self.assertEqual(str(y),"7 of Hearts")

## Test that if you create a deck instance, it will have 52 cards in its cards instance variable

class test_deck(unittest.TestCase):
	
	def test_deck_52(self):
		x = Deck()
		self.assertEqual(len(x.cards),52)

## Test that if you invoke the pop_card method on a deck, it will return a card instance.


class test_pop_deck(unittest.TestCase):
	
	def test_pop(self):
		
		y = Deck()
		x = Card()
		self.assertEqual(type(y.pop_card()),type(x))

	
## Test that the return value of the play_war_game function is a tuple with three elements, the first of which is a string. (This will probably require multiple test methods!)



class test_playwar1(unittest.TestCase):
	
	def test_playwargame(self):
		
		x = play_war_game(testing = True)
		y = (1,3,4)
		self.assertEqual(type(x),type(y))

	def test_playwargame2(self):
		
		x = play_war_game(testing = True)
		z = "s"
		self.assertEqual(type(x[0]),type(z))

	def test_playwargame3(self):
		
		x = play_war_game(testing = True)
		m = (1,2,3)
		self.assertEqual(len(x),3)
		
## Write at least 2 additional tests (not repeats of the above described tests). Make sure to include a descriptive message in these two so we can easily see what you are testing!

class test_pop_card_num(unittest.TestCase):
	
	def test_pop_num(self):
		x = Deck()
		x.pop_card()
		x.pop_card()
		self.assertEqual(len(x.cards),50)

# To test that after popping two cards, the number will be 50 instead of 52. This fully test the pop_function

class test_shuffle(unittest.TestCase):
	
	def test_shuffle(self):
		
		x = Deck()
		y = x
		x.shuffle()
	#	x.cards.sort()
		self.assertEqual(set(x.cards),set(y.cards))






## Add tests, as described in instructions.
## Here is a sample.
#class HandClassTests(unittest.TestCase):
	#def test_add_card(self):
		#d = Deck()
		#h = Hand(d) # default number of cards
		#num = len(h.cards_in_hand) # length of the cards list in the hand
		#new_card = d.pop_card() # pop another card off the deck
		#h.add_card(new_card) # invoke add_card method with the card that we popped off the deck
		#self.assertEqual(len(h.cards_in_hand),num+1) # Testing that the new number of cards in the hand is equal to the old number plus 1
	# Add more here!
#	print("rubbish")
class HandClass2Tests(unittest.TestCase):
	
	def test_init_card(self):
		d = Deck()
		round = len(d.cards)
		c = d
		#print(c)
		
		#pdb.set_trace()
	#	d.pop_card(0)
		
		#self.assertEqual(c,d)
		#print(c)
		#print(d)
		# copy to make sure it does not get modified
		#h = Hand(d)
		hand1 = Hand(d)
		
	      #	def test_init_card2(self):
		f = Deck()
		#h = Hand(d)
	#	hand1 = Hand(self,d,num_cards=5)
		self.assertEqual(len(hand1.cards_in_hand),round-len(d.cards))

class Hand_class_test(unittest.TestCase):
	
#	Cardone = Card(2,7)
	def test_add_card(self):
		d = Deck()
		Cardone = Card(2,7)
		hand1 = Hand(d)
		if Cardone not in hand1.cards_in_hand:
			hand1.cards_in_hand.append(Cardone)
			nowlen = len(hand1.cards_in_hand)
			hand1.add_card(Cardone)
			now2len = len(hand1.cards_in_hand)
			self.assertEqual(nowlen,now2len)
		
			
class Hand_class_test3(unittest.TestCase):
	
	def test_constructor(self):
		d = Deck()
		hand1 = Hand(d,10)
		self.assertEqual(len(hand1.cards_in_hand),10)


class Hand_Class_Suit(unittest.TestCase):
	
	def test_suit(self):
		# by default, if I have more than 14 cards, there should be more than one suit
		d = Deck()
		hand1 = Hand(d,14)
		lensuit=hand1.get_suits_available()
	#	pdb.set_trace()
		#print(len(lensuit))

		self.assertTrue(len(lensuit)>1)

class Hand_suit_test(unittest.TestCase):

	def test_suit_2(self):
		
		f = Deck()
		hand1 = Hand(f,25)
		lensuit = hand1.get_suits_available()
		self.assertTrue(len(lensuit)>2)


class Hand_rank_test(unittest.TestCase):
	
	def test_rank(self):
		
		g = Deck()
		hand2 = Hand(g,17)
		rans = hand2.get_ranks_available()
		#print(rans)
		setranks= set([x for x in rans if rans.count(x) > 1])
		#pdb.set_trace()
		#print(setranks)
		self.assertTrue(len(setranks)==0)


class Hand_rank_test2(unittest.TestCase):
	
	def test_rank2(self):
		
		d1 = Deck()
		
		hand3 = Hand(d1,11)
		rans = hand3.get_ranks_available()
		setranks = set([ x for x in rans if rans.count(x) > 1])
		self.assertTrue(len(setranks)==0)

class Hand_specific_card(unittest.TestCase):
	
	def test_specific_card(self):
		
		d1 = Deck()
		hand3 = Hand(d1)
		onecard = Card(2,7)
		hand3.add_card(onecard)
		
		# to makesure it is in here
		returncard = hand3.specific_card("Hearts",7)
		#pdb.set_trace()
		self.assertEqual(returncard,onecard)


## Hints to help come up with tests:
## - Create a Deck instance in each method where you want to test an instance of class Hand, because you need a Deck instance to create a Hand instance!
## - To test the Hand constructor, you may want to test that the Hand class creates a hand with 3 cards if you pass in a Deck instance to the constructor, and use the default num_cards.
## - You should also test that if you pass in a specific number of cards to the Hand class constructor, it creates an instance of class Hand with that specific number of cards! Gotta be sure that part of the Hand class constructor (__init__ method) works correctly.



#############

unittest.main(verbosity=2) 
