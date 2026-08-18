from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        counts = Counter(hand)

        for h in hand:
            if counts[h] == 0:
                continue
            for i in range(h, h+groupSize):
                if counts[i] == 0:
                    return False
                counts[i] -= 1
        return True
                





