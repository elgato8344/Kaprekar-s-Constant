# Kaprekar's Constant (6174)
# • The Math: Take any 4-digit number (as long as it is not all identical digits,
# like 1111). Arrange the digits in descending order, then ascending order, and
# subtract the smaller number from the larger one. If you repeat this process, you
# will always reach the number 6174 in 7 steps or fewer.
# • The Challenge: Write a Python function that takes a 4-digit number, loops through
# the subtraction steps, and counts how many iterations it takes to hit 6174.

def find_steps(n: int):
    """first and maybe only attempt at this one, I am liking how this one looks"""
    num = f"{n:04d}"
    steps = 0
    while num not in ("6174", "0000"):
        steps += 1
        desc = ''.join(sorted(num, reverse=True))
        asc = desc[::-1]
        diff = int(desc) - int(asc)
        print(f"{diff:04d}")
        num = f"{diff:04d}"
    return steps

# t_steps = find_steps(6829)
# print(t_steps)

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
