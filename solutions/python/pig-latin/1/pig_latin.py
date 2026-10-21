VOWELS = ["a", "e", "i", "o", "u"]

def translate(text):
    words = []

    for word in text.split():
        words.append(_translate_word(word))

    return " ".join(words)


def _translate_word(word):
    first_letter = word[0:1]
    first_two_letters = word[0:2]

    if first_letter in VOWELS or first_two_letters in ["xr", "yt"]:
        return word + "ay"

    for n, char in enumerate(word):
        if char == "u" and n > 0 and word[n - 1:n + 1] == "qu":
            return word[n + 1:] + word[:n + 1] + "ay"
        if char == "y" and n > 0:
            return word[n:] + word[:n] + "ay"
        if char in VOWELS:
            return word[n:] + word[0: n] + "ay"

    return ""
