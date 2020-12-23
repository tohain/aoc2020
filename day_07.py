import sys

import numpy as np

def parse_file( fn ):
    """Reads the rule file and parses them into a collection of nodes
(colors) and edges (which color holds which)"""

    
    nodes = dict() # all colors
    edges = dict() # which color holds which color
    
    with open( fn, 'r' ) as ff:

        for line in ff:

            line=line.strip()
            # separate containing bag and contained colors
            line=line.split("contain")

            #
            #containing bag
            #
            
            # assumes color always consists of two words, easy to
            # adapt if necessary
            color = " ".join(line[0].split(" ")[0:2])

            #add color to nodes
            if( color not in nodes ):
                start = len(nodes)
                nodes[color] = len(nodes)
            else:
                start = nodes[color]

            #contained bag
            if( line[1] != ' no other bags.' ):

                # the end points of all edges originating in current color
                node_edges=[]

                for i in line[1].split(','):
                    tmp=i.split("bag")[0].split(" ")
                    color=" ".join(tmp[2:4])
                    amount=int(tmp[1])
                    
                    if( color not in nodes ):
                        end = len(nodes)
                        nodes[color] = len(nodes)
                    else:
                        end = nodes[color]

                    node_edges.append( [end, amount] )

                edges[start] = node_edges
                        
            else:
                #do nothing, there is no other edge to add here
                pass


    return nodes, edges


def graph_analysis( nodes, edges, cid ):

    # use numpy for higher efficency arrays
    visited = np.zeros( len(nodes) ) # did we already chck this node?
    contains_gold = np.zeros( len(nodes) ) # does this allow or any of its children allow a shiny gold bag?

    visited_count = 0

    # make sure we visit all nodes, in case the graph has disconnected components
    for n in nodes:

        to_visit = [nodes[n]]

        # this keeps track of the path we went to reach the current node
        # if we find 'shiny gold' we need to mark all of these nodes as
        # 'golden'. -1 denotes start
        path = dict( { nodes[n] : [-1] } )

        # keep going until visited all nodes of current component
        while( len(to_visit) > 0 ):
            cur_node = to_visit.pop(0)

            if( visited[ cur_node ] == 0 ):
                visited[cur_node] = 1
                
                #check children
                if cur_node in edges: 
                    for i in edges[cur_node]:
                        #check if there is a shiny golden allowed
                        if( i[0] == cid or contains_gold[ i[0] ] == 1 ):
                            #found gold at children, mark path and this node golden
                            contains_gold[cur_node] = 1
                            for j in path[cur_node]:
                                if( j >= 0 ): #skip the -1 start
                                    contains_gold[ j ] = 1
               

                        # add children to visit and mark path
                        if( visited[ i[0] ] == 0 ):
                            to_visit.append( i[0] )
                            if( i[0] not in path ):
                                path[ i[0] ] = path[cur_node] + [cur_node]
                            else:
                                path[i[0]].append( cur_node )
                    
                                

    return contains_gold


# This function returns the number of bags inside the current bags
# recursivley
def part_2_recursive( cur_node, nodes, edges ):

    bags = 1 # start with one bag, i.e. itself!
    
    if cur_node in edges:
        for i in edges[cur_node]:
            bags += i[1] * part_2_recursive( i[0], nodes, edges )
        return bags
    else:
        # this node is a dead end, so no more bags are contained in this on
        return bags
    


if __name__ == '__main__':
    nodes, edges = parse_file( sys.argv[1] )
    gold_bags = graph_analysis( nodes, edges, nodes['shiny gold'] )
    print(f"part1: {len(np.where(gold_bags==1)[0])}")
    nr_bags = part_2_recursive( nodes['shiny gold'], nodes, edges )
    print(f"part2: {nr_bags-1}") # substract one, since we added the
                                 # shiny golden bag itself also, but
                                 # this one does not count
