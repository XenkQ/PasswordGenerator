import string
import random

CHARACTERS_BAD_FOR_PASSWORD = "0O1 Il5S<>[]{}|\\/^~`\"'"

class Password:
    @staticmethod
    def generate_password(letters_count:int, digits_count:int, punctuation_count:int, exclude_characters="") -> str:
        password, characters = "", ""
        password_length = letters_count + digits_count + punctuation_count

        if letters_count:
            characters += string.ascii_letters
        if digits_count:
            characters += string.digits
        if punctuation_count:
            characters += string.punctuation

        for c in exclude_characters:
            if c in characters:
                characters.replace(c, '')

        for _ in range(password_length):
            password = ''.join(random.choice(characters) for _ in range(password_length))

        return password
