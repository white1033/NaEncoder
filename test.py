from Encoder.encoder import ascii_table
from Encoder.encoder import make_codes_2_words
from Encoder.encoder import make_words_2_codes

def main():
    ascii_table()
    words = "ABCDEFGHIJK"
    print("[BEGIN]" + make_words_2_codes(words) + "[END]")
    print(make_codes_2_words(make_words_2_codes(words)))

if __name__ == '__main__':
    main()
