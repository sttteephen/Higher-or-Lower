from card import Card, Deck
import os

def get_card_value(card_number):
	if card_number == 'J' or card_number == 'Q' or card_number == 'K':
		card_number = 10
	elif card_number == 'A':
		card_number = 1
	else:
		card_number = int(card_number)

	return card_number

os.system('cls' if os.name == 'nt' else 'clear')

deck = Deck()
deck.shuffle()

card_list = deck._cards[:8]

print("Welcome to Higher or Lower!")
print("Guess 8 cards correctly to win.\n")

game_over = False

print("The first card is:", card_list[0])

while game_over == False:

	card = card_list.pop(0)
	card_one_number = card.number
	card_two_number = card_list[0].number

	card_one_number = get_card_value(card_one_number)
	card_two_number = get_card_value(card_two_number)

	guess = input("Do you think the next card will be higher(H) or lower(L)? ")[0].upper()
	print("The next card is", card_list[0], "\n")

	if (card_two_number < card_one_number) and (guess == 'L'):
		print("Correct!")
	elif (card_two_number > card_one_number) and (guess == 'H'):
		print("Correct!")
	else:
		print("Wrong. Better luck next time :(")
		game_over = True
		continue

	if (len(card_list) == 1):
		print("Well done, you've won!!!")
		print("See you next time.")
		game_over = True
		continue