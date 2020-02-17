#Deniz Erdem COMP 1405 Assignment 2
#student number: 101161756

#importing the random library
import random


#funciton that calculates the sum of the hand
def handSum(handList):
	total = 0
	#for loop that goes through every place in the list
	for x in range(0, len(handList)):
		if handList[x] == "J":
			total += 10
		elif handList[x] == "Q":
			total += 10
		elif handList[x] == "K":
			total += 10
		elif handList[x] == "A":
			if total < 11:
				total += 11
			else:
				total += 1
		else:
			total += handList[x]

	#return the total sum of the hand
	return total

#function that prints all the places in the list, used to print the hand list, no return value
def displayHand(handList):
	for x in range(0, len(handList)):
		print(handList[x])

#returns a card valued 1 to 11
def dealCard(hand, deck, timesThrough):
	hand.append(deck[timesThrough])
	return	hand

#function that creates an authentic deck
def createDeck():
	deck = ["A",2,3,4,5,6,7,8,9,10,"A", "J", "Q", "K"]*4
	return deck

#funciton that shuffles the deck
def shuffleDeck(deck):
	random.shuffle(deck)
	return deck

#function that gets the first two cards of the hand
def getHand(deck):
	hand = []
	hand.append(deck[0])
	hand.append(deck[1])
	return hand

#prints the hand list that is given to it	
def printHand(hand):
	print("Your hand:", end=" ")
	for x in range(0, len(hand)):
		print(hand[x], end=" ")
		


#gets the rank of the player relative to wha ttheir score was
def getRank(score):
	if score >= 95:
		return "95+: Ace!"
	elif score >= 85 and score <= 94:
		return "85 to 94: King"
	elif score >= 75 and score <= 84:
		return "75 to 84: Queen"	
	elif score >= 50 and score <= 74:
		return "50 to 74: Jack"
	elif score >= 25 and score <= 49:
		return "25 to 49: Commoner"
	else:
		return "-5 to 24: Noob"


#displays the score at the star tof each round
def displayScore(score):
	print("Your score is:",score)
	return


#main funciton where everythin happens
def main():	
	#Authorized variables 
	MAX_ROUNDS = 5
	HAND_POINTS_LIMIT = 21

	score = 100
	round = 1
	#make a deck
	deck = createDeck()
	while round <= MAX_ROUNDS:
		print("\n\n")
		#shuffle the deck
		deck = shuffleDeck(deck)
		#printing the score
		print("Round",round)
		displayScore(score)
		#gettin ghte first hand
		hand = getHand(deck)
		printHand(hand)
		print("\nThe sum of ur hand is:", handSum(hand),end=" ")
		answer = 0
		timesThrough = 2
		
		#error checking for the respomse and cases
		while answer != "stand":
			
			answer = input("\nWould you like to hit or stand?")
			#if they want a hit
			if answer == "hit":
				dealCard(hand, deck, timesThrough)
				timesThrough += 1
				#bust case
				if handSum(hand) > 21:
					print("Your hand is:" ,end=" ")
					printHand(hand)					
					print("\nBUST")
					score = score - 21
					answer = "stand"
				else:
					print()
				printHand(hand)
				print("\nThe sum of ur hand is:", handSum(hand), end=" ")			
			
			# if they want to stand
			elif answer == "stand":
				score -= (HAND_POINTS_LIMIT - handSum(hand))
			else:
				print("Please enter a valid input")

		round += 1

	#get rank
	rank = getRank(score)
	print("\n\nThank you for playing")
	print("Your rank is", rank)


#makes the main function work
if __name__== "__main__":
	main()




		