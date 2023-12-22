
from enum import Enum
from functools import cmp_to_key
import re


class Hand_Type(Enum):
    FIVEOFAKIND = 1    
    FOURFOAKIND = 2
    FULLHOUSE = 3
    THREEOFAKIND = 4
    TWOPAIR = 5
    ONEPAIR = 6
    HIGHCARD = 7



# poker 5 cards
def hand_value(hand: str) -> int:

    # every char is the same:
    if len(set(hand)) == 1:
        return Hand_Type.FIVEOFAKIND.value
    
    # ful house
    if len(set(hand)) == 2:
        if hand.count(hand[0]) == 2 or hand.count(hand[0]) == 3:
            return Hand_Type.FULLHOUSE.value
        else:
            return Hand_Type.FOURFOAKIND.value
    
    # three of a kind
    if len(set(hand)) == 3:
        if hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
            return Hand_Type.THREEOFAKIND.value
        else:
            return Hand_Type.TWOPAIR.value
        
    # two pair
    if len(set(hand)) == 4:
        return Hand_Type.ONEPAIR.value
    
    # high card
    if len(set(hand)) == 5:
        return Hand_Type.HIGHCARD.value
    
    return -1


def compare_hands(hand1: str, hand2: str) -> int:

    if hand_value(hand1) > hand_value(hand2):
        return 1
    elif hand_value(hand1) < hand_value(hand2):
        return -1
    else:
        # here there should be char coparison A J Q K ...
        return hand1 > hand2

def run(input: list[str]):

    hands_with_bid = []

    for line in input:
        hand = line.split(' ')[0]
        bid = line.split(' ')[1]
        hands_with_bid.append((hand, bid))


    hands = []

    for hand, bid in hands_with_bid:
        print(f'hand: {hand} has value: {hand_value(hand)}')
        hands.append(hand)

    # aaa = hands.sort(key=compare_hands)
    aaa = sorted(hands, key=cmp_to_key(compare_hands))
    print(aaa)

    # # group hands by type
    # hands_grouped = {}

    # for hand in hands:
    #     value = hand_value(hand)
    #     if value in hands_grouped:
    #         hands_grouped[value].append(hand)
    #     else:
    #         hands_grouped[value] = [hand]

    # print(hands_grouped) 



