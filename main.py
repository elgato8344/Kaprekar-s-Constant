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

t_steps = find_steps(6829)
print(t_steps)
