from random import randint

def Steepest(tree, start, goal, heuristic, step_by_step = False):
    if step_by_step:
        print("--------")
    path = [start]
    if start == goal:
        return path
    
    while True:
        current_node = path[-1]
        current_distance = heuristic(current_node, goal)
        neighbors = [edge[1] for edge in tree[0] if edge[0] == current_node]
        sorted_neighbors = sorted(neighbors, key = lambda x: heuristic(x, goal))
        next_node = sorted_neighbors[0]
        if step_by_step: 
            print(f"next node: {next_node}")
            print(f"current distance: {current_distance}")
            print(f"heuristic: {heuristic(next_node, goal)}")
        if heuristic(next_node, goal) <= current_distance:
            path.append(next_node)
            if next_node == goal:
                return path
        else:
            if step_by_step:
                print([(neighbor, heuristic(neighbor, goal)) for neighbor in sorted_neighbors])
                print(path)
            return "No se encontro camino"

def Stochastic(tree, start, goal, heuristic, step_by_step = False):
    if step_by_step:
        print("------------")
    path = [start]
    if start == goal:
        return path
    
    while True:
        current_node = path[-1]
        
        current_distance = heuristic(current_node, goal)
        neighbors = [edge[1] for edge in tree[0] if edge[0] == current_node]
        filtered_neighbors = list(filter(lambda x: heuristic(x, goal) < current_distance, neighbors))
        if step_by_step:
            print(f"current node: {current_node}")
            print(f"neighbors: {neighbors}")
            print(f"filtered neighbors: {filtered_neighbors}")
        if filtered_neighbors != []:
            random_index = randint(0, len(filtered_neighbors) - 1)
            next_node = filtered_neighbors[random_index]
            if step_by_step:
                print(f"next node: {next_node}")
            path.append(next_node)
        else:
            if current_node == goal:
                return path
            else:
                return "No se pudo encontrar un camino"