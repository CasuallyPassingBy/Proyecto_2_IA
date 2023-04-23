''' 
Search Tree
(ciudad origen) - (ciudad destino) - (peso/coste)
Arad -> Timisoara (118)
Arad -> Sibiu (140)
Arad -> Zerind (75)

Timisoara -> Lugoj (111)
Sibiu -> Rimni Vilcea (80)
Sibiu -> Fagaras (99)
Zerind -> Oradea (71)

Lugoj -> Mehadia (70)
Rimni Vilcea -> Craiova (146)
Rimni Vilcea -> Pitesti (97)
Fagaras -> Bucarest (211)
Oradea -> Sibiu (151)

Mehadia -> Drobeta (75)
Craiova -> Pitesti (138)
Pitesti -> Bucatest (101)
Bucarest -> Giurgiu (90)
Bucarest -> Urziceni (85)

Drobeta -> Craiova (120)
Urziceni -> Hirsova (98)
Urziceni -> Vaslui (142)

Hirsova -> Efoire (86)
Vaslui -> Iasi (92)

Iasi -> Neamt (87)


=============================
=============================
Matrix
            Arad    Timisoara   Sibiu   Zerind  Lugoj   Rimnicu  Fagaras    Oradea  Mehadia Craiova Pitesti Bucarest    Drobeta Giurgiu Urziceni    Hirsova Vaslui  Efoire  Iasi    Neamt
                                                        Vilcea
Arad        0           118     140     75      0       0           0           0       0       0       0       0           0       0       0           0       0       0   0       0
Timisoara   0           0       0       0       111     0           0           0       0       0       0       0           0       0       0           0       0       0   0       0
Sibiu       0           0       0       0       0       80          99          0       0       0       0       0           0       0       0           0       0       0   0       0
Zerind      0           0       0       0       0       0           0           71      0       0       0       0           0       0       0           0       0       0   0       0
Lugoj       0           0       0       0       0       0           0           0       70      0       0       0           0       0       0           0       0       0   0       0
Rimnicu     0           0       0       0       0       0           0           0       0       146     97      0           0       0       0           0       0       0   0       0
Vilcea
Fagaras     0           0       0       0       0       0           0           0       0       0       0       211         0       0       0           0       0       0   0       0
Oradea      0           0       151     0       0       0           0           0       0       0       0       0           0       0       0           0       0       0   0       0
Mehadia     0           0       0       0       0       0           0           0       0       0       0       0           75      0       0           0       0       0   0       0
Craiova     0           0       0       0       0       0           0           0       0       0       138     0           0       0       0           0       0       0   0       0
Pitesti     0           0       0       0       0       0           0           0       0       0       0       101         0       0       0           0       0       0   0       0
Bucarest    0           0       0       0       0       0           0           0       0       0       0       0           0       90      85          0       0       0   0       0
Drobeta     0           0       0       0       0       0           0           0       0       120     0       0           0       0       0           0       0       0   0       0
Giurgiu     0           0       0       0       0       0           0           0       0       0       0       0           0       0       0           0       0       0   0       0
Urziceni    0           0       0       0       0       0           0           0       0       0       0       0           0       0       0           98      142     0   0       0
Hirsova     0           0       0       0       0       0           0           0       0       0       0       0           0       0       0           0       0       86  0       0
Vaslui      0           0       0       0       0       0           0           0       0       0       0       0           0       0       0           0       0       0   92      0
Efoire      0           0       0       0       0       0           0           0       0       0       0       0           0       0       0           0       0       0   0       0
Iasi        0           0       0       0       0       0           0           0       0       0       0       0           0       0       0           0       0       0   0       87
Neamt       0           0       0       0       0       0           0           0       0       0       0       0           0       0       0           0       0       0   0       0
'''

