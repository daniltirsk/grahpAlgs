import numpy as np

class AntColony:
    def __init__(self, distances, n_ants, iters, alpha=1, beta=1, decay=0.2):
        self.n_ants = n_ants
        self.iters = iters
        self.dist_matrix = distances
        self.alpha = alpha
        self.beta = beta
        self.decay = decay

        self.node_ids = [i for i in range(self.dist_matrix.shape[0])]

        self.pher_matrix = np.ones(self.dist_matrix.shape)


    def search(self, start, finish):
        min_path = ([],np.inf)

        for i in range(self.iters):
            ant_paths = []
            for i in range(self.n_ants):
                path = self.get_ant_path(start)
                ant_paths.append(path)

            self.update_pher(ant_paths)

            for path in ant_paths:
                if path[0][-1] == finish and path[1] < min_path[1]:
                    min_path = path

        return min_path
                    
            

    def update_pher(self, ant_paths):
        for path, _ in ant_paths:
            for i in range(len(path)-1):
                self.pher_matrix[path[i],path[i+1]] += 1/self.dist_matrix[path[i],path[i+1]]

        self.pher_matrix *= self.decay           

    def get_ant_path(self,start):
        path = [start]
        visited = set([start])
        prev = start
        distance = 0

        while True:
            step, stop = self.pick_node(prev,visited)
            if stop:
                break
            distance += self.dist_matrix[prev,step]
            path.append(step)
            visited.add(step)
            prev = step

        return path,distance

    def pick_node(self, prev, visited):
        node = -1
        stop = False
        
        pher = np.copy(self.pher_matrix[prev])
        dist = np.copy(self.dist_matrix[prev])

        pher[list(visited)] = 0

        prob = pher ** self.alpha * ((1.0/dist) ** self.beta)
        

        if prob.sum() == 0:
            stop = True
        else:
            prob /= prob.sum()
            node = np.random.choice(self.node_ids, 1, p = prob)[0]
        
        return node, stop

