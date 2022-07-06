def intervalIntersection(firstList, secondList):
    # edge case
    if len(firstList) == 0 or len(secondList) == 0:
        return []

    i, j = 0, 0
    res = []
    while i < len(firstList) and j < len(secondList):
        firstListItem = firstList[i]
        secondListItem = secondList[j]

        max_start = max(firstListItem[0], secondListItem[0])
        min_end = min(firstListItem[1], secondListItem[1])

        if max_start <= min_end:
            res.append([max_start, min_end])

        endFirstListItem = firstListItem[1]
        endSecondListItem = secondListItem[1]

        if endFirstListItem <= endSecondListItem:

            i += 1
        else:
            j += 1
    return res