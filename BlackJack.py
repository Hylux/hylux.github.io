import random
##Create Deck
deck = {}
for card in range(13):
    if card == 0:
        deck.update({"A S" : 1})
    elif card == 10:
        deck.update({"J S" : 10})
    elif card == 11:
        deck.update({"Q S" : 10})
    elif card == 12:
        deck.update({"K S" : 10})
    else:
        deck.update({str(card + 1) + " S" : card + 1})
for card in range(13):
    if card == 0:
        deck.update({"A H" : 1})
    elif card == 10:
        deck.update({"J H" : 10})
    elif card == 11:
        deck.update({"Q H" : 10})
    elif card == 12:
        deck.update({"K H" : 10})
    else:
        deck.update({str(card + 1) + " H" : card + 1})
for card in range(13):
    if card == 0:
        deck.update({"A C" : 1})
    elif card == 10:
        deck.update({"J C" : 10})
    elif card == 11:
        deck.update({"Q C" : 10})
    elif card == 12:
        deck.update({"K C" : 10})
    else:
        deck.update({str(card + 1) + " C" : card + 1})
for card in range(13):
    if card == 0:
        deck.update({"A D" : 1})
    elif card == 10:
        deck.update({"J D" : 10})
    elif card == 11:
        deck.update({"Q D" : 10})
    elif card == 12:
        deck.update({"K D" : 10})
    else:
        deck.update({str(card + 1) + " D" : card + 1})
        
##Player Data        
playerCount = int(raw_input("Number of Players (Max 4): "))
hand1 = {}
hand2 = {}
hand3 = {}
hand4 = {}
money1 = 1000
money2 = 1000
money3 = 1000
money4 = 1000


def drawCard(hand):
    c1 = random.choice(deck.keys())
    hand.update({c1 : deck[c1]})
    del deck[c1]

for deal in range(playerCount):
    if deal < 1:
        raw_input("Enter any key when you are ready.")
        drawCard(hand1)
        drawCard(hand1)
        print "Player 1 hand: ", hand1.keys()
        print "Hand value is: ", sum(hand1.values())
        raw_input("Enter any key if you are done.")
    elif deal < 2:
        raw_input("Enter any key when you are ready.")
        drawCard(hand2)
        drawCard(hand2)
        print "Player 2 hand: ", hand2.keys()
        print "Hand value is: ", sum(hand2.values())
        raw_input("Enter any key if you are done.")
    elif deal < 3:
        raw_input("Enter any key when you are ready.")
        drawCard(hand3)
        drawCard(hand3)
        print "Player 3 hand: ", hand3.keys()
        print "Hand value is: ", sum(hand3.values())
        raw_input("Enter any key if you are done.")
    elif deal < 4:
        raw_input("Enter any key when you are ready.")
        drawCard(hand4)
        drawCard(hand4)
        print "Player 4 hand: ", hand4.keys()
        print "Hand value is: ", sum(hand4.values())
        raw_input("Enter any key if you are done.")

##Win Condition
end = {}
end1 = sum(hand1.values())
end2 = sum(hand2.values())
end3 = sum(hand3.values())
end4 = sum(hand4.values())
cdn1 = "Null"
cdn2 = "Null"
cdn3 = "Null"
cdn4 = "Null"

