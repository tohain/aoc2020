import sys

# check if condition for a valid password in part 1 is given
def check_string( char, lo, hi, word ):
    
    counter = 0
    for i in word:
        if i == char:
            counter+=1
    if( lo <= counter <= hi ):
        return 1
    else:
        return 0


# if condition for a valid password is given in part 2
def check_string_part2( char, first, second, word ):

    # indeces start at 1, not 0
    first-=1
    second-=1

    #check if condition is met
    if( (word[first] == char and word[second] != char) or
        (word[first] != char and word[second] == char) ):
        return 1
    else:
        return 0


# parse input file line by line
def parse_file( fn, valid_func ):

    # track number of (in)valid passwords
    counter_true = 0
    counter_false = 0 #check if both numbers add up to total nr. of lines
    
    with open( fn, 'r' ) as ff:

        line = ff.readline()
        # keep reading lines until EOF
        while( line != "" ):

            # parse the conditions
            line=line.strip().split(" ")
            lo = int( line[0].split("-")[0] )
            hi = int( line[0].split("-")[1] )
            char = line[1][0]
            word = line[2]

            
            if( valid_func( char, lo, hi, word )  ):
                counter_true+=1
            else:
                counter_false+=1

            #get next line
            line = ff.readline()

    return (counter_true, counter_false )
            

if __name__ == '__main__':
    t,f = parse_file( sys.argv[1], check_string )
    print(f"part1: valid={t} invalid={f}")
    t,f = parse_file( sys.argv[1], check_string_part2 )
    print(f"part2: valid={t} invalid={f}")    
