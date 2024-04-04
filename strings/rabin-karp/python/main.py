# Reference: Algorithms 4th Ed., Robert Sedgewick, Kevin Wayne

Q = 1000000007  # A large prime number
R = 256  # Radix


def _hash(text):
    h = 0
    for c in text:
        h = (h * R + ord(c)) % Q
    return h


def find(text, pat):
    if len(text) < len(pat):
        return -1

    m = len(pat)
    power = 1
    for i in range(m - 1):
        power = (power * R) % Q

    text_hash = _hash(text[0:m])
    pat_hash = _hash(pat)

    if text_hash == pat_hash and text[0:m] == pat:
        return 0

    for i in range(m, len(text)):
        # Remove leading character
        leading = ord(text[i - m])
        text_hash = (text_hash + Q - (power * leading) % Q) % Q

        # Add trailing character
        trailing = ord(text[i])
        text_hash = (text_hash * R + trailing) % Q

        if text_hash == pat_hash and text[i - m + 1:i + 1] == pat:
            return i - m + 1

    return -1

