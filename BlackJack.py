import random
card_value = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,[1,11],[1,11],[1,11],[1,11]]

def Option(player_card,dealer_card,card_value,i,hands,bet):
    #hit stand split double_down
    print("Here are the options of the game for hand {} ".format(i))
    print("1: Hit")
    print("2: Stand")
    print("3: Split")
    print("4: Double Down")
    
    c = input("Please enter your decision ")
    if c == '1':
        player_card[i].extend(Hit(card_value))
        return True
    elif c == '2':
        Stand(dealer_card,card_value)
        #player_card.pop(i)
        #bet.pop(i)
        hands.remove(i)
        return
    elif c == '3':
        print("For Ace type 1 or 11 ")
        value = int(input("card you wants to resplit: "))
        hand = int(input("Which hand to split: "))
        if value == 1 or value == 11:
            value = [1,11]
        Split(player_card,dealer_card,value,card_value,hand,bet)
        return True
    elif c == '4':
        Double_Down(player_card[i],dealer_card,i,bet)
        #player_card.pop(i)
        hands.remove(i)
def Hit(card_value):
    return random.sample(card_value,1)

def Stand(dealer_card,card_value):
    dealer_total = Card_Sum(dealer_card)
    if dealer_total < 17:
        dealer_card.extend(Hit(card_value))

def Double_Down(player_card,dealer_card,i,bet):
    bet[i] = 2*bet[i][0]
    player_card.extend(Hit(card_value))

def Split(player_card,dealer_card,value,card_value,hand,bet):
    global hands
    global hand_count
    counter = 0
    for i in range(len(player_card[hand])):
        if value == player_card[hand][i]:
            counter += 1
    if counter == 1:
        print("sorry you can't split ")
        return
    hand_count += 1
    dollar = int(input("How much money you will bet for this hand "))
    if value == [1,11]:
        bet[hand_count] = [dollar]
        player_card[hand_count] = [value]
        player_card[hand].remove(value)
        player_card[hand].extend(Hit(card_value))
        player_card[hand_count].extend(Hit(card_value))
        hands.remove(hand)
    else:  
        hands.append(hand_count)
        bet[hand_count] = [dollar]
        player_card[hand_count] = [value]
        player_card[hand].remove(value)
        player_card[hand].extend(Hit(card_value))
        player_card[hand_count].extend(Hit(card_value))
        

    
def Card_Sum(player_card):
    cards = len(player_card)
    total = 0
    aces = []
    for i in range(cards):
        try:
            total += player_card[i]
        except TypeError:
            aces.append(player_card[i])
    if len(aces):
        if len(aces)>1 and total + 11 + len(aces)-1 <= 21:
            return total + 11 + len(aces)-1
        elif total <= 10:
            return total + 11
        else:
            return total + len(aces)
    return total   
            
            
        
    
def Busted(player_card):
    if Card_Sum(player_card) > 21:
        return True
    return False

def BlackJack(player_card):
    if Card_Sum(player_card) == 21 and len(player_card) == 2:
        return True
    return False
        
def WhoWon(player_card,dealer_card,bet,i):
    player_total = Card_Sum(player_card)
    dealer_total = Card_Sum(dealer_card)
    
    if Busted(player_card):
        print("Your hand {} loses {} dollar ".format(i,bet[i]))
        print("Dealer Cards ",dealer_card)
        print("Player Cards ",player_card)
    elif Busted(dealer_card):
        print("Your hand {} wins a profit of {} dollar ".format(i,bet[i]))
        print("Dealer Cards ",dealer_card)
        print("Player Cards ",player_card)
    elif dealer_total > player_total:
        print("Your hand {} loses {} dollar ".format(i,bet[i]))
        print("Dealer Cards ",dealer_card)
        print("Player Cards ",player_card)
    elif  dealer_total < player_total:
        print("Your hand {} wins a profit of {} dollar ".format(i,bet[i]))
        print("Dealer Cards ",dealer_card)
        print("Player Cards ",player_card)
    else:
        print("no conclusion")
        print("Dealer Cards ",dealer_card)
        print("Player Cards ",player_card)

        
player_card = {}
dealer_card = []
bet = {}
hands = [1]
hand_count = 1
player_card[1] = random.sample(card_value,2)
dealer_card.extend(random.sample(card_value,2))
true = True
dollar = int(input("How much you are betting for this game for hand 1 "))
bet[1] = [dollar]
while true:
    hands1 = hands[:]
    for i in hands1:
        print("dealer cards are: ",dealer_card[0]," x")
        print("player cards are: ",player_card)
        if BlackJack(player_card[i]):
            print("Your hand {} wins and made a profit of {} ".format(i,1.5*bet[i]))
            print("Dealer Cards: ",dealer_card)
            print("your cards of hand {} are: ".format(i),player_card[i])
            player_card.pop(i)
            bet.pop(i)
            hands.remove(i)
        elif Busted(player_card[i]):
            print("Your hand {} loses {} ".format(i,bet[i]))
            print("Dealer Cards: ",dealer_card)
            print("your cards: of hand {} are ".format(i),player_card[i])
            player_card.pop(i)
            bet.pop(i)
            hands.remove(i)
        else:
            Option(player_card,dealer_card,card_value,i,hands,bet)
    if not len(hands):
        break
for i in player_card:
    WhoWon(player_card[i],dealer_card,bet,i)
