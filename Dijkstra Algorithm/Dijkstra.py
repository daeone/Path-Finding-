import copy


#==============================================================================================================================#
    #=============================================== Dijkstra algorithm  ==================================================#
#==============================================================================================================================# 

class droute:
    # The class droute implements dijkstra routing algorithm. It only has two attributes to store the route from o to d in the graph A,
    # and the minimum cost of the travel. v for route and c for minimum cost. 

    def __init__ (self):
        self.v = []
        self.c = 0

    def dijkstra (self,A, o, d):
        start = min(o,d) - 1          # For the convenience of the routing we assume o start is smaller node than

        destination = max(o,d) - 1    # the destination (e.g. 5 -> 6 and 6 -> 5 have identical cost and route
                                      # but the order is always ascending)
        matrix = copy.deepcopy(A)      

        visited = []                  # Keep track of visited nodes in order 

        self.v = [0] * (len(matrix) + 1)    # Store the predecessors from node 1 to length of A. For example vector[3] = 2          
                                            # iff the node 3 has a minimum cost link to node 2.
                                            # By default v[o] = 0 meaning the origin node itself has predecessor of 0

        infinite_weight = float("inf")  

        ## Convert the cost of any unconnected node from start to infinity (initially, cost = 0). If connected, then we simply copy the cost into matrix. 
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][j] = infinite_weight

        ## Initialization 
        distances = matrix[start]       # Distances have cost to connected node and unconnected node from the start node.
        visited.append(start+1)         # The start node is included in visited nodes.
        distances[start] = 0
        for i  in range(1,len(self.v)): 
            if i != start + 1:
                self.v[i] = start+1
            else:
                self.v[i] = 0
                

        print("start nodes\t   from 1 \tfrom 2 \tfrom 3 \tfrom 4 \tfrom 5 \tfrom 6")
        
        # Until the destination node is found, keep searching the minimum path and append it to
        # the vector list
        for i in range(0,len(distances)):
            minimum_cost = infinite_weight
            print('{:<20}'.format(str(visited)), end="") 

            ## Find minimum next node if not visited and append it to the visited list
            for j in range(0,len(distances)):
                if minimum_cost > distances[j] and not j+1 in visited:
                    minimum_cost = distances[j]
                    nextNode = j
                print("("+ str(distances[j]) + "," + str(self.v[j+1]) + ")", end="\t")
            print("\n")
            visited.append(nextNode+1)
            
            # If the minimum next node has the shorter cost of path than existing known path
            # update the cost  
            for k in range(0,len(distances)):
                if not k+1 in visited:
                    if minimum_cost + matrix[nextNode][k] < distances[k]:
                        distances[k] = minimum_cost + matrix[nextNode][k]
                        self.v[k+1] = nextNode + 1


                
        # Trace back the route from destination to start and record the sequence in the list
        # Reverse the array to properly format the vector from start to destination.
        temp = []
        predecessor = destination + 1
        while (predecessor != start+1):
            temp.append(predecessor)
            predecessor = self.v[predecessor]
        temp.append(start+1)
        temp.reverse()
        self.v = temp
        self.c = distances[destination]

        return (self.v, self.c)


