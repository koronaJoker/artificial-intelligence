import re


def finite_automation(word):
    state = "q0"

    for symbol in word:

        if state == "q0":
            if symbol == "a":
                state = "q1"
            else:
                state = "dead"

        elif state == "q1":
            if symbol == "a":
                state = "q2"
            elif symbol == "d":
                state = "q4"
            else:
                state = "dead"

        elif state == "q2":
            if symbol == "b":
                state = "q3"
            else:
                state = "dead"

        elif state == "q3":
            if symbol == "c":
                state = "q1"
            else:
                state = "dead"

        elif state == "q4":
            if symbol == "e":
                state = "q5"
            else:
                state = "dead"

        elif state == "q5":
            if symbol == "d":
                state = "q4"
            else:
                state = "dead"

        elif state == "dead":
            state = "dead"


    if state == "q1":
        if word == "a":
            return False

        return True

    elif state == "q5":

        return True

    else:
        return False


def regg(word):
    pattern = r"^a(?:(abc)+(de)*|(de)+)$"

    return re.fullmatch(pattern, word) is not None


words = [
    "a",
    "aabc",
    "aabcabc",
    "ade",
    "adede",
    "aabcde",
    "aabcdede",
    "adeabc",
    "aab",
    "aabcd",
    "abc",
    "aabcdef"
]

for word in words:
    print(f"\nСлово: {word}")
    print(f"Автомат: {finite_automation(word)}")
    print(f"Регулярное выражение: {regg(word)}")


