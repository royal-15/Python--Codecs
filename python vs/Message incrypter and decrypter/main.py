import random
from random import randint
import string


class keygenerator:
    def generate_substitution_key(self):
        alphabet = list(string.ascii_lowercase + string.ascii_uppercase)
        random.shuffle(alphabet)
        return "".join(alphabet)

    def generate_caeser_key(self):
        return randint(0, 25)


class translator:
    def __init__(self):

        self.key_gen = keygenerator()

    # * encodes message into caeser cipher, substitution cipher or custom encode
    def encode(self, message, method="custom"):
        if method == "caeser cipher":
            return self.caeser_cipher(message)
        elif method == "substitution cipher":
            return self.substitution_cipher(message)
        else:
            return self.custom_encode(message)

    def decode(self, code):
        pass

    # * converts message into caeser cipher code format
    def caeser_cipher(self, message):
        self.key = self.key_gen.generate_caeser_key()
        alphabet = string.ascii_lowercase + string.ascii_uppercase
        shifted_alphabet = alphabet[self.key :] + alphabet[: self.key]
        # print("shifted_alphabet: ", shifted_alphabet)
        # print("alphabet: ", alphabet)
        table = str.maketrans(alphabet, shifted_alphabet)
        return message.translate(table)

    # * converts message into substitution cipher code format
    def substitution_cipher(self, message, key):
        original_alphabet = string.ascii_lowercase + string.ascii_uppercase
        table = str.maketrans(
            original_alphabet, self.key_gen.generate_substitution_key()
        )
        return message.translate(table)

    def custom_encode(message):
        # todo add custom encode
        pass

    def help():
        # todo add help
        pass


# msg = input(": ")
msg = "rajat"
t = translator()
print(t.encode(message=msg, method="caeser cipher", key=5))
# print(
#     t.encode(
#         message=msg,
#         method="substitution cipher",
#         key=string.ascii_uppercase + string.ascii_lowercase,
#     )
# )
