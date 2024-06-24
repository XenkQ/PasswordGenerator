import string
import random

#similar characters to exclude on default
CHARACTERS_BAD_FOR_PASSWORD = "0O1 Il5S<>[]{}|\\/^~`\"'"


class Password:
    __character_sets = None
    __previously_excluded = CHARACTERS_BAD_FOR_PASSWORD

    @staticmethod
    def generate_password(lower_letters_count: int, upper_letters_count: int, digits_count: int, special_signs_count: int, exclude_characters="") -> str:
        sets_length = [lower_letters_count, upper_letters_count, digits_count, special_signs_count]
        password = ""

        if Password.__character_sets is None or Password.__previously_excluded != exclude_characters:
            Password.__character_sets = {
                "lower_letters": string.ascii_lowercase,
                "upper_letters": string.ascii_uppercase,
                "digits": string.digits,
                "special_characters": string.punctuation
            }

            for key in Password.__character_sets:
                new_set = []

                characters = Password.__character_sets[key]
                for c in characters:
                    if c not in exclude_characters:
                        new_set.append(c)

                Password.__character_sets[key] = "".join(new_set)

            Password.__previously_excluded = exclude_characters

        for i, key in enumerate(Password.__character_sets):
            if sets_length[i]:
                password += ''.join(random.choice(Password.__character_sets[key]) for _ in range(sets_length[i]))

        return password
