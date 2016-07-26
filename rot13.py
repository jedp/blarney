import string

rot13 = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")


def encrypt(s):
    return string.translate(s, rot13)

# Run tests.
if __name__ == '__main__':
    assert(encrypt("Attack at dawn!") == "Nggnpx ng qnja!")
