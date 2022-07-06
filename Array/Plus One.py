def plusOne(digits) -> list:
    for i in range(1, len(digits) +1 ):
        if digits[-i] == 9:
            digits[-1] = 0
        else:
            digits[-1] += 1
            break
    if digits[0] == 0:
        digits[0] = 1
        digits.append(0)
    return digits

