def merge(intervals):
    # [[1,3], [2,6]]

    # sort the interval by the start (i[0])
    intervals.sort(key=lambda i: i[0])

    res = [intervals[0]]

    # iterate through the interval list
    for start, end in intervals[1:]:
        # if overlap, then merge

        # get the latest element by res[-1], and take the 'end' value res[-1][1]
        lastEnd = res[-1][1]
        if start <= lastEnd:
            res[-1][1] = max(lastEnd, end)
        else:
            res.append([start, end])

    return res


