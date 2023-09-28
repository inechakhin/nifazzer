import sys


def find_pair(string: str, right_char: str, left_idx: int) -> int:
    left_char = string[left_idx]
    curr_idx = left_idx + 1

    if right_char == " " or left_char == "\"" or left_char == "*":
        while curr_idx < len(string):
            curr_char = string[curr_idx]
            if curr_char == right_char:
                break
            curr_idx = curr_idx + 1
    else:
        left_count = 0
        while curr_idx < len(string):
            curr_char = string[curr_idx]
            if curr_char == right_char:
                if left_count == 0:
                    break
                else:
                    left_count = left_count - 1
            if curr_char == left_char:
                left_count = left_count + 1
            curr_idx = curr_idx + 1

    return curr_idx


def find_index_of_char(string: str, char: str) -> int:
    i = 0
    while i < len(string):
        if string[i] == char:
            return i
        if string[i] == '"':
            i = find_pair(string, '"', i)
        i = i + 1
    return i


def get_repeat(tag):
    atleast, atmost = tag[1:].split(",")[0], tag[1:].split(",")[1]

    if atleast == "":
        atleast = 0
    else:
        atleast = int(atleast)

    if atmost == "":
        atmost = sys.maxsize
    else:
        atmost = int(atmost)

    return atleast, atmost
