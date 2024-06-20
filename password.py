import string
import random


class Password:

    @staticmethod
    def generate_password(length=8, use_letters=True, use_digits=True, use_punctuation=True) -> str:
        password, characters = "", ""

        if use_letters:
            characters += string.ascii_letters
        if use_digits:
            characters += string.digits
        if use_punctuation:
            characters += string.punctuation

        for _ in range(length):
            password = ''.join(random.choice(characters) for _ in range(length))

        return password
