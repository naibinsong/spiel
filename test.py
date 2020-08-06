# Give the user some context.


import itertools
import random
def karten_austeilen():
    WERT = ["2", "3", "4", "5", "6", "7", "8", "9", "10", " Bube ", "Dame", "König",  "Ass"]
    FARBE = ["Kreuz", "Herz", "Karo", "Pik"]
    kartenblatt = list(itertools.product(FARBE, WERT))
    Karten_deck = kartenblatt + kartenblatt
    random.shuffle(Karten_deck)
    hand1 = Karten_deck[0:14]
    hand2 = Karten_deck[14:27]
    hand3 = Karten_deck[27:40]
    zugstapel = Karten_deck[40:104]
    ablagestapel = []
    return hand1,hand2,hand3,zugstapel,ablagestapel

def farbe_wert_trennen(hand):
    hand_farbe = []
    hand_wert = []
    for i in hand:
        #print(i)
        hand_farbe.append (i[0])
        hand_wert.append (i[1])
    return hand_farbe, hand_wert

def karte_ablegen(hand,auswahl):
    #print(hand[auswahl-1])
    auswahl_karte = hand[auswahl-1]
    #print(hand)
    del hand[auswahl-1]
    #print(hand)
    return auswahl_karte

def karte_ziehen(hand,quelle):
    hand.append(quelle[-1])
    del quelle[-1]
    return hand



def farbe_wert_trennen(hand):
    Hand_Farbe = []
    Hand_Wert = []
    for i in hand:
        #print(i)
        Hand_Farbe.append (i[0])
        Hand_Wert.append (i[1])
    return Hand_Farbe, Hand_Wert

def check_unique_farbe(hand_farbe,auswahl):
    auswahl_farbe =[]
    for i in auswahl:
        auswahl_farbe.append(hand_farbe[i])
    flag = len(set(auswahl_farbe))== (len(auswahl_farbe))
    if (flag):
        print('Farbe ist unterschiedlich.')
        unque_farbe = True
    else:
        print('Farbe ist nicht unique.')
        unque_farbe = False
    return unque_farbe


def check_gleich_wert(auswahl_wert):
    count_same_element = auswahl_wert.count(auswahl_wert[0])
    #print(count_same_element)
    if count_same_element == len(auswahl_wert):
        #print('all the element is the same.')
        gleich_wert = True
    else:
        #print("nicht gleich Farbe.")
        gleich_wert = False
    return gleich_wert


def ist_satz(hand, auswahl):
    if len(auswahl) > 2:

        ##trenen karte von farbe und wert.
        hand_farbe, hand_wert = farbe_wert_trennen(hand)
        ##
        auswahl_wert = []
        auswahl_farbe = []
        for i in auswahl:

            auswahl_wert.append(hand_wert[i])

        bool_gleich_wert = check_gleich_wert(auswahl_wert)
        if bool_gleich_wert:
            bool_unique_farbe = check_unique_farbe(hand_farbe,auswahl)
            if bool_unique_farbe:
                print('Die Karte bilden ein Satz')
                return True
            else:
                print('Die Karte bilden keinen Satz')
                return False
        else:
            print('Die Karte bilden keinen Satz')
            return False
    else:
        print("list has not correct elements.")
        return False

def checkConsecutiveEnde(l):
    if max(l) == 12:
        if min(l) == 0:
            l.remove(max(l))
    return sorted(l) == list(range(min(l), max(l)+1))

def ist_sequenz(hand,auswahl):
    if len(auswahl) <3:
        print("list has not correct elements.")
        return False

    else:
        WERT = ["2", "3", "4", "5", "6", "7", "8", "9", "10", " Bube ", "Dame", "König", "Ass"]
        ##trenen karte von farbe und wert.
        hand_farbe, hand_wert = farbe_wert_trennen(hand)
        auswahl_farbe = []
        auswahl_wert = []
        for i in auswahl:
            auswahl_wert.append(hand_wert[i])
            auswahl_farbe.append(hand_farbe[i])
        print('Auswahl_wert')
        print(auswahl_wert)
        bool_gleich_farbe = check_gleich_wert(auswahl_farbe)
        if bool_gleich_farbe:
            print('gleiche Farbe')
            index_wert = [WERT.index(i) for i in auswahl_wert]
            print(index_wert)
            bool_nuerische_wert = checkConsecutiveEnde(index_wert)
            if bool_nuerische_wert:
                print('Die Karte bilden ein Ssequence')
                return True
            else:
                print('Die Karte bilden keinen Ssequence')
                return False



auswahl_list =[]
# Set our game ending flag to False
bool_auswahl  = input("Soll ausgelegt werden (j/n)?")
if bool_auswahl == 'j':
    game_running = True
elif bool_auswahl == 'n':
    game_running = False
    auswahl = int(input("Weleche karte ablegen (1-14)?"))
    abgelegt_karte = karte_ablegen(hand3, auswahl)
    ablagestapel.append(abgelegt_karte)
    print('ablagestapel :')
    print(ablagestapel)
    print('Hand 3:')
    print(hand3)
    print('zugstapel')
    print(zugstapel)

while game_running:

    # Greet the user to our game
    #print("I'm thinking of a number between 1 and 10, can you guess it?")


    # Set the player's guess number to something outside the range
    guess_number = 0

    # Loop until the player guesses our number
    while guess_number != "Ende":

        guess = input("Welche Karte auslegen (1-14, Ende zum Beenden der Auswahl):")
        # Does the user want to quit?
        if guess == "Ende":
            game_running = False
            print('auswahl:', auswahl_list)
            auswahl_list = [i-1 for i in auswahl_list]
            bool_satz = ist_satz(hand3, auswahl_list)
            bool_sequenz = ist_sequenz(hand3, auswahl_list)
            if bool_sequenz or bool_satz:
                auswahl_karte = [hand3[i] for i in auswahl_list]
                for i in auswahl_karte:
                    hand3.remove(i)
                print('Ausgelegt wurden',auswahl_karte)
                print('Hand 3:',hand3)
                auswahl = int(input("Weleche karte ablegen (1-11)?"))
                abgelegt_karte = karte_ablegen(hand3, auswahl)
                ablagestapel.append(abgelegt_karte)
                print('ablagestapel :')
                print(ablagestapel)
                print('Hand 3:')
                print(hand3)

            break

        # Otherwise, nop2e, player wants to keep going
        else:
            # Convert the players guess from a string to an integer
            guess_number = int(guess)
            # Add the new name to our list.
            auswahl_list.append(guess_number)


