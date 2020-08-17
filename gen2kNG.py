#!/usr/bin/env python

__author__    = 'cmpone'
__email__     = 'cmpone[at]blackarch[dot]org'
__license__   = 'BSD'
__version__   = 'PROD'
__date__      = '17/08/2020'

import sys
from itertools import product


"""
##############################  GEN2K  ####################################

                    Automated Word List Generator

> Generates passwords combinations by combining words from wordlist.
> Covers frequently used number patterns used along with words.
> Generates passwords combinations using year/date combo.
> Generates custom user defined value(s) combination with word list.
> Option to auto convert words to upper/lowercase & capitalisation.
> WPA/WPA2 password validation check.
> No external dependencies.

---------------------------------------------------------------------------

                            HINTS:

  * DO NOT USE A GENERAL PURPOSE WORDLIST
  * SUPPLIED WORDLIST MUST ONLY CONTAIN KNOWN FACTS ABOUT TARGET
    E.G NAMES, ADDRESS, FAVORITE ARTIST, PLACE, EVENT, ETC.
  * TRY TO KEEP WORDLIST AT A MINIMUM, DON'T INCLUDE TOO MUCH DETAILS
  * THE FINAL GENERATED WORD LIST CAN GET EXTREMELY LARGE!

###########################################################################
"""


def help():
    print("""


         ######   ######## ##    ##  #######  ##    ##        ##    ##  ######
        ##    ##  ##       ###   ## ##     ## ##   ##         ###   ## ##    ##
        ##        ##       ####  ##        ## ##  ##          ####  ## ##
        ##   #### ######   ## ## ##  #######  #####    ####   ## ## ## ##   ####
        ##    ##  ##       ##  #### ##        ##  ##          ##  #### ##    ##
        ##    ##  ##       ##   ### ##        ##   ##         ##   ### ##    ##
         ######   ######## ##    ## ######### ##    ##        ##    ##  ######

             ================ Automated Word List Generator ===============
                             Copyright (C) irenicus09 2013

                                RIP: brah today is 2049


    USAGE:  ./gen2kNG.py -i wordlist [options]

    EXAMPLES:
              ./gen2kNG.py -i wordlist -u -x '_,-,.,@,!' -n -y
               1 word --> 1122 words

              ./gen2kNG.py -i wordlist -u -x '_,-,.,@,!,*,$,?,&,%' -n -y
               1 word --> 1142 words (only +20 words because -n -y are not combined with -x)
              => use -X to force max combine

              ./gen2kNG.py -i wordlist -u -X -x '_,-,.,@,!,*,$,?,&,%' -n -y
              1 word --> 23142 words

    [ -o ] Output filename. (DEFAULT PRINTS TO SCREEN)

    [ -i ] Path to INPUT word list file.
           Wordlist must contain info related to Target.

    ------------------------------------------------------------------------------

    [ -u ] make fist char of word upper and lower case

    [ -x ] Combine custom strings with list (comma separated)

    [ -n ] Enable frequently used number combination with wordlist.

    [ -y ] Enable year (1990 - 2049) combination with wordlist.

    [ -c ] Word combinations (words from wordlist)
           Note: `cat wordlist`
                secret
                pass
           Produces:
                passsecret
                secretpass

    ------------------------------------------------------------------------------
    [ -r ] remove all words from this list
           Note: Useful if you already bruteforced some prior generated passwords
                 and now want to generate a bigger list with no prior tested passwords.

    [ -w ] wpa/wpa2 fitness check
           Note: This only removes passwords

    [ -l ] Enable leet combination with wordlist.
           Note: (!! BIG LIST !!)

    [ -z ] Conversion of ALL characters in wordlist to UPPER & lower case letters.
           Note: (!! BIG LIST - approx x4 vs '-l' !!)

    [ -h ] Prints this help.
    """)




def main():

    if exist('-h'):
        help()
        sys.exit(0)

    if not (exist('-i') or exist('-o')):
        help()
        sys.exit(1)

    if exist('-z') and exist('-u'):
        print('[!] either -z or -u NOT both')
        help()
        sys.exit(1)

    master_list = load_words(find('-i')) # List supplied by user

    if exist('-r'):
        remove_list = load_words(find('-r')) # List supplied by user

    data = master_list # Final wordlist
    temp = [] # Temporary wordlist

    if exist('-l'):
        master_list = gen_leet(master_list)
        data = master_list

    if exist('-u'):
        master_list = gen_case(master_list)
        data = master_list

    if exist('-z'):
        master_list = gen_all_cases(master_list)
        data = master_list

    if exist('-c'):
        temp = gen_word_combo(master_list)
        data = list(set(temp+data))

    if exist('-n'):
        temp = gen_numbers(master_list)
        data = list(set(temp+data))

    if exist('-y'):
        temp = gen_year(master_list)
        data = list(set(temp+data))

    if exist('-x'):
        try:
            custom_values = find('-x').split(',')
        except (AttributeError):
            print('[!] -x "Combine custom strings" needs values!!')
            sys.exit(1)

        if exist('-X'):
            temp = gen_custom(data, custom_values)
        else:
            temp = gen_custom(master_list, custom_values)

        data = list(set(temp+data))

    if exist('-w'):
        data = wpa_validation_check(data)

    if exist('-r'):
        generated_passwords = []
        for new_pass in data:
            if new_pass not in remove_list:
                generated_passwords.append(new_pass)
    else:
        generated_passwords = data

    if exist('-o'):
        write_file(find('-o'), generated_passwords)
    else:
        for password in generated_passwords:
            print(password)

    print('[*] Total words generated: %d' % (len(generated_passwords)))
    sys.exit(0)


