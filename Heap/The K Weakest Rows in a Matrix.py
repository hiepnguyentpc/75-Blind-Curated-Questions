class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        hashmap = {}
        for i in range(len(mat)):
            # print(Counter(mat[i])[1])
            hashmap.update({i: Counter(mat[i])[1]})

        hashmap = {k: v for k, v in sorted(hashmap.items(), key=lambda item: item[1])}
        sorted_key = list(hashmap.keys())

        res = []
        for i in range(k):
            res.append(sorted_key[i])

        return (res)


