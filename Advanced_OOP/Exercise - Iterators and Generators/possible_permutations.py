def possible_permutations(lst):
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            current = lst[i]
            remaining = lst[:i] + lst[i+1:]
            for perm in possible_permutations(remaining):
                yield [current] + perm


[print(n) for n in possible_permutations([1, 2, 3])]