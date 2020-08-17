# gen2kNG


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
    
