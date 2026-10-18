def find_steps_v2(number: int):
    '''I lied, here is attempt 2 after giving this a bit more thought.'''
    steps = 0
    while number not in (6174, 0):
        steps += 1
        q, d4 = divmod(number, 10)
        q, d3 = divmod(q, 10)
        d1, d2 = divmod(q, 10)
        digits = [d1, d2, d3, d4]
        digits.sort(reverse=True)
        number = (
            999 * (digits[0] - digits[3]) + 90 * (digits[1] - digits[2])
        )
        print(f"{number:04d}")
    return steps

print(f"{{find_steps_v2(1234)}")
