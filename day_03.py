import sys
import math


def count_trees( mappy, r, d ):
    # keep track of nr. of trees
    tree_count = 0

    # dimensions of the map
    cols = len(mappy[0])
    rows = len(mappy)

    # these two variables stor our current position
    col = 0
    row = 0

    #go through each line of the map
    while( row < rows-1 ):

        col+=r
        # when using iterators instead of loading map into memory, we
        # would just replace current line by the next line here
        row+=d

        # periodic boundary conditions
        if( col >= cols ):
            col-=cols

        # hit a tree!
        if( mappy[row][col] == '#' ):
            tree_count+=1

    return tree_count


# reads the entire file into memory, could be more efficient by just
# parsing line by line, but considering part 2 you might as well just
# keep it in memory
def readfile(fn):

    data = []
    with open( fn, 'r' ) as ff:
        for line in ff:
            data.append( line.strip() )
            
    return data
            
if __name__ == '__main__':
    # get the map
    data = readfile( sys.argv[1])
    nr1 = count_trees( data, 1, 1 )
    nr2 = count_trees( data, 3, 1 )
    nr3 = count_trees( data, 5, 1 )
    nr4 = count_trees( data, 7, 1 )
    nr5 = count_trees( data, 1, 2 )
    print(f"(1,1)={nr1}, (3,1)={nr2}, (5,1)={nr3}, (7,1)={nr4}, (1,2)={nr5}")
    print(f"part2: { math.prod( [nr1, nr2, nr3, nr4, nr5] )}" )
