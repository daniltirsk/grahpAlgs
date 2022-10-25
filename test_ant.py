from AntColony import *
inp = open("input.txt","r").read().split('\n')

num_of_nodes = int(inp[0])
start = int(inp[1])-1
end = int(inp[2])-1


dist = np.zeros((num_of_nodes,num_of_nodes))
dist[dist==0] = np.inf


for i in range(3,len(inp)):
    x, y, cost = list(map(str, inp[i].split()))
    dist[int(x)-1,int(y)-1] = int(cost)
     
print(dist)

ant_colony = AntColony(dist, 1, 5, alpha=1, beta=1, decay=0.95)
shortest_path = ant_colony.search(start,end)
print ("shortest_path: {}".format(shortest_path))
        
        

