def isAnagram(self, s: str, t: str) -> bool:
    hashmap = {}
    for char in s:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1

    for char in t:
        if char in hashmap:
            hashmap[char] -= 1
        else:
            return False

    for item in hashmap:
        if hashmap[item] != 0:
            return False
    return True
