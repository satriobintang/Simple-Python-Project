#Created By Satrio Bintang (Alt5chm3rz)
#https://github.com/satriobintang
#June 2023

def lookup3_checksum(text):
    def rot(x, k):
        return ((x << k) | (x >> (32 - k))) & 0xFFFFFFFF

    def mix(a, b, c):
        a = (a - c) & 0xFFFFFFFF
        a ^= rot(c, 4) ^ b
        b = (b + a) & 0xFFFFFFFF
        b ^= rot(a, 6) ^ c
        c = (c - b) & 0xFFFFFFFF
        c ^= rot(b, 8) ^ a
        a = (a + c) & 0xFFFFFFFF
        a ^= rot(c, 16) ^ b
        b = (b - a) & 0xFFFFFFFF
        b ^= rot(a, 19) ^ c
        c = (c + b) & 0xFFFFFFFF
        c ^= rot(b, 4) ^ a
        a = (a - c) & 0xFFFFFFFF
        a ^= rot(c, 14) ^ b
        b = (b + a) & 0xFFFFFFFF
        b ^= rot(a, 8) ^ c
        c = (c - b) & 0xFFFFFFFF
        c ^= rot(b, 13) ^ a
        a = (a + c) & 0xFFFFFFFF
        a ^= rot(c, 6) ^ b
        b = (b - a) & 0xFFFFFFFF
        b ^= rot(a, 17) ^ c
        c = (c + b) & 0xFFFFFFFF
        c ^= rot(b, 5) ^ a
        a = (a - c) & 0xFFFFFFFF
        a ^= rot(c, 20) ^ b
        b = (b + a) & 0xFFFFFFFF
        b ^= rot(a, 9) ^ c
        c = (c - b) & 0xFFFFFFFF
        c ^= rot(b, 19) ^ a
        a = (a + c) & 0xFFFFFFFF
        a ^= rot(c, 22) ^ b
        b = (b - a) & 0xFFFFFFFF
        b ^= rot(a, 24) ^ c
        c = (c + b) & 0xFFFFFFFF
        return a, b, c

    def final_mix(a, b, c):
        c ^= b
        c -= rot(b, 14) & 0xFFFFFFFF
        a ^= c
        a -= rot(c, 11) & 0xFFFFFFFF
        b ^= a
        b -= rot(a, 25) & 0xFFFFFFFF
        c ^= b
        c -= rot(b, 16) & 0xFFFFFFFF
        a ^= c
        a -= rot(c, 4) & 0xFFFFFFFF
        b ^= a
        b -= rot(a, 14) & 0xFFFFFFFF
        c ^= b
        c -= rot(b, 24) & 0xFFFFFFFF
        return a, b, c

    length = len(text)
    a = b = c = 0xdeadbeef + (length << 2) + 0x98765432

    k1 = k2 = k3 = 0

    index = 0
    while index + 12 <= length:
        k1 = (ord(text[index + 2]) << 16) | (ord(text[index + 1]) << 8) | ord(text[index])
        k2 = (ord(text[index + 6]) << 16) | (ord(text[index + 5]) << 8) | ord(text[index + 4])
        k3 = (ord(text[index + 10]) << 16) | (ord(text[index + 9]) << 8) | ord(text[index + 8])

        a += k1
        b += k2
        c += k3

        a, b, c = mix(a, b, c)

        index += 12

    k3 = k2 = k1 = 0

    remaining = length - index
    if remaining > 0:
        if remaining >= 4:
            k1 |= ord(text[index + 3]) << 16
        if remaining >= 3:
            k1 |= ord(text[index + 2]) << 8
        if remaining >= 2:
            k1 |= ord(text[index + 1])
        k1 |= ord(text[index])

        a += k1

    a, b, c = final_mix(a, b, c)

    return c

while True:
    try:
        text = input('Enter the text to encrypt: ')
        checksum = lookup3_checksum(text)
        print(f'Checksum: {checksum}')
        break
    except Exception as e:
        print(e)
