import sys


def parse_entries( fn ):

    entries = []
    #init first empty dict for first passport
    pairs = dict()

    # go through all lines, when reading an empty line, add current
    # dict to entries array and clear it for the next passport entries
    with open( sys.argv[1], 'r' ) as ff:

        for line in ff:

            line=line.strip()

            if(line == "" ):
                #finished, add tmp dict and clear it
                entries.append( pairs )
                pairs = dict()
            else:        
                for i in line.split(" "):
                    tmp=i.split(":")
                    pairs[tmp[0]] = tmp[1]


        return entries

# check for valid entries here. might want to move the actual validity
# check into separate function, especially for part 2
def check_entries( data  ):
    counter_valid = 0
    counter_invalid = 0
    for i in data:
        if len(i) == 8:
            counter_valid+=1
        elif len(i) == 7:
            if( 'cid' not in i ):
                counter_valid+=1
            else:
                counter_invalid+=1
    
    return counter_valid, counter_invalid



if __name__ == '__main__':
    # parse the entire file and create a dict/map for each passport
    data = parse_entries( sys.argv[1] )
    # count valid entries
    cv, ci = check_entries( data )
    print(f"valid={cv} invalid={ci}")
