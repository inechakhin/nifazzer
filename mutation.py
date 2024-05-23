import random


def delete_random_character(s: str) -> str:
    if s == "":
        return s
    pos = random.randint(0, len(s) - 1)
    return s[:pos] + s[pos + 1 :]


def insert_random_character(s: str) -> str:
    pos = random.randint(0, len(s))
    random_character = chr(random.randrange(32, 127))
    return s[:pos] + random_character + s[pos:]


def flip_random_character(s: str) -> str:
    if s == "":
        return s
    pos = random.randint(0, len(s) - 1)
    random_character = chr(random.randrange(32, 127))
    return s[:pos] + random_character + s[pos + 1 :]


def duplicate_random_character(s: str) -> str:
    if s == "":
        return s
    pos = random.randint(0, len(s) - 1)
    return s[:pos] + s[pos] + s[pos:]


def mutate(s: str) -> str:
    mutators = [
        delete_random_character,
        insert_random_character,
        flip_random_character,
        duplicate_random_character,
    ]
    mutator = random.choice(mutators)
    print(mutator)
    return mutator(s)


def mutation(list: list) -> list:
    new_list = []
    for s in list:
        new_list.append(mutate(s.decode()).encode())
    return new_list
