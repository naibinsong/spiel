

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
    hand.append(quelle[0])
    del quelle[0]
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

def check_gleich_farbe(auswahl_farbe):
    count_same_element = auswahl_farbe.count(auswahl_farbe[0])
    #print(count_same_element)
    if count_same_element == len(auswahl_farbe):
        #print('all the element is the same.')
        gleich_wert = True
    else:
        #print("nicht gleich Farbe.")
        gleich_wert = False
    return gleich_wert

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


WERT = ["2", "3", "4", "5", "6", "7", "8", "9", "10", " Bube ", "Dame", "König", "Ass"]
WERT_add = ["2", "3", "4", "5", "6", "7", "8", "9", "10", " 10 ", " 10 ", " 10 ", " 11 "]
FARBE = ["Kreuz", "Herz", "Karo", "Pik"]
index= 3

#randoWert = ["2", "König", "Ass"]
randoWert = [ "Ass"]*3
#randomfarbe = ["Kreuz"] * 3
randomfarbe = ["Kreuz", "Herz", "Karo"]
karte_teil = list(zip(randomfarbe,randoWert))

auswahl =list(range(len(karte_teil)))
bool_satz = ist_satz(karte_teil, auswahl)
bool_sequenz = ist_sequenz(karte_teil , auswahl)
if bool_sequenz or bool_satz:
    save_list = [karte_teil[i] for i in auswahl]
    print(save_list)
    punkte = zaehle_punkte(save_list)
    print(punkte)
    print("Welche Karte ablegen (1-%s)" % len(save_list))
else:
    print('keinen satz or sequenze')







