
arr = [1,2,3,3]

sumBottomUp = [0] * len(arr)
sumBottomUp[0] = arr[0]
for i in range(1, len(arr)):
    sumBottomUp[i] = sumBottomUp[i - 1] + arr[i]


sumTopDown = [0] * len(arr)
sumTopDown[len(arr) - 1] = arr[len(arr) - 1]
for i in range(len(arr) - 2, -1, -1):
    sumTopDown[i] = sumTopDown[i + 1] + arr[i]

for i in range(1, len(arr) - 1, 1):
    if sumBottomUp[i] == sumTopDown[i]:
        print(i)



