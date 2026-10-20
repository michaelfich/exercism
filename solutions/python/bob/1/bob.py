RESPONSE_QUESTION = "Sure."
RESPONSE_YELLING = "Whoa, chill out!"
RESPONSE_YELLING_QUESTION = "Calm down, I know what I'm doing!"
RESPONSE_SILENCE = "Fine. Be that way!"
RESPONSE_DEFAULT = "Whatever."

def response(hey_bob):
    trimmed_message = hey_bob.strip()

    is_yelling = trimmed_message.isupper()
    is_blank = trimmed_message == ""
    is_question = not is_blank and trimmed_message[-1] == "?"

    if is_yelling and is_question:
        return RESPONSE_YELLING_QUESTION
    if is_yelling:
        return RESPONSE_YELLING
    if is_question:
        return RESPONSE_QUESTION
    if is_blank:
        return RESPONSE_SILENCE

    return RESPONSE_DEFAULT
