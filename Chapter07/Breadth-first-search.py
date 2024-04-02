"""
This algorithm (breadth-first search) is used to tell if there is a possible path between two vertexes.
If so, it finds the shorter path betweens to vertexes/things
It is used to find the approach that takes the minimum of steps to get to a goal

This algorithm uses graph in its process to find the shorter path

A graph is a group of connections. Each point that is connected to another point, is a vertex.
And the thing that connects the vertexes is a path

The "breadth-first search" start looking for a target item in a vertex. If the target item is not on that vertex, it adds, to its lists
of search, all of the neighboors of that vertex, so that they can also be searched

Important: n-1 degree connections are always checked before a n degree connection, given that n is >= 1
Following this rule, the vertexes start being added to a search list in this order. 
This way, always the shorter path is going to be find

"""
