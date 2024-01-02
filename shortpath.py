def shortest_path(graph, start, target = ''):
    unvisited = list(graph) # Will iterate over the keys of the graph and have a list of unvisited nodes

    distances = {node: 0 if node == start else float('inf') for node in graph} # Will keep record of the distance from the starting node to each node. If the node is the same as the start node, it'll have a distance of '0', if not, the distance will be infinity

    paths = {node: [] for node in graph} # Initializing empty lists for each of the nodes

    paths[start].append(start) # Adding the start node to its own path
    
    while unvisited: # As long as unvisited is not empty, the loop will run

        current = min(unvisited, key=distances.get) # Will find the minimum distance from the start node. `distances` is a dictionary, initialized before. `key=distances.get` will take the node(s) from the unvisited list and compare the values of those nodes. To simplify, [('B', 3), ('C', 2)]. The `key=distances.get` will return 2 as the minimum value. As node 'C' has the value of 2. 'C' will be assigned to the variable `current`

        
        for node, distance in graph[current]: # Iterates over the current node of the graph

            if distance + distances[current] < distances[node]: 
                # `distance` = Distance from the current node to the neighbor 
                # `distances[current]` = Distance from the start node to the current node 
                # `distances[node]` = Distance from the start node to neighbor

                # To simplify, 'F': [('B', 2), ('D', 3)], 'B' and 'D' are neighbor of 'F'. If the LHS summation is less than RHS, 

                distances[node] = distance + distances[current] # It becomes the value of the summation. If it was previously known as 5, it will now become 2 in case of 'B'.

                if paths[node] and paths[node][-1] == node: # If node's path exists and if the last node of the path is the current node itself

                    paths[node] = paths[current][:] # Make a copy of the `current` node path  and assigning to the path for the node
                
                else:
                    paths[node].extend(paths[current]) #  Else if node's path exists and but the last node of the path is not the current node itself, In this case, we extend the existing node path  with the current node path.

                paths[node].append(node) # Update the node path by node

        unvisited.remove(current) # # Removes the current node from the unvisited list
    
    targets_to_print = [target] if target else graph # Decides what to print

    for node in targets_to_print: # Iterating over nodes of targets_to_print
        if node == start: # If it is the starting node
            continue # Skip

        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths


my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

shortest_path(my_graph, 'F', 'A')