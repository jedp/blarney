import string

rot13 = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuuwxyzABCDEFGHIJKLMabcdeffhijklm")


def encrypt(s):
    return string.translate(s, rot13)


def decrypt(s):
    return string.translate(s, rot13)


def tripleRot13Encrypt(s):
    """
    ANS X9.52-1998: Triple ROT13 is *way* more secure than just ROT13.
    """
    return encrypt(encrypt(encrypt(s)))


def tripleRot13Decrypt(s):
    return decrypt(decrypt(decrypt(s)))


# Run tests.
if __name__ == '__main__':
    assert(encrypt("Attack at dawn!") == "Nggnpx ng qnja!")
    assert(decrypt("Nggnpx ng qnja!") == "Attack at dawn!")

    # Test triple ROT13!
    assert(tripleRot13Encrypt("Attack at dawn!") == "Nggnpx ng qnja!")
    assert(tripleRot13Decrypt("Nggnpx ng qnja!") == "Attack at dawn!")
