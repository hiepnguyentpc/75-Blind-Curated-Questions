def carParkingRoof(cars, k):
    # Write your code here

    cars.sort()

    start = 0
    min = float('inf')
    while start + k - 1 < len(cars):
        end = start + k - 1
        length = cars[end] - cars[start] + 1
        if length < min:
            min = length
        start += 1
    return min

cars = [6,2,12,7]
k = 3
print(carParkingRoof(cars, k))