import collections


def groupAnagrams(strs):
    map = collections.defaultdict(list)
    for item in strs:
        map[tuple(sorted(item))].append(item)

    return map.values()

def groupAnagrams2(strs):
    map = collections.defaultdict(list)

    for item in strs:
        count = [0] * 26
        for char in item:
            count[ord(char) - ord('a')] += 1

        map[tuple(count)].append(item)
    return map.values()