for turn in range(5):
    ##Player 1
    if playerCount > 0:
        cdn1 = ""
        raw_input("Enter any key when you are ready.")
        while sum(hand1.values()) < 21:
            print "Turn: ", turn + 1, "Current player:  Player 1 ", "Current hand: ", hand1.keys(), " Value: ", sum(hand1.values())
            draw = raw_input("Do you draw a card? (Y/N)")
            if draw == "Y" or draw == "y":
                draw = True
            else:
                draw = False
            if draw == True:
                drawCard(hand1)
                print hand1
                print "Hand value is: ", sum(hand1.values())
            elif draw == False:
                print "You passed."
            if sum(hand1.values()) == 21 or (len(hand1.keys()) > 4 and sum(hand1.values()) < 21):
                cdn1 = "W1"
                end.update({cdn1 : end1})
                print "You've won! But don't tell the others."
            elif sum(hand1.values()) > 21:
                cdn1 = "1"
                end.update({cdn1 : end1})
                print "You've lost! But don't tell the others."
            break
        else:
            print "Turn: ", turn + 1, "Current Player: Player 1"
            if sum(hand1.values()) == 21:
                print "You've won! But don't tell the others."
            elif sum(hand1.values()) > 21:
                print "You've lost! But don't tell the others."
        raw_input("Enter any key if you are done.")
    ##Player 2
    if playerCount > 1:
        cdn1 = ""
        raw_input("Enter any key when you are ready.")
        while sum(hand2.values()) < 21:
            print "Turn: ", turn + 1, "Current player:  Player 2 ", "Current hand: ", hand2.keys(), " Value: ", sum(hand2.values())
            draw = raw_input("Do you draw a card? (Y/N)")
            if draw == "Y" or draw == "y":
                draw = True
            else:
                draw = False
            if draw == True:
                drawCard(hand2)
                print hand2
                print "Hand value is: ", sum(hand2.values())
            elif draw == False:
                print "You passed."
            if sum(hand2.values()) == 21 or (len(hand2.keys()) > 4 and sum(hand2.values()) < 21):
                cdn2 = "W2"
                end.update({cdn2 : end2})
                print "You've won! But don't tell the others."
            elif sum(hand2.values()) > 21:
                cdn2 = "2"
                end.update({cdn2 : end2})
                print "You've lost! But don't tell the others."
            break
        else:
            print "Turn: ", turn + 1, "Current Player: Player 1"
            if sum(hand2.values()) == 21:
                print "You've won! But don't tell the others."
            elif sum(hand2.values()) > 21:
                print "You've lost! But don't tell the others."
        raw_input("Enter any key if you are done.")
    ##Player 3
    if playerCount > 2:
        cdn1 = ""
        raw_input("Enter any key when you are ready.")
        while sum(hand3.values()) < 21:
            print "Turn: ", turn + 1, "Current player:  Player 3 ", "Current hand: ", hand3.keys(), " Value: ", sum(hand3.values())
            draw = raw_input("Do you draw a card? (Y/N)")
            if draw == "Y" or draw == "y":
                draw = True
            else:
                draw = False
            if draw == True:
                drawCard(hand3)
                print hand3
                print "Hand value is: ", sum(hand3.values())
            elif draw == False:
                print "You passed."
            if sum(hand3.values()) == 21 or (len(hand3.keys()) > 4 and sum(hand3.values()) < 21):
                cdn3 = "W3"
                end.update({cdn3 : end3})
                print "You've won! But don't tell the others."
            elif sum(hand3.values()) > 21:
                cdn3 = "3"
                end.update({cdn3 : end3})
                print "You've lost! But don't tell the others."
            break
        else:
            print "Turn: ", turn + 1, "Current Player: Player 1"
            if sum(hand3.values()) == 21:
                print "You've won! But don't tell the others."
            elif sum(hand3.values()) > 21:
                print "You've lost! But don't tell the others."
        raw_input("Enter any key if you are done.")
    ##Player 4
    if playerCount > 3:
        cdn1 = ""
        raw_input("Enter any key when you are ready.")
        while sum(hand4.values()) < 21:
            print "Turn: ", turn + 1, "Current player:  Player 4 ", "Current hand: ", hand4.keys(), " Value: ", sum(hand4.values())
            draw = raw_input("Do you draw a card? (Y/N)")
            if draw == "Y" or draw == "y":
                draw = True
            else:
                draw = False
            if draw == True:
                drawCard(hand4)
                print hand4
                print "Hand value is: ", sum(hand4.values())
            elif draw == False:
                print "You passed."
            if sum(hand4.values()) == 21 or (len(hand4.keys()) > 4 and sum(hand4.values()) < 21):
                cdn4 = "W4"
                end.update({cdn4 : end4})
                print "You've won! But don't tell the others."
            elif sum(hand4.values()) > 21:
                cdn4 = "4"
                end.update({cdn4 : end4})
                print "You've lost! But don't tell the others."
            break
        else:
            print "Turn: ", turn + 1, "Current Player: Player 1"
            if sum(hand4.values()) == 21:
                print "You've won! But don't tell the others."
                
            elif sum(hand4.values()) > 21:
                print "You've lost! But don't tell the others."
        raw_input("Enter any key if you are done.")
    if turn == 4:
        print "The round has ended.", "Deck: ", len(deck)
    ##Check Game End
    if len(cdn1) != 0 and len(cdn2) != 0 and len(cdn3) != 0 and len(cdn4) != 0:
        print "The round has ended.", "Deck: ", len(deck)
        break

def winCheck():
    ##Determine Winners and Losers
    print "Player 1: ", end1, "|","Player 2: ", end2, "|","Player 3: ", end3, "|","Player 4: ", end4 ##Don't display non-players
    #Player 1
    if playerCount > 0:
        if end1 > 21:
            print "Player 1 overshot."
        elif len(hand1.keys()) > 4:
            print "Player 1 has 5 cards!"
        elif end1 == 21:
            print "Player 1 got exactly 21!"
        else:
            cdn1 = "DK1"
            end.update({cdn1 : end1})
    #Player 2
    if playerCount > 1:
        if end2 > 21:
            print "Player 2 overshot."
        elif len(hand2.keys()) > 4:
            print "Player 2 has 5 cards!"
        elif end2 == 21:
            print "Player 2 got exactly 21!"
        else:
            cdn2 = "DK2"
            end.update({cdn2 : end2})
    ##Player 3
    if playerCount > 2:
        if end3 > 21:
            print "Player 3 overshot."
        elif len(hand3.keys()) > 4:
            print "Player 3 has 5 cards!"
        elif end3 == 21:
            print "Player 3 got exactly 21!"
        else:
            cdn3 = "DK3"
            end.update({cdn3 : end3})
    ##Player 4
    if playerCount > 3:
        if end4 > 21:
            print "Player 4 overshot."
        elif len(hand4.keys()) > 4:
            print "Player 4 has 5 cards!"
        elif end4 == 21:
            print "Player 4 got exactly 21!"
        else:
            cdn4 = "DK4"
            end.update({cdn4 : end4})
    ##Compute End
    rank = []
    same = []
    cdn = end.keys()
    print cdn


            
        
    
    
     
    
        


































