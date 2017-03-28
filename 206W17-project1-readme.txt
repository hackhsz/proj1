206 Project 1 - Code for playing cards
README

Your name:Shizhong_Hu
Anyone you worked with: None

----- Add your README file content for the Project 1 code.

This code ... <your overall description should go here; continue below!>.

1. Code Description 

This code bascially creates three class, namely Card, Deck and Hand used by Player to play a game to compete the final score. The result will be three types, p1 wins, p2 wins or a tie. From the Card class, we know that it has a function called suit names to support four suits, a rank level list and the constructor and str_method. The deck objects supports the function for a deck, including shufffling a deck, pop a card or replace a card while the Hand includes what a player has during the game. 


2a

Class Card
      It creates a Card instance with rank and suit.
      2. The default constructor of Card will create a card with rank 2 and suit of Hearts.
      3. (a) suit_names:a public list variable functions as a string list for the instances
      	 (b) rank_levels:a public list variable functions as a list for the ranks on the instances
	 (c) faces: a dict for all the ranks that are greater than 10
	 (d) constructor: the default constructor was explained above while the input could be a suit defined in the suit_names and a rank value from 1 to 13.It creates an instance with the settgin involved
	 (e) string function will print the card instance into "rank" of "suit"

Class Deck
      It creates a deck instance with 56 cards
      2. The default constrcutor will create a deck without taking an argument.      3. (a) the constructor takes nothing and add cards into the deck
      	 (b) The pop_card method takes an integer which pop a card, the defaultcard is the last one in the deck and returns the card popped. 
	 (c) The shuffle method takes no arguement but use an random shuffle method to shuffle the whole deck
	 (d) The replace_card method takes an argument of a card, and append this card to the last of the deck if it is not in the deck
	 (e) The sort_cards method takes no argument  

Class Hand
      It creates a hand of cards of a player
      2. The default constructor takes three arguments including a deck, itself and the number of cards to have for a hand. It creates a deck
      3. (a) place_card method takes an integer indexing the place of the card in player's hand, and pop it from player's hand and return it
      	 (b) get_suits availible: takes no argument and return all the cards availbile from the hand
	 (c) get_ranks_available: takes no argument and return all the ranks avaibale(a set) from the hand
	 (d) specific card: takes an argument of a card, return this card by calling the place_card method if found this card in the hand. Return none if not found
	 (e) add_card: add card to hand if there is no same ones. 

	 
