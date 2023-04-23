# encuentra un camino desde el nodo de inicio hasta el nodo meta utilizadno
# el algoritmo de Greedy-Best First Search:
# entrada:
#   start: nombre de la ciudad de inicio
#   goal: nombre de la ciudad meta
#   tree: tupla que contiene las aristas y sus pesos
#   h_sld: diccionario [string][int] tal que guarda los valores de la de la distancia 
#       a la ciudad meta
# salida:
#   path: es el camino encontrado con el menor peso a partir de la heuristica
def greedy(tree, start, goal, h_sld):
    """encuentra un camino desde el nodo de inicio hasta el nodo meta utilizando 
    el algoritmo de Greedy-Best First Search:
    entrada:
        start: nombre de la ciudad de inicio
        goal: nombre de la ciudad meta
        tree: tupla que contiene las aristas y sus pesos
        tree: tupla que contiene las aristas y sus pesos
        h_sld: diccionario [string][int] tal que guarda los valores de la de la distancia 
            a la ciudad meta
        salida:
        path: es el camino encontrado con el menor peso a partir de la heuristica
    """
    if start == goal:
        # returns the path along with its transition cost
        return ([start],0)
    
    # here we will store all the paths availables as we process them
    # to store the first path, we need to obtain its heuristic value
    path = {h_sld[start] : [start]}

    # update the iteration number
    iteration_counter = 1
    while True:
        
        # select the path with the lowest cost
        key_path_with_lower_value = min([int(key) for key, values in path.items()])
        
        current_node = path[key_path_with_lower_value][-1]
        if current_node == goal:
            # returns the path along with its transition cost
            return (path[key_path_with_lower_value], key_path_with_lower_value)

        # search for the childs of the current node
        childs = [node_weights_list[1] for node_weights_list in tree[1] if node_weights_list[0] == current_node]
        # these childs have the cost of the action, we need to find its heuristic value
        if childs != []:
            childs_with_h_values = []

            for child in childs[0]:
                child_name = child[0]
                # get the heuristic cost of the node
                child_heuristic_value = h_sld[child_name]

                # calculate the transition cost of the current node to the current child via
                #   f(n) = h(n)
                total_transition_cost = child_heuristic_value

                # save the path with the corresponding transition cost
                childs_with_h_values.append((child_name,total_transition_cost))

            sorted_childs_with_h_values = sorted(childs_with_h_values, key = lambda x: x[1])
            # update the paths expanded so far; in this way, we save the alternative paths
            for child in sorted_childs_with_h_values:
                temp_updated_path = path[key_path_with_lower_value].copy()
                temp_updated_path.append(child[0])
                # stores the new paths in the path dictionary
                path[child[1]] = temp_updated_path

            # delete the current path (old)
            del path[key_path_with_lower_value]
        else:
            # After visiting its neighbors, we mark the node as "visited"
            return 'Unable to find a path'
        
        iteration_counter += 1
        
# encuentra un camino desde el nodo de inicio hasta el nodo meta utilizadno
# el algoritmo de A* Search:
# entrada:
#   start: nombre de la ciudad de inicio
#   goal: nombre de la ciudad meta
#   tree: tupla que contiene las aristas y sus pesos
#   h_sld: es un diccionario[string][int] que contiene la heuristica de
#       la distancia de la linea recta, hasta la ciudad meta
# salida:
#   path: es el camino encontrado con el menor peso a partir de la heuristica
#   cost: es el costo del camino según la euristica y el costo de transisión entre nodos
def a_estrella(tree,start,goal, h_sld):
    """encuentra un camino desde el nodo de inicio hasta el nodo meta utilizadno
    el algoritmo de A* Search:
    entrada:
      start: nombre de la ciudad de inicio
      goal: nombre de la ciudad meta
      tree: tupla que contiene las aristas y sus pesos
      h_sld: es un diccionario[string][int] que contiene la heuristica de
          la distancia de la linea recta, hasta la ciudad meta
    salida:
      path: es el camino encontrado con el menor peso a partir de la heuristica
      cost: es el costo del camino según la euristica y el costo de transisión entre nodos"""
    if start == goal:
        # returns the path along with its transition cost
        return ([start],0)
    
    iteration_counter = 0
    print('\n--- search iteration {} ---'.format(iteration_counter))
    
    # here we will store all the paths availables as we process them
    #   to store the first path, we need to obtain its heuristic value
    path = {h_sld[start]: [start]}
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

# encuentra un camino desde el nodo de inicio hasta el nodo meta utilizadno
# el algoritmo de wieghted A* Search:
# entrada:
#   start: nombre de la ciudad de inicio
#   goal: nombre de la ciudad meta
#   tree: tupla que contiene las aristas y sus pesos
#   h_sld: es un diccionario[string][int] que contiene la heuristica de
#       la distancia de la linea recta, hasta la ciudad meta
# salida:
#   path: es el camino encontrado con el menor peso a partir de la heuristica
#   cost: es el costo del camino según la euristica y el costo de transisión entre nodos     
def a_estrella_ponderada(tree,start,goal, h_sld):
    """Encuentra un camino desde el nodo de inicio hasta el nodo meta utilizadno
    el algoritmo de wieghted A* Search:
    entrada:
      start: nombre de la ciudad de inicio
      goal: nombre de la ciudad meta
      tree: tupla que contiene las aristas y sus pesos
      h_sld: es un diccionario[string][int] que contiene la heuristica de
          la distancia de la linea recta, hasta la ciudad meta
    salida:
      path: es el camino encontrado con el menor peso a partir de la heuristica
      cost: es el costo del camino según la euristica y el costo de transisión entre nodos  """   
    if start == goal:
        # returns the path along with its transition cost
        return ([start],0)
    
    iteration_counter = 0
    print('\n--- search iteration {} ---'.format(iteration_counter))
    
    # here we will store all the paths availables as we process them
    #   to store the first path, we need to obtain its heuristic value
    path = {((1.3)* h_sld[start]): [start]}
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
                child_heuristic_value_with_detour_index = ((1.3) * h_sld[child_name])
                print('\nchild = {}, action = {}, heuristic = {}'.format(child_name,child_action_value,child_heuristic_value_with_detour_index))
                
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
                total_transition_cost = acucumulative_transition_cost + child_heuristic_value_with_detour_index
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

