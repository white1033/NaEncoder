KEY = '@'
LINKER = chr(127)


# Type 1
def make_words_2_keys(words):
    return LINKER.join(make_char_2_key(c) for c in words)


def make_keys_2_words(keys_string):
    keys_list = keys_string.split(LINKER)
    return ''.join(make_keys_2_char(keys) for keys in keys_list)


def make_char_2_key(char):
    return KEY * ord(char)


def make_keys_2_char(keys):
    return chr(len(keys))


# Type 2
def make_words_2_codes(words):
    return LINKER.join(make_char_2_code(c) for c in words)


def make_codes_2_words(codes):
    codes_list = codes.split(LINKER)
    return ''.join(make_code_2_char(code) for code in codes_list)


def make_char_2_code(char):
    ascii = ord(char)
    if 33 <= ascii < 66:
        code = chr(ascii-33)
    elif 66 <= ascii < 98:
        code = chr(ascii-65) * 2
    elif 98 <= ascii < 127:
        code = chr(ascii-97) * 3
    elif ascii == 32:
        code = " "
    else:
        code = ""
    return code


def make_code_2_char(code):
    if code == " ":
        char = " "
    elif len(code) == 1:
        char = chr(ord(code[:1])+33)
    elif len(code) == 2:
        char = chr(ord(code[:1])+65)
    elif len(code) == 3:
        char = chr(ord(code[:1])+97)
    else:
        char = ""
    return char


def ascii_table():
    print("====================================================================================================================================")
    print("[ ASCII TABLE ]  -- Display characters for Ascii codes from 33 to 127 only. ")
    print("====================================================================================================================================")
    count = 0
    for ascii in range(128):
        if (0 <= ascii <= 127):
            character = chr(ascii)
        else:
            character = unicode(chr(ascii), "latin1")
        if ascii > 32:
            count += 1
            print "ASCII: " + str(ascii) + " -> " + character + "   ",
            if count % 7 == 0:
                print ""
    print ""