def merge_list(temp_list=[], final_list=[]):
    """
    Merges contents from temp_list (1st param) with final_list (2nd param)
    """
    for word in temp_list:
        if word not in final_list:
            final_list.append(word)


def load_words(path_to_file):
    """
    Function to fetch all possible words.
    """
    data = []

    try:
        handle = open(path_to_file, 'r')
        temp_list = handle.readlines()
        handle.close()

    except(BaseException):
        print('[!] Error occured while reading wordlist.')
        sys.exit(1)

    for word in temp_list:
        word = word.strip()
        if word != '':
            data.append(word)

    return data


def write_file(path_to_file, data=[]):
    """
    Writing to specified file.
    """
    try:
        handle = open(path_to_file, 'wb+')

        for word in data:
            handle.write(word.encode('UTF-8')+b'\n')

        handle.close()
    except(BaseException):
        print('[!] Error occured while writing to file.')
        sys.exit(1)


def gen_case(words=[]):
    """
    Function to change first char to Upper & Lower case.
    """
    wordlist = []

    for word in words:
        charPostfix = word[1:]
        char = word[:1]
        wordlist.append(char.lower()+charPostfix)
        wordlist.append(char.upper()+charPostfix)
    return wordlist


def gen_all_cases(words=[]):
    """
    Function to change all chars to Upper & Lower case.
    """
    word_list = []

    for word in words:
        word_list += list(map(''.join, product(*(sorted(set((c.upper(), c.lower()))) for c in word))))

    return word_list


def gen_numbers(words=[]):
    """
    Function to mix words with commonly used numbers patterns.
    """
    word_list = []

    if len(words) <= 0:
        return word_list

    num_list = ['0', '01', '012', '0123', '01234', '012345', '0123456', '01234567', '012345678', '0123456789',
    '1', '12', '123', '1234','12345', '123456','1234567','12345678','123456789', '1234567890', '9876543210',
    '987654321', '87654321', '7654321', '654321', '54321', '4321', '321', '21']

    for word in words:
        for num in num_list:
            word_list.append((word+num))
            word_list.append((num+word))

    return word_list


def gen_year(words=[]):
    """
    Function to mix auto generated year with words from wordlist.

    Hint: Date of birth & special dates are often
          combined with certain words to form
          passwords.
    """
    word_list = []

    if len(words) <= 0:
        return word_list

    # Double digit dates
    start = 1
    while(start <= 99):
        for word in words:
            word_list.append(word + str("%02d") % (start))
            word_list.append(str("%02d") % start + word)
        start += 1

    # Four digit dates
    start = 1900
    while (start <= 2049):
        for word in words:
            word_list.append(word+str(start))
            word_list.append(str(start)+word)
        start += 1

    return word_list


def gen_word_combo(words=[]):
    """
    Function to mix multiple words from given list.
    """
    word_list = []

    if len(words) <= 1:
        return word_list

    for word in words:
        for second_word in words:
            if word != second_word:
                word_list.append(second_word+word)

    return word_list


def gen_custom(words=[], data=[]):
    """
    Funtion to combine user defined input with wordlist.

    > Takes a comma separated list via cmdline as values.
    """
    word_list = []
    if (len(words) <= 0 or len(data) <= 0):
        return word_list

    for item in data:
        for word in words:
            word_list.append(item+word)
            word_list.append(word+item)

    return word_list


def gen_leet(words=[]):
    REPLACE = {'a': '4', 'b': '8', 'e': '3', 'g': '6', 'i': '1','o': '0', 's': '5', 't': '7', 'z': '2'}
    word_list  = []
    for word in words:
        possibles = []
        for l in word.lower():
            ll = REPLACE.get(l, l)
            possibles.append( (l,) if ll == l else (l, ll) )
        word_list += [ ''.join(t) for t in product(*possibles) ]
    return word_list


def wpa_validation_check(words=[]):
    """
    Function to optimise wordlist for wpa cracking

    > Removes Duplicates.
    > Removes passwords < 8 or > 63 characters in length.
    """
    custom_list =  list(set(words))
    custom_list = [x for x in custom_list if not (len(x) < 8 or len(x) > 63)]

    return custom_list


def find(flag):
    # S3my0n's argument parsers, thx brah :)
    try:
        a = sys.argv[sys.argv.index(flag)+1]
    except (IndexError, ValueError):
        return None
    else:
        return a


def exist(flag):
    if flag in sys.argv[1:]:
        return True
    else:
        return False

if __name__ == '__main__':
    main()
