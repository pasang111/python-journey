# Caesar Cipher

# What does Caesar Cipher do?
# Caesar Cipher is a simple encryption method.
# It shifts each letter in a message by a certain number of positions in the alphabet.
# For example, with a shift of 3:
# a becomes d
# b becomes e
# c becomes f

# Am I calling a function? -> use ()
# Am I selecting something from a string or list? -> use []

def caesar(text, shift, encrypt=True):

    # checking if shift is an integer
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # shift should be between 1 and 25
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # normal alphabet used for mapping
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # if encrypt is False we reverse the shift
    # this allows us to decrypt the message
    if not encrypt:
        shift = -shift

    # creating a shifted alphabet
    # Example:
    # alphabet = abcdefghijklmnopqrstuvwxyz
    # shift = 3
    # shifted_alphabet = defghijklmnopqrstuvwxyzabc
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # str.maketrans() creates a translation table
    # it creates rules for replacing one character with another
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # translate() applies the translation rules to the text
    encrypted_text = text.translate(translation_table)

    # return the final encrypted or decrypted text
    return encrypted_text


# helper function for encryption
def encrypt(text, shift):
    return caesar(text, shift)


# helper function for decryption
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


# encrypted message
encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."

# decrypting the message using shift 13
decrypted_text = decrypt(encrypted_text, 13)

# printing the final readable message
print(decrypted_text)