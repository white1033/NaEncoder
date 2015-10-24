KEY = "@"
LINKER = chr(127)


# Type 1
def make_words_2_keys(words):
    keys = ""
    for c in words:
        k = make_char_2_key(c)
        keys += (k + LINKER)
    return keys


def make_keys_2_words(keys_string):
    words = ""
    L = keys_string.split(LINKER)
    for keys in L:
        words += make_keys_2_char(keys)
    return words


def make_char_2_key(char):
    ascii = ord(char)
    keys = KEY * ascii
    return keys


def make_keys_2_char(keys):
    return chr(len(keys))


# Type 2
def make_words_2_codes(words):
    codes = ""
    for c in words:
        code = make_char_2_code(c)
        codes += (code + LINKER)
    return codes


def make_codes_2_words(codes):
    words = ""
    L = codes.split(LINKER)
    for code in L:
        words += make_code_2_char(code)
    return words


def make_char_2_code(char):
    ascii = ord(char)
    if 33 <= ascii < 66:
        code = chr(ascii-33)
    elif 66 <= ascii < 98:
        code = chr(ascii-65) * 2
    elif 98 <= ascii < 127:
        code = chr(ascii-97) * 3
    else:
        code = ""
    return code


def make_code_2_char(code):
    if len(code) == 1:
        char = chr(ord(code[:1])+33)
    elif len(code) == 2:
        char = chr(ord(code[:1])+65)
    elif len(code) == 3:
        char = chr(ord(code[:1])+97)
    else:
        char = ""
    return char


def ascii_table():
    print("====[ ASCII Table ]====")
    for ascii in range(128):
        if (0 <= ascii <= 127):
            character = chr(ascii)
        else:
            character = unicode(chr(ascii), "latin1")
        print("ASCII: " + str(ascii) + " -> " + character)


def main():
    ascii_table()
    words = "ABCDEFGHIJK"
    print("[BEGIN]" + make_words_2_codes(words) + "[END]")
    print(make_codes_2_words(make_words_2_codes(words)))

if __name__ == '__main__':
    main()
