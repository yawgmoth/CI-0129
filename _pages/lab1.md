---
title: "Lab 1"
layout: single
excerpt: "Lab 1: Search"
sitemap: true
permalink: /labs/lab1.html
frontpageorder: 4
categories: []
---

* TOC
{:toc}

## Search Algorithm

For this task, you will implement a (directed) graph search algorithm, A &ast; in python. The input to this algorithm is a graph, consisting of nodes/vertices and edges. However, in order to be able to use this search 
algorithm for the planner later, our graphs will not be represented in their entirety in memory, but rather use a [lazy](https://en.wikipedia.org/wiki/Lazy_evaluation) representation. What this means is that our graph 
will be represented by **one** node, which can generate neighboring nodes as needed. This representation is implemented in `graph.py`, and does not have to be modified. If you want to modify `graph.py`, please do not 
change `Node` and `Edge` and their interfaces. When in doubt what you can change, ask. For this task, you only have to implement one function: `astar(start, heuristic, goal)`. This function takes a graph, represented 
by the start vertex/node, a heuristic function, and a goal predicate and searches for a path from the start to **a** node that satisfies the goal predicate. The result of the function should be four values:
   - The path, represented as a sequence of `Edge` objects
   - The total length of the path 
   - The number of nodes visited, i.e. added to the frontier, during search
   - The number of nodes expanded, i.e. removed from the frontier, during search 
If no path is found, the first two values should be `None`, but the number of visited and expanded nodes should still be reported. 

As mentioned above, the graph is not represented explicitly, instead only a single `Node` object is passed to the algorithm, which has a method `get_neighbors` which returns a list of `Edge` objects representing 
outgoing edges. Each `Edge` object stores its target, the cost to use the edge, and its name (used for printing the path). The target is another `Node` object, which can then in turn be asked for its own neighbors, 
and so on. Note that to simplify development, nodes do not need to be cached between calls, and are instead identified by a unique id, which can be obtained from the `get_id` method. `graph.py` shows how this representation 
can be used to represent finite and infinite graphs.

Mandatory function in `pathfinding.py`, following the API described there:
   - `astar`
   
Do **not** remove or change the `default_heuristic` in `pathfinding.py`.

**Note:** The comment for `get_neighbors` in `graph.py` used to incorrectly state that its return value was a list of 3-tuples. In fact the return value is a list of `Edge` object, each of which contains three attributes. This has been corrected in the framework on 7/9/2019. This was only a change in documentation, the actual functionality was unaffected by this change.
