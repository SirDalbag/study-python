# Task 1. Анаграмм.
def anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)


def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) == 0 and len(s2) == 0:
        return True
    if s1[0] in s2:
        return is_anagram(s1[1:], s2.replace(s1[0], "", 1))
    else:
        return False
