def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    # Since heap is sorted in increasing order,
    # negate the distance to simulate max heap
    # and fill the heap with the first k elements of points

    minHeap = []
    for x, y in points:
        dist = (x ** 2) + (y ** 2)
        minHeap.append([dist, x, y])

    heapq.heapify(minHeap)

    res = []
    while k > 0:
        dist, x, y = heapq.heappop(minHeap)
        res.append([x, y])
        k -= 1

    return res