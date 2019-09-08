# BlackJack
This repository contains a Standard BlackJack game with some modified rules

##Goal:
The goal of this assignment is to code a game of black jack for any number of players
Scenario:
The game of Blackjack.
Terminology cards: a standard deck of playing cards is used, i.e., four suits (clubs, diamonds, spades, and hearts) and 13 different cards within each suit (the numbers 2 through 10, jack, queen, king, and ace). In this assignment, we will replace 10, jack, queen and king with a generic 'face card'. We will assume an infinite number of decks available in the pack.
card values: the numbered cards (2 through 9) count as their numerical value. The generic face card (replacing 10, jack, queen, and king) counts as 10, and the ace may count as either 1 or 11 (whichever works in the player's favor).
hand value: the value of a hand is the sum of the values of all cards in the hand. The values of the aces in a hand are such that they produce the highest value that is 21 or under (if possible). A hand where any ace is counted as 11 is called a soft hand. The suits of the cards do not matter in blackjack.
pair: the two card hand where both cards have the same value. (example, two aces, a pair of sixes, and for our assignment, a pair of face cards).
blackjack: is a two-card hand where one card is an ace and the other card is any face card.
busted: the value of the hand has exceeded 21.
Rules of Play
There are some slight variations on the rules and procedure of blackjack. Below is the simplified
procedure that we will use for this assignment. We will not be using insurance, surrender or dealer
peeking, which are options in a standard casino game.
1. Each player places a bet on the hand.
2. The dealer deals two cards to each player, including himself. The player's cards will be face-up.
One of the dealers cards is face-up, but the other is face-down.
3. If a player has blackjack, then that player wins immediately. The player makes a profit of 1.5
times his or her bet.
4. If not, the player must do one of the following:
H - Hit: the player receives one additional card (face up). A player can receive as many cards as
he or she wants, but if the value of the player's hand exceeds 21, the player busts and loses the bet
on this hand irrespective of dealer's hand.
S - Stand: the player does not want any additional cards
D - Double-down: before the player has received any additional cards, she may double-down. This
means that the player doubles her bet on the hand and will receive exactly one additional card. The
disadvantage of doubling-down is that the player cannot receive any more cards (beyond the one
additional card); the advantage is that the player can use this option to increase the bet when
conditions are favorable.
P - sPlit: before the player has received any additional cards, if the original hand is a pair, then the
player may split the hand. This means that instead of playing one hand the player will be playing
two independent hands. She puts in the bet amount for the second hand. Two additional cards are
drawn, one for each hand. The play goes on as if the player was playing two hands instead of one.
If the drawn cards result in more pairs she is allowed to resplit. The player is allowed endless
resplits in our version of the game. [There is an exception associated with a pair of Aces, see
below]
5. Once the player stands, the dealer turns over his face-down card. The dealer then hits or stands
according to the following deterministic policy: If the value of the hand is less than 17 (or soft 17),
the dealer must hit. Otherwise, the dealer must stand. This means, that the dealer stands if his Cards
are (A,2,4) because that makes a soft 17. If the dealer busts, then he loses the bets with the nonbusted
players.
6. PayOffs (in this order)
(a) If the player had a blackjack she already received 2.5 times her bet thus making a profit of 1.5
times. (b) If the player busted, she lost her bet.
(c) If the dealer busted, he lost and the dealer pays the player double her bet, i.e., the player makes
a profit equal to her bet.
(d) If the value of dealer's hand is greater than player's the player loses her bet.
(e) If the value of player's hand is greater than dealer's the player won and dealer pays double her
bet.
(f) If the dealer has blackjack and the player has non-blackjack 21 the dealer wins.
(g) If the value of the two hands is equal, it is a push and the player gets back her bet money. That
is, no profit no loss.
7. Other rules and exceptions.
(a) Doubling is allowed after split. That means, after splitting the pair, the player is allowed to
double down either or both her hands if she wishes to.
(b) Player can resplit as many times as she desires (whenever allowed).
(c) Splitting Aces. This is an exception to the rule. If the player gets a pair of aces that is a very
strong hand. She can split this but she will only get one additional card per split hand, and she will
not be allowed to resplit. Moreover, if the card is a face card, it will not be counted as blackjack,
and will be treated as a regular 21.