formed_graph = [
    [0,118,140,75,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,111,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,80,99,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,71,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,70,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,146,97,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,211,0,0,0,0,0,0,0,0],
    [0,0,151,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,75,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,138,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,101,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,90,85,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,120,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,98,142,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,86,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,87],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

h_sld = {
    'Arad': 366,
    'Timisoara': 329,
    'Sibiu': 253,
    'Zerind': 374,
    'Lugoj': 244,
    'Rimnicu Vilcea': 193,
    'Fagaras': 176,
    'Oradea': 380,
    'Mehadia': 241,
    'Craiova': 160,
    'Pitesti': 100,
    'Bucarest': 0,
    'Drobeta': 242,
    'Giurgiu': 77,
    'Urziceni': 80,
    'Hirsova': 151,
    'Vaslui': 199,
    'Efoire': 161,
    'Iasi': 226,
    'Neamt': 234
}

def generate_states(graph):
    nodes_tuples = []
    nodes_connection_weights = []
    available_nodes_names = ['Arad','Timisoara','Sibiu','Zerind','Lugoj','Rimnicu Vilcea','Fagaras','Oradea','Mehadia','Craiova','Pitesti','Bucarest','Drobeta','Giurgiu','Urziceni','Hirsova','Vaslui','Efoire','Iasi','Neamt'] 
    for matrix_row_index in range(len(graph)):
        #print('matrix row' , graph[matrix_row_index])
        connections_and_weights = []
        for matrix_column_index in range(len(graph[0])):
            if graph[matrix_row_index][matrix_column_index] != 0:
                nodes_tuples.append((available_nodes_names[matrix_row_index], available_nodes_names[matrix_column_index]))
                connections_and_weights.append((available_nodes_names[matrix_column_index],graph[matrix_row_index][matrix_column_index]))
        if len(connections_and_weights) != 0:
            nodes_connection_weights.append([available_nodes_names[matrix_row_index], connections_and_weights])
    return nodes_tuples, nodes_connection_weights

def generate_unidirectional_weights(tree):
    unidirectional_tree = tree[0].copy()
    unidirectional_weights = []

    # iterate through the tuples to obtain the reversed connections
    for node_tuple in tree[0]:
        reversed_tuple = (node_tuple[1], node_tuple[0])
        # add the reversed tuple to the unidirectional tree
        unidirectional_tree.append(reversed_tuple)

    # obtain the reversed weights
    reversed_weights = {}
    for weight in tree[1]:
        for connection in weight[1]:
            if connection[0] not in reversed_weights:
                reversed_weights[connection[0]] = [(weight[0],connection[1])]
            else:
                previous_reversed_weight_value = reversed_weights[connection[0]]
                previous_reversed_weight_value.append((weight[0],connection[1]))
                reversed_weights[connection[0]] = previous_reversed_weight_value
    
    # merge the weights lists
    for weight in tree[1]:
        # get the reversed weight and connections of the current node being iterated
        current_reversed_weights = []
        try:
            current_reversed_weights = reversed_weights[weight[0]]
        except:
            current_reversed_weights = []

        current_connections = weight[1].copy()
        if len(current_reversed_weights) != 0:
            for current_reversed_weight in current_reversed_weights:
                current_connections.append(current_reversed_weight)
        
        unidirectional_weights.append([weight[0], current_connections])

    return unidirectional_tree, unidirectional_weights



def a_star(tree,start_node,goal):
    if start_node == goal:
        # returns the path along with its transition cost
        return ([start_node],0)
    
    iteration_counter = 0
    print('\n--- search iteration {} ---'.format(iteration_counter))
    
    # here we will store all the paths availables as we process them
    #   to store the first path, we need to obtain its heuristic value
    path = {h_sld[start_node]: [start_node]}
    print('path initialised = ', path)

    # update the iteration number
    iteration_counter += 1

    while True:
        print('\n--- search iteration {} ---'.format(iteration_counter))
        
        # select the path with the lowest cost
        key_path_with_lower_value = min([int(key) for key, values in path.items()])
        print(key_path_with_lower_value)
        
        current_node = path[key_path_with_lower_value][-1]
        print('\nnode being explored = ', current_node)

        if current_node == goal:
            # returns the path along with its transition cost
            return (path[key_path_with_lower_value], key_path_with_lower_value)

        # search for the childs of the current node
        childs = [node_weights_list[1] for node_weights_list in tree[1] if node_weights_list[0] == current_node]
        print('\nchilds = ', childs)

        # these childs have the cost of the action, we need to find its heuristic value
        if len(childs) != 0:
            childs_with_h_values = []

            for child in childs[0]:
                print('\nchild being processed ', child)
                child_name = child[0]
                # get the transition cost to the node
                child_action_value = child[1]
                # get the heuristic cost of the node
                child_heuristic_value = h_sld[child_name]
                print('\nchild = {}, action = {}, heuristic = {}'.format(child_name,child_action_value,child_heuristic_value))
                
                # check for the previous cities to update the transition cost
                acucumulative_transition_cost = 0
                current_path = path[key_path_with_lower_value]
                for node_index in range(len(path[key_path_with_lower_value])-1):
                    for transition_cost in tree[1]:
                        if transition_cost[0] == current_path[node_index]:
                            for node in transition_cost[1]:
                                # get the node to transition to
                                if node[0] == current_path[node_index+1]:
                                    acucumulative_transition_cost += node[1]

                acucumulative_transition_cost += child_action_value
                print('acucumulative_transition_cost ', acucumulative_transition_cost)

                # calculate the transition cost of the current node to the current child via
                #   f(n) = g(n) + h(n)
                total_transition_cost = acucumulative_transition_cost + child_heuristic_value
                print('total_transition_cost ', total_transition_cost)

                # save the path with the corresponding transition cost
                childs_with_h_values.append((child_name,total_transition_cost))

            print('\nchilds with h values = ', childs_with_h_values)
            sorted_childs_with_h_values = sorted(childs_with_h_values, key=lambda x: x[1])
            print('\nchilds with h values sorted = ', sorted_childs_with_h_values)

            # update the paths expanded so far; in this way, we save the alternative paths
            for child in sorted_childs_with_h_values:
                temp_updated_path = path[key_path_with_lower_value].copy()
                temp_updated_path.append(child[0])
                # stores the new paths in the path dictionary
                path[child[1]] = temp_updated_path

            # delete the current path (old)
            del path[key_path_with_lower_value]

            print('\navailable paths = ', path)
        else:
            # After visiting its neighbors, we mark the node as "visited"
            return 'Unable to find a path'
        
        iteration_counter += 1
        
def a_star_2(tree,start_node,goal):
    if start_node == goal:
        # returns the path along with its transition cost
        return ([start_node],0)
    
    # here we will store all the paths availables as we process them
    #   to store the first path, we need to obtain its heuristic value
    path = {start_node : h_sld[start_node]}

    # update the iteration number
    iteration_counter = 1

    while True:
        
        # select the path with the lowest cost
        current_path_tuple, cost = sorted(path.items(), key= lambda x: x[1])[0]
        if type(current_path_tuple) == str:
            current_path = [current_path_tuple]
        else:
            current_path = list(current_path_tuple)

        current_node = current_path[-1]

        if current_node == goal:
            # returns the path along with its transition cost
            return (current_path, cost)

        # search for the childs of the current node
        childs = [node_weights_list[1] for node_weights_list in tree[1] if node_weights_list[0] == current_node]

        # these childs have the cost of the action, we need to find its heuristic value
        if len(childs) != 0:
            childs_with_h_values = []

            for child in childs[0]:
                child_name = child[0]
                # get the transition cost to the node
                child_action_value = child[1]
                # get the heuristic cost of the node
                child_heuristic_value = h_sld[child_name]
                
                # check for the previous cities to update the transition cost
                acucumulative_transition_cost = 0
                current_path = current_path
                for node_index in range(len(current_path)-1):
                    for transition_cost in tree[1]:
                        if transition_cost[0] == current_path[node_index]:
                            for node in transition_cost[1]:
                                # get the node to transition to
                                if node[0] == current_path[node_index+1]:
                                    acucumulative_transition_cost += node[1]

                acucumulative_transition_cost += child_action_value

                # calculate the transition cost of the current node to the current child via
                #   f(n) = g(n) + h(n)
                total_transition_cost = acucumulative_transition_cost + child_heuristic_value

                # save the path with the corresponding transition cost
                childs_with_h_values.append((child_name,total_transition_cost))

            sorted_childs_with_h_values = sorted(childs_with_h_values, key=lambda x: x[1])

            # update the paths expanded so far; in this way, we save the alternative paths
            for child in sorted_childs_with_h_values:
                temp_updated_path = current_path.copy()
                temp_updated_path.append(child[0])
                # stores the new paths in the path dictionary
                path[child[1]] = tuple(temp_updated_path)

            # delete the current path (old)
            del current_path_tuple

        else:
            # After visiting its neighbors, we mark the node as "visited"
            return 'Unable to find a path'
        
        iteration_counter += 1

def main():
    tree = generate_states(formed_graph)
    #print('\n directed tree = ', tree[0], '\n')
    #print('directed weights = ', tree[1], '\n')
    

    unidirectional_tree = generate_unidirectional_weights(tree)
    print('unidirectional tree = ', unidirectional_tree[0], '\n')
    print('unidirectional weights = ', unidirectional_tree[1], '\n')

    #start = input('start node?: ')
    start = 'Arad'
    goal = 'Bucarest'

    # execute the algorithm with the unidirectional tree/graph
    a_star_result = a_star(unidirectional_tree, start, goal)
    

    if type(a_star_result) == str:
        print('\n*****\n A Star Search was {}\n From {} to {}'.format(a_star_result,start,goal))
    else:
        print('\n*****\n From {} to {}\n A Star search obtained the following path = {}\n with a cost of {}\n*****'.format(start, goal, a_star_result[0], a_star_result[1]))

    a_star_2_result = a_star_2(unidirectional_tree, start, goal)

    if type(a_star_2_result) == str:
        print('\n*****\n A Star Search was {}\n From {} to {}'.format(a_star_2_result,start,goal))
    else:
        print('\n*****\n From {} to {}\n A Star search obtained the following path = {}\n with a cost of {}\n*****'.format(start, goal, a_star_2_result[0], a_star_2_result[1]))
    

if __name__ == "__main__":
    main()
