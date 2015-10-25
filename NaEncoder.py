from Encoder.encoder import ascii_table
from Encoder.encoder import make_codes_2_words
from Encoder.encoder import make_words_2_codes
import sys

def main():
    print "====[ Welcome to NaEncoder ]=========================================================================================="
    print "  NaEncoder.py is a tool to transfer words into invisible characters, and restore them back into the origin words."
    print "  Usage: NaEncoder [ old_file ] [ new_file ] [ transfer_mode ] ( -r: transfer / -t: restore )"
    print "======================================================================================================================"

    # Collect arguments input from command line
    old_file = sys.argv[1] # old_file
    new_file = sys.argv[2] # new_file
    mode = sys.argv[3] # transfer_mode

    # Display Ascii Table
    #ascii_table()

    print ("[ Read file ]: " + old_file)
    words = ""

    #read file
    for line in open(old_file,'r'):
        print line
        words += line
    print "Count = " + str(len(words))

    if mode == "-t":
        # transfer words
        print "[ Transfer words ]:" 
        new_words = make_words_2_codes(words)
        print new_words
        print "Count = " + str(len(new_words))

    elif mode == "-r":
        # restore words
        print "[ Restore words ]:"
        new_words = make_codes_2_words(words)
        print new_words
        print "Count = " + str(len(new_words))
    else:
        print "[ Warning ]: the transfer mode '"+ mode +"' is not available!"
        return

    # output file
    output = open(new_file,'w')
    output.write(new_words)

    print("------------------------------------------------------------------")
    print "[ok] Successfully transfer " + old_file + " into "+ new_file + "!"
    print("------------------------------------------------------------------")

if __name__ == '__main__':
    main()


