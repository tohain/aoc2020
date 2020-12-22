
import sys
import numpy as np

# N^2, not really nice, but though sorting it first would be faster, I
# feel it doesn't add much algorithmic 'beauty' to it
def find_pair( data, val ):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if ( data[i] + data[j] == val ):
                return i, j, data[i], data[j]


# same as above            
def find_tripel( data, val ):
    for i in range(len(data)):
        for j in range( i+1, len(data) ):
            for k in range( j+1, len(data) ):
                if( data[i] + data[j] + data[k] == val ):
                    return i, j, k, data[i], data[j], data[k]

            
if __name__ == '__main__':
    data = np.loadtxt( sys.argv[1], dtype=np.int32 )
    i1, i2, val1, val2 = find_pair( data, 2020 )
    print(f"part1: {val1*val2}")
    i1, i2, i3, val1, val2, val3 = find_tripel( data, 2020 )
    print(f"part2: {val1*val2*val3}")
