

import itertools
import random
def karten_austeilen():
    WERT = ["2", "3", "4", "5", "6", "7", "8", "9", "10", " Bube ", "Dame", "König",  "Ass"]
    FARBE = ["Kreuz", "Herz", "Karo", "Pik"]
    kartenblatt = list(itertools.product(FARBE, WERT))
    Karten_deck = kartenblatt + kartenblatt
    random.shuffle(Karten_deck)
    hand1 = Karten_deck[0:13]

    zugstapel = Karten_deck[13:104]
    ablagestapel = []
    return hand1,zugstapel

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
    print('Es wurde gezogen:', quelle[-1])
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

def check_unique_farbe(auswahl_farbe):
    flag = len(set(auswahl_farbe)) == (len(auswahl_farbe))
    if (flag):
        print('Farbe ist unique.')
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

def checkConsecutiveEnde(l):
    if max(l) == 12:
        if min(l) == 0:
            l.remove(max(l))
    return sorted(l) == list(range(min(l), max(l)+1))

def ist_satz(hand, auswahl):
    if len(auswahl) < 3:
        print("list has not correct elements.")
        return False
    else:
        ##trenen karte von farbe und wert.
        hand_farbe, hand_wert = farbe_wert_trennen(hand)
        auswahl_wert = []
        auswahl_farbe = []
        for i in auswahl:
            auswahl_wert.append(hand_wert[i])
            auswahl_farbe.append(hand_farbe[i])
        print('Auswahl_wert')
        print(auswahl_wert)
        print('Auswahl_farbe ')
        print(auswahl_farbe )
        bool_gleich_wert = check_gleich_wert(auswahl_wert)
        bool_unique_farbe = check_unique_farbe(auswahl_farbe)
        if bool_gleich_wert and bool_unique_farbe:
            print('Die Karte bilden ein Satz')
            return True
        else:
            print('Die Karte bilden keinen Satz')
            return False

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
        bool_gleich_farbe = check_gleich_wert(auswahl_farbe)
        index_wert = [WERT.index(i) for i in auswahl_wert]
        bool_nuerische_wert = checkConsecutiveEnde(index_wert)
        if bool_gleich_farbe and bool_nuerische_wert:
            print('Die Karte bilden ein Sequence')
            return True
        else:
            print('Die Karte bilden keinen Sequence')
            return False

def zaehle_punkte(liste):
    WERT = ["2", "3", "4", "5", "6", "7", "8", "9", "10", " Bube ", "Dame", "König", "Ass"]
    WERT_add = ["2", "3", "4", "5", "6", "7", "8", "9", "10", " 10 ", " 10 ", " 10 ", " 11 "]
    hand_farbe, hand_wert = farbe_wert_trennen(liste)
    auswahl = list(range(len(liste)))
    auswahl_wert = [hand_wert[i] for i in auswahl]
    index_wert = [WERT.index(i) for i in auswahl_wert]
    if bool_sequenz and set([0, 12]).issubset(index_wert):
        WERT_add = ["2", "3", "4", "5", "6", "7", "8", "9", "10", " 10 ", " 10 ", " 10 ", " 1 "]
        punkte_list = [int(WERT_add[i]) for i in index_wert]
    else:
        punkte_list = [int(WERT_add[i]) for i in index_wert]
    sum_p = sum(punkte_list)
    return sum_p

def anfragen_soll_ausgelegt_test(hand):
    # Set new_name to something other than 'quit'.
    soll_ausgelegt = ''
    auswahl_list = []
    # Start a loop that will run until the user enters 'quit'.
    while soll_ausgelegt != 'n':
        # Ask the user for a name.
        soll_ausgelegt = input("Soll ausgelegt werden (j/n)? ")
        if soll_ausgelegt:
            game_running =True
        else:
            game_running = False

        while game_running:
            guess = input("Welche Karte auslegen (1-14, Ende zum Beenden der Auswahl):")
            # Does the user want to quit?
            if guess == "Ende":
                game_running = False
                print('auswahl:', auswahl_list)

                auswahl_list = [i-1 for i in auswahl_list]
                auswahl_karte = [hand[i] for i in auswahl_list]
                print('auswahl_karte:', auswahl_karte)
                bool_satz = ist_satz(hand, auswahl_list)
                bool_sequenz = ist_sequenz(hand, auswahl_list)
                if (bool_satz  or bool_sequenz):
                    auswahl_karte = [hand[i] for i in auswahl_list]
                    for i in auswahl_karte:
                        hand.remove(i)
                    print('Ausgelegt wurden',auswahl_karte)
                    print('Hand:',hand)

                break

            # Otherwise, nop2e, player wants to keep going
            else:
                # Convert the players guess from a string to an integer
                guess_number = int(guess)
                # Add the new name to our list.
                auswahl_list.append(guess_number)


###Teil1
hand1,zugstapel = karten_austeilen()

##teil2
print('Hand 1:')
print(hand1)
hand1 = karte_ziehen(hand1,zugstapel)
print('Hand 1:')
#anfragen_soll_ausgelegt_test(hand1)


auswahl_list =[]
# Set our game ending flag to False
bool_auswahl  = input("Soll ausgelegt werden (j/n)?")
if bool_auswahl == 'j':
    game_running = True
elif bool_auswahl == 'n':
    game_running = False
    auswahl = int(input("Weleche karte ablegen (1-14)?"))

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
            auswahl_karte = [hand1[i] for i in auswahl_list]
            print('auswahl_karte:', auswahl_karte)
            bool_satz = ist_satz(hand1, auswahl_list)
            bool_sequenz = ist_sequenz(hand1, auswahl_list)
            if (bool_satz  or bool_sequenz):
                save_list = [hand1[i] for i in auswahl_list]
                for i in save_list:
                    hand1.remove(i)
                punkte = zaehle_punkte(save_list)

                print("Ausgelegt wurden mit (%s)" % punkte)
                print('Hand 1:',hand1)



            break

        # Otherwise, nop2e, player wants to keep going
        else:
            # Convert the players guess from a string to an integer
            guess_number = int(guess)
            # Add the new name to our list.
            auswahl_list.append(guess_number)



bool_auswahl1  = input("Soll ausgelegt werden (j/n)?")
if bool_auswahl1 == 'n':
    auswahl_end = int(input("Weleche karte ablegen (1-11)?"))
    karte_ablegen(hand1,auswahl_end)
    print('Hand 1:')
    print(hand1)








