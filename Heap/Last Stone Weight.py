class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            two_largest = heapq.nlargest(2, stones, key=None)
            if two_largest[0] == two_largest[1]:
                stones.remove(two_largest[0])
                stones.remove(two_largest[1])
                if len(stones) == 0:
                    stones.append(0)
            elif two_largest[0] > two_largest[1]:
                new_weight = two_largest[0] - two_largest[1]
                stones.remove(two_largest[1])
                index_of_larger = stones.index(two_largest[0])
                stones[index_of_larger] = new_weight

        return (stones[0])